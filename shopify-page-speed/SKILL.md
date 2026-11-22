---
name: shopify-page-speed
description: "Shopify Core Web Vitals diagnosis. Reads Shopify's web performance report and PageSpeed Insights (LCP, INP, CLS) per template, finds which pages and elements cause slow loading or layout shifts, and explains the measurements. Use when a Shopify store owner asks what their speed score or Core Web Vitals mean or which pages are slow (for the fix plan use `shopify-speed-optimization`)."
nexscope:
  name: "Shopify Page Speed"
  category: "Site Performance"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "shopify"
    - "page-speed"
    - "performance"
    - "core-web-vitals"
  model: "any"
  tokens: "~2000"
  keywords:
    - "shopify page speed"
---

# Shopify Page Speed

AI-powered Shopify page speed optimization skill. Diagnoses performance bottlenecks, provides Core Web Vitals improvement plans, and recommends theme and app optimizations for faster Shopify stores.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Measuring Core Web Vitals and diagnosing which pages and elements are slow.

Part of: Shopify store speed. For neighbouring jobs, use the matching skill instead:

- `shopify-speed-optimization` — Full speed audit of a Shopify store and the prioritized fix plan (apps, images, scripts, theme).
- `shopify-theme-optimization` — Choosing and tuning the Shopify theme itself: Liquid code, sections, mobile UX.

<!-- role-and-scope:end -->

## Capabilities

- Generates actionable site performance frameworks based on your specific business context
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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-page-speed -g
```

## Usage

**Input:**
Shopify store URL, current theme, installed apps

**Output:**
Speed diagnostic report, Core Web Vitals improvement plan, theme optimization guide, app performance audit

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up shopify page speed for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
