---
name: shopify-inventory-management
description: "Shopify inventory management across locations. Sets up locations and fulfillment priority, inventory tracking per variant, transfers and receiving, cycle counts, low-stock alerts with Shopify Flow and Shopify inventory reports. Use when a Shopify store owner asks how to track or organize stock in Shopify or manage several warehouses or stores (for reorder formulas use `restock-alert`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Inventory Management

Multi-location inventory — transfers, low stock alerts, demand forecasting, safety stock, ABC analysis.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Managing stock in Shopify across locations.

Part of: Inventory and replenishment. For neighbouring jobs, use the matching skill instead:

- `warehouse-optimization` — Warehouse and FBA inventory optimization: safety stock, ABC analysis, IPI, storage costs.
- `restock-alert` — Reorder points, safety stock and stock-out risk for replenishment decisions.
- `inventory-tracking-software` — Designing the inventory tracking system: monitoring, alerts and multi-channel sync.
- `tiktok-shop-inventory` — Stock planning for viral demand on TikTok Shop.

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Keep Shopify stock accurate across locations and reorder before products run out.

## Inputs to Collect

Locations (warehouse, store, 3PL), how stock is updated (manual, POS, 3PL integration), number of SKUs, sales per SKU, supplier lead times, current stock-outs and overstock.

## Workflow

1. **Locations**: set up each location and its fulfillment priority; decide which locations sell online.
2. **Tracking**: turn on inventory tracking for every variant; decide per product whether to allow selling when out of stock (pre-orders only with a clear message).
3. **Transfers and receiving**: record incoming stock and transfers between locations instead of editing quantities by hand.
4. **Counts**: regular cycle counts on fast movers; adjust with a reason so history stays clear.
5. **Reorder points** per SKU from daily sales and lead time (formulas in `restock-alert`); low-stock alerts with Shopify Flow or an inventory app.
6. **ABC analysis**: A items (most revenue) get tighter control and safety stock (`warehouse-optimization` covers the method).
7. **Reports**: inventory value, days of cover, sell-through and aged stock from Shopify's inventory reports.

## Output Format

1. Location and fulfillment setup
2. Reorder point and safety stock per key SKU
3. Alert rules (Flow or app)
4. Weekly inventory routine

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-inventory-management -g
```

## Example Requests

- "Help me with shopify inventory management for my Shopify store"
- "What are the best practices for shopify inventory management?"
- "Audit my current shopify inventory management setup and suggest improvements"
- "Create a step-by-step shopify inventory management implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
