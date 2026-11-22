---
name: etsy-offsite-ads
description: "Etsy Offsite Ads analysis. Explains how Offsite Ads fees are charged on attributed sales, measures their real cost and return on the seller's margins, and decides whether to opt out (when the shop is eligible to). Use when an Etsy seller asks about Offsite Ads fees, attribution, or whether to opt out (for on-Etsy ads use `etsy-advertising`)."
metadata:
  nexscope:
    category: etsy
---

# Etsy Offsite Ads

Offsite Ads analysis — when to opt out, ROI tracking, fee impact on margins, attribution.

Understand what Etsy Offsite Ads really cost the shop and decide whether to stay in or opt out.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Etsy Offsite Ads fees, attribution and the opt-out decision.

Part of: Etsy pricing, traffic and operations. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-pricing-strategy` — Setting Etsy prices from costs, Etsy fees and competition.
- `etsy-shipping-strategy` — Etsy shipping profiles, prices, processing times and free shipping.
- `etsy-advertising` — Etsy Ads on Etsy search (budgets, listings, ROAS).
- `etsy-social-media-marketing` — Bringing outside traffic to an Etsy shop from Pinterest, Instagram and TikTok.
- `etsy-seasonal-strategy` — Preparing an Etsy shop for holidays and seasonal peaks.
- `etsy-review-strategy` — Getting more honest Etsy reviews and handling bad ones.
- `etsy-custom-orders` — Personalized and made-to-order items on Etsy.
- `etsy-digital-products` — Selling digital downloads on Etsy.
- `etsy-print-on-demand` — Print-on-demand products on Etsy with a production partner.

<!-- role-and-scope:end -->

## When to Use

- A seller sees Offsite Ads fees on orders and wants to understand them
- Deciding whether to opt out
- Adjusting prices to absorb the fee

## How It Works (confirm in Etsy's Fees & Payments Policy)

- Etsy advertises listings on external sites (search engines, social networks…) at its own cost.
- The seller pays a fee **only when a sale is attributed** to an Offsite Ad (a click on the ad followed by a purchase within the attribution window, commonly 30 days).
- The fee is commonly **15%** of the order total, or **12%** for shops above $10,000 in sales in the last 12 months, **capped at $100 per order**.
- Shops under the $10,000 threshold can usually **opt out**; above it, participation is mandatory at the lower rate.

## Inputs to Collect

Orders with Offsite Ads fees over the last 3-6 months, their revenue and fee, the shop's profit margin per item, the shop's 12-month sales, overall sales trend.

## Workflow

1. **Measure**: share of orders and revenue coming from Offsite Ads; total fees paid.
2. **Profit check**: margin after the Offsite Ads fee per attributed order. If negative or thin on low-margin items, the program costs money.
3. **Incrementality**: would these buyers have come anyway? Compare periods or similar shops; attributed sales are not all new sales.
4. **Decide**:
   - Margin comfortable and attributed sales mostly new → stay in.
   - Margin thin → raise prices to absorb the worst-case fee, or opt out if eligible.
   - Above the threshold (mandatory) → price every item so a 12% fee still leaves profit.
5. Re-check every quarter and when crossing the $10,000 threshold.

## Output Format

1. Offsite Ads cost and revenue summary
2. Margin per item with and without the fee
3. Recommendation (stay, opt out, reprice) and the price changes

## Example Requests

- "I paid 15% Offsite Ads fees on three orders. Should I opt out?"
- "Help me with etsy offsite ads for my Etsy shop"
- "What are the best practices for etsy offsite ads?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-offsite-ads -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
