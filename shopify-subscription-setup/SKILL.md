---
name: shopify-subscription-setup
description: "Shopify subscription program setup. Sets up recurring orders on Shopify (subscription apps, frequencies, discounts, customer portal) and reduces churn. Use when a Shopify store owner wants to sell subscriptions or subscribe-and-save (for designing the subscription business model use `ecommerce-subscription-model`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Subscription Setup

Subscription program setup — recurring billing, frequency options, churn reduction, lifetime value.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Implementing subscriptions on a Shopify store.

Part of: Subscriptions. For neighbouring jobs, use the matching skill instead:

- `ecommerce-subscription-model` — Designing the subscription offer and business model.

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Implement subscriptions on a Shopify store: app, plans, customer portal and churn controls.

## Inputs to Collect

Products suited to repeat purchase and their usage cycle, planned discount, payment provider (subscription apps need a compatible gateway such as Shopify Payments), expected volume, need for bundles or build-a-box.

The subscription offer itself (model, pricing tiers, economics) is designed with `ecommerce-subscription-model`; this skill puts it in place on Shopify.

## Workflow

1. **App**: Shopify Subscriptions (free, basic needs) or a dedicated app (Recharge, Skio, Loop, Seal…) for advanced portals, bundles and retention tools.
2. **Selling plans**: delivery frequencies matching usage (e.g. every 30/60/90 days), subscribe-and-save discount, minimum commitment if any.
3. **Product page**: clear choice between one-time and subscription, savings shown, frequency selector, "cancel anytime" if true.
4. **Customer portal**: skip, swap, change frequency, pause and cancel; easy changes reduce cancellations.
5. **Dunning**: retry failed payments and email customers to update cards.
6. **Retention**: cancellation flow with alternatives (skip, pause, frequency change), pre-shipment reminder email.
7. **Metrics**: active subscribers, churn rate, average subscription length, revenue per subscriber.

## Output Format

1. App recommendation and setup steps
2. Selling plan configuration
3. Product page and portal changes
4. Retention and dunning flows
5. KPI dashboard

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-subscription-setup -g
```

## Example Requests

- "Help me with shopify subscription setup for my Shopify store"
- "What are the best practices for shopify subscription setup?"
- "Audit my current shopify subscription setup setup and suggest improvements"
- "Create a step-by-step shopify subscription setup implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
