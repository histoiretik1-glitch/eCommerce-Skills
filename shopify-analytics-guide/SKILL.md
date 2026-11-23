---
name: shopify-analytics-guide
description: "Master Shopify analytics and reporting. Understand key metrics, build custom reports, track customer behavior, and make data-driven decisions to grow your Shopify store. Use when the user asks for help understanding Shopify reports and metrics, cohort analysis, LTV or building custom Shopify reports."
---

# Shopify Analytics Guide

Master Shopify analytics and reporting. Understand key metrics, build custom reports, track customer behavior, and make data-driven decisions to grow your Shopify store.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Reading Shopify reports and KPIs: sales definitions, funnel, AOV, repeat customers, cohorts.

Part of: Shopify setup, analytics and conversion, Sales reporting and analytics. For neighbouring jobs, use the matching skill instead:

- `shopify-store-setup` — Launching a new Shopify store: plan, payments, theme, products, shipping, taxes, domain.
- `shopify-conversion-optimization` — CRO on a Shopify store: theme, apps, product pages, Shopify checkout.
- `shopify-ab-testing` — Running A/B tests on a Shopify store with Shopify tools and apps.
- `sales-tracking-tool` — Cross-channel sales tracking: metric dictionary, contribution by channel and SKU, anomalies, reconciliation.
- `tiktok-shop-analytics` — Reading TikTok Shop performance data across videos, LIVE, affiliates and ads.
- `etsy-shop-analytics` — Reading Etsy Stats to find what drives or blocks sales.

<!-- role-and-scope:end -->

## Capabilities

- Dashboard metrics interpretation (sessions, CVR, AOV, revenue)
- Customer acquisition and behavior analysis
- Product performance reporting
- Marketing channel attribution
- Cohort analysis and customer lifetime value
- Custom report building
- Third-party analytics integration (GA4, Triple Whale, Polar)
- Benchmarking against industry averages

## Platform Rules and Constraints

How Shopify defines and reports its metrics, at the last review of this skill (November 2026, Shopify Help Center > Analytics). Items marked **[check]** must be confirmed in the Help Center.

- **Sales definitions:** gross sales = product price × quantity before discounts; **net sales** = gross sales − discounts − returns; **total sales** = net sales + shipping + duties + taxes **[check]**.
- **Average order value** in Shopify Analytics is based on gross sales minus discounts divided by orders, excluding shipping and taxes **[check]**. The order export's *Total* includes shipping and taxes, so an AOV computed from *Total* is higher.
- **Online store conversion rate** = sessions that completed checkout ÷ sessions; the *conversion rate breakdown* shows added to cart, reached checkout and completed checkout.
- **Sessions** end after 30 minutes of inactivity and at midnight UTC **[check]**; bots are filtered by Shopify; consent banners in some regions reduce tracked sessions.
- **Reports by plan:** the dashboard and standard reports are on all plans; custom reports and some report families depend on the plan **[check]**. Reports are built on ShopifyQL.
- **Time zone:** reports use the store's time zone (Settings > General); exports use timestamps with offsets.
- **Returning customer rate** = customers with more than one order ÷ customers in the period; Shopify also offers a customer cohort analysis report.
- **Attribution:** Shopify's marketing reports attribute sessions and sales by UTM / referrer with its own model; GA4 and ad platforms use other models, so numbers will not match exactly.

## Data Needed

| Data | Where |
|------|-------|
| Sessions, conversion rate breakdown, AOV, total and net sales | Analytics > Overview and Reports (choose the same date range) |
| Order export | Orders > Export > All orders / date range > Plain CSV file |
| Sessions and sales by channel / referrer / UTM | Analytics > Reports > Sessions by referrer, Sales by channel |
| Product performance | Reports > Sales by product, Product analytics |
| Customer cohorts and returning customers | Reports > Customer cohort analysis, Returning customers |
| Marketing spend by channel | Ad platforms (Meta, Google, TikTok) for the same dates |

## Workflow

