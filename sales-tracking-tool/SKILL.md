---
name: sales-tracking-tool
description: "Track and analyze e-commerce sales performance across platforms. Set up KPI dashboards, trend analysis, and performance alerts to catch issues and opportunities early. Use when a seller wants a sales KPI dashboard, to understand why sales changed, or alerts on unusual sales drops or spikes."
metadata:
  nexscope:
    emoji: "📉"
    category: ecommerce
---

# Sales Tracking Tool 📉

Track and analyze e-commerce sales performance across platforms. Set up KPI dashboards, trend analysis, and performance alerts to catch issues and opportunities early.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Cross-channel sales tracking: metric dictionary, contribution by channel and SKU, anomalies, reconciliation.

Part of: Sales reporting and analytics. For neighbouring jobs, use the matching skill instead:

- `shopify-analytics-guide` — Reading Shopify reports and KPIs: sales definitions, funnel, AOV, repeat customers, cohorts.
- `tiktok-shop-analytics` — Reading TikTok Shop performance data across videos, LIVE, affiliates and ads.
- `etsy-shop-analytics` — Reading Etsy Stats to find what drives or blocks sales.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill sales-tracking-tool -g
```

## Usage

```
Help me set up sales tracking for my business. I sell on Amazon ($30K/mo) and Shopify ($10K/mo). What KPIs should I track and how often?
```

## Capabilities

- Cross-platform sales dashboard framework (Amazon, Shopify, Walmart, etc.)
- KPI definition and target setting by business stage
- Trend analysis methodology (daily, weekly, monthly, YoY)
- Anomaly detection framework (unusual spikes or drops)
- SKU-level performance tracking
- Cohort analysis for customer behavior insights

## Principles and Constraints

Rules for tracking sales across channels, as known at the last review of this skill (November 2026).

- **One definition per metric, written down:** "revenue" can mean gross sales, net of discounts, net of returns, with or without shipping and tax; each channel reports differently (e.g. Amazon ordered product sales vs settlement amounts, Shopify gross/net/total sales). Normalise before comparing.
- **Contribution beats revenue:** track contribution after COGS, channel fees, fulfilment and ads per channel and SKU; a growing channel can lose money.
- **Ordered vs settled:** marketplace reports by order date and payouts by settlement date differ; operations use order date, finance reconciles with settlements.
- **Time zones and partial periods:** channels close days in different time zones; compare complete periods (whole weeks/months) and same days of the week.
- **Data access:** use official exports and APIs (Amazon SP-API reports, Shopify Admin API/exports, Walmart reports, TikTok Shop data exports); avoid screen-scraped seller dashboards.
- **Scope:** this skill is the cross-channel sales tracking system. Channel-specific analytics are in `shopify-analytics-guide`, `tiktok-shop-analytics` and `etsy-shop-analytics`; customer cohorts in `ecommerce-customer-retention`.

## Data Needed

| Data | Where |
|------|-------|
| Orders or daily sales by channel and SKU: date, units, revenue | Channel exports/APIs (Amazon Business Reports or order reports, Shopify orders, Walmart, TikTok Shop) |
| Unit landed cost per SKU | Purchasing / ERP |
| Channel fees and fulfilment fees per order or per period | Marketplace fee reports, settlement reports, 3PL invoices |
| Ad spend by channel (and SKU where possible) | Ad platforms |
| Refunds and returns by date and SKU | Channel return reports |
| Targets (budget) by month and channel | Business plan |

## Workflow

1. **Write the metric dictionary:** revenue definition, contribution formula, order date convention, currency and time zone.
2. **Set up the data flow:** one CSV or database table with date, channel, SKU, units, revenue, cost, fees, ad spend (the input format of `sales_report.py`), refreshed daily or weekly.
3. **Build the dashboard views:** by channel, by SKU (top and loss-making), by period with targets; daily for operations, weekly for management, monthly for finance.
4. **Define KPIs by business stage:** early stage (orders, conversion, CAC), growth (contribution margin, repeat rate, stock cover), mature (contribution per channel, inventory turns, return rate).
5. **Set anomaly rules:** daily revenue outside the expected band by weekday, SKU sales at zero while in stock, sudden fee or ad spend spikes.
6. **Reconcile monthly** with settlements and the accounting system; explain differences above 2%.
7. **Review weekly:** variance to target, top movers (SKU × channel), loss-making SKUs, stock-outs that explain drops.
8. **Act and record:** each review ends with 3 actions and owners; next review checks them.

## Calculations and Tools

- **Contribution** = revenue − COGS − fees − ad spend; **contribution margin** = contribution ÷ revenue.
- **Growth** = (period − previous period) ÷ previous period; **YoY** for seasonal businesses.
- **Expected daily band** = mean of the same weekday over the last 8 weeks ± 2 standard deviations; values outside are anomalies to explain.
- **Variance to target** = actual − target, in value and %.
- **TACoS** = ad spend ÷ total revenue per channel.

```bash
python3 scripts/sales_report.py examples/synthetic_sales.csv
```

`examples/synthetic_sales.csv` is **synthetic test data** (invented sales of three SKUs on three channels); replace it with your merged channel exports.

## Worked Example

*Illustrative example using the synthetic file above, not real data.* The command reports Amazon with the largest revenue share ($2,136.92, 42.5%) but the lowest contribution margin (32.6%), Shopify at 60.8% and Etsy at 56.1%. Revenue grew 18.1% from September to October. BOWL-03 makes only $14.69 of contribution on $417.78 of revenue (3.5%): its Amazon ads ($109 over two months) consume almost all its margin.

- Actions: cut BOWL-03 Amazon ad spend or raise its price; shift budget to Shopify where margin is highest; check that October is a complete month before reporting growth.

## Example Requests

- "Help me set up sales tracking for Amazon ($30K/month) and Shopify ($10K/month): which KPIs and how often?"
- "Merge my Amazon, Shopify and Etsy exports and show contribution by channel and SKU."
- "Our revenue dropped 20% on Tuesday. Is it an anomaly and where does it come from?"

## Output Format

1. Metric dictionary.
2. Data flow and refresh schedule per channel.
3. Dashboard tables: by channel, by SKU, by period vs target (script output).
4. Anomaly rules and the weekly review template.
5. Monthly reconciliation checklist.

## Quality Checks

- Revenue and contribution definitions identical across channels.
- Complete periods compared; time zones stated.
- Costs, fees and ads included in contribution; missing costs flagged, not set to zero silently.
- Monthly totals reconciled with settlements/accounting within a stated tolerance.
- Each anomaly has an explanation or an open action.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** channel exports, settlements and ad spend for stated periods.
- **Estimates:** allocated costs (e.g. ad spend split across SKUs), forecasts and targets.
- Method reviewed in November 2026.

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
