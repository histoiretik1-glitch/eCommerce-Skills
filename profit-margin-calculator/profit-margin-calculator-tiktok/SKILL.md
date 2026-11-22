---
name: profit-margin-calculator-tiktok
version: 1.0.0
description: "TikTok Shop profit margin calculator. Computes per-unit cost breakdown with the TikTok Shop referral fee, creator (affiliate) commission, FBT or self-fulfillment, ads and returns, then break-even price and target-margin pricing. No API key required. Use when a TikTok Shop seller asks whether a product is profitable, what price to set, how much creator commission they can afford, or how returns and affiliate fees eat their margin."
metadata: {"nexscope":{"emoji":"💰","category":"ecommerce"}}
---

# Profit Margin Calculator — TikTok Shop 💰

Calculate product profitability for TikTok Shop sellers — cost breakdowns, profit margins, and affiliate commission analysis.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill profit-margin-calculator-tiktok -g
```

## Cost Components

| Cost Item | Description | Notes |
|-----------|-------------|-------|
| Product Cost | FOB purchase price | - |
| Inbound Shipping | To FBT warehouse | - |
| FBT Fulfillment | Fulfillment by TikTok | Optional |
| **Referral Fee** | ~8% US default (6-8% reported) | Confirm in Seller Center |
| **Affiliate Commission** | 10-30% | Main cost ⚠️ |
| Advertising | TikTok Ads | - |
| Return Cost | Higher return rate | 5-15% |

## TikTok Characteristics

- **Referral fee**: percentage of the sale, ~6-8% for most US categories (5% for jewelry); confirm your category rate in Seller Center
- **High affiliate commission**: 10-30%, main cost driver
- **High return rate**: Impulse buying, 5-15% returns
- **Short viral cycle**: Need fast inventory turnover

## Script Parameters

`scripts/calculator.py` is shared by the four profit-margin-calculator skills. It reads the platform from the `platform` field (`amazon`, `shopify`, `tiktok`, `walmart`) or, by default, from this skill's folder, so the commands below need no `platform` field.

Common fields: `selling_price`, `product_cost`, `shipping_cost` (inbound), `ad_spend_ratio` (0-1), `return_rate` (0-1), `return_processing_fee`, `other_fees`, `fixed_costs`, `sku`, `name`.

Fields specific to TikTok Shop: `fulfillment_fee` (FBT or own shipping, aliases `fbt_fee`, `fba_fee`), `affiliate_commission_rate` (alias `creator_commission_rate`), `affiliate_order_share` (share of orders sold by creators, default 1.0), `category`, `region` (default `US`), `referral_fee_rate`.

An unknown field stops the script with the list of accepted fields. Fee defaults are estimates dated 2026-11: when the seller knows their own rate, pass it explicitly (`referral_fee_rate`, `payment_processing_rate`).

## Usage

```bash
python3 scripts/calculator.py

python3 scripts/calculator.py '{"selling_price": 19.99, "creator_commission_rate": 0.15, "product_cost": 5, "fulfillment_fee": 3.5}'

# Seller Center shows a 6% referral fee and creators drive 60% of orders
python3 scripts/calculator.py '{"selling_price": 19.99, "product_cost": 5, "referral_fee_rate": 0.06, "affiliate_commission_rate": 0.15, "affiliate_order_share": 0.6}'
```

## Output Example

```
💰 **TikTok Shop Profit Analysis Report**

Selling Price         $19.99   100.0%
────────────────────────────────────────
Product Cost          -$5.00    25.0%
FBT Fulfillment       -$3.50    17.5%
Referral Fee          -$1.60    8.0%
Affiliate Commission  -$3.00    15.0%  ⬅️ Main cost
...
────────────────────────────────────────
Net Profit            (depends on fulfillment, ads and returns entered)
```

## TikTok Fee Structure

| Fee Type | Rate | Notes |
|----------|------|-------|
| Referral Fee | ~8% US default (6-8% reported, 5% jewelry) | Fee table changed in 2026; check Seller Center |
| Affiliate Commission | 10-30% | Varies by influencer tier |
| FBT Fulfillment | ~$3-5/order | Similar to FBA |
| Return Processing | ~$2-3/return | Higher return rate |

## Key Considerations

1. **Affiliate costs are variable** — Top influencers demand higher rates
2. **Plan for returns** — Budget 5-15% return rate
3. **Fast turnover needed** — Viral products have short cycles
4. **Lower referral fees than Amazon** — ~6-8% vs Amazon's 8-15% for most categories

## vs Amazon

| Item | Amazon | TikTok |
|------|--------|--------|
| Referral fee | 8-15% | ~6-8% |
| Affiliate | N/A | 10-30% |
| Return rate | 5-10% | 5-15% |
| Traffic | Search | Content |

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
