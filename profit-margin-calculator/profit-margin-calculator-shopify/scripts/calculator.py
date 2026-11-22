#!/usr/bin/env python3
"""
Multi-platform Profit Calculator - Core Engine

Shared by the profit-margin-calculator-{amazon,shopify,tiktok,walmart} skills.
The file is identical in every skill folder; the platform is taken from the
"platform" input field, or else from the skill folder name.

Features:
- Cost breakdown calculation with a fee model per platform
  * amazon : category referral fee + FBA fulfillment/storage
  * shopify: payment processing (by plan) + optional third-party gateway fee, no commission
  * tiktok : category referral fee + affiliate (creator) commission + FBT/seller fulfillment
  * walmart: category referral fee (incl. price tiers) + WFS fulfillment/storage
- Profit margin calculation (gross/net)
- Break-even analysis
- Pricing recommendations
- Batch calculation support (JSON list or CSV)

Fee defaults are estimates dated FEE_SCHEDULE_DATE. Platforms change fees often:
always confirm the seller's own rate (Seller Center, statements, plan page) and
pass it explicitly (referral_fee_rate, payment_processing_rate, ...) when known.

Version: 2.0.0
"""

import json
import csv
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import List, Dict, Optional
from enum import Enum
import sys


FEE_SCHEDULE_DATE = "2026-11"
SUPPORTED_PLATFORMS = ("amazon", "shopify", "tiktok", "walmart")


class ProfitStatus(Enum):
    HEALTHY = "healthy"      # >20% net margin
    WARNING = "warning"      # 5-20% net margin
    DANGER = "danger"        # <5% net margin
    LOSS = "loss"            # Negative margin


# ============================================================
# Amazon Referral Fee Rates (by category)
# ============================================================
REFERRAL_FEE_RATES = {
    # Category: Rate
    "default": 0.15,
    "electronics": 0.08,
    "computers": 0.08,
    "camera": 0.08,
    "video_games": 0.15,
    "books": 0.15,
    "clothing": 0.17,
    "shoes": 0.15,
    "jewelry": 0.20,
    "watches": 0.15,
    "furniture": 0.15,
    "home": 0.15,
    "kitchen": 0.15,
    "beauty": 0.15,
    "health": 0.15,
    "grocery": 0.15,
    "pet": 0.15,
    "toys": 0.15,
    "baby": 0.15,
    "sports": 0.15,
    "outdoors": 0.15,
    "automotive": 0.12,
    "industrial": 0.12,
    "office": 0.15,
}

# ============================================================
# Walmart Marketplace referral fees (estimates, see FEE_SCHEDULE_DATE)
# Walmart publishes 6-15% for most categories, with price tiers for some.
# Each entry: list of (max_total_price or None, rate), checked in order.
# ============================================================
WALMART_REFERRAL_FEE_RATES = {
    "default": [(None, 0.15)],
    "electronics": [(None, 0.08)],
    "computers": [(None, 0.08)],
    "camera": [(None, 0.08)],
    "video_games": [(None, 0.08)],
    "jewelry": [(None, 0.20)],
    "clothing": [(15.0, 0.05), (20.0, 0.10), (None, 0.15)],
    "apparel": [(15.0, 0.05), (20.0, 0.10), (None, 0.15)],
}

# ============================================================
# TikTok Shop referral fees (estimates, see FEE_SCHEDULE_DATE)
# US: sources disagree between 6% and 8% for most categories after the
# reported August 2026 change; 8% is used as the conservative default.
# Other regions: no default, pass referral_fee_rate explicitly.
# ============================================================
TIKTOK_REFERRAL_FEE_RATES = {
    "US": {
        "default": 0.08,
        "jewelry": 0.05,
    },
}

# ============================================================
# Shopify Payments online card rates (US) and third-party gateway fees
# ============================================================
SHOPIFY_PAYMENT_RATES = {
    # plan: (percentage, fixed fee per order)
    "basic": (0.029, 0.30),
    "grow": (0.027, 0.30),
    "advanced": (0.025, 0.30),
}
SHOPIFY_THIRD_PARTY_FEES = {
    # Extra Shopify fee when NOT using Shopify Payments (on top of the gateway's own fee)
    "basic": 0.02,
    "grow": 0.01,
    "advanced": 0.006,
    "plus": 0.002,
}

