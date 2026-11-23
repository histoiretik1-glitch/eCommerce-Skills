---
name: shopify-seo
description: "Comprehensive Shopify SEO optimization guide. Technical SEO, on-page optimization, collection pages, blog strategy, site architecture, and link building for Shopify stores. Use when the user asks for help auditing or improving Shopify SEO (technical, product and collection pages, blog, schema, internal links)."
---

# Shopify SEO

Comprehensive Shopify SEO optimization guide. Technical SEO, on-page optimization, collection pages, blog strategy, site architecture, and link building for Shopify stores.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** SEO of a Shopify store.

Part of: Store and product page SEO. For neighbouring jobs, use the matching skill instead:

- `product-page-seo` — Platform-independent product page SEO: on-page, structured data, speed, content.
- `woocommerce-seo` — SEO of a WooCommerce store.

<!-- role-and-scope:end -->

## Capabilities

- Technical SEO audit: site speed, mobile, crawlability, indexing
- Product page SEO: titles, meta descriptions, image alt text
- Collection page optimization and URL structure
- Blog content strategy for organic traffic
- Internal linking and site architecture
- Schema markup for Shopify (Product, FAQ, Breadcrumb)
- Shopify SEO app recommendations and setup
- Duplicate content handling (variants, pagination)

## Platform Rules and Constraints

How Shopify handles SEO technically, at the last review of this skill (November 2026, Shopify Help Center > Online store > SEO). Items marked **[check]** must be confirmed.

- **Fixed URL structure:** /products/handle, /collections/handle, /pages/handle, /blogs/blog-name/article-handle. Prefixes cannot be removed; only handles can be edited.
- **Duplicate product paths:** products are also reachable at /collections/x/products/handle; Shopify themes set the canonical to /products/handle. Variant URLs (?variant=) canonicalise to the product.
- **Redirects:** when a handle is changed, tick "Create a URL redirect" (or add it in Content/Online Store > Navigation > URL redirects) to keep links and rankings.
- **Title tag and meta description** per product, collection, page and article in the "Search engine listing" section; Shopify shows a character counter (about 70 characters for titles and 320 for descriptions **[check]**); Google truncates around 600 px of title width.
- **sitemap.xml** is generated automatically (products, collections, pages, blogs, images) and **robots.txt** can be customised through robots.txt.liquid; do not block /collections or /products.
- **Structured data** (Product, Offer, BreadcrumbList, Organization) comes from the theme; check it with Google's Rich Results Test and fix gaps in the theme or an app.
- **International:** Shopify Markets adds hreflang tags for market subfolders or domains automatically **[check]**.
- **Thin pages:** tag-filtered collection URLs (/collections/x/tag) and search pages can create many thin pages; keep them out of internal links unless they are curated.
- **Domain:** set one primary domain; other domains and the myshopify.com address redirect to it.

## Data Needed

| Data | Where |
|------|-------|
| Indexing status, queries, impressions, clicks, CTR, position per page | Google Search Console (Pages and Performance reports) |
| Organic sessions and sales by landing page | Shopify Analytics > Sessions by landing page (referrer: search) or GA4 |
| Product, collection and blog content, title tags, meta descriptions | Shopify admin, or bulk via product CSV export |
| Structured data validity | Search Console enhancement reports, Rich Results Test |
| Speed (Core Web Vitals) | Search Console > Core Web Vitals, PageSpeed Insights |
| Competitor pages ranking for target queries | Google search results for the target queries |

## Workflow

1. **Connect Search Console** (domain property), submit /sitemap.xml and check the Pages report for "Crawled – not indexed", duplicates and redirect issues.
2. **Map keywords to page types:** category-level queries → collection pages; specific product and model queries → product pages; how-to and comparison queries → blog articles. One primary query per URL.
3. **Optimise collection pages:** unique title tag and meta description, an intro paragraph above or below the grid (100–300 words) with the primary query, internal links to sub-collections.
4. **Optimise product pages:** title tag with product name + key attribute, unique description (no copied manufacturer text), image alt text describing the image, reviews visible, Product structured data valid.
5. **Fix technical issues:** handle changes with redirects, broken links (404s in Search Console), duplicate content from tags, internal links that point to /collections/x/products/ paths instead of /products/.
6. **Build internal links:** main navigation to key collections, breadcrumbs, related products, blog articles linking to collections.
7. **Plan the blog:** articles for informational queries with a clear link to the relevant collection; update or merge articles that get no impressions after 6 months.
8. **Measure monthly** in Search Console: clicks, impressions, CTR and average position for the mapped queries; rewrite title tags of pages with many impressions and low CTR.

## Calculations and Tools

- **CTR** = clicks ÷ impressions (Search Console).
- **Title-rewrite priority** = impressions × (expected CTR at the current position − actual CTR); use the site's own CTR by position from Search Console as the expected curve, not an external benchmark.
- **Index coverage** = indexed product + collection URLs ÷ URLs in the sitemap.
- **Content gap** = target queries with no mapped page, or mapped to a page ranking beyond position 20.
- **Title length** check: characters ≤ the Shopify counter and the main term in the first 50 characters.

## Worked Example

*Illustrative example with invented figures.* A collection "Linen Aprons" has 18,000 impressions over the last 3 months and 0.9% CTR at average position 6.2; the store's own Search Console data shows 3.5% CTR for other pages at positions 5–7.

- Priority = 18,000 × (0.035 − 0.009) ≈ **468 extra clicks/quarter** (estimate) if CTR reached the store's own average.
- Fix: title "Linen Aprons for Women & Men | Handmade in Portugal – BrandName" (63 characters), meta description with delivery and returns, 180-word intro with links to "Kids Aprons" and "Tea Towels".
- Check 4–6 weeks later in Search Console with the same date length.

## Example Requests

- "Audit the SEO of my Shopify store: indexing issues, duplicate URLs, title tags and structured data."
- "My Shopify collection 'linen aprons' has 18,000 impressions but under 1% CTR. Rewrite its title tag, meta description and intro."
- "Plan 12 blog articles for my Shopify kitchenware store that link to the right collections."

## Output Format

1. Technical audit table: issue, affected URLs (count and examples), fix, priority.
2. Keyword-to-page map: query, page type, URL, current position and CTR.
3. Rewritten title tags, meta descriptions and collection intros (with character counts).
4. Internal linking and blog plan.
5. Monthly measurement sheet with baseline from Search Console.

## Quality Checks

- Every changed handle has a redirect; no internal link points to a collection-scoped product path.
- One primary query per URL; no two pages targeting the same query.
- Title tags unique across the store and within the Shopify counter limit.
- Structured data validated after theme or app changes.
- Recommendations based on the store's Search Console data, not on generic keyword volumes alone.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** Search Console and Shopify figures for stated dates, URL lists from the store's sitemap.
- **Estimates:** extra clicks from title rewrites, keyword volumes from third-party tools, ranking expectations.
- Shopify SEO behaviour was reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-seo -g
```

## Usage

Ask your AI agent:

- "Run an SEO audit on my Shopify store."
- "Optimize my Shopify collection pages for better rankings."
- "Create a blog content plan to drive organic traffic to my store."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
