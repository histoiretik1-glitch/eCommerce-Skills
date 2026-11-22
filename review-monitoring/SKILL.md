---
name: review-monitoring
description: "Set up systematic review monitoring across e-commerce platforms. Track new reviews, detect negative review spikes, monitor competitor reviews, and automate review response workflows. Use when a seller wants alerts on new or negative reviews, to track competitor reviews, or a process to respond to reviews."
metadata:
  nexscope:
    emoji: "👁️"
    category: ecommerce
---

# Review Monitoring 👁️

Set up systematic review monitoring across e-commerce platforms. Track new reviews, detect negative review spikes, monitor competitor reviews, and automate review response workflows.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill review-monitoring -g
```

## Usage

```
Set up a review monitoring system for my products. I sell on Amazon (3 ASINs) and Etsy (15 listings). I want to catch negative reviews within 24 hours.
```

## Capabilities

- Multi-platform review monitoring setup (Amazon, Etsy, Walmart, Shopify)
- Negative review alert framework and response templates
- Review velocity tracking and anomaly detection
- Competitor review monitoring strategy
- Review response best practices by platform
- Review solicitation compliance guide (per platform rules)

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