# FBA Fulfillment Fee Reference (simplified, based on size tier)
FBA_FULFILLMENT_FEES = {
    "small_standard": 3.22,      # Small standard (<1lb)
    "large_standard_1lb": 4.75,  # Large standard (<1lb)
    "large_standard_2lb": 5.40,  # Large standard (1-2lb)
    "large_standard_3lb": 6.10,  # Large standard (2-3lb)
    "small_oversize": 9.73,      # Small oversize
    "medium_oversize": 19.05,    # Medium oversize
    "large_oversize": 89.98,     # Large oversize
}

# Profit margin thresholds
PROFIT_THRESHOLDS = {
    "healthy": 0.20,    # >20%
    "warning": 0.05,    # 5-20%
    "danger": 0.00,     # 0-5%
}

# Display labels per platform
PLATFORM_LABELS = {
    "amazon": {"title": "Amazon", "fulfillment": "FBA Fulfillment", "storage": "FBA Storage", "referral": "Referral Fee"},
    "shopify": {"title": "Shopify/DTC", "fulfillment": "3PL Fulfillment", "storage": "Storage", "referral": "Platform Commission"},
    "tiktok": {"title": "TikTok Shop", "fulfillment": "FBT/Fulfillment", "storage": "Storage", "referral": "Referral Fee"},
    "walmart": {"title": "Walmart", "fulfillment": "WFS Fulfillment", "storage": "WFS Storage", "referral": "Referral Fee"},
}

# Accepted alternative input names -> canonical field
INPUT_ALIASES = {
    "fba_fee": "fba_fulfillment_fee",
    "wfs_fee": "fba_fulfillment_fee",
    "fbt_fee": "fba_fulfillment_fee",
    "fulfillment_fee": "fba_fulfillment_fee",
    "storage_fee": "fba_storage_fee",
    "wfs_storage_fee": "fba_storage_fee",
    "creator_commission_rate": "affiliate_commission_rate",
    "commission_rate": "affiliate_commission_rate",
    "ad_ratio": "ad_spend_ratio",
    "return_fee": "return_processing_fee",
    "plan": "shopify_plan",
}


def detect_platform(default: str = "amazon") -> str:
    """Platform implied by the skill folder name (profit-margin-calculator-<platform>)."""
    folder = Path(__file__).resolve().parent.parent.name.lower()
    for platform in SUPPORTED_PLATFORMS:
        if folder.endswith("-" + platform):
            return platform
    return default


# ============================================================
# Data Structures
# ============================================================

@dataclass
class ProductInput:
    """Single product input data"""
    sku: str = "SKU001"
    name: str = "Product"

    # Selling price
    selling_price: float = 0.0

    # Cost items
    product_cost: float = 0.0           # Product cost (FOB)
    shipping_cost: float = 0.0          # Inbound shipping
    fba_fulfillment_fee: float = 0.0    # Fulfillment fee per unit (FBA / WFS / FBT / 3PL)
    fba_storage_fee: float = 0.0        # Storage fee per unit (monthly avg)

    # Optional costs
    ad_spend_ratio: float = 0.0         # Ad spend ratio (0-1)
    return_rate: float = 0.0            # Return rate (0-1)
    return_processing_fee: float = 0.0  # Return processing fee per unit
    other_fees: float = 0.0             # Other fees

    # Platform related
    category: str = "default"           # Category (for Referral Fee)
    referral_fee_rate: Optional[float] = None  # Custom commission rate

    # For batch calculation
    monthly_sales: int = 0              # Monthly sales (for fixed cost allocation)
    fixed_costs: float = 0.0            # Fixed costs (for break-even)

    # Multi-platform fields
    platform: Optional[str] = None      # amazon | shopify | tiktok | walmart (default: skill folder)
    region: str = "US"                  # Marketplace region (TikTok fee table)
    affiliate_commission_rate: float = 0.0  # TikTok creator commission (0-1)
    affiliate_order_share: float = 1.0  # Share of orders sold through affiliates (0-1)
    shopify_plan: str = "basic"         # basic | grow | advanced | plus
    uses_shopify_payments: bool = True  # False = third-party gateway
    payment_processing_rate: Optional[float] = None  # Custom payment % (0-1)
    payment_fixed_fee: Optional[float] = None        # Custom fixed fee per order

    def __post_init__(self):
        self.platform = (self.platform or detect_platform()).lower()
        if self.platform not in SUPPORTED_PLATFORMS:
            raise ValueError(f"unknown platform '{self.platform}' (expected one of {', '.join(SUPPORTED_PLATFORMS)})")
        self.shopify_plan = self.shopify_plan.lower()
        self.region = self.region.upper()


