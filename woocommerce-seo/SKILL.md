---
name: woocommerce-seo
description: "Optimize WooCommerce stores for search engines. Covers technical SEO, product page optimization, schema markup, site speed, URL structure, and content strategy for organic traffic growth. Use when the user asks for help auditing or improving WooCommerce SEO (technical, product pages, schema, speed, URL structure, content)."
---

# WooCommerce SEO

Optimize WooCommerce stores for search engines. Covers technical SEO, product page optimization, schema markup, site speed, URL structure, and content strategy for organic traffic growth.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** SEO of a WooCommerce store.

Part of: Store and product page SEO. For neighbouring jobs, use the matching skill instead:

- `product-page-seo` — Platform-independent product page SEO: on-page, structured data, speed, content.
- `shopify-seo` — SEO of a Shopify store.

<!-- role-and-scope:end -->

## Capabilities

- Technical SEO audit for WooCommerce sites
- Product page title, meta description, and URL optimization
- Schema markup: Product, Review, FAQ, Breadcrumb
- Site speed optimization (image compression, caching, CDN)
- Category and tag taxonomy strategy
- Internal linking structure for product pages
- Blog content strategy for product-related keywords
- XML sitemap and robots.txt configuration

## Principles and Constraints

How WordPress and WooCommerce behave for SEO, as known at the last review of this skill (November 2026). Items marked **[check]** depend on versions and plugins and must be confirmed on the site.

- **Permalinks:** WooCommerce uses a product base (default `/product/`) and category base (default `/product-category/`), set in Settings > Permalinks; changing them later needs 301 redirects for every URL.
- **Structured data:** WooCommerce outputs basic Product markup; SEO plugins (Yoast WooCommerce SEO, Rank Math, All in One SEO) extend it **[check]**. Avoid two plugins emitting duplicate Product schema.
- **Sitemaps:** WordPress core generates `/wp-sitemap.xml` since 5.5; SEO plugins usually replace it with their own (e.g. `/sitemap_index.xml`) **[check]**. Submit only one in Search Console.
- **Thin and duplicate pages:** product tags, attribute archives, layered-navigation filter parameters (`?filter_`, `?orderby=`, `?min_price=`), cart/checkout/my-account pages and internal search results should not be indexed; handle with noindex (plugin settings) and canonical tags rather than robots.txt blocks on pages already indexed.
- **Variations:** variable products use one URL with variation parameters; keep the canonical on the parent product.
- **Performance is plugin-driven:** page builders, sliders and many plugins slow product pages; use caching (server or plugin), image optimisation (WebP/AVIF), a CDN, and keep the PHP version supported. Core Web Vitals "good": LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1.
- **Scope:** WooCommerce/WordPress implementation. Platform-independent product page work is `product-page-seo`; Shopify stores use `shopify-seo`.

## Data Needed

| Data | Where |
|------|-------|
| WordPress, WooCommerce, theme and SEO plugin versions; active plugins | WP admin > Plugins, Site Health |
| Permalink settings and URL patterns | Settings > Permalinks, a crawl |
| Index coverage, queries, CTR, positions | Google Search Console |
| Crawl of the site (status codes, canonicals, noindex, duplicate titles) | A crawler (e.g. Screaming Frog, Sitebulb) |
| Core Web Vitals per template | Search Console, PageSpeed Insights |
| Structured data output | Rich Results Test on product and category pages |

## Workflow

1. **Inventory the stack:** versions, SEO plugin, caching, page builder; one SEO plugin only.
2. **Crawl the site** and Search Console: list indexable URLs by type (products, categories, tags, attributes, filters, pages, posts) and compare with what should be indexed.
3. **Set indexation rules:** index products, product categories, key pages and blog posts; noindex tags (unless curated), attribute archives, filters, search, cart, checkout, account pages; check canonicals on variations and paginated categories.
4. **Fix the sitemap:** one sitemap from the SEO plugin containing only indexable URLs; submit it; remove the duplicate.
5. **Optimise templates:** product title tag and meta description patterns in the SEO plugin with manual overrides for top products; category pages with an intro text and unique titles; breadcrumbs enabled.
6. **Validate structured data:** single Product schema with offers, reviews (real), brand, GTIN where available; BreadcrumbList.
7. **Improve speed:** caching, image optimisation, remove unused plugins/scripts on product pages, lazy-load below-the-fold images only, measure field data.
8. **Plan content and internal links:** buying guides and comparisons linking to categories; related products; monitor monthly in Search Console.

## Calculations and Tools

- **Indexable waste** = indexable URLs that should not be indexed (tags, filters, search) ÷ total indexable URLs from the crawl.
- **Index rate of products** = indexed product URLs (Search Console) ÷ published products.
- **Duplicate title share** = pages with a title used elsewhere ÷ crawled HTML pages.
- **CTR gap** = expected CTR at position (from the site's own data) − actual CTR, × impressions = click opportunity.
- **Plugin weight** = number of scripts and their transfer size on the product template (browser DevTools coverage), before and after clean-up.

## Worked Example

*Illustrative example with invented figures.* A WooCommerce store with 420 products: the crawl finds 3,860 indexable URLs, of which 2,950 are filter and tag URLs (e.g. `?filter_color=blue`, `/product-tag/gift/`).

- Indexable waste = 2,950 ÷ 3,860 = **76.4%**; Search Console shows 310 of 420 products indexed (73.8%) and many "Crawled – currently not indexed" products.
- Fixes: noindex tags and filter parameters through the SEO plugin, canonical on filtered category URLs to the clean category, one sitemap with products and categories only, category intros for the top 15 categories.
- Re-measure product index rate and organic clicks 6–8 weeks later.

## Example Requests

- "Audit my WooCommerce store SEO and give me a fix list."
- "Thousands of filter and tag URLs from my WooCommerce shop are indexed. How do I clean this up safely?"
- "Set up proper schema markup for my WooCommerce products without duplicate plugins."

## Output Format

1. Stack inventory and plugin conflicts.
2. Index coverage table by URL type: indexable now vs should be.
3. Indexation and canonical rules (plugin settings to change).
4. Template optimisation (title/meta patterns, category intros, breadcrumbs) and structured data validation results.
5. Speed findings and plugin clean-up list.
6. Monthly monitoring sheet.

## Quality Checks

- Only one SEO plugin and one sitemap active.
- Noindex/canonical used for pages already indexed (not robots.txt blocking).
- Permalink changes come with complete 301 redirects.
- Structured data validated after each plugin or theme update.
- Speed measured with field data on product and category templates.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** crawl results, Search Console figures and speed measurements with dates.
- **Estimates:** click opportunity, ranking expectations after clean-up.
- WordPress/WooCommerce behaviour was reviewed in November 2026; confirm items marked [check] for the site's versions.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill woocommerce-seo -g
```

## Usage

Ask your AI agent:

- "Audit my WooCommerce store SEO and give me a fix list."
- "Optimize my product pages for better Google rankings."
- "Set up proper schema markup for my WooCommerce products."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
