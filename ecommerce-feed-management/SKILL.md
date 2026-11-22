---
name: ecommerce-feed-management
description: "Product feed management and monitoring for any channel (Google Merchant Center, Meta catalog, Amazon, Walmart, TikTok Shop, marketplaces). Validates feeds for missing required attributes, invalid prices, availability and GTINs, duplicate IDs and title length with a script, diagnoses sync errors and missing SKUs between the store and each channel, and sets feed rules, supplemental feeds and monitoring. Use when products are disapproved, missing or out of sync on a channel, or a seller needs to clean up or monitor product feeds."
nexscope:
  name: "E-Commerce Feed Management"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "product-feed"
    - "catalog"
    - "monitoring"
    - "data-quality"
  model: "any"
  tokens: "~2000"
  keywords:
    - "ecommerce feed management"
---

# E-Commerce Feed Management

AI-powered product feed management and monitoring skill. Designs feed health checks, sync error diagnostics, missing SKU detection, and attribute completeness validation for e-commerce product catalogs.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Monitoring and fixing product feeds for any channel (sync errors, missing SKUs, attributes).

Part of: Google Shopping and product feeds. For neighbouring jobs, use the matching skill instead:

- `google-shopping-optimization` — Google Shopping and Performance Max campaign strategy, bids and ROAS.
- `shopify-google-channel` — Connecting a Shopify store to Google with the Google & YouTube channel and Merchant Center.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Feed file or export (CSV/TSV/XML) per channel | Feed app, platform export, Merchant Center |
| Channel diagnostics (disapprovals, warnings) | Merchant Center Diagnostics, Meta Commerce Manager, Seller Central / Seller Center catalog errors |
| Catalog of record (all active SKUs) | Store platform export |
| Channel specifications | Each channel's product data specification |

## Workflow

1. **Inventory feeds**: which channels, how each feed is produced (native app, feed tool, file), refresh frequency.
2. **Validate** each feed with the script and the channel's own diagnostics.
3. **Reconcile SKUs**: active products in the store vs products in each channel; list missing, extra and stale items.
4. **Fix at the source** when possible (product data in the store), otherwise with feed rules or supplemental feeds (e.g. GTIN, brand, product category, custom labels).
5. **Optimize** titles and attributes per channel (`product-title-optimization`), images that meet each channel's rules.
6. **Monitor**: daily diagnostics check, alert when disapprovals or missing SKUs exceed a threshold, check after every catalog import or price change.
7. **Document** feed rules so they survive staff changes.

## Calculations and Tools

`scripts/feed_check.py` validates a CSV/TSV/JSON feed against Google Merchant Center basics (required attributes, availability values, price format, URLs, duplicate IDs, GTIN check digit, length limits):

```bash
python3 scripts/feed_check.py '[{"id": "SKU-1", "title": "Steel Bottle 750 ml", "description": "Insulated", "link": "https://example.com/p/1", "image_link": "https://example.com/i/1.jpg", "availability": "in_stock", "price": "24.99 USD", "brand": "Acme", "gtin": "4006381333931"}]'
```

- **Coverage** = SKUs present and approved on the channel ÷ active SKUs in the store.
- **Disapproval rate** = disapproved items ÷ submitted items.

## Example Requests

- "200 products are disapproved in Google Merchant Center. Check our feed and tell us what to fix first."
- "Our TikTok Shop catalog has fewer products than Shopify. Find the missing SKUs."
- "Validate this product feed CSV before we upload it."

## Output Format

```
FEED HEALTH — [Channel, date]
Coverage: X% (approved / active)   Disapproval rate: X%
| Issue | Type | Products | Fix (source / feed rule / supplemental feed) |
Missing SKUs: [...]   Monitoring rules: [...]
```

## Quality Checks

- Findings are confirmed against the channel's own diagnostics before large changes.
- Fixes are made at the source when possible; feed rules are documented.
- Specification limits are cited as "per the channel's published spec, to confirm".
- No change removes GTINs or brands to silence errors.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: script findings on the provided feed; channel diagnostics.
- **To confirm**: channel specifications change; the script implements commonly published Google basics, not every category rule.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-feed-management -g
```

## Usage

**Input:**
Product feed URL/file, marketplace requirements, catalog size

**Output:**
Feed health report, sync error diagnosis, missing SKU detection, attribute completeness audit

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up e-commerce feed management for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
