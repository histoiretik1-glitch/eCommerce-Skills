---
name: competitor-price-tracker
description: "Set up competitor price tracking and monitoring workflows. Track price changes, detect promotions, analyze pricing patterns, and get alerts for competitive price movements. Use when a seller wants to monitor competitor prices over time, detect promotions or price drops, or decide how to respond to a price war (for one-off pricing analysis use `competitor-price-analysis`)."
metadata:
  nexscope:
    emoji: "📊"
    category: ecommerce
---

# Competitor Price Tracker 📊

Set up competitor price tracking and monitoring workflows. Track price changes, detect promotions, analyze pricing patterns, and get alerts for competitive price movements.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Ongoing tracking of competitor prices with alerts.

Part of: Pricing. For neighbouring jobs, use the matching skill instead:

- `competitor-price-analysis` — One-off analysis of competitor prices and positioning.
- `competitive-pricing-strategy` — Price architecture and response rules against competitors.
- `dynamic-pricing-ecommerce` — Automated repricing rules with floors, ceilings and guardrails.
- `price-optimization-tool` — Choosing a price from unit economics, elasticity and price tests.
- `walmart-price-tracker` — Walmart-specific price tracking and repricing.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill competitor-price-tracker -g
```

## Usage

```
Help me track pricing for 10 competitor products on Amazon. I want to know when they change prices or run promotions so I can respond quickly.
```

## Capabilities

- Competitor price monitoring setup methodology
- Price change detection and alert framework
- Promotional pricing pattern analysis (frequency, depth, timing)
- Price war detection and response strategy
- MAP violation monitoring setup
- Historical price trend analysis methodology

## How This Skill Works

**Step 1:** Collect information from the user's message — product, platform, current situation, and goals.

**Step 2:** Ask one follow-up with all remaining questions using multiple-choice format. Allow shorthand answers (e.g., "1b 2c 3a").

**Step 3:** Research and analyze using the frameworks and methodology below.

**Step 4:** Deliver structured, actionable output with specific recommendations, not vague advice.

## Output Format

- Start with a summary of findings
- Include specific data points and benchmarks where available
- Provide prioritized action items
- Mark estimates with ⚠️ when based on incomplete data
- End with concrete next steps

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
