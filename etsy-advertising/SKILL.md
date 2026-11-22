---
name: etsy-advertising
description: "Etsy Ads for promoted listings inside Etsy search. Sets the daily budget, picks which listings to promote, reads views, clicks, orders and ROAS per listing and decides what to pause or scale against the break-even ROAS. Use when an Etsy seller asks whether Etsy Ads are worth it, how much to spend or which listings to advertise (for the Offsite Ads fee program use `etsy-offsite-ads`)."
metadata:
  nexscope:
    category: etsy
---

# Etsy Advertising

Etsy Ads strategy — budget allocation, bid management, promoted listings, offsite ads opt-out analysis.

Run Etsy Ads (promoted listings in Etsy search) profitably: what to promote, how much to spend, and when to stop.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Etsy Ads on Etsy search (budgets, listings, ROAS).

Part of: Etsy pricing, traffic and operations. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-pricing-strategy` — Setting Etsy prices from costs, Etsy fees and competition.
- `etsy-shipping-strategy` — Etsy shipping profiles, prices, processing times and free shipping.
- `etsy-offsite-ads` — Etsy Offsite Ads fees, attribution and the opt-out decision.
- `etsy-social-media-marketing` — Bringing outside traffic to an Etsy shop from Pinterest, Instagram and TikTok.
- `etsy-seasonal-strategy` — Preparing an Etsy shop for holidays and seasonal peaks.
- `etsy-review-strategy` — Getting more honest Etsy reviews and handling bad ones.
- `etsy-custom-orders` — Personalized and made-to-order items on Etsy.
- `etsy-digital-products` — Selling digital downloads on Etsy.
- `etsy-print-on-demand` — Print-on-demand products on Etsy with a production partner.

<!-- role-and-scope:end -->

## When to Use

- Deciding whether to start Etsy Ads
- Ads spend money without sales
- Scaling ads on listings that already sell

For the separate Offsite Ads program (ads on Google, social and other sites, paid on sales), use `etsy-offsite-ads`.

## Inputs to Collect

Etsy Ads dashboard for the last 30 days (views, clicks, orders, revenue, spend per listing), each listing's price, profit per order and organic conversion rate, daily budget.

## Key Numbers

- **ROAS** = ad revenue ÷ ad spend.
- **Break-even ROAS** = 1 ÷ profit margin before ads (a 40% margin needs ROAS ≥ 2.5).
- **Cost per order** = spend ÷ ad orders; must stay below profit per order.

## Workflow

1. **Only advertise listings that convert organically**: good photos, reviews and price first; ads amplify, they do not fix a weak listing.
2. **Start small**: a modest daily budget across the best 5-20 listings; let data build for 2-4 weeks.
3. **Review per listing**: keep listings above break-even ROAS, lower bids or stop the others (Etsy Ads lets sellers set listing-level controls; check the current options).
4. **Fix before you pay**: listings with many clicks and no orders need photo, price or description work (`etsy-shop-analytics`).
5. **Seasonal boosts**: raise budget 2-4 weeks before peak periods for proven listings (`etsy-seasonal-strategy`).

## Output Format

1. Listing-level ads table (spend, revenue, ROAS, break-even ROAS, decision)
2. Recommended daily budget
3. Listings to fix before advertising
4. Review date and success metric

## Example Requests

- "I spend $5/day on Etsy Ads and get 1 sale a week. Is it worth it?"
- "Help me with etsy advertising for my Etsy shop"
- "What are the best practices for etsy advertising?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-advertising -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
