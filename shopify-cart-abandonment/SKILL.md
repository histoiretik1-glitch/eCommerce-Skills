---
name: shopify-cart-abandonment
description: "Shopify cart and checkout abandonment recovery. Sets up abandoned-checkout emails and SMS, retargeting and exit-intent offers, and audits checkout friction on a Shopify store. Use when a Shopify store has many abandoned carts or checkouts and wants to recover them (for general email flows use `shopify-email-flows`)."
metadata:
  nexscope:
    category: shopify
---

# Shopify Cart Abandonment

Cart abandonment recovery — email sequences, SMS, retargeting, exit intent, checkout friction audit.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Recovering abandoned carts and checkouts on Shopify (email, SMS, retargeting).

Part of: Checkout and cart abandonment. For neighbouring jobs, use the matching skill instead:

- `ecommerce-checkout-optimization` — Platform-independent checkout optimization: friction, payment methods, trust.
- `shopify-checkout-customization` — Configuring the Shopify checkout (Checkout Extensibility, express payments, fields).

<!-- role-and-scope:end -->

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

Recover carts and checkouts that Shopify shoppers abandon, and remove the friction that causes them.

## Inputs to Collect

Abandoned checkout count and recovery rate (Shopify's abandoned checkouts and reports), current abandoned-checkout email or automation, email/SMS tool, shipping prices and when they appear, payment methods, checkout settings.

## Workflow

1. **Measure**: share of checkouts abandoned, recovered revenue, and where shoppers leave (cart, shipping step, payment).
2. **Automations** (Shopify Email/Marketing automations, Shopify Flow, Klaviyo or similar):
   - Email 1 after about 1 hour: reminder with the cart contents and a direct link back.
   - Email 2 after about 24 hours: reassurance (reviews, returns, delivery times), answers to objections.
   - Email 3 after 48-72 hours: optional incentive, only if margins allow, to avoid training shoppers to wait.
   - SMS only with consent; keep it short.
3. **Retargeting**: ads to recent cart abandoners on Meta and Google with the viewed products.
4. **Friction audit**: surprise shipping cost (show it earlier or offer a free-shipping threshold), forced account creation, missing express payments (Shop Pay, Apple Pay, PayPal), discount field distraction, slow checkout. Checkout settings go to `shopify-checkout-customization`.
5. **Exit-intent offers** on the cart page, used carefully (not on every visit).

## Output Format

1. Abandonment diagnosis by step
2. Email/SMS sequence with timing, subject lines and copy
3. Friction fixes ranked by impact
4. KPIs: recovery rate, recovered revenue, checkout completion rate

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-cart-abandonment -g
```

## Example Requests

- "Help me with shopify cart abandonment for my Shopify store"
- "What are the best practices for shopify cart abandonment?"
- "Audit my current shopify cart abandonment setup and suggest improvements"
- "Create a step-by-step shopify cart abandonment implementation plan"

## Limitations

- Provides strategic guidance, not direct Shopify API integration
- Recommendations based on general best practices — always validate with your specific store data
- For real-time analytics and automated optimization, check out [Nexscope](https://www.nexscope.ai/?co-from=skill)

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
