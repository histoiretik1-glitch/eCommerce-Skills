---
name: shopify-email-flows
description: "Shopify email automations setup. Turns on and configures the core automated flows of a Shopify store in priority order (welcome, abandoned checkout, browse abandonment, post-purchase, win-back, replenishment) in Shopify Email or Klaviyo, with triggers, timing and filters. Use when a Shopify store owner asks which automations to turn on or how to configure them (see `ecommerce-email-marketing-builder` for a complete program with copywriting)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Email Flows

Email automation flows — welcome series, abandoned cart, post-purchase, win-back, browse abandonment.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Setting up the core automated email flows of a Shopify store.

Part of: Email marketing. For neighbouring jobs, use the matching skill instead:

- `ecommerce-email-marketing-builder` — Complete email program with flows, copy, segmentation and ESP setup, for any store.

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Set up the core automated email flows of a Shopify store, in the order that brings the most revenue first.

## Inputs to Collect

Email tool (Shopify Email and marketing automations, Klaviyo, Omnisend…), list size and signup sources, existing automations and their results, brand voice, average order value and repeat rate.

## Flows in Priority Order

| Flow | Trigger | Emails | Goal |
|------|---------|--------|------|
| Welcome | Newsletter signup | 3-4 over 1-2 weeks | First purchase |
| Abandoned checkout | Checkout started, not completed | 2-3 over 72 h | Recover the order |
| Abandoned cart / browse | Product added or viewed | 1-2 | Bring back browsers |
| Post-purchase | Order placed / delivered | 2-3 | Reassure, educate, ask for a review |
| Win-back | No order for X days | 2-3 | Second or next purchase |
| Replenishment | Expected reorder date | 1-2 | Repeat purchase of consumables |

## Workflow

1. Check consent settings and that signups flow into the tool (Shopify customer marketing status).
2. Build flows in the order above; start with simple text-and-image templates in brand style.
3. Personalize with product blocks and customer data (first name, last product).
4. Exclude recent buyers from promotional emails; avoid stacking discounts across flows.
5. Measure revenue per recipient, conversion and unsubscribe rates per flow; improve the weakest email first.

## Output Format

1. Flow map with triggers, timing and filters
2. Subject lines and outline of each email
3. Setup steps in the chosen tool
4. KPIs and review cadence

For a complete email program with full copywriting, use `ecommerce-email-marketing-builder`.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-email-flows -g
```

## Example Requests

- "Help me with shopify email flows for my Shopify store"
- "What are the best practices for shopify email flows?"
- "Audit my current shopify email flows setup and suggest improvements"
- "Create a step-by-step shopify email flows implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
