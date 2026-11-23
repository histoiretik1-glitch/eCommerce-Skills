---
name: ebay-product-research
description: "Research profitable products to sell on eBay. Analyze completed listings, sell-through rates, average selling prices, competition density, and seasonal demand patterns. Use when the user asks for help finding products to sell on eBay, checking sell-through rates, sold prices, competition or seasonality."
---

# eBay Product Research

Research profitable products to sell on eBay. Analyze completed listings, sell-through rates, average selling prices, competition density, and seasonal demand patterns.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Deciding what to sell on eBay from sold listings: sell-through rate, sold prices, net per sale.

Part of: eBay research, search and ads, Product research and launch. For neighbouring jobs, use the matching skill instead:

- `ebay-seller-guide` — How to sell on eBay, from first listing to Top Rated Seller.
- `ebay-seo` — Ranking eBay listings in Best Match search: titles, item specifics, category, identifiers.
- `ebay-advertising` — Paid eBay Promoted Listings (General, Priority, Offsite): ad rates, bids, break-even and ROAS.
- `dropshipping-product-research` — Screening dropshipping products: supplier quotes, landed cost, max CPA, delivery time, policy checks.
- `shopify-dropshipping` — Running a dropshipping store on Shopify: apps, supplier connections and order flow.
- `tiktok-shop-product-research` — Scoring and validating a product idea for TikTok Shop.
- `product-launch-strategy` — Planning a product launch on any channel: timeline, stock, pricing, compliant reviews, launch ads.

<!-- role-and-scope:end -->

## Capabilities

- Completed listings analysis for real selling prices
- Sell-through rate calculation and benchmarks
- Competition density assessment by category
- Seasonal demand pattern identification
- Sourcing opportunity identification (arbitrage, wholesale, thrift)
- Category-specific fee analysis
- Trending product detection on eBay

## Platform Rules and Constraints

eBay data sources and rules relevant to product research, as published at the last review of this skill (November 2026). Items marked **[check]** must be confirmed on eBay's current pages.

- **Sold and completed listings:** the "Sold items" filter on eBay search shows roughly the last 90 days of sales **[check]**; Seller Hub > Research (Terapeak product research) shows up to 3 years of sold data, free for sellers **[check]**.
- **Final value fees** are a percentage of the total sale amount (item + shipping), per category, plus a per-order fee **[check: about 13–15% for most categories and $0.30–$0.40 per order on eBay.com, lower with a Store subscription]**. Always use the rate from eBay's fee page for the exact category.
- **Restricted and prohibited items:** check the *prohibited and restricted items* policy before sourcing (e.g. recalled items, some cosmetics, used undergarments, items needing authorization). Brands enrolled in VeRO can have listings removed.
- **Authenticity Guarantee** applies to some categories and price thresholds (sneakers, watches, handbags, trading cards) **[check]**: plan the extra handling time.
- **Selling limits:** new accounts have monthly limits on item count and value (Seller Hub > Overview > Selling limits).
- **Sold prices include accepted Best Offers** shown with a crossed-out price; the accepted amount is not always visible in search: Terapeak shows the sold price.

## Data Needed

| Data | Where |
|------|-------|
| Sold listings for the exact item (price, shipping, date, condition) | eBay search > Sold items filter, or Seller Hub > Research (Terapeak) |
| Number of active listings for the same item and condition | eBay search with the same keywords and filters (Buy It Now + auctions) |
| Category final value fee rate and per-order fee | eBay fee page for the seller's site and store level |
| Landed cost per unit (purchase, inbound shipping, prep) | Supplier invoice, thrift receipt |
| Shipping label cost | eBay shipping calculator / carrier rates for the packed size and weight |

## Workflow

