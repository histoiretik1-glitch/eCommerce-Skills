---
name: inventory-tracking-software
description: "Inventory tracking system design. Chooses or designs the tracking setup (spreadsheet, inventory app, ERP), the data each SKU needs, monitoring dashboards, alert rules and multi-channel stock sync so every channel shows the right quantity. Use when a business asks which inventory software to use or how to set up inventory tracking and sync across channels."
nexscope:
  name: "Inventory Tracking Software"
  category: "Supply Chain & Logistics"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "inventory"
    - "stock-management"
    - "monitoring"
    - "supply-chain"
  model: "any"
  tokens: "~2000"
  keywords:
    - "inventory tracking software"
---

# Inventory Tracking Software

AI-powered inventory tracking and monitoring skill for e-commerce businesses. Designs inventory monitoring systems, low-stock alerts, reorder point calculations, and multi-channel sync strategies.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Designing the inventory tracking system: monitoring, alerts and multi-channel sync.

Part of: Inventory and replenishment. For neighbouring jobs, use the matching skill instead:

- `warehouse-optimization` — Warehouse and FBA inventory optimization: safety stock, ABC analysis, IPI, storage costs.
- `restock-alert` — Reorder points, safety stock and stock-out risk for replenishment decisions.
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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill inventory-tracking-software -g
```

## Usage

**Input:**
SKU list, sales velocity data, platform(s), warehouse info

**Output:**
Inventory monitoring framework, low-stock alert rules, reorder point calculations, multi-channel sync strategy

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up inventory tracking software for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
