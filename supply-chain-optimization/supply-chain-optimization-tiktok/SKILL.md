---
name: supply-chain-optimization-tiktok
version: 1.0.0
description: "TikTok Shop supply chain bottleneck analyzer. Computes margins after the TikTok referral fee and creator commissions, FBT or self-fulfillment costs, inventory days and cash cycle against TikTok Shop benchmarks, flags stock left after a viral peak and proposes actions; optional Markdown/HTML report. No API key required. Use when a TikTok Shop seller asks about cash flow, restocking a viral product, FBT costs, returns or how affiliate payouts affect working capital."
metadata: {"nexscope":{"emoji":"📦","category":"ecommerce"}}
---

# Supply Chain Optimization — TikTok Shop 📦

Supply chain bottleneck analyzer for TikTok Shop sellers. Diagnose cash flow, inventory, affiliate costs, and return rates.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill supply-chain-optimization-tiktok -g
```

## Platform Characteristics

| Feature | TikTok Shop | vs Amazon |
|---------|-------------|-----------|
| Fulfillment | FBT / Self-ship | FBA |
| Referral fee | ~6-8% most US categories (5% jewelry), confirm in Seller Center | 8-15% |
| Payment cycle | 7-15 days | 14 days |
| Traffic source | Content-driven | Search-driven |
| Return rate | Higher (impulse buying) | Medium |

## Cost Structure (TikTok Shop)

```
Selling Price $XX
├── Product Cost
├── Inbound Shipping
├── FBT Fulfillment / Self-ship
├── Referral Fee (~8% US default; 6-8% reported, 5% jewelry; confirm in Seller Center)
├── Affiliate Commission (10-30%)  ← TikTok-specific
├── Advertising (Spark Ads)
└── Net Profit
```

## Benchmark Configuration

```python
BENCHMARKS = {
    "tiktok": {
        "gross_margin": {
            "healthy": 0.45,    # Need to cover affiliate commission
            "warning": 0.35,
            "danger": 0.25
        },
        "shipping_ratio": {
            "healthy": 0.05,
            "warning": 0.08,
            "danger": 0.12
        },
        "inventory_days": {
            "healthy": 30,      # TikTok viral cycle is short
            "warning": 45,
            "danger": 60
        },
        "cash_cycle": {
            "healthy": 60,      # Fast payment
            "warning": 90,
            "danger": 120
        },
        "net_margin": {
            "healthy": 0.15,    # After affiliate split
            "warning": 0.08,
            "danger": 0.03
        },
        # TikTok-specific metrics
        "return_rate": {
            "healthy": 0.10,    # <10% healthy
            "warning": 0.20,
            "danger": 0.30
        },
        "affiliate_ratio": {
            "healthy": 0.20,    # Affiliate commission ratio
            "warning": 0.30,
            "danger": 0.40
        }
    }
}
```

## TikTok-Specific Costs

### Affiliate Commission

```
Livestream selling: 10-30% commission
Short video promotion: 10-25% commission
Top influencers: May require upfront fees
```

### Return Costs

```
TikTok return rates typically higher than traditional e-commerce (impulse buying)
Must account for:
├── Return shipping cost
├── Product damage/loss
└── Restocking fees
```

## Input Data

```
**Sales (TikTok-specific)**
• Average Selling Price: $___
• FBT Fulfillment Fee: $___/unit
• Referral Fee: ___% (from Seller Center; ~6-8% for most US categories)
• Affiliate Commission Rate: ___% (if applicable)
• Spark Ads Spend Ratio: ___%

**Risk (TikTok-specific)**
• Return Rate: ___%
• Return Processing Cost: $___/unit
```

## API Integration

### TikTok Shop API

```bash
export TIKTOK_APP_KEY="xxx"
export TIKTOK_APP_SECRET="xxx"
export TIKTOK_ACCESS_TOKEN="xxx"
```

### Available Data

| Data | API |
|------|-----|
| Orders | Order API |
| Products | Product API |
| Logistics | Logistics API |
| Affiliates | Affiliate API |

## Script Usage

`scripts/calculator.py` (plus `report_doc.py` and `report_html.py`) is shared by the four supply-chain-optimization skills. The platform comes from the `platform` field (`amazon`, `shopify`, `tiktok`, `walmart`) or, by default, from this skill's folder. It sets the benchmarks, the payout delay used in the cash cycle (15 days by default, override with `payout_days`), the fulfillment labels and the aged-stock advice.

```bash
python3 scripts/calculator.py '{"product_cost": 5, "supplier_payment_days": 0, "production_days": 15, "shipping_cost_per_unit": 0.6, "shipping_days": 20, "selling_price": 19.99, "fulfillment_fee": 3.5, "storage_fee": 0.2, "ad_spend_ratio": 0.05, "inventory_days": 35, "has_long_term_storage": true, "referral_fee_rate": 0.08, "affiliate_commission_rate": 0.15}'
```

Required fields: `product_cost`, `supplier_payment_days`, `production_days`, `shipping_cost_per_unit`, `shipping_days`, `selling_price`, `fba_fee` (aliases `fulfillment_fee`, `wfs_fee`, `fbt_fee`), `storage_fee`, `ad_spend_ratio`, `inventory_days`, `has_long_term_storage`. Optional: `referral_fee_rate`, `affiliate_commission_rate`, `payout_days`, `daily_sales`, `current_inventory`. An unknown field stops the script with the list of accepted fields.

## Bottleneck Diagnosis Focus

TikTok Shop-specific bottlenecks:

1. **High affiliate commission** → Profit erosion
2. **High return rate** → Hidden costs
3. **Slow inventory turnover** → Short viral cycle, high stagnation risk
4. **Content dependency** → Unstable traffic

## vs Amazon Comparison

| Item | Amazon | TikTok |
|------|--------|--------|
| Referral fee | 8-15% | ~6-8% |
| Affiliate split | None | 10-30% |
| Payment cycle | 14 days | 7-15 days |
| Return rate | 5-15% | 10-30% |
| Traffic | Stable | Volatile |
| Viral cycle | Long | Short |

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**


