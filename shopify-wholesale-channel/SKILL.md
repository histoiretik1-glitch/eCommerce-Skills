---
name: shopify-wholesale-channel
description: "Shopify B2B and wholesale. Sets up wholesale selling on Shopify: B2B catalogs and price lists, minimum orders, payment terms, wholesale customer accounts or a separate wholesale store. Use when a Shopify store owner wants to sell to retailers or businesses."
metadata:
  nexscope:
    category: shopify
---

# Shopify Wholesale Channel

B2B/wholesale setup — wholesale pricing, minimum orders, custom catalogs, net payment terms.

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Sell wholesale (B2B) from Shopify: price lists, minimums, payment terms and a buying experience for retailers.

## Inputs to Collect

Shopify plan, number of wholesale customers, wholesale prices and minimums, payment terms needed (e.g. net 30), whether B2B and retail should share one store, catalog differences.

## Options

- **B2B on Shopify** (Shopify Plus): company accounts, catalogs with price lists, quantity rules, payment terms, B2B checkout in the same store. It replaced the older separate Wholesale channel.
- **Other plans**: wholesale apps (price lists by customer tag, order forms, minimums), or a separate wholesale store.

## Workflow

1. **Policy**: who qualifies, application form, minimum order value or quantities, pricing (often a discount from retail), payment terms, shipping rules.
2. **Customer setup**: companies/locations (Plus) or tagged customers (apps); approval process.
3. **Catalog and prices**: price lists per customer group, case packs and quantity increments, products hidden from retail if needed.
4. **Ordering**: quick order form, reorder from past orders, draft orders for phone/email orders.
5. **Payments**: credit card, invoices with payment terms, deposits; reminders for overdue invoices.
6. **Operations**: separate fulfillment priorities, packing slips, wholesale-specific emails.

## Output Format

1. Recommended setup (B2B on Plus, app or separate store) and why
2. Wholesale policy draft
3. Configuration steps
4. Wholesale customer onboarding email

Shopify admin menus, app names and plan features change; confirm in the Shopify Help Center before acting.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-wholesale-channel -g
```

## Example Requests

- "Help me with shopify wholesale channel for my Shopify store"
- "What are the best practices for shopify wholesale channel?"
- "Audit my current shopify wholesale channel setup and suggest improvements"
- "Create a step-by-step shopify wholesale channel implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