@dataclass
class CostBreakdown:
    """Cost breakdown"""
    selling_price: float
    product_cost: float
    shipping_cost: float
    fba_fulfillment_fee: float
    fba_storage_fee: float
    referral_fee: float
    ad_cost: float
    return_cost: float
    other_fees: float
    payment_fee: float = 0.0
    affiliate_fee: float = 0.0

    total_cost: float = 0.0
    gross_profit: float = 0.0
    net_profit: float = 0.0
    gross_margin: float = 0.0
    net_margin: float = 0.0

    def __post_init__(self):
        self.total_cost = (
            self.product_cost +
            self.shipping_cost +
            self.fba_fulfillment_fee +
            self.fba_storage_fee +
            self.referral_fee +
            self.ad_cost +
            self.return_cost +
            self.other_fees +
            self.payment_fee +
            self.affiliate_fee
        )
        self.gross_profit = (self.selling_price - self.product_cost - self.shipping_cost
                             - self.fba_fulfillment_fee - self.referral_fee
                             - self.payment_fee - self.affiliate_fee)
        self.net_profit = self.selling_price - self.total_cost
        self.gross_margin = self.gross_profit / self.selling_price if self.selling_price > 0 else 0
        self.net_margin = self.net_profit / self.selling_price if self.selling_price > 0 else 0


@dataclass
class BreakEvenAnalysis:
    """Break-even analysis"""
    min_price: float              # Minimum price (break-even)
    break_even_units: int         # Break-even units
    safety_margin: float          # Safety margin
    current_margin_above_min: float  # Current price above minimum


@dataclass
class PricingSuggestion:
    """Pricing recommendation"""
    target_margin: float          # Target profit margin
    suggested_price: float        # Suggested price
    profit_per_unit: float        # Profit per unit


@dataclass
class AnalysisResult:
    """Complete analysis result"""
    product: ProductInput
    cost_breakdown: CostBreakdown
    break_even: BreakEvenAnalysis
    pricing_suggestions: List[PricingSuggestion]
    status: ProfitStatus
    summary: str


# ============================================================
# Input handling
# ============================================================

def product_from_dict(data: Dict) -> ProductInput:
    """Build a ProductInput from a dict, accepting documented aliases."""
    allowed = {f.name for f in fields(ProductInput)}
    clean = {}
    unknown = []
    for key, value in data.items():
        canonical = INPUT_ALIASES.get(key, key)
        if canonical not in allowed:
            unknown.append(key)
            continue
        clean[canonical] = value
    if unknown:
        raise ValueError(
            f"unknown field(s): {', '.join(unknown)}. "
            f"Allowed: {', '.join(sorted(allowed))}; aliases: {', '.join(sorted(INPUT_ALIASES))}"
        )
    return ProductInput(**clean)


# ============================================================
# Core Calculation Functions
# ============================================================

def get_referral_fee_rate(category: str, custom_rate: Optional[float] = None,
                          platform: str = "amazon", selling_price: float = 0.0,
                          region: str = "US") -> float:
    """Get Referral Fee rate for a platform/category"""
    if custom_rate is not None:
        return custom_rate
    category = (category or "default").lower()
    if platform == "shopify":
        return 0.0
    if platform == "walmart":
        tiers = WALMART_REFERRAL_FEE_RATES.get(category, WALMART_REFERRAL_FEE_RATES["default"])
        for max_price, rate in tiers:
            if max_price is None or selling_price <= max_price:
                return rate
    if platform == "tiktok":
        table = TIKTOK_REFERRAL_FEE_RATES.get(region)
        if table is None:
            raise ValueError(
                f"no default TikTok Shop referral fee for region '{region}': "
                "pass referral_fee_rate from Seller Center"
            )
        return table.get(category, table["default"])
    return REFERRAL_FEE_RATES.get(category, REFERRAL_FEE_RATES["default"])


