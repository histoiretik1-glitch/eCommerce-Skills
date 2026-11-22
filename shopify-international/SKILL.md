---
name: shopify-international
description: "Shopify Markets international selling. Configures Shopify Markets: multi-currency, translations, domains, duties and taxes, localized prices and content per market. Use when a Shopify store owner wants to sell abroad or set up a new country (for choosing which countries to enter use `cross-border-ecommerce`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify International Selling

Shopify Markets — multi-currency, translation, duties/taxes, localized pricing, market-specific content.

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Sell to other countries from one Shopify store with Shopify Markets: local currencies, languages, domains, duties and prices.

## Inputs to Collect

Target countries (`cross-border-ecommerce` helps choose), current markets setup, payment provider (some features need Shopify Payments), shipping options abroad, product restrictions, translation resources.

## Workflow

1. **Markets**: create a market per country or region; set currency, language and domain or subfolder (e.g. `/fr-ca`).
2. **Pricing**: automatic currency conversion with rounding, or fixed local prices per market for key products; adjust for duties and shipping.
3. **Duties and import taxes**: decide whether buyers pay duties at checkout (delivered duty paid) or on delivery; set HS codes and countries of origin on products.
4. **Translations**: Translate & Adapt or a translation app; translate product content, checkout, notifications and policies; review machine translations of key pages.
5. **Shipping and returns** per market: carriers, delivery estimates, international returns policy.
6. **Payments**: local payment methods per market.
7. **SEO**: market-specific domains/subfolders with hreflang (handled by Shopify for markets), translated URLs and meta tags.
8. **Test** a checkout from each market (currency, taxes, duties, delivery).

## Output Format

1. Market structure (countries, currencies, languages, domains)
2. Pricing and duties approach per market
3. Translation plan
4. Launch checklist per market

Shopify admin menus, app names and plan features change; confirm in the Shopify Help Center before acting.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-international -g
```

## Example Requests

- "Help me with shopify international selling for my Shopify store"
- "What are the best practices for shopify international selling?"
- "Audit my current shopify international selling setup and suggest improvements"
- "Create a step-by-step shopify international selling implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
