---
name: google-shopping-optimization
description: "Google Shopping and Performance Max campaign strategy for any store. Structures campaigns and asset groups, sets bidding and ROAS targets, splits budgets by product performance, and uses feed quality as a lever for campaign results. Use when a seller asks how to run, structure or improve Google Shopping or Performance Max ads and their ROAS (to connect a Shopify store to Merchant Center use `shopify-google-channel`; to fix feed errors on any channel use `ecommerce-feed-management`)."
metadata:
  nexscope:
    emoji: "🛒"
    category: ecommerce
---

# Google Shopping Optimization 🛒

Optimize Google Shopping campaigns and product feeds for maximum visibility and ROAS. Feed optimization, bidding strategy, campaign structure, and Performance Max integration.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Google Shopping and Performance Max campaign strategy, bids and ROAS.

Part of: Google Shopping and product feeds. For neighbouring jobs, use the matching skill instead:

- `shopify-google-channel` — Connecting a Shopify store to Google with the Google & YouTube channel and Merchant Center.
- `ecommerce-feed-management` — Monitoring and fixing product feeds for any channel (sync errors, missing SKUs, attributes).

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill google-shopping-optimization -g
```

## Usage

```
Optimize my Google Shopping feed. I have 200 products on Shopify. Current ROAS is 3x, I want to hit 5x. Monthly budget: $5,000.
```

## Capabilities

- Product feed optimization (titles, descriptions, images, attributes)
- Google Merchant Center compliance and error resolution
- Campaign structure (Standard Shopping vs Performance Max)
- Bidding strategy selection and optimization
- Product segmentation and priority campaign structure
- ROAS optimization by product group
- Negative keyword management for Shopping campaigns

## Principles and Constraints

Google Merchant Center and Google Ads rules for Shopping campaigns, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed in Google's product data specification and Ads help pages.

- **Feed requirements:** each product needs at least id, title, description, link, image_link, availability, price and, for most products, brand and GTIN (or `identifier_exists` = no when there is none) **[check: Merchant Center product data specification]**. Title up to 150 characters; the first ~70 are what users usually see **[check]**.
- **Landing page must match the feed:** price, availability and currency mismatches cause item disapprovals; repeated misrepresentation (hidden fees, missing contact or return information) can suspend the whole account.
- **Campaign types:** Performance Max (Shopping inventory plus other Google placements, asset groups and listing groups) and Standard Shopping (Shopping only, campaign priorities, manual or Smart Bidding). Smart Shopping was replaced by Performance Max in 2022.
- **Controls:** listing groups and custom labels (`custom_label_0` to `custom_label_4`) segment products; brand exclusions, search themes and negative keywords in Performance Max are available within limits **[check current limits]**; Standard Shopping uses negative keyword lists.
- **Smart Bidding depends on conversion value quality:** track purchases with correct values (consistent tax/shipping treatment, deduplicated), ideally with enhanced conversions; wrong values make tROAS optimise the wrong thing.
- **Change carefully:** large tROAS or budget changes restart learning; change by about 10–20% at a time and wait one to two conversion cycles (working rule based on Google's guidance to avoid abrupt changes).
- **Scope:** this skill is campaign strategy, bidding and ROAS. Connecting a Shopify store is `shopify-google-channel`; fixing feed errors across channels is `ecommerce-feed-management`.

## Data Needed

| Data | Where |
|------|-------|
| Product performance per item: clicks, cost, conversions, conversion value | Google Ads > Products report (or Merchant Center performance), 30–90 days |
| Feed diagnostics: disapprovals, warnings, missing attributes | Merchant Center > Products > Diagnostics / Needs attention |
| Margin per product or category | Finance; used to set break-even ROAS |
| Campaign structure, bidding strategy, targets, budgets | Google Ads |
| Search terms (Standard Shopping) and insights (PMax) | Google Ads reports |
| Conversion tracking set-up (tags, values, enhanced conversions) | Google Ads > Conversions |

## Workflow

1. **Audit tracking:** confirm the purchase conversion counts once, carries the right value and matches the store's orders within a few percent.
2. **Fix feed health:** clear disapprovals, add missing GTINs/brands, improve titles (product type + brand + key attributes in the first 70 characters), use the best image, set `product_type` and `google_product_category`.
3. **Compute break-even ROAS per product group** from margins (formula below); targets above break-even only.
4. **Segment products** with `product_buckets.py` (hero, sidekick, villain, zombie) and write the bucket into a custom label through a supplemental feed or feed rules.
5. **Structure campaigns:** heroes in their own PMax campaign or asset group with a budget that is not limited; sidekicks with a lower tROAS to gather data; villains with a higher tROAS or price/page fixes; zombies checked for feed issues first.
6. **Set bidding:** maximise conversion value with tROAS once there are enough conversions (Google suggests a conversion history; start without a target if data is thin, then add one).
7. **Control queries:** brand exclusions or separate brand campaign, negative keywords for irrelevant queries (Standard Shopping search terms, PMax insights).
8. **Review every 2 weeks:** bucket movements, ROAS vs break-even per bucket, impression share lost to budget vs rank, feed diagnostics; change targets gradually.

## Calculations and Tools

- **ROAS** = conversion value ÷ cost; **break-even ROAS** = 1 ÷ contribution margin before ads (e.g. 25% margin → ROAS 4).
- **Target ROAS for profit** = 1 ÷ (margin − target profit share), e.g. 25% margin and 10% profit → 1 ÷ 0.15 = 6.67.
- **CPC ceiling per product** = conversion rate × AOV × (margin − target profit share).
- **Impression share lost (budget vs rank)**: budget-limited heroes need budget; rank-limited ones need higher bids/lower tROAS or better feed/price.
- **Bucket rules:** see the script header (thresholds are inputs: target ROAS, minimum clicks, minimum conversions).

```bash
python3 scripts/product_buckets.py '{"target_roas": 4.0, "min_clicks": 100, "products": [{"id": "A1", "title": "Linen apron", "clicks": 820, "cost": 410.0, "conversions": 41, "conv_value": 2050.0}, {"id": "A2", "title": "Kids apron", "clicks": 150, "cost": 90.0, "conversions": 6, "conv_value": 390.0}, {"id": "T1", "title": "Tea towel set", "clicks": 640, "cost": 352.0, "conversions": 18, "conv_value": 720.0}, {"id": "B9", "title": "Bread bag", "clicks": 35, "cost": 17.5, "conversions": 1, "conv_value": 24.0}]}'
```

## Worked Example

*Illustrative example with invented figures.* 200 products, $5,000/month, account ROAS 3, target 5; average contribution margin before ads 30% → break-even ROAS 3.33, so the account currently loses money on ads.

- Bucket output (command above): Linen apron hero (ROAS 5.0), Kids apron sidekick (4.33), Tea towel set villain (2.05 on $352), Bread bag zombie (35 clicks).
- Actions: hero in its own asset group with uncapped budget; villain gets a price/feed review and a higher tROAS (or exclusion if margin cannot reach 3.33); zombie title rewritten and checked for disapprovals; overall tROAS raised from 300% to 350% then 400% over 4–6 weeks while watching conversion volume.

## Example Requests

- "Optimise my Google Shopping for 200 Shopify products: current ROAS 3, target 5, budget $5,000 a month."
- "Split my products into Performance Max asset groups by performance using my products report."
- "What target ROAS should I set with a 25% contribution margin if I want 10% profit?"

## Output Format

1. Tracking and feed health summary (issues, counts, fixes).
2. Break-even and target ROAS per product group.
3. Bucket table (script output) and the custom label plan.
4. Campaign structure: campaigns/asset groups, budgets, bidding targets, exclusions.
5. Two-week review checklist and change log.

## Quality Checks

- Conversion values verified against store orders before any bidding change.
- No target ROAS below break-even unless an explicit acquisition goal is stated.
- Feed titles and attributes match landing pages; no disapproval ignored.
- Bucket thresholds stated; products with too little data not judged.
- Target changes made gradually and logged with dates.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** Google Ads and Merchant Center reports for stated dates, the seller's margins.
- **Estimates:** expected ROAS after restructuring, impression share gains, benchmark ROAS by category.
- Google features and limits were reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
