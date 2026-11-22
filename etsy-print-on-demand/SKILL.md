---
name: etsy-print-on-demand
description: "Etsy print-on-demand (POD). Sets up Printful, Printify or similar integrations with Etsy, picks niches and designs, creates mockups, prices products after POD and Etsy fees, and handles production times and Etsy's production-partner disclosure. Use when someone wants to sell print-on-demand products on Etsy or improve POD margins."
metadata:
  nexscope:
    category: etsy
---

# Etsy Print on Demand

POD integration — Printful, Printify, mockups, niche selection, margin optimization.

Sell print-on-demand (POD) products on Etsy with healthy margins, honest disclosure and reliable fulfillment.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Print-on-demand products on Etsy with a production partner.

Part of: Etsy pricing, traffic and operations. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-pricing-strategy` — Setting Etsy prices from costs, Etsy fees and competition.
- `etsy-shipping-strategy` — Etsy shipping profiles, prices, processing times and free shipping.
- `etsy-advertising` — Etsy Ads on Etsy search (budgets, listings, ROAS).
- `etsy-offsite-ads` — Etsy Offsite Ads fees, attribution and the opt-out decision.
- `etsy-social-media-marketing` — Bringing outside traffic to an Etsy shop from Pinterest, Instagram and TikTok.
- `etsy-seasonal-strategy` — Preparing an Etsy shop for holidays and seasonal peaks.
- `etsy-review-strategy` — Getting more honest Etsy reviews and handling bad ones.
- `etsy-custom-orders` — Personalized and made-to-order items on Etsy.
- `etsy-digital-products` — Selling digital downloads on Etsy.

<!-- role-and-scope:end -->

## When to Use

- Starting POD (t-shirts, mugs, posters, phone cases…) on Etsy
- POD sales with thin margins or many delivery complaints
- Questions about Etsy rules for production partners

## Etsy Rules (confirm in the Creativity Standards)

- The seller must **design** the products; POD of others' artwork, brands, characters or trends that copy protected work is not allowed.
- The **production partner** (Printful, Printify, Gelato…) must be **declared** in the listing's production partner settings.
- Processing and delivery times must reflect the partner's production and shipping.

## Inputs to Collect

Niche and design style, POD provider and its base costs and shipping, target retail price, partner production times and ship-from countries, current listing photos (mockups).

## Workflow

1. **Niche first**: a specific audience (e.g. nurses, dog breeds, hobbies) with original designs, not generic slogans.
2. **Unit economics**: retail price − POD base cost − POD shipping − Etsy fees (`etsy-pricing-strategy`) − Offsite Ads (worst case). Aim for a margin that survives sales.
3. **Provider choice**: print quality (order samples), production time, ship-from location close to buyers, Etsy integration.
4. **Listings**: realistic mockups plus at least one real photo from a sample; size charts; care instructions; production partner declared.
5. **Delivery times**: set processing times from the provider's averages; monitor late orders (`etsy-star-seller`).
6. **Quality loop**: track defects and reprints by product; switch providers or products with repeated issues.

## Output Format

1. Niche and design plan
2. Margin table per product (base cost, shipping, fees, profit)
3. Provider comparison and recommendation
4. Listing checklist (mockups, sample photos, size chart, production partner)

## Example Requests

- "Is Printify profitable for t-shirts on Etsy at $24? What must I disclose?"
- "Help me with etsy print on demand for my Etsy shop"
- "What are the best practices for etsy print on demand?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-print-on-demand -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
