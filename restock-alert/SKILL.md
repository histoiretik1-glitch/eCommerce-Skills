---
name: restock-alert
description: "Restock alert and replenishment planning. Calculates reorder points, safety stock and stockout risk per SKU from sales velocity and supplier lead time, and tells the seller when and how much to reorder to avoid lost sales. Use when a seller asks when to reorder, how much safety stock to keep, or how to avoid running out of stock."
nexscope:
  name: "Restock Alert"
  category: "Supply Chain & Logistics"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "inventory"
    - "restock"
    - "supply-chain"
    - "alerts"
  model: "any"
  tokens: "~2000"
  keywords:
    - "restock alert"
---

# Restock Alert

AI-powered restock alert and replenishment planning skill. Calculates optimal reorder points, safety stock levels, and stockout risk scores to prevent lost sales from inventory gaps.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Reorder points, safety stock and stock-out risk for replenishment decisions.

Part of: Inventory and replenishment. For neighbouring jobs, use the matching skill instead:

- `warehouse-optimization` — Warehouse and FBA inventory optimization: safety stock, ABC analysis, IPI, storage costs.
- `inventory-tracking-software` — Designing the inventory tracking system: monitoring, alerts and multi-channel sync.
- `shopify-inventory-management` — Managing stock in Shopify across locations.
- `tiktok-shop-inventory` — Stock planning for viral demand on TikTok Shop.

<!-- role-and-scope:end -->

## Capabilities

- Generates actionable supply chain & logistics frameworks based on your specific business context
- Works across major e-commerce platforms (Amazon, Shopify, Walmart, WooCommerce, Etsy, TikTok Shop)
- Provides data-driven recommendations with industry benchmarks
- Outputs ready-to-implement plans, not just generic advice

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill restock-alert -g
```

## Usage

**Input:**
SKU data, sales velocity, lead times, storage costs

**Output:**
Restock alert rules, safety stock calculations, reorder timing windows, stockout risk scores

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up restock alert for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
