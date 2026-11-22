---
name: restock-alert
description: "AI-powered restock alert and replenishment planning skill. Calculates optimal reorder points, safety stock levels, and stockout risk scores to prevent lost sales from inventory gaps. Use when the user asks for help calculating reorder points, safety stock, stockout risk or planning replenishment."
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
