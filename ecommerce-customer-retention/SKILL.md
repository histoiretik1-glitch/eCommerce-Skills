---
name: ecommerce-customer-retention
description: "Increase customer retention and repeat purchases for e-commerce businesses. Email flows, loyalty programs, subscription models, customer segmentation, and win-back strategies. Use when the user asks for help improving repeat purchase rate, LTV, loyalty, RFM segmentation, post-purchase or win-back flows."
---

# E-Commerce Customer Retention

Increase customer retention and repeat purchases for e-commerce businesses. Email flows, loyalty programs, subscription models, customer segmentation, and win-back strategies.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Retention from order data: cohorts, RFM segments, lifecycle flows with holdouts.

Part of: Retention, loyalty and personalization. For neighbouring jobs, use the matching skill instead:

- `ecommerce-personalization` — Personalising site content and recommendations by segment, with consent and holdouts.
- `shopify-loyalty-program` — Loyalty and rewards programmes on Shopify.
- `shopify-upsell-cross-sell` — Upsell and cross-sell offers on a Shopify store.
- `shopify-email-flows` — Setting up the core automated email flows of a Shopify store.

<!-- role-and-scope:end -->

## Capabilities

- Customer retention metrics and benchmarking (by industry)
- Post-purchase email and SMS flow design
- Loyalty and rewards program setup
- Subscription and auto-replenishment models
- Customer segmentation: RFM analysis
- Win-back campaign strategy for lapsed customers
- Review and referral program integration
- Customer lifetime value optimization

## Principles and Constraints

Cross-platform rules for retention programmes, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed for the seller's country.

- **Define retention from purchase data, not opinions:** a customer is "lapsed" when they have not ordered for about 2× the median time between first and second order of your store (a working rule of this skill), not after an arbitrary 90 days.
- **Consent first:** marketing email needs opt-in under GDPR/ePrivacy in the EU and UK (soft opt-in for existing customers in some cases **[check]**) and an unsubscribe link under CAN-SPAM in the US; marketing SMS in the US needs prior express written consent (TCPA) **[check]**.
- **Marketplace customers are not your contacts:** Amazon, Walmart, eBay and TikTok Shop forbid using buyer data for marketing outside their tools. Retention there happens through the marketplace's own features (follow, brand messaging where allowed, Subscribe & Save, store pages).
- **Discounts are not retention:** habitual discounts train customers to wait; prefer replenishment reminders, service, bundles and loyalty benefits, and track margin per returning order.
- **Loyalty points are a liability** until redeemed or expired; ask your accountant how to book them before launching a points programme.
- **Neighbouring skills:** flow set-up in Shopify Email (`shopify-email-flows`), loyalty apps on Shopify (`shopify-loyalty-program`), subscription design (`ecommerce-subscription-model`), full email programme copy (`ecommerce-email-marketing-builder`).

## Data Needed

| Data | Where |
|------|-------|
| Order list: customer ID, order date, order revenue (12–24 months) | Store order export (any platform) |
| Product purchased per order and its consumption cycle (days a unit lasts) | Catalogue knowledge, reviews |
| Contribution margin per order | Finance, or the profit margin calculator skill for your platform |
| Email/SMS lists with consent status and current flow performance | Email/SMS platform |
| Discounts used by returning customers | Order export (discount codes) |

## Workflow

1. **Build the cohort table** with `cohorts.py` from the order list: repeat purchase rate, month-by-month return by acquisition month, median days to second order.
2. **Segment with RFM**: score Recency, Frequency and Monetary value 1–5 by quintile; name the segments (champions, loyal, new, at risk, lapsed) and count customers and revenue in each.
3. **Find the second-order gap:** most of the retention value is converting first-time buyers into second-time buyers; measure the share of first-time buyers who reorder within the median gap.
4. **Design lifecycle flows** with timings from your data: welcome, post-purchase (usage tips, review request after delivery), replenishment at the consumption cycle minus 5–7 days, cross-sell, win-back at 1.5–2× the median gap, VIP recognition.
5. **Choose retention mechanics** that fit the category: replenishment and subscriptions for consumables, collections/new-drops for fashion and décor, service and accessories for durables, loyalty tiers when purchase frequency is high.
6. **Set holdout groups** (5–10% of each flow's audience receives nothing) to measure incremental revenue, not just attributed revenue.
7. **Protect margin:** cap discounts in win-back flows, compare contribution per returning order with and without incentive.
8. **Review monthly** the cohort table and segment movements; one retention test per month.

## Calculations and Tools

- **Repeat purchase rate** = customers with 2+ orders ÷ customers (over the same window for each cohort).
- **Purchase frequency** = orders ÷ customers in 12 months; **median days to 2nd order** from the order list.
- **Historical LTV (12 months)** = cumulative revenue per customer of a cohort after 12 months × contribution margin %.
- **RFM score**: R, F, M each 1–5 by quintile; segment rules stated in the deliverable.
- **Incremental revenue of a flow** = (revenue per recipient in flow − revenue per customer in holdout) × recipients.

```bash
python3 scripts/cohorts.py examples/synthetic_orders.csv
```

`examples/synthetic_orders.csv` is **synthetic test data** (invented customer IDs and orders); replace it with your own order list.

## Worked Example

*Illustrative example using the synthetic file above, not real data.* 10 customers placed 16 orders: repeat purchase rate **50%**, median **43 days** to the second order. In the July cohort, 1 of 3 customers ordered in month 1 and again in month 3; cumulative revenue per July customer is $89.17.

- Replenishment reminder: at about day 36–38 (43 days minus a week), not at an arbitrary 30 or 60 days.
- Win-back: start at 65–85 days (1.5–2× the median gap) with a holdout of 10%.

## Example Requests

- "Here is my order export for the last 18 months. Build the cohort table, tell me my repeat purchase rate and when to send replenishment and win-back emails."
- "Segment my customers with RFM and propose one action for each segment."
- "Should my coffee brand use a loyalty points programme or a subscription to increase repeat purchases?"

## Output Format

1. Cohort table and key metrics (repeat rate, median days to 2nd order, 12-month historical LTV).
2. RFM segment table: rules, customer count, revenue share, action.
3. Lifecycle flow map with triggers and timings derived from the data, plus holdout sizes.
4. Retention mechanic recommendation with margin impact.
5. Monthly KPI sheet and test backlog.

## Quality Checks

- Flow timings come from the store's measured purchase gaps.
- Recent cohorts are not compared with older ones on months they have not reached yet.
- Every flow has a holdout or a before/after comparison with stated limits.
- Marketing messages only to contacts with valid consent; no marketplace buyer data used off-platform.
- Discount cost per returning order is reported.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** cohort and RFM figures computed from the store's order data for a stated period.
- **Estimates:** projected LTV beyond observed months, expected uplift of a flow, industry retention benchmarks.
- Consent rules were reviewed in November 2026; confirm items marked [check] for the seller's country.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-customer-retention -g
```

## Usage

Ask your AI agent:

- "Build a customer retention strategy for my Shopify store."
- "Design a loyalty program for my beauty brand."
- "Create win-back email flows for customers who haven't purchased in 90 days."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