def get_payment_terms(product: ProductInput):
    """(percentage, fixed per order) payment cost. Only Shopify/DTC pays it separately."""
    if product.platform != "shopify":
        return (product.payment_processing_rate or 0.0, product.payment_fixed_fee or 0.0)
    plan = product.shopify_plan if product.shopify_plan in SHOPIFY_PAYMENT_RATES else "basic"
    rate, fixed = SHOPIFY_PAYMENT_RATES[plan]
    if product.payment_processing_rate is not None:
        rate = product.payment_processing_rate
    if product.payment_fixed_fee is not None:
        fixed = product.payment_fixed_fee
    if not product.uses_shopify_payments:
        rate += SHOPIFY_THIRD_PARTY_FEES.get(product.shopify_plan, SHOPIFY_THIRD_PARTY_FEES["basic"])
    return (rate, fixed)


def get_affiliate_rate(product: ProductInput) -> float:
    """Effective affiliate commission as a share of the selling price."""
    return product.affiliate_commission_rate * product.affiliate_order_share


def _referral_rate(product: ProductInput) -> float:
    return get_referral_fee_rate(product.category, product.referral_fee_rate,
                                 product.platform, product.selling_price, product.region)


def calculate_costs(product: ProductInput) -> CostBreakdown:
    """Calculate cost breakdown"""
    # Referral Fee
    referral_rate = _referral_rate(product)
    referral_fee = product.selling_price * referral_rate

    # Payment processing (Shopify/DTC) and affiliate commission (TikTok)
    pay_rate, pay_fixed = get_payment_terms(product)
    payment_fee = product.selling_price * pay_rate + pay_fixed if product.selling_price > 0 else 0.0
    affiliate_fee = product.selling_price * get_affiliate_rate(product)

    # Ad cost
    ad_cost = product.selling_price * product.ad_spend_ratio

    # Return cost = return rate × (processing fee + product cost loss ratio)
    return_cost = product.return_rate * (product.return_processing_fee + product.product_cost * 0.5)

    return CostBreakdown(
        selling_price=product.selling_price,
        product_cost=product.product_cost,
        shipping_cost=product.shipping_cost,
        fba_fulfillment_fee=product.fba_fulfillment_fee,
        fba_storage_fee=product.fba_storage_fee,
        referral_fee=round(referral_fee, 2),
        ad_cost=round(ad_cost, 2),
        return_cost=round(return_cost, 2),
        other_fees=product.other_fees,
        payment_fee=round(payment_fee, 2),
        affiliate_fee=round(affiliate_fee, 2),
    )


def calculate_break_even(product: ProductInput, costs: CostBreakdown) -> BreakEvenAnalysis:
    """Calculate break-even point"""
    # Variable cost (per unit)
    variable_cost = (
        product.product_cost +
        product.shipping_cost +
        product.fba_fulfillment_fee +
        product.fba_storage_fee +
        costs.referral_fee +
        costs.return_cost +
        product.other_fees +
        costs.payment_fee +
        costs.affiliate_fee
    )

    # Minimum price (cover variable cost + ad spend)
    # Ad ratio unchanged: min_price - variable_cost - min_price * ad_ratio = 0
    # min_price * (1 - ad_ratio) = variable_cost
    if product.ad_spend_ratio < 1:
        min_price = variable_cost / (1 - product.ad_spend_ratio)
    else:
        min_price = variable_cost * 2  # Abnormal case

    # Break-even units (if fixed costs exist)
    if product.fixed_costs > 0 and costs.net_profit > 0:
        break_even_units = int(product.fixed_costs / costs.net_profit) + 1
    else:
        break_even_units = 0

    # Safety margin
    safety_margin = (product.selling_price - min_price) / product.selling_price if product.selling_price > 0 else 0
    margin_above_min = (product.selling_price - min_price) / min_price if min_price > 0 else 0

    return BreakEvenAnalysis(
        min_price=round(min_price, 2),
        break_even_units=break_even_units,
        safety_margin=round(safety_margin, 4),
        current_margin_above_min=round(margin_above_min, 4)
    )


def calculate_pricing_suggestions(product: ProductInput, target_margins: List[float] = None) -> List[PricingSuggestion]:
    """Calculate pricing recommendations"""
    if target_margins is None:
        target_margins = [0.15, 0.20, 0.25, 0.30]

    suggestions = []
    pay_rate, pay_fixed = get_payment_terms(product)

    # Base cost (excluding fees that are a % of price)
    base_cost = (
        product.product_cost +
        product.shipping_cost +
        product.fba_fulfillment_fee +
        product.fba_storage_fee +
        product.other_fees +
        product.return_rate * product.return_processing_fee +
        pay_fixed
    )

    referral_rate = _referral_rate(product)
    percent_fees = referral_rate + pay_rate + get_affiliate_rate(product)

    for target_margin in target_margins:
        # selling_price = base_cost / (1 - target_margin - percent_fees - ad_ratio)
        denominator = 1 - target_margin - percent_fees - product.ad_spend_ratio
        if denominator > 0:
            suggested_price = base_cost / denominator
            profit_per_unit = suggested_price * target_margin

            suggestions.append(PricingSuggestion(
                target_margin=target_margin,
                suggested_price=round(suggested_price, 2),
                profit_per_unit=round(profit_per_unit, 2)
            ))

    return suggestions


