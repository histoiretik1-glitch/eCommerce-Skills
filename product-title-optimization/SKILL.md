---
name: product-title-optimization
description: "Optimize product titles for search visibility and click-through rate across e-commerce platforms. Platform-specific title rules for Amazon (200 chars), Etsy (140 chars), Walmart, Shopify SEO, and eBay. Use when a seller asks to write or improve product titles for search ranking and click-through on a specific marketplace."
metadata:
  nexscope:
    emoji: "✏️"
    category: ecommerce
---

# Product Title Optimization ✏️

Optimize product titles for search visibility and click-through rate across e-commerce platforms. Platform-specific title rules for Amazon (200 chars), Etsy (140 chars), Walmart, Shopify SEO, and eBay.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Writing compliant product titles for each channel from one verified attribute set.

Part of: Keywords, titles and product copy. For neighbouring jobs, use the matching skill instead:

- `ecommerce-keyword-research` — Cross-channel keyword map: discovery, intent, priority scores and seasonal calendar.
- `product-description-generator` — Writing product descriptions and bullet copy.
- `etsy-keyword-research` — Finding the search phrases Etsy buyers use, before writing titles and tags.
- `ebay-seo` — Ranking eBay listings in Best Match search: titles, item specifics, category, identifiers.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill product-title-optimization -g
```

## Usage

```
Optimize my product title for Amazon and Etsy. Product: handmade leather wallet, RFID blocking, bifold, for men. Current Amazon title: 'Leather Wallet for Men'.
```

## Capabilities

- Platform-specific title structure templates
- Keyword placement optimization (front-loading high-value terms)
- Character limit compliance per platform
- Click-through rate optimization (benefit-driven language)
- A/B title variant generation for testing
- Multi-platform title adaptation from a single product

## Principles and Constraints

Title rules by channel, as known at the last review of this skill (November 2026). Limits change and vary by category: every figure marked **[check]** must be confirmed in the channel's current style guide before use.

| Channel | Length rule [check] | Main constraints |
|---------|---------------------|------------------|
| Amazon | Up to 200 characters in most categories, shorter limits in some; Amazon's title policy restricts special characters and repeating the same word more than twice | Brand first, no promotional phrases ("best seller", "free shipping"), no ALL CAPS, category style guide |
| Walmart | Style guides recommend about 50–75 characters | Brand + defining qualities + item name + count/size; no promotional words |
| eBay | 80 characters | Buyer keywords, no filler (see `ebay-seo`) |
| Etsy | Up to 140 characters; Etsy recommends short, readable titles | Clear item description first; tags carry extra keywords (see `etsy-seo-tags`) |
| Google Shopping | Up to 150 characters; about the first 70 visible | Product type, brand, key attributes early (see `google-shopping-optimization`) |
| TikTok Shop | Category-specific limits | No exaggerated claims; see `tiktok-shop-listing-optimization` |

- **Front-load:** the first 60–80 characters are what most mobile shoppers see on every channel.
- **Accuracy over keywords:** every word must be true for the product; irrelevant keywords and competitor brands break marketplace rules and hurt conversion.
- **One master attribute set, several titles:** build titles from the same verified attributes so channels stay consistent.

## Data Needed

| Data | Where |
|------|-------|
| Product attributes: brand, product type, model, material, size, colour, count, compatibility, key benefit | Catalogue, packaging |
| Priority keywords per channel | `ecommerce-keyword-research`, search term reports |
| Current titles and their CTR / conversion per channel | Marketplace business reports, ad reports, Search Console |
| Category style guide per channel | Channel seller help |
| Competitor titles on page 1 | Channel search results |

## Workflow

1. **Collect and verify attributes** in a master sheet (one row per SKU, one column per attribute).
2. **Map keywords** to attributes: the primary keyword usually equals the product type plus the most searched qualifier.
3. **Choose the channel template** (e.g. Amazon: Brand + Product line + Product type + Key feature + Material + Size/Count + Colour) from the category style guide.
4. **Write the master long title**, then derive each channel version by trimming from the end within its limit, keeping the primary keyword in the first 60–80 characters.
5. **Check compliance:** length, banned characters and words, repeated words, capitalisation, claims.
6. **Write 2–3 variants** for testing where a test tool exists (Amazon Manage Your Experiments, ad copy tests) or plan sequential tests with stable traffic.
7. **Publish and log** the date and old title for each channel.
8. **Measure after 2–4 weeks:** CTR (impressions to clicks) and conversion, compared with the same period before and with traffic changes noted.

## Calculations and Tools

- **Character budget** = channel limit − characters already used by mandatory elements (brand, product type, size/count).
- **Visible-part keyword coverage** = priority keywords present in the first 80 characters ÷ priority keywords.
- **Title CTR** = clicks ÷ impressions (marketplace search or ads); **unit session percentage / conversion** = orders ÷ sessions.
- **Change effect** = (CTR after − CTR before) ÷ CTR before, with the same season and price; only one listing element changed at a time.
- For eBay titles use `title_check.py` in `ebay-seo`.

## Worked Example

*Illustrative example with invented product details.* Handmade leather wallet, RFID blocking, bifold, for men; current Amazon title "Leather Wallet for Men" (22 characters).

- Master attributes: Brand "Oakline", full-grain leather, RFID blocking, bifold, 8 card slots, gift box, colour brown.
- Amazon: "Oakline Mens Leather Wallet – RFID Blocking Bifold, Full-Grain Leather, 8 Card Slots, Gift Box, Brown" (101 characters; primary phrase within the first 40).
- Etsy: "Handmade Leather Wallet for Men, RFID Bifold Wallet, Full Grain Leather, Personalized Gift" (90 characters; "personalized" only if the seller really offers engraving).
- Measure CTR and conversion on both channels 3 weeks before and after, with no price change in between.

## Example Requests

- "Optimise my product title for Amazon and Etsy: handmade leather wallet, RFID blocking, bifold, for men."
- "Rewrite 50 product titles for Walmart from our Amazon titles, following Walmart's style guide length."
- "Give me three title variants to test in Amazon Manage Your Experiments for my main product."

## Output Format

1. Master attribute sheet and keyword mapping.
2. Title per channel with character count and the template used.
3. Compliance check per title (length, banned words/characters, repetition, claims).
4. Test variants and measurement plan with dates.

## Quality Checks

- Each limit and rule checked against the channel's current style guide (marked with the date).
- Every word true for the product; no competitor brands or promotional claims.
- Primary keyword in the first 60–80 characters on every channel.
- Only one listing element changed per measurement window.
- Results compared on the same season and price.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** channel limits read on the style guide with date, CTR and conversion from channel reports.
- **Estimates:** expected CTR uplift, keyword volumes from third-party tools.
- Limits were reviewed in November 2026 and differ by category; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
