---
name: ecommerce-feed-management
description: "AI-powered product feed management and monitoring skill. Designs feed health checks, sync error diagnostics, missing SKU detection, and attribute completeness validation for e-commerce product catalogs. Use when the user asks for help fixing or monitoring product feeds (Google Merchant Center, marketplaces), sync errors, missing SKUs or attributes."
nexscope:
  name: "E-Commerce Feed Management"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "product-feed"
    - "catalog"
    - "monitoring"
    - "data-quality"
  model: "any"
  tokens: "~2000"
  keywords:
    - "ecommerce feed management"
---

# E-Commerce Feed Management

AI-powered product feed management and monitoring skill. Designs feed health checks, sync error diagnostics, missing SKU detection, and attribute completeness validation for e-commerce product catalogs.

## Capabilities

- Generates actionable monitoring & alerts frameworks based on your specific business context
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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-feed-management -g
```

## Usage

**Input:**
Product feed URL/file, marketplace requirements, catalog size

**Output:**
Feed health report, sync error diagnosis, missing SKU detection, attribute completeness audit

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up e-commerce feed management for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
