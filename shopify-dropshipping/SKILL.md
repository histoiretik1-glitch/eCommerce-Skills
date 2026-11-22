---
name: shopify-dropshipping
description: "Shopify dropshipping setup and scaling. Connects suppliers and dropshipping apps to a Shopify store, sets pricing and margins, automates orders and handles shipping times and customer service. Use when someone wants to start or scale a dropshipping store on Shopify (to find products use `dropshipping-product-research`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Dropshipping

Dropshipping setup and scaling — supplier integration, automation, pricing strategy, customer experience.

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Set up and scale a Shopify dropshipping store with reliable suppliers, honest delivery times and healthy margins.

## Inputs to Collect

Niche and products (`dropshipping-product-research` for selection), target countries, supplier platforms considered, product cost and shipping time per supplier, budget for ads, store status.

## Workflow

1. **Supplier app**: connect a supplier platform (e.g. DSers for AliExpress, Spocket, Syncee, Zendrop, CJ Dropshipping) and compare shipping times to the main market, product quality (order samples) and branding options.
2. **Product import**: rewrite titles and descriptions (never keep supplier text), own photos where possible, correct variants and weights.
3. **Pricing**: landed cost + payment fees + expected ad cost per order + returns; check with `profit-margin-calculator-shopify`.
4. **Shipping and policies**: show realistic delivery times on product pages and in the shipping policy; clear returns process with the supplier.
5. **Order automation**: auto-fulfillment rules, tracking sync, out-of-stock and price-change alerts from the supplier app.
6. **Customer experience**: order confirmation that explains shipping time, proactive delay messages, support templates.
7. **Scale**: move winners to faster suppliers or local warehouses, add bundles and post-purchase upsells.

## Output Format

1. Supplier comparison and choice
2. Store setup checklist (products, policies, automation)
3. Pricing table per product
4. Customer communication templates
5. Scaling plan

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-dropshipping -g
```

## Example Requests

- "Help me with shopify dropshipping for my Shopify store"
- "What are the best practices for shopify dropshipping?"
- "Audit my current shopify dropshipping setup and suggest improvements"
- "Create a step-by-step shopify dropshipping implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