1. **Define the exact item and condition** (model number, edition, size, new / used / for parts). Mixing conditions distorts prices.
2. **Pull sold data** for the last 90 days with the same keywords and condition; exclude lots, accessories and listings for a different item; record price and shipping for each sale.
3. **Count active listings** with the same search and filters on the same day.
4. **Run `sold_analysis.py`**: sell-through rate, sales per day, sold total quartiles, fees and net per sale at the median.
5. **Check seasonality** in Terapeak (12-36 months view): note months with more than 1.5× the average monthly sales and plan buying ahead of them.
6. **Check competition quality**: how many active listings come from Top Rated sellers with free shipping and returns; prices of active listings vs sold median (active far above sold = stale inventory).
7. **Check restrictions** (prohibited/restricted items, VeRO brand, Authenticity Guarantee).
8. **Decide** with the buy rule below and write the maximum buy cost.

## Calculations and Tools

- **Sell-through rate (STR)** = sold ÷ (sold + active) for the same period and search. Working rule used in this skill (not an eBay rule): below 40% = more supply than demand; 40–60% balanced; above 60% demand exceeds supply.
- **Sales per day** = sold ÷ days in the period; **days to sell your stock** ≈ your units ÷ (sales per day × your expected share of sales).
- **Final value fee** = rate × sale total + per-order fee.
- **Net per sale** = median sold total − final value fee − landed cost − shipping label.
- **Maximum buy cost** for a target margin m = median sold total × (1 − fee rate − m) − per-order fee − shipping label.

```bash
python3 scripts/sold_analysis.py '{"item": "Canon AE-1 Program body", "period_days": 90, "active_listings": 140, "sold": [{"price": 165.0, "shipping": 0}, {"price": 149.99, "shipping": 12.5}, {"price": 120.0, "shipping": 15.0}, {"price": 189.0, "shipping": 0}, {"price": 175.5, "shipping": 0}, {"price": 139.0, "shipping": 10.0}], "final_value_rate": 0.136, "per_order_fee": 0.40, "item_cost": 70.0, "shipping_cost": 12.0}'
```

## Worked Example

*Illustrative example with invented figures.* 6 sold and 140 active listings of a camera body over 90 days give a sell-through rate of 6 ÷ 146 = 4.1%: far more supply than demand. The median sold total is $163.75; with a 13.6% rate and $0.40 per order, fees are 0.136 × 163.75 + 0.40 = $22.67 and net per sale after a $70 cost and $12 label is $59.08 (36.1%). These are the figures the command above prints. Verdict: margin is good but at 0.07 sales per day a single unit may take weeks; buy one, not ten.

## Example Requests

- "I found 20 vintage Pyrex bowls at $4 each. Check eBay sold listings for the last 90 days and tell me the sell-through rate and net profit per bowl."
- "Here are 35 sold prices and 60 active listings for a Nintendo DS Lite: what is the maximum I should pay per unit for a 30% margin?"
- "Which months do Halloween costumes sell best on eBay according to Terapeak, and when should I list them?"

## Output Format

1. Item definition (exact model and condition) and data period.
2. Metrics table: sold, active, sell-through rate, sales per day, sold total quartiles, fees and net per sale at the median.
3. Seasonality note (peak months) and competition notes (Top Rated share, active price vs sold median).
4. Restriction check result.
5. Decision: buy / test one unit / skip, with the maximum buy cost and expected days to sell.

## Quality Checks

- Sold and active counts use the same keywords, condition and date range.
- Lots, parts-only and unrelated items are excluded from the sold list; the number excluded is stated.
- The fee rate is the category rate from eBay's fee page, not a generic percentage.
- At least 10 sold listings before giving a price recommendation; with fewer, say the sample is too small.
- Seasonal items are judged on the same season of previous years, not on the last 90 days only.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** sold and active counts and prices observed by the seller on a stated date, fee rates copied from eBay's fee page.
- **Estimates:** days to sell, the seller's future share of sales, seasonal uplift from previous years, the STR thresholds of this skill.
- Data windows and fee ranges were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ebay-product-research -g
```

## Usage

Ask your AI agent:

- "Research profitable product categories to sell on eBay."
- "Analyze the sell-through rate for vintage watches on eBay."
- "Find low-competition niches on eBay with high demand."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
