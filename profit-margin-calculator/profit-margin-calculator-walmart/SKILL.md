---
name: profit-margin-calculator-walmart
version: 1.0.0
description: "Walmart Marketplace profit margin calculator with a tested script: per-unit costs with Walmart category referral fees (including apparel price tiers), WFS fulfillment and storage, ads and returns, then break-even and target-margin prices. Use when a seller asks any Walmart profit, WFS cost or referral fee question, even a quick one, instead of estimating fees by hand, and for Walmart vs Amazon margins."
metadata: {"nexscope":{"emoji":"💰","category":"ecommerce"}}
---

# Profit Margin Calculator — Walmart 💰

Calculate product profitability for Walmart Marketplace sellers — cost breakdowns, profit margins, and WFS fee analysis.

## Workflow

1. **Collect the inputs**: selling price, product cost, inbound shipping, Walmart category (for the referral fee), WFS fulfillment and storage fees, return rate and return cost.
2. **Confirm the fees**: use the seller's own rates when known (`referral_fee_rate`, `payment_processing_rate`); otherwise state that the script's dated defaults are estimates.
3. **Run the calculator**: `python3 scripts/calculator.py '<json>'` (see Script Parameters); unknown fields stop the script with the list of accepted ones.
4. **Read the result**: net margin and status, break-even price, prices for 15-30% target margins, fee notes.
5. **Test scenarios**: campaign price, higher ad spend or commission, higher return rate; compare margins.
6. **Recommend**: price, maximum discount or commission, cost reductions, with each figure labelled verified or estimate.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill profit-margin-calculator-walmart -g
```

## Cost Components

| Cost Item | Description |
|-----------|-------------|
| Product Cost | FOB purchase price |
| Inbound Shipping | Sea/air freight to WFS |
| WFS Fulfillment | Walmart Fulfillment Services |
| WFS Storage | Monthly storage fee |
| Referral Fee | Platform commission (6-15% for most categories, price tiers for some) |
| Advertising | Walmart Connect ads |
| Return Cost | Return processing loss |

## Walmart vs Amazon

| Item | Walmart | Amazon |
|------|---------|--------|
| Fulfillment | WFS | FBA |
| Referral fee | Lower | Higher |
| Monthly storage | WFS storage fees apply (check current WFS rate card) | Yes |
| Competition | Lower | High |

## Script Parameters

`scripts/calculator.py` is shared by the four profit-margin-calculator skills. It reads the platform from the `platform` field (`amazon`, `shopify`, `tiktok`, `walmart`) or, by default, from this skill's folder, so the commands below need no `platform` field.

Common fields: `selling_price`, `product_cost`, `shipping_cost` (inbound), `ad_spend_ratio` (0-1), `return_rate` (0-1), `return_processing_fee`, `other_fees`, `fixed_costs`, `sku`, `name`.

Fields specific to Walmart: `fulfillment_fee` (WFS, alias `wfs_fee`), `storage_fee` (alias `wfs_storage_fee`), `category` (`apparel`/`clothing` use price tiers), `referral_fee_rate`.

An unknown field stops the script with the list of accepted fields. Fee defaults are estimates dated 2026-11: when the seller knows their own rate, pass it explicitly (`referral_fee_rate`, `payment_processing_rate`).

## Usage

```bash
python3 scripts/calculator.py

python3 scripts/calculator.py '{"selling_price": 24.99, "product_cost": 6, "wfs_fee": 4.95}'
```

## Output Example

```
💰 **Walmart Profit Analysis Report**

Selling Price         $24.99   100.0%
────────────────────────────────────────
Product Cost          -$6.00    24.0%
WFS Fulfillment       -$4.95    19.8%
Referral Fee          -$3.75    15.0%
...
────────────────────────────────────────
Net Profit            $10.29    41.2%
```

## Walmart Advantages

| Advantage | Benefit |
|-----------|---------|
| **Simpler storage fees** | Check the WFS rate card for aged inventory |
| **Lower referral fees** | 6-15% vs 8-15% |
| **Less competition** | Easier ranking |
| **Growing marketplace** | More opportunities |

## Referral Fee Rates

| Category | Rate |
|----------|------|
| Electronics | 8% |
| Apparel / clothing | 5% (≤ $15), 10% ($15-20), 15% (> $20) |
| Home & Kitchen | 15% |
| Most categories | 15% default in the script (6-15% range) |

Rates are estimates dated 2026-11. Walmart shows each seller's contract category and rate on the Statements page in Seller Center; pass it as `referral_fee_rate`.

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