def evaluate_profit_status(net_margin: float) -> ProfitStatus:
    """Evaluate profit status"""
    if net_margin < 0:
        return ProfitStatus.LOSS
    elif net_margin < PROFIT_THRESHOLDS["warning"]:
        return ProfitStatus.DANGER
    elif net_margin < PROFIT_THRESHOLDS["healthy"]:
        return ProfitStatus.WARNING
    else:
        return ProfitStatus.HEALTHY


def analyze_product(product: ProductInput, target_margins: List[float] = None) -> AnalysisResult:
    """Analyze single product"""
    costs = calculate_costs(product)
    break_even = calculate_break_even(product, costs)
    pricing = calculate_pricing_suggestions(product, target_margins)
    status = evaluate_profit_status(costs.net_margin)

    # Generate summary
    status_text = {
        ProfitStatus.HEALTHY: "✅ Healthy",
        ProfitStatus.WARNING: "⚠️ Warning",
        ProfitStatus.DANGER: "🔴 Danger",
        ProfitStatus.LOSS: "💀 Loss",
    }
    summary = f"{status_text[status]} | Net Margin {costs.net_margin*100:.1f}% | Profit/Unit ${costs.net_profit:.2f}"

    return AnalysisResult(
        product=product,
        cost_breakdown=costs,
        break_even=break_even,
        pricing_suggestions=pricing,
        status=status,
        summary=summary
    )


def analyze_batch(products: List[ProductInput], target_margins: List[float] = None) -> List[AnalysisResult]:
    """Batch analysis"""
    return [analyze_product(p, target_margins) for p in products]


def max_affordable_cac(costs: CostBreakdown) -> float:
    """Contribution per order before advertising (break-even CAC for one order)."""
    return round(costs.net_profit + costs.ad_cost, 2)


# ============================================================
# Output Formatting
# ============================================================

def format_cost_breakdown(costs: CostBreakdown, platform: str = "amazon") -> str:
    """Format cost breakdown"""
    def pct(val):
        return f"{val/costs.selling_price*100:.1f}%" if costs.selling_price > 0 else "0%"

    labels = PLATFORM_LABELS.get(platform, PLATFORM_LABELS["amazon"])

    def row(label, value):
        return f"{label:<22}-${value:.2f}    {pct(value)}"

    lines = [
        f"Selling Price         ${costs.selling_price:.2f}   100%",
        "─" * 40,
        f"Product Cost          -${costs.product_cost:.2f}    {pct(costs.product_cost)}",
        f"Inbound Shipping      -${costs.shipping_cost:.2f}    {pct(costs.shipping_cost)}",
        row(labels["fulfillment"], costs.fba_fulfillment_fee),
        row(labels["storage"], costs.fba_storage_fee),
    ]
    if platform == "shopify":
        lines.append(row("Payment Processing", costs.payment_fee))
    else:
        lines.append(row(labels["referral"], costs.referral_fee))
    if platform == "tiktok":
        lines.append(row("Affiliate Commission", costs.affiliate_fee))
    lines.extend([
        f"Advertising           -${costs.ad_cost:.2f}    {pct(costs.ad_cost)}",
        f"Returns               -${costs.return_cost:.2f}    {pct(costs.return_cost)}",
        f"Other Fees            -${costs.other_fees:.2f}    {pct(costs.other_fees)}",
        "─" * 40,
        f"Total Cost            ${costs.total_cost:.2f}    {pct(costs.total_cost)}",
        f"Net Profit            ${costs.net_profit:.2f}    {costs.net_margin*100:.1f}%",
    ])
    return "\n".join(lines)


