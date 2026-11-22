---
name: profit-margin-calculator-shopify
version: 1.0.0
description: "Shopify/DTC profit margin calculator. Computes per-order cost breakdown with Shopify Payments processing by plan (or third-party gateway fees), 3PL fulfillment, ad spend, returns, break-even price, target-margin pricing and max affordable CAC. No platform commission. No API key required. Use when a Shopify or DTC store owner asks about product margins, pricing, ad spend limits, CAC or payment fees."
metadata: {"nexscope":{"emoji":"💰","category":"ecommerce"}}
---

# Profit Margin Calculator — Shopify/DTC 💰

Calculate product profitability for Shopify and DTC stores — cost breakdowns, profit margins, and CAC/LTV analysis.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill profit-margin-calculator-shopify -g
```

## Cost Components

| Cost Item | Description | Notes |
|-----------|-------------|-------|
| Product Cost | FOB purchase price | - |
| Inbound Shipping | To 3PL warehouse | - |
| 3PL Fulfillment | ShipBob/Deliverr etc. | - |
| **Payment Processing** | 2.9% + $0.30 (Basic), 2.7% (Grow), 2.5% (Advanced) | Shopify Payments, US online cards |
| **Advertising** | 20-40% | Main cost ⚠️ |
| Return Cost | Return processing | - |
| Customer Shipping | If free shipping offered | Optional |

## DTC Characteristics

- **No platform commission**: Only payment processing fees
- **High ad spend ratio**: 20-40%, main cost driver
- **Requires high margins**: 60%+ gross margin to support ads
- **Focus on LTV/CAC**: Recommended >3

## Key Metrics

| Metric | Recommended |
|--------|-------------|
| Gross Margin | >60% |
| Net Margin | >20% |
| LTV/CAC | >3 |
| Repeat Rate | Higher = better |

## Script Parameters

`scripts/calculator.py` is shared by the four profit-margin-calculator skills. It reads the platform from the `platform` field (`amazon`, `shopify`, `tiktok`, `walmart`) or, by default, from this skill's folder, so the commands below need no `platform` field.

Common fields: `selling_price`, `product_cost`, `shipping_cost` (inbound), `ad_spend_ratio` (0-1), `return_rate` (0-1), `return_processing_fee`, `other_fees`, `fixed_costs`, `sku`, `name`.

Fields specific to Shopify/DTC: `fulfillment_fee` (3PL, alias of `fba_fulfillment_fee`), `shopify_plan` (`basic` 2.9% + $0.30, `grow` 2.7% + $0.30, `advanced` 2.5% + $0.30), `uses_shopify_payments` (`false` adds Shopify's third-party fee: 2% / 1% / 0.6%), `payment_processing_rate`, `payment_fixed_fee`.

An unknown field stops the script with the list of accepted fields. Fee defaults are estimates dated 2026-11: when the seller knows their own rate, pass it explicitly (`referral_fee_rate`, `payment_processing_rate`).

## Usage

```bash
python3 scripts/calculator.py

python3 scripts/calculator.py '{"selling_price": 49.99, "ad_spend_ratio": 0.20, "product_cost": 12, "fulfillment_fee": 4.5}'

# Grow plan with a third-party payment gateway
python3 scripts/calculator.py '{"selling_price": 49.99, "product_cost": 12, "shopify_plan": "grow", "uses_shopify_payments": false}'
```

## Output Example

```
💰 **Shopify/DTC Profit Analysis Report**

Selling Price         $49.99   100.0%
────────────────────────────────────────
Product Cost          -$12.00    24.0%
3PL Fulfillment       -$4.50     9.0%
Payment Processing    -$1.75     3.5%
Advertising           -$10.00    20.0%  ⬅️ Main cost
...
────────────────────────────────────────
Net Profit            $18.59    37.2%

💡 Max Affordable CAC: $10.00
```

## DTC Golden Ratios

```
DTC Health Formula:
├── Gross Margin > 60%
├── Ad Spend < 30%
├── Fulfillment < 15%
├── Net Margin > 15%
└── LTV/CAC > 3
```

## vs Amazon

| Item | Amazon | Shopify/DTC |
|------|--------|-------------|
| Platform fee | 8-15% | 0% |
| Payment fee | Included | 2.9% + $0.30 |
| Ad spend | 10-20% | 20-40% |
| Margin need | 40%+ | 60%+ |
| Traffic | Platform | Self-built |

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