1. **Fix the reporting basics:** store time zone, test orders excluded, UTM tags on all campaigns, GA4 connected through Shopify's Google & YouTube app if used.
2. **Build the weekly KPI sheet:** sessions, conversion rate (and the three funnel steps), AOV, net sales, returning customer rate, refunds, marketing spend and MER.
3. **Compute KPIs from the order export** with `orders_kpis.py` to cross-check the dashboard and get repeat-customer data per period.
4. **Read the funnel:** the biggest drop between sessions → added to cart → reached checkout → completed points to the area to work on (`shopify-conversion-optimization`).
5. **Break down by channel and device:** conversion and AOV per traffic source; a channel with high sessions and low conversion needs targeting or landing-page work.
6. **Product analysis:** sales by product, sell-through vs inventory, products with high views and low add-to-cart.
7. **Customer analysis:** cohort report (repeat purchase by first-order month), time between orders, LTV estimate.
8. **Write the weekly review:** 3 changes vs last week and vs the same week last year, their likely cause, one action each.

## Calculations and Tools

- **Conversion rate** = completed checkouts ÷ sessions; **add-to-cart rate** = sessions with add to cart ÷ sessions.
- **AOV (Shopify)** = (gross sales − discounts) ÷ orders; **revenue per session** = net sales ÷ sessions.
- **MER (marketing efficiency ratio)** = total sales ÷ total marketing spend.
- **Repeat customer rate** = customers with 2+ orders ÷ customers in the period.
- **Simple LTV (gross margin)** = AOV × orders per customer over 12 months × gross margin %.
- **Discount rate** = discounts ÷ (subtotal + discounts).

```bash
python3 scripts/orders_kpis.py examples/synthetic_orders_export.csv
```

`examples/synthetic_orders_export.csv` is **synthetic test data** (invented orders with example.com emails) in the layout of Shopify's order export; replace it with your own export.

## Worked Example

*Illustrative example using the synthetic file above, not real store data.* The command reports 5 orders (1 voided order excluded), gross $440.05, refunds $32.00, net $408.05, AOV $88.01 on order totals vs $80.38 on merchandise subtotals, 3 customers of whom 2 ordered twice (repeat customer rate 66.7%), discount rate 3.2%. The $7.63 gap between the two AOVs is shipping and tax: compare only the merchandise AOV with Shopify's dashboard.

## Example Requests

- "Here is my Shopify order export for Q3. Calculate AOV, repeat customer rate and revenue by month, and explain why it differs from my dashboard."
- "My Shopify conversion rate dropped from 2.1% to 1.6% last week. Walk me through the reports to find out why."
- "Build a weekly KPI report for my Shopify store with sessions, conversion funnel, AOV, MER and returning customers."

## Output Format

1. KPI table for the period vs previous period vs same period last year, with Shopify's definitions.
2. Funnel table (sessions, added to cart, reached checkout, completed) with step rates and the biggest drop highlighted.
3. Channel and device breakdown with conversion, AOV and revenue per session.
4. Customer section: repeat rate, cohort observations, LTV estimate labelled as an estimate.
5. Three findings with one action each.

## Quality Checks

- Same date range and time zone across all reports compared.
- AOV definition stated (Shopify's vs order total) whenever an AOV is quoted.
- Test and voided orders excluded; refunds handled explicitly.
- Channel numbers from Shopify are not mixed with GA4 or ad-platform numbers in the same column.
- Customer emails are never copied into the deliverable.
- Any benchmark (e.g. "typical conversion rate") is labelled as an estimate with its source.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** Shopify reports and exports for stated dates, computed with the formulas above.
- **Estimates:** LTV projections, causes of a change, industry benchmarks.
- Metric definitions were reviewed in November 2026; confirm items marked [check] in Shopify's Help Center.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-analytics-guide -g
```

## Usage

Ask your AI agent:

- "Explain my Shopify analytics dashboard and what to focus on."
- "Build a weekly KPI report template for my Shopify store."
- "How do I track customer lifetime value in Shopify?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
