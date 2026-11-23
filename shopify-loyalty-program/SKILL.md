---
name: shopify-loyalty-program
description: "Shopify loyalty and rewards program. Designs points, VIP tiers and referral rewards for a Shopify store, picks a loyalty app and measures repeat-purchase impact. Use when a Shopify store owner wants a loyalty or referral program or more repeat customers."
metadata:
  nexscope:
    category: shopify
---

# Shopify Loyalty Program

Customer loyalty and rewards — points systems, VIP tiers, referral programs, app selection.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Loyalty and rewards programmes on Shopify.

Part of: Retention, loyalty and personalization. For neighbouring jobs, use the matching skill instead:

- `ecommerce-customer-retention` — Retention from order data: cohorts, RFM segments, lifecycle flows with holdouts.
- `ecommerce-personalization` — Personalising site content and recommendations by segment, with consent and holdouts.
- `shopify-upsell-cross-sell` — Upsell and cross-sell offers on a Shopify store.
- `shopify-email-flows` — Setting up the core automated email flows of a Shopify store.

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Design and launch a Shopify loyalty or referral program that increases repeat purchases at a controlled cost.

## Inputs to Collect

Repeat purchase rate, average order value, gross margin, purchase frequency, customer base size, existing discounts, preferred apps (Smile.io, LoyaltyLion, Yotpo, Rivo…).

## Workflow

1. **Choose the model**:
   - Points (earn on purchases and actions, redeem for discounts) for frequent buyers.
   - VIP tiers for high-value customers.
   - Referral rewards (give X, get X) for word-of-mouth products.
2. **Reward economics**: reward value as a share of spend (often 3-10%); check the cost against margin and the expected lift in repeat rate.
3. **Earning rules**: purchases, account creation, birthday, reviews, social follows; keep it simple.
4. **Redemption**: thresholds reachable within 2-3 orders; rewards that bring customers back (discounts, free shipping, exclusive products).
5. **Communication**: launch email to existing customers, widget on the store, points balance in emails and account pages.
6. **Measure**: repeat rate and frequency of members vs non-members, redemption rate, program cost.

## Output Format

1. Program design (model, earning and redemption rules)
2. Cost model with break-even lift
3. App recommendation and setup steps
4. Launch plan and KPIs

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-loyalty-program -g
```

## Example Requests

- "Help me with shopify loyalty program for my Shopify store"
- "What are the best practices for shopify loyalty program?"
- "Audit my current shopify loyalty program setup and suggest improvements"
- "Create a step-by-step shopify loyalty program implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
