---
name: google-shopping-optimization
description: "Google Shopping and Performance Max campaign strategy for any store. Structures campaigns and asset groups, sets bidding and ROAS targets, splits budgets by product performance, and uses feed quality as a lever for campaign results. Use when a seller asks how to run, structure or improve Google Shopping or Performance Max ads and their ROAS (to connect a Shopify store to Merchant Center use `shopify-google-channel`; to fix feed errors on any channel use `ecommerce-feed-management`)."
metadata:
  nexscope:
    emoji: "🛒"
    category: ecommerce
---

# Google Shopping Optimization 🛒

Optimize Google Shopping campaigns and product feeds for maximum visibility and ROAS. Feed optimization, bidding strategy, campaign structure, and Performance Max integration.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Google Shopping and Performance Max campaign strategy, bids and ROAS.

Part of: Google Shopping and product feeds. For neighbouring jobs, use the matching skill instead:

- `shopify-google-channel` — Connecting a Shopify store to Google with the Google & YouTube channel and Merchant Center.
- `ecommerce-feed-management` — Monitoring and fixing product feeds for any channel (sync errors, missing SKUs, attributes).

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill google-shopping-optimization -g
```

## Usage

```
Optimize my Google Shopping feed. I have 200 products on Shopify. Current ROAS is 3x, I want to hit 5x. Monthly budget: $5,000.
```

## Capabilities

- Product feed optimization (titles, descriptions, images, attributes)
- Google Merchant Center compliance and error resolution
- Campaign structure (Standard Shopping vs Performance Max)
- Bidding strategy selection and optimization
- Product segmentation and priority campaign structure
- ROAS optimization by product group
- Negative keyword management for Shopping campaigns

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
