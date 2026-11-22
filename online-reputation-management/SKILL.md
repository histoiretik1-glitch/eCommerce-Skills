---
name: online-reputation-management
description: "AI-powered online reputation management skill for e-commerce brands. Builds reputation monitoring frameworks, negative review response strategies, rating recovery plans, and crisis communication templates. Use when the user asks for help managing brand reputation, responding to negative reviews, recovering ratings or handling a PR crisis."
nexscope:
  name: "Online Reputation Management"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "reputation"
    - "brand-monitoring"
    - "crisis-management"
    - "review-management"
  model: "any"
  tokens: "~2000"
  keywords:
    - "online reputation management"
---

# Online Reputation Management

AI-powered online reputation management skill for e-commerce brands. Builds reputation monitoring frameworks, negative review response strategies, rating recovery plans, and crisis communication templates.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Brand-level reputation: monitoring framework, rating recovery and crisis communication.

Part of: Reviews, feedback and reputation. For neighbouring jobs, use the matching skill instead:

- `product-review-analysis` — Deep analysis of product reviews: pain points, praise, feature requests, sentiment.
- `customer-feedback-analysis` — Analysis of all customer feedback channels (reviews, surveys, tickets) into improvement priorities.
- `review-monitoring` — Ongoing review monitoring: alerts on new or negative reviews and the response workflow.

<!-- role-and-scope:end -->

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill online-reputation-management -g
```

## Usage

**Input:**
Brand name, product name, or store URL

**Output:**
Reputation monitoring plan, negative review response templates, rating recovery roadmap, crisis response playbook

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up online reputation management for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