def format_break_even(be: BreakEvenAnalysis, current_price: float) -> str:
    """Format break-even analysis"""
    lines = [
        f"Break-even Price: ${be.min_price:.2f}",
        f"├── Below this price = Loss",
        f"",
        f"Current Price: ${current_price:.2f}",
        f"├── {be.current_margin_above_min*100:.1f}% above break-even",
        f"",
        f"Safety Margin: {be.safety_margin*100:.1f}%",
        f"├── Room for price reduction",
    ]
    if be.break_even_units > 0:
        lines.extend([
            f"",
            f"Break-even Units: {be.break_even_units}",
            f"├── Units needed to cover fixed costs",
        ])
    return "\n".join(lines)


def format_pricing_suggestions(suggestions: List[PricingSuggestion], current_price: float, current_margin: float) -> str:
    """Format pricing recommendations"""
    lines = [
        "| Target Margin | Recommended Price | Profit/Unit |",
        "|---------------|-------------------|-------------|",
    ]
    for s in suggestions:
        lines.append(f"| {s.target_margin*100:.0f}% | ${s.suggested_price:.2f} | ${s.profit_per_unit:.2f} |")

    lines.append(f"\nCurrent Price ${current_price:.2f} → Net Margin {current_margin*100:.1f}%")
    return "\n".join(lines)


def format_fee_notes(product: ProductInput, costs: CostBreakdown) -> str:
    """Platform-specific notes (empty for Amazon to keep its historical output)."""
    platform = product.platform
    if platform == "amazon":
        return ""
    notes = []
    if platform == "shopify":
        rate, fixed = get_payment_terms(product)
        gateway = "Shopify Payments" if product.uses_shopify_payments else "third-party gateway (+ Shopify fee)"
        notes.append(f"- Payment: {rate*100:.2f}% + ${fixed:.2f} per order ({product.shopify_plan} plan, {gateway}); no platform commission")
        notes.append(f"- Max affordable CAC (break-even, one order): ${max_affordable_cac(costs):.2f}")
    elif platform == "tiktok":
        rate = _referral_rate(product)
        notes.append(f"- Referral fee used: {rate*100:.1f}% ({product.region}, category '{product.category}')")
        notes.append(f"- Affiliate commission: {product.affiliate_commission_rate*100:.1f}% on {product.affiliate_order_share*100:.0f}% of orders")
        if product.referral_fee_rate is None:
            notes.append("- US referral fee reported as 6% or 8% depending on source and date: confirm your rate in Seller Center and pass referral_fee_rate")
    elif platform == "walmart":
        rate = _referral_rate(product)
        notes.append(f"- Referral fee used: {rate*100:.1f}% (category '{product.category}', total price ${product.selling_price:.2f})")
        if product.referral_fee_rate is None:
            notes.append("- Confirm your contract category rate on the Statements page in Seller Center and pass referral_fee_rate")
    notes.append(f"- Fee defaults dated {FEE_SCHEDULE_DATE}; platforms change fees often")
    return "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\nℹ️ **Fee Notes**\n\n" + "\n".join(notes) + "\n"


def format_full_report(result: AnalysisResult) -> str:
    """Generate full report"""
    status_icons = {
        ProfitStatus.HEALTHY: "✅",
        ProfitStatus.WARNING: "⚠️",
        ProfitStatus.DANGER: "🔴",
        ProfitStatus.LOSS: "💀",
    }
    platform = result.product.platform
    title = PLATFORM_LABELS[platform]["title"]

    report = f"""
💰 **{title} Profit Analysis Report**

**Product**: {result.product.name} ({result.product.sku})
**Status**: {status_icons[result.status]} {result.summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Cost Breakdown**

```
{format_cost_breakdown(result.cost_breakdown, platform)}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 **Break-Even Analysis**

{format_break_even(result.break_even, result.product.selling_price)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 **Pricing Recommendations**

{format_pricing_suggestions(result.pricing_suggestions, result.product.selling_price, result.cost_breakdown.net_margin)}

{format_fee_notes(result.product, result.cost_breakdown)}"""
    return report


