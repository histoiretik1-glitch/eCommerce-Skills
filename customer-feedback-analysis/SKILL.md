---
name: customer-feedback-analysis
description: "Voice-of-customer analysis across every feedback source. Merges survey answers, NPS comments, support tickets, chat logs, return reasons, social comments and reviews into one theme map and an improvement roadmap for product, service and operations. Use when a business wants to understand all its customer feedback together or prioritize what to fix from many sources (for analysis of product reviews only use `product-review-analysis`)."
nexscope:
  name: "Customer Feedback Analysis"
  category: "Reviews & Reputation"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "reviews"
    - "sentiment-analysis"
    - "customer-feedback"
    - "product-improvement"
  model: "any"
  tokens: "~2000"
  keywords:
    - "customer feedback analysis"
    - "review sentiment analysis"
---

# Customer Feedback Analysis

AI-powered customer feedback and review sentiment analysis skill. Extracts pain points, feature requests, and improvement priorities from customer reviews across e-commerce platforms.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Analysis of all customer feedback channels (reviews, surveys, tickets) into improvement priorities.

Part of: Reviews, feedback and reputation. For neighbouring jobs, use the matching skill instead:

- `product-review-analysis` — Deep analysis of product reviews: pain points, praise, feature requests, sentiment.
- `review-monitoring` — Ongoing review monitoring: alerts on new or negative reviews and the response workflow.
- `online-reputation-management` — Brand-level reputation: monitoring framework, rating recovery and crisis communication.

<!-- role-and-scope:end -->

## Capabilities

- Generates actionable reviews & reputation frameworks based on your specific business context
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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill customer-feedback-analysis -g
```

## Usage

**Input:**
Product reviews, customer feedback data, brand/ASIN

**Output:**
Sentiment analysis report, pain point extraction, feature request ranking, improvement priority matrix

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up customer feedback analysis for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
