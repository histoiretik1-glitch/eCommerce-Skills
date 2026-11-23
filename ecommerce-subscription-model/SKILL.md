---
name: ecommerce-subscription-model
description: "Design and launch subscription-based e-commerce businesses. Subscribe-and-save, membership boxes, replenishment models, pricing tiers, and churn reduction strategies. Use when the user asks for help designing a subscription or subscribe-and-save offer, membership box, pricing tiers or reducing subscriber churn."
---

# E-Commerce Subscription Model

Design and launch subscription-based e-commerce businesses. Subscribe-and-save, membership boxes, replenishment models, pricing tiers, and churn reduction strategies.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Designing the subscription offer and business model.

Part of: Subscriptions. For neighbouring jobs, use the matching skill instead:

- `shopify-subscription-setup` — Implementing subscriptions on a Shopify store.

<!-- role-and-scope:end -->

## Capabilities

- Subscription model types: replenishment, curation, access
- Platform setup: Shopify subscriptions, Amazon Subscribe & Save, ReCharge
- Pricing and tier design for maximum LTV
- Subscriber acquisition strategy
- Onboarding flow optimization
- Churn analysis and reduction tactics
- Subscription analytics: MRR, churn rate, ARPU
- Regulatory compliance (auto-renewal laws)

## Principles and Constraints

Rules for designing a subscription offer on any platform, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed with counsel for the seller's markets (this is not legal advice).

- **Auto-renewal law:** in the US, ROSCA requires clear disclosure of terms, express informed consent before charging, and a simple cancellation method; many states add rules (California's automatic renewal law, amended for July 2025, requires online cancellation and renewal reminders **[check]**). The FTC "click-to-cancel" amendments were vacated by a federal court in July 2025 **[check current status]**, but state laws still apply.
- **EU/UK:** pre-contract information and withdrawal rights apply to subscription sign-ups; Germany requires a cancellation button on websites (since July 2022) **[check]**.
- **Model fit:** replenishment (consumables with a predictable usage cycle), curation (boxes, discovery) and access/membership (perks, early access) have different churn drivers; pick the one your product supports.
- **Discount discipline:** the subscribe discount is paid on every order for the subscriber's lifetime; it must be covered by higher retention and lower acquisition cost per order.
- **Marketplace subscriptions:** Amazon Subscribe & Save requires eligible products and seller-funded discounts **[check]**; customers belong to the marketplace.
- **Scope:** this skill designs the offer and economics; installing selling plans on Shopify is `shopify-subscription-setup`; lifecycle messaging `ecommerce-customer-retention`.

## Data Needed

| Data | Where |
|------|-------|
| Product usage cycle (days a unit lasts), reorder intervals of current customers | Product data, order history |
| Price, COGS, fulfilment and payment costs per order | Finance |
| Current repeat purchase rate and median days to reorder | `cohorts.py` in `ecommerce-customer-retention` |
| CAC for one-time vs subscription customers | Ad platforms, analytics |
| For existing programmes: active subscribers, new, cancelled, paused per month, cancellation reasons, failed payments | Subscription app reports |

## Workflow

1. **Validate fit:** a product with a usage cycle of 2–12 weeks, repeat buying already happening, and a reason to stay (convenience, savings, exclusive items).
2. **Choose the model and cadence options** from measured reorder intervals (offer the 2–3 intervals most customers already use).
3. **Set price and perks:** subscribe discount and/or non-price perks (free shipping, gift, early access); test whether a smaller discount plus perks converts as well.
4. **Model the economics** with `subscription_economics.py`: contribution per order, LTV over 24 months, LTV:CAC, CAC payback, maximum churn for LTV:CAC 3.
5. **Design sign-up and compliance:** clear terms at checkout, consent checkbox, confirmation email with cancellation instructions, reminders where required.
6. **Design retention mechanics:** skip/pause/swap options, cadence change, reminder before each charge, card updater and dunning for failed payments, cancellation flow with a reason question and a save offer (not an obstacle).
7. **Launch to existing repeat buyers first** (lower CAC, faster learning), then acquisition campaigns.
8. **Track monthly:** MRR, subscriber churn, involuntary churn (failed payments), ARPU, retention by sign-up cohort; act on the top cancellation reasons.

## Calculations and Tools

- **MRR** = active subscribers × average monthly revenue per subscriber; **ARPU** = MRR ÷ active subscribers.
- **Monthly churn** = subscribers cancelled in the month ÷ active subscribers at the start of the month (voluntary and involuntary separately).
- **LTV** = Σ monthly contribution × (1 − churn)^m over a horizon (or monthly contribution ÷ churn uncapped).
- **CAC payback** = first month where cumulative expected contribution ≥ CAC.
- **Discount break-even**: the subscription must add at least (discount per order × orders per subscriber) of extra contribution via more orders or lower CAC.

```bash
python3 scripts/subscription_economics.py '{"price": 32.0, "one_time_price": 36.0, "orders_per_month": 1, "cogs": 9.5, "fulfillment": 6.0, "payment_fee_rate": 0.03, "monthly_churn": 0.09, "cac": 45.0, "horizon_months": 24}'
```

## Worked Example

*Illustrative example with invented figures.* A coffee subscription at $32/month (one-time price $36), COGS $9.50, fulfilment $6, payment fees 3%, 9% monthly churn, CAC $45. The command above prints:

- Contribution per order **$15.54**; 57% of subscribers still active after 6 months, 32% after 12.
- LTV over 24 months **$154.71** → LTV:CAC 3.44; CAC payback in **4 months**.
- Churn must stay below **11.5%** a month to keep LTV:CAC at 3 (uncapped); every order gives away $4.00 of discount, so the programme works only if subscribers order more often than one-time buyers.

## Example Requests

- "Should I add a subscription option to my coffee product, and at what discount?"
- "Design a subscribe-and-save programme for my consumable product, with cadence options and cancellation flow."
- "How do I reduce subscription churn for my box service? 12% of subscribers cancel every month."

## Output Format

1. Fit assessment and chosen model with cadence options from reorder data.
2. Offer design: price, discount, perks, terms.
3. Economics table (script output) with the churn and CAC limits.
4. Compliance checklist per selling country.
5. Retention mechanics and cancellation flow; KPI dashboard (MRR, churn split, ARPU, cohort retention).

## Quality Checks

- Cadences based on measured reorder intervals.
- Economics computed with the seller's real costs; churn assumption stated and later replaced by measured cohort retention.
- Sign-up discloses terms and cancellation; cancellation is as easy as sign-up.
- Involuntary churn (failed payments) tracked separately from voluntary churn.
- Discount cost compared with retention gains.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** subscription app reports and cost data for stated periods.
- **Estimates:** churn before launch, projected LTV, conversion to subscription, benchmark churn rates.
- Legal points were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-subscription-model -g
```

## Usage

Ask your AI agent:

- "Should I add a subscription option to my product?"
- "Design a subscribe-and-save program for my consumable product."
- "How do I reduce subscription churn for my box service?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
