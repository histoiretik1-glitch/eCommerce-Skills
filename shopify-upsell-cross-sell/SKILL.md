---
name: shopify-upsell-cross-sell
description: "Shopify upsell and cross-sell strategy. Adds product recommendations, cart and checkout upsells, post-purchase offers and bundles to a Shopify store to raise average order value. Use when a Shopify store owner wants higher AOV or asks which upsell apps and offers to use."
metadata:
  nexscope:
    category: shopify
---

# Shopify Upsell & Cross-Sell

Upsell and cross-sell strategy — product recommendations, cart upsells, post-purchase offers, bundles.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Upsell and cross-sell offers on a Shopify store.

Part of: Retention, loyalty and personalization. For neighbouring jobs, use the matching skill instead:

- `ecommerce-customer-retention` — Retention from order data: cohorts, RFM segments, lifecycle flows with holdouts.
- `ecommerce-personalization` — Personalising site content and recommendations by segment, with consent and holdouts.
- `shopify-loyalty-program` — Loyalty and rewards programmes on Shopify.
- `shopify-email-flows` — Setting up the core automated email flows of a Shopify store.

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Raise average order value on Shopify with relevant upsells, cross-sells and bundles at each step of the purchase.

## Inputs to Collect

Average order value and items per order, best-selling products and frequently bought together pairs (order reports), margins, current apps, theme.

## Placements and Tools

| Placement | Offer type | Tools |
|-----------|-----------|-------|
| Product page | Complementary products, bundles, upgrades | Search & Discovery recommendations, Shopify Bundles, theme sections |
| Cart / cart drawer | Add-ons, free-shipping progress bar | Theme cart features or apps |
| Checkout | Small add-ons | Checkout UI extensions (see `shopify-checkout-customization`) |
| Post-purchase page | One-click offer after payment | Post-purchase upsell apps |
| Email | Replenishment, accessories | Post-purchase flows (`shopify-email-flows`) |

## Workflow

1. **Find pairs** from order data (products bought together, accessories, consumables).
2. **Choose offers** that help the buyer: complementary items, larger size, bundle discount, gift wrap.
3. **Set rules**: one or two offers per placement, priced below the main item, relevant to the cart.
4. **Free-shipping threshold** slightly above the current average order value with a progress bar.
5. **Measure** take rate per offer, AOV, conversion rate (check that upsells do not lower conversion).

## Output Format

1. Offer map by placement
2. Bundle and pricing proposals
3. Tool setup steps
4. KPIs and test plan

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-upsell-cross-sell -g
```

## Example Requests

- "Help me with shopify upsell & cross-sell for my Shopify store"
- "What are the best practices for shopify upsell & cross-sell?"
- "Audit my current shopify upsell & cross-sell setup and suggest improvements"
- "Create a step-by-step shopify upsell & cross-sell implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
