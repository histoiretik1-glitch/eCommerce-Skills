---
name: shopify-facebook-instagram-shop
description: "Shopify Facebook and Instagram shops. Sets up the Facebook & Instagram channel for a Shopify store: product catalog sync, Facebook Shop, Instagram Shopping, product tags and social checkout. Use when a Shopify store owner wants to sell on Facebook or Instagram or fix catalog sync problems."
metadata:
  nexscope:
    category: shopify
---

# Shopify Facebook & Instagram Shop

Social selling setup — Facebook Shop, Instagram Shopping, product tagging, social checkout.

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Sell through Facebook and Instagram from a Shopify store with a clean product catalog and shoppable posts.

## Inputs to Collect

Meta Business account and Facebook page, Instagram professional account, product catalog size, markets, product categories (some are restricted on Meta), current ad pixel/Conversions API setup.

## Workflow

1. **Install the Facebook & Instagram app** (Meta's sales channel for Shopify) and connect the Meta Business account, page, Instagram account, ad account and pixel.
2. **Data sharing**: enable the maximum data-sharing level the store's consent setup allows (Conversions API improves ad measurement).
3. **Catalog sync**: choose which products sync; fix products rejected for policy, missing GTIN/brand, image or price issues; keep titles and images clean.
4. **Shop setup**: collections for the Facebook and Instagram shop, checkout method available in the region (on Meta or redirect to the Shopify checkout).
5. **Shoppable content**: tag products in posts, Reels and stories; use product stickers; feature collections.
6. **Ads**: catalog-based ads (Advantage+ catalog ads) for retargeting viewers and cart abandoners.
7. **Monitor** catalog errors and sales by channel in Shopify.

## Output Format

1. Connection checklist
2. Catalog issues and fixes
3. Shop collections plan
4. Content and ads plan for the first month

Shopify admin menus, app names and plan features change; confirm in the Shopify Help Center before acting.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-facebook-instagram-shop -g
```

## Example Requests

- "Help me with shopify facebook & instagram shop for my Shopify store"
- "What are the best practices for shopify facebook & instagram shop?"
- "Audit my current shopify facebook & instagram shop setup and suggest improvements"
- "Create a step-by-step shopify facebook & instagram shop implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
