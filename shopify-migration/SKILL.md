---
name: shopify-migration
description: "Migration to Shopify. Plans a move from WooCommerce, Magento, BigCommerce or another platform to Shopify: data transfer (products, customers, orders), URL redirects to keep SEO, apps and launch checklist. Use when someone plans or is doing a migration to Shopify."
metadata:
  nexscope:
    category: shopify
---

# Shopify Migration

Platform migration to Shopify — from WooCommerce, Magento, BigCommerce, data transfer, URL redirects.

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Move a store to Shopify from WooCommerce, Magento, BigCommerce or another platform without losing data, rankings or sales.

## Inputs to Collect

Current platform, number of products, variants, customers and orders, custom features and apps, URL structure, top organic landing pages (Search Console), integrations (ERP, 3PL, email), launch deadline.

## Workflow

1. **Inventory of what moves**: products and variants, images, collections/categories, customers (passwords cannot be migrated; plan account invitation emails), orders history, reviews, blog posts, pages, redirects, gift cards.
2. **Migration tool**: Shopify's Store Importer app for supported platforms, CSV imports, or a migration app/service (e.g. Matrixify) for complex catalogs.
3. **Data mapping**: categories to collections, attributes to variants or metafields, customer tags.
4. **URL redirects**: export old URLs, map each to the new Shopify URL, import 301 redirects (Online Store → Navigation → URL redirects, or CSV); start with top traffic pages.
5. **Rebuild features**: theme, apps for the old plugins, payments, shipping, taxes, email flows.
6. **Test** on the unpublished store: imports, redirects, checkout, emails, tracking.
7. **Launch**: switch the domain, submit the sitemap in Search Console, monitor 404 errors, rankings and conversion for 4-8 weeks.

## Output Format

1. Migration scope and data map
2. Tool choice
3. Redirect plan
4. Launch-day checklist and post-launch monitoring

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-migration -g
```

## Example Requests

- "Help me with shopify migration for my Shopify store"
- "What are the best practices for shopify migration?"
- "Audit my current shopify migration setup and suggest improvements"
- "Create a step-by-step shopify migration implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
