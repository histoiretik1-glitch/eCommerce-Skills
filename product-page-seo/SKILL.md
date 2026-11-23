---
name: product-page-seo
description: "Optimize e-commerce product pages for search engine visibility. On-page SEO, structured data, page speed, mobile optimization, and content strategy for Google, Bing, and platform-specific search. Use when a store wants its product pages to rank better in Google, needs structured data (schema), or an on-page SEO audit."
metadata:
  nexscope:
    emoji: "🔎"
    category: ecommerce
---

# Product Page SEO 🔎

Optimize e-commerce product pages for search engine visibility. On-page SEO, structured data, page speed, mobile optimization, and content strategy for Google, Bing, and platform-specific search.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Platform-independent product page SEO: on-page, structured data, speed, content.

Part of: Store and product page SEO. For neighbouring jobs, use the matching skill instead:

- `shopify-seo` — SEO of a Shopify store.
- `woocommerce-seo` — SEO of a WooCommerce store.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill product-page-seo -g
```

## Usage

```
Audit the SEO of my Shopify product page for a yoga mat. URL: [paste URL]. I'm getting zero organic traffic from Google.
```

## Capabilities

- Product page SEO audit framework (title tag, meta description, H1, URL)
- Structured data markup (Product schema, Review schema, FAQ schema)
- Image optimization (alt text, file size, WebP conversion)
- Page speed optimization recommendations
- Mobile usability optimization
- Internal linking strategy for product pages
- Content enrichment (FAQs, buying guides, comparison tables)

## Principles and Constraints

Search engine rules for product pages on any platform, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed in Google Search Central documentation.

- **Structured data:** mark up Product with Offer (price, currency, availability) and, if real, AggregateRating/Review; Google's merchant listing structured data can also carry shipping and return policy details **[check]**. Markup must match visible content; fake or self-serving reviews violate guidelines.
- **FAQ rich results are limited:** since August 2023 Google shows FAQ rich results mainly for authoritative government and health sites, so FAQ schema on a store rarely gives a rich result; keep FAQs for users and long-tail content.
- **One indexable URL per product:** variants via parameters or separate URLs need canonical tags pointing to the main product URL unless variants have their own search demand.
- **Out of stock and discontinued:** keep temporarily out-of-stock pages live with availability marked; redirect permanently discontinued products (301) to the closest product or category.
- **Core Web Vitals "good":** LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at the 75th percentile of real users.
- **Images:** descriptive file names and alt text, modern formats (WebP/AVIF), explicit width/height to avoid layout shift, the main product image crawlable (not only lazy-loaded by script).
- **Scope:** platform-independent product page SEO. Platform specifics are in `shopify-seo` and `woocommerce-seo`; marketplace search (Amazon, eBay) follows different rules (`ebay-seo`); description writing in `product-description-generator`.

## Data Needed

| Data | Where |
|------|-------|
| Product page URLs, their queries, impressions, clicks, CTR, position | Google Search Console (Performance, filtered by page) |
| Indexing status of product URLs | Search Console > Pages, URL inspection |
| Structured data validity | Search Console enhancements (Product snippets, Merchant listings), Rich Results Test |
| Page content: title tag, H1, description length, images, reviews | The page / crawler export |
| Core Web Vitals by template | Search Console, PageSpeed Insights |
| Competing pages ranking for the target queries | Google results |

## Workflow

1. **Pick target queries** per product from Search Console and the keyword map (one primary query per URL).
2. **Check indexing and canonicals:** the product URL is indexed, canonical is self-referencing (or to the main variant), no noindex, included in the sitemap.
3. **Optimise the title tag and H1:** primary query + brand/model + key attribute; title tag unique, about 50–60 characters visible.
4. **Write unique content:** description answering buyer questions (use, size, materials, care, compatibility), specification table, FAQ from real questions; no copied manufacturer text.
5. **Add or fix structured data** (Product, Offer, real reviews, shipping/returns where supported) and validate.
6. **Optimise images and speed** for the product template (LCP image size, lazy-loading below the fold only, CLS fixes).
7. **Link internally:** from categories, related products, buying guides; breadcrumbs with structured data.
8. **Measure** after 4–8 weeks: impressions, clicks, CTR, position per target query; iterate on titles with low CTR.

## Calculations and Tools

- **CTR gap** = expected CTR at current position (from the site's own Search Console data) − actual CTR; **click opportunity** = impressions × CTR gap.
- **Structured data coverage** = product URLs with valid Product markup ÷ product URLs.
- **Index rate** = indexed product URLs ÷ product URLs in the sitemap.
- **Content uniqueness check** = share of description text found on other sites (sample with exact-phrase searches).
- **Template LCP** = 75th percentile LCP for product pages from field data.

## Worked Example

*Illustrative example with invented figures.* A yoga mat page gets zero organic traffic.

- Search Console: URL "Crawled – currently not indexed"; the description is the manufacturer's text found on 40 other sites; the canonical points to a variant URL with a colour parameter.
- Fixes: self-referencing canonical, 250-word unique description with thickness/grip/care facts and a size table, title tag "Non-Slip Yoga Mat 6mm – Natural Rubber | BrandName", Product + Offer markup validated, request indexing.
- After 6 weeks, report impressions/clicks for "non slip yoga mat 6mm" from Search Console; no ranking promise.

## Example Requests

- "Audit the SEO of my product page for a yoga mat: I get zero organic traffic from Google."
- "Which structured data should my product pages have, and why don't my FAQs show in Google?"
- "Fix duplicate content on my product variants and out-of-stock products."

## Output Format

1. Page audit table: URL, target query, indexing, canonical, title/H1, content uniqueness, structured data, CWV, internal links.
2. Rewritten title tag, H1, description outline and FAQ from real questions.
3. Structured data snippet (JSON-LD) matching visible content.
4. Fix list by priority with expected measurement date.

## Quality Checks

- Structured data matches visible content and validates without errors.
- Canonicals and redirects consistent; no indexable duplicate variants without demand.
- Content unique and factual; reviews in markup are genuine.
- Speed measured on mobile field data when available.
- Results reported from Search Console with dates; no guaranteed rankings.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** Search Console, structured data reports and speed measurements with dates.
- **Estimates:** click opportunity, expected ranking changes, third-party keyword volumes.
- Google rules were reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
