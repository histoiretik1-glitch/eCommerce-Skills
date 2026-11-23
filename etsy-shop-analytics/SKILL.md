---
name: etsy-shop-analytics
description: "Etsy shop analytics. Reads Etsy Stats (visits, traffic sources, search terms, conversion rate, top listings) to find what drives sales and which listings to fix. Use when an Etsy seller asks why sales dropped, which listings perform best, or how to use Etsy Stats."
metadata:
  nexscope:
    category: etsy
---

# Etsy Shop Analytics

Shop analytics — traffic sources, conversion rates, search terms, top listings performance.

Turn Etsy Stats into decisions: which listings to fix, where traffic comes from, and why sales go up or down.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Reading Etsy Stats to find what drives or blocks sales.

Part of: Etsy selling, Sales reporting and analytics. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-shop-setup` — Opening a new Etsy shop: account, policies, payments, first listings and launch checklist.
- `etsy-shop-branding` — Shop identity on Etsy: name, banner, logo, About section, photo style and packaging.
- `etsy-multi-shop` — Deciding on and running more than one Etsy shop.
- `etsy-star-seller` — Reaching and keeping the Etsy Star Seller badge (messages, shipping, reviews).
- `sales-tracking-tool` — Cross-channel sales tracking: metric dictionary, contribution by channel and SKU, anomalies, reconciliation.
- `shopify-analytics-guide` — Reading Shopify reports and KPIs: sales definitions, funnel, AOV, repeat customers, cohorts.
- `tiktok-shop-analytics` — Reading TikTok Shop performance data across videos, LIVE, affiliates and ads.

<!-- role-and-scope:end -->

## When to Use

- Sales dropped and the seller does not know why
- Choosing which listings to improve, promote or retire
- Monthly or quarterly shop review

## Inputs to Collect

From Etsy Stats for the last 30 and 90 days (and the same period last year): visits, orders, conversion rate, revenue, traffic sources, search terms, and per-listing views, favorites and orders. Plus any changes made (prices, photos, ads, holidays).

## Workflow

1. **Shop funnel.** Visits → orders = conversion rate. Compare with the shop's own history, not with other shops.
2. **Traffic sources.** Etsy search, Etsy app and marketplace, Etsy Ads, Offsite Ads, social, direct. A drop in one source points to the cause (SEO, ads, social activity).
3. **Search terms.** Terms bringing visits but no orders → listing does not match the search; terms with orders → reinforce in titles and tags.
4. **Listing matrix.**

| Views | Conversion | Action |
|-------|-----------|--------|
| High | High | Protect and promote (ads, variations) |
| High | Low | Fix photos, price, description, reviews |
| Low | High | Improve SEO and visibility |
| Low | Low | Rework or retire |

5. **Seasonality.** Compare with the same period last year before concluding.
6. **Action list.** At most 5 actions for the next 30 days, each linked to a specialist skill (`etsy-seo`, `etsy-pricing-strategy`, `etsy-advertising`...).

## Output Format

1. KPI table (visits, orders, conversion, revenue, average order value) with trends
2. Traffic source breakdown and changes
3. Listing matrix with the action per listing
4. Top 5 actions and the date of the next review

## Example Requests

- "My Etsy visits are stable but orders dropped 30% this month. What should I check?"
- "Help me with etsy shop analytics for my Etsy shop"
- "What are the best practices for etsy shop analytics?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-shop-analytics -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
