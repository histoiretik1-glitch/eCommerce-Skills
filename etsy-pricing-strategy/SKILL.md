---
name: etsy-pricing-strategy
description: "Etsy pricing strategy. Builds a price from materials, labor, Etsy fees, shipping and profit, compares with competing listings, and plans sales and coupons without losing money. Use when an Etsy seller asks how to price handmade or vintage items, whether their prices are too low, or how Etsy fees affect their margin."
metadata:
  nexscope:
    category: etsy
---

# Etsy Pricing Strategy

Etsy pricing — cost calculation, competitor pricing, perceived value, shipping cost integration, sales and coupons.

Price Etsy items so every sale pays for materials, time and Etsy fees, while staying credible against competing listings.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Setting Etsy prices from costs, Etsy fees and competition.

Part of: Etsy pricing, traffic and operations. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-shipping-strategy` — Etsy shipping profiles, prices, processing times and free shipping.
- `etsy-advertising` — Etsy Ads on Etsy search (budgets, listings, ROAS).
- `etsy-offsite-ads` — Etsy Offsite Ads fees, attribution and the opt-out decision.
- `etsy-social-media-marketing` — Bringing outside traffic to an Etsy shop from Pinterest, Instagram and TikTok.
- `etsy-seasonal-strategy` — Preparing an Etsy shop for holidays and seasonal peaks.
- `etsy-review-strategy` — Getting more honest Etsy reviews and handling bad ones.
- `etsy-custom-orders` — Personalized and made-to-order items on Etsy.
- `etsy-digital-products` — Selling digital downloads on Etsy.
- `etsy-print-on-demand` — Print-on-demand products on Etsy with a production partner.

<!-- role-and-scope:end -->

## When to Use

- Pricing a new item
- The seller suspects prices are too low (busy but not profitable)
- Planning sales, coupons or free shipping

## Inputs to Collect

Materials per item, production time and the hourly rate the seller wants, packaging, shipping cost, overheads per month and expected orders, competitor prices (`etsy-competitor-analysis`), country (payment processing differs).

## Etsy Fees in the Price

Etsy fees and limits below are the commonly published values in 2026; confirm them in Etsy's Fees & Payments Policy and Seller Handbook before relying on them, as they differ by country and change.

| Fee | Typical value | Based on |
|-----|---------------|----------|
| Listing | $0.20 | Per listing, renewed after a sale or 4 months |
| Transaction | 6.5% | Item price + shipping + gift wrap |
| Payment processing | ~3% + $0.25 (US) | Order total |
| Offsite Ads (if attributed) | 12-15% | Order total, capped per order |

## Workflow

1. **Cost per item** = materials + packaging + labor (hours × rate) + share of overheads.
2. **Fee-aware floor price**: price where profit is zero after transaction, processing, listing and (worst case) Offsite Ads fees. Solve: price × (1 − fee %) − fixed fees − cost = 0.
3. **Target price**: add the desired profit margin (many makers aim for 30%+ after fees); round to a credible price point.
4. **Market check**: compare with similar listings of similar quality; if far above, strengthen the perceived value (photos, packaging, personalization, story) or justify the gap.
5. **Shipping in the price**: decide between charging shipping and building it into the price for free shipping (see `etsy-shipping-strategy`).
6. **Discounts**: plan sales and coupons from the target price so the discounted price stays above the floor.

## Output Format

```
PRICING — [Item]
Cost: materials $X + packaging $X + labor $X + overheads $X = $X
Floor price (incl. fees, worst case Offsite Ads): $X
Target price: $X (net margin X%)
Max discount for sales: X%
Market position: [below / in line / above competitors] — why
```

## Example Requests

- "My earrings cost $4 in materials and take 40 minutes. What should I charge on Etsy?"
- "Help me with etsy pricing strategy for my Etsy shop"
- "What are the best practices for etsy pricing strategy?"

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-pricing-strategy -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
