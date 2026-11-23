---
name: ecommerce-keyword-research
description: "Cross-platform keyword research for e-commerce. Discover high-converting keywords across Amazon, Shopify, Etsy, Google Shopping, TikTok Shop, and Walmart. Analyzes search volume signals, competition indicators, commercial intent, and long-tail opportunities. Use when a seller asks which keywords to target for product titles, listings, ads or SEO on one or several marketplaces."
metadata:
  nexscope:
    emoji: "🔍"
    category: ecommerce
---

# E-Commerce Keyword Research 🔍

Cross-platform keyword research for e-commerce. Discover high-converting keywords across Amazon, Shopify, Etsy, Google Shopping, TikTok Shop, and Walmart. Analyzes search volume signals, competition indicators, commercial intent, and long-tail opportunities.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Cross-channel keyword map: discovery, intent, priority scores and seasonal calendar.

Part of: Keywords, titles and product copy. For neighbouring jobs, use the matching skill instead:

- `product-title-optimization` — Writing compliant product titles for each channel from one verified attribute set.
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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-keyword-research -g
```

## Usage

```
Find the best keywords for my bamboo cutting board. I sell on Amazon US and my own Shopify store.
```

## Capabilities

- Cross-platform keyword discovery (Amazon, Google, Etsy, Walmart, TikTok)
- Long-tail keyword expansion with commercial intent scoring
- Keyword grouping by search intent (informational, commercial, transactional)
- Competition assessment based on keyword structure and modifier analysis
- Seasonal trend identification and keyword calendar planning
- Platform-specific keyword optimization (Amazon A9, Etsy SEO, Google Shopping)

## Principles and Constraints

How keyword data behaves on each channel, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed in the channel's documentation.

- **Each channel has its own searchers and data source:** Google (Keyword Planner volume ranges unless you advertise, Search Console queries for your site), Amazon (Brand Analytics: Search Query Performance and Top Search Terms for brand-registered sellers **[check]**, autocomplete, Sponsored Products search term reports), Etsy (search bar suggestions, Etsy Ads keywords), Walmart (autocomplete, Ad Center search term reports), TikTok (search suggestions and Creative Center).
- **Third-party volumes are estimates:** Helium 10, Jungle Scout, Semrush, Ahrefs and similar tools model volumes; use them to rank keywords, not as exact counts, and say which tool and date.
- **Intent decides the page:** transactional and product-specific queries → product pages and marketplace listings; category queries → collection pages; informational queries → content.
- **Respect listing policies:** no competitor brand names, no keyword stuffing, no irrelevant terms; Amazon backend search terms have a byte limit (249 bytes in many marketplaces **[check]**).
- **Language and locale matter:** "cutting board" vs "chopping board" (US vs UK); research each marketplace separately.
- **Hand-off:** this skill builds the cross-channel keyword map. Writing titles is `product-title-optimization`; product page SEO `product-page-seo`; Etsy tags `etsy-keyword-research`; eBay titles and specifics `ebay-seo`.

## Data Needed

| Data | Where |
|------|-------|
| Product facts: type, material, size, uses, audience, compatibility | Catalogue |
| Seed terms customers use | Reviews, customer questions, support tickets |
| Search suggestions per channel | Autocomplete on Google, Amazon, Etsy, Walmart, TikTok |
| Volumes / rankings per channel | Keyword Planner, Brand Analytics, third-party tool (with date) |
| Your current queries and conversions | Search Console, ad search term reports |
| Competitor titles and listings | Top-ranking listings per channel |

## Workflow

1. **Collect seed terms** from product facts and customer language (reviews, questions): product type, materials, use cases, problems solved.
2. **Expand per channel** with autocomplete (add a–z after the seed), related searches and ad search term reports; keep the channel next to each term.
3. **Add data:** volume or rank from the channel source first, third-party estimates second; mark the source and date of each figure.
4. **Classify intent** (informational, commercial investigation, transactional) and relevance (3 = exactly this product, 2 = close, 1 = related).
5. **Assess competition** per term: number of results, strength of top listings (reviews, brands), ad density.
6. **Score and group** terms into clusters (one primary term per page or listing, secondary terms and attributes).
7. **Map clusters to assets:** marketplace title/bullets/backend terms, product page, collection page, ad groups, content.
8. **Build the seasonal calendar** from monthly trends and re-check every quarter with actual search term reports.

## Calculations and Tools

- **Priority score** (this skill's formula) = volume index × relevance (1–3) × intent weight (transactional 1.0, commercial 0.7, informational 0.3) ÷ competition (1 low – 3 high).
- **Volume index** = term volume ÷ the largest volume in the list (keeps different sources comparable within one channel).
- **Seasonality index** = monthly volume ÷ average monthly volume; above 1.3 marks a peak month (working rule).
- **Search term conversion** (from ad reports) = orders ÷ clicks per term: the best relevance check you have.
- **Coverage** = priority terms used in the listing (title, bullets, backend, attributes) ÷ priority terms mapped to it.

## Worked Example

*Illustrative example with invented figures.* Bamboo cutting board sold on Amazon US and Shopify.

- Amazon autocomplete gives "bamboo cutting board set", "bamboo cutting board with juice groove", "large bamboo cutting board"; Google adds "is bamboo cutting board safe" (informational).
- Scores: "bamboo cutting board set" volume index 1.0 × relevance 3 × 1.0 ÷ competition 3 = **1.0**; "bamboo cutting board with juice groove" 0.35 × 3 × 1.0 ÷ 1 = **1.05** (smaller but easier, exact match to the product); "is bamboo cutting board safe" 0.4 × 2 × 0.3 ÷ 2 = 0.12 → blog/FAQ content.
- Map: Amazon title leads with "Bamboo Cutting Board with Juice Groove", set terms in bullets; Shopify product page title follows Google wording; FAQ answers the safety question.

## Example Requests

- "Find the best keywords for my bamboo cutting board for Amazon US and my Shopify store."
- "Build a keyword map for 30 kitchen products across Amazon, Walmart and Google."
- "Which keywords should go in my Amazon backend search terms and which in the title for this product?"

## Output Format

1. Keyword table: term, channel, source and date of volume, intent, relevance, competition, priority score.
2. Clusters with the primary term and secondary terms.
3. Asset map: where each cluster is used (listing fields, pages, ad groups, content).
4. Seasonal calendar by month and channel.
5. Review plan using search term reports.

## Quality Checks

- Each figure carries its source and date; third-party volumes labelled as estimates.
- No competitor brand names or irrelevant terms in listing recommendations.
- Each page or listing has one primary term; no two pages target the same primary term.
- Locale spelling checked per marketplace.
- Recommendations re-validated with real search term conversion data when available.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** Search Console and ad search term data, Brand Analytics figures, observed autocomplete suggestions with date.
- **Estimates:** third-party search volumes, competition scores, expected traffic.
- Channel data sources were reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