def format_batch_summary(results: List[AnalysisResult]) -> str:
    """Format batch analysis summary"""
    status_icons = {
        ProfitStatus.HEALTHY: "✅",
        ProfitStatus.WARNING: "⚠️",
        ProfitStatus.DANGER: "🔴",
        ProfitStatus.LOSS: "💀",
    }

    lines = [
        "📊 **Batch Analysis Summary**",
        "",
        "| SKU | Price | Total Cost | Net Profit | Margin | Status |",
        "|-----|-------|------------|------------|--------|--------|",
    ]

    total_profit = 0
    for r in results:
        c = r.cost_breakdown
        icon = status_icons[r.status]
        lines.append(f"| {r.product.sku} | ${c.selling_price:.2f} | ${c.total_cost:.2f} | ${c.net_profit:.2f} | {c.net_margin*100:.1f}% | {icon} |")
        total_profit += c.net_profit

    lines.append("")
    lines.append(f"**Total**: {len(results)} SKUs | Avg Profit/Unit ${total_profit/len(results):.2f}")

    # Statistics
    healthy = sum(1 for r in results if r.status == ProfitStatus.HEALTHY)
    warning = sum(1 for r in results if r.status == ProfitStatus.WARNING)
    danger = sum(1 for r in results if r.status == ProfitStatus.DANGER)
    loss = sum(1 for r in results if r.status == ProfitStatus.LOSS)

    lines.append(f"**Status Distribution**: ✅ {healthy} | ⚠️ {warning} | 🔴 {danger} | 💀 {loss}")

    return "\n".join(lines)


# ============================================================
# CSV Batch Processing
# ============================================================

def parse_csv(csv_content: str, platform: Optional[str] = None) -> List[ProductInput]:
    """Parse CSV content"""
    products = []
    reader = csv.DictReader(csv_content.strip().split('\n'))

    for row in reader:
        product = ProductInput(
            sku=row.get('sku', 'SKU'),
            name=row.get('name', 'Product'),
            selling_price=float(row.get('selling_price', 0)),
            product_cost=float(row.get('product_cost', 0)),
            shipping_cost=float(row.get('shipping_cost', 0)),
            fba_fulfillment_fee=float(row.get('fba_fee') or row.get('fulfillment_fee') or 0),
            fba_storage_fee=float(row.get('storage_fee', 0)),
            ad_spend_ratio=float(row.get('ad_ratio', 0)),
            return_rate=float(row.get('return_rate', 0)),
            return_processing_fee=float(row.get('return_fee', 0)),
            other_fees=float(row.get('other_fees', 0)),
            category=row.get('category', 'default'),
            platform=row.get('platform') or platform,
            affiliate_commission_rate=float(row.get('affiliate_commission_rate', 0) or 0),
        )
        products.append(product)

    return products


# ============================================================
# CLI Entry Point
# ============================================================

DEFAULT_TEST_PRODUCTS = {
    "amazon": dict(sku="TEST001", name="Kitchen Gadget", selling_price=29.99, product_cost=6.00,
                   shipping_cost=1.50, fba_fulfillment_fee=5.50, fba_storage_fee=0.30,
                   ad_spend_ratio=0.10, return_rate=0.03, return_processing_fee=2.00,
                   other_fees=0.50, category="kitchen"),
    "shopify": dict(sku="TEST001", name="DTC Skincare Set", selling_price=49.99, product_cost=12.00,
                    shipping_cost=1.00, fba_fulfillment_fee=4.50, ad_spend_ratio=0.20,
                    return_rate=0.05, return_processing_fee=3.00, shopify_plan="basic"),
    "tiktok": dict(sku="TEST001", name="Viral Phone Stand", selling_price=19.99, product_cost=5.00,
                   shipping_cost=0.80, fba_fulfillment_fee=3.50, affiliate_commission_rate=0.15,
                   affiliate_order_share=1.0, ad_spend_ratio=0.05, return_rate=0.08,
                   return_processing_fee=2.50),
    "walmart": dict(sku="TEST001", name="Storage Bins (3-pack)", selling_price=24.99, product_cost=6.00,
                    shipping_cost=1.20, fba_fulfillment_fee=4.95, fba_storage_fee=0.25,
                    ad_spend_ratio=0.08, return_rate=0.03, return_processing_fee=2.00, category="home"),
}


def main():
    """Command line entry"""
    platform = detect_platform()
    test_product = ProductInput(platform=platform, **DEFAULT_TEST_PRODUCTS[platform])

    # If JSON input provided
    if len(sys.argv) > 1:
        try:
            input_data = json.loads(sys.argv[1])
            if isinstance(input_data, list):
                # Batch mode
                products = [product_from_dict(p) for p in input_data]
                results = analyze_batch(products)
                print(format_batch_summary(results))
                return
            else:
                test_product = product_from_dict(input_data)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Single product analysis
    result = analyze_product(test_product)
    print(format_full_report(result))


if __name__ == "__main__":
    main()
