---
name: walmart-advertising-strategy
description: "Master Walmart Connect advertising. Sponsored Products, Sponsored Brands, Display Ads, and onsite/offsite campaigns with bidding strategy, budget allocation, and ROAS optimization. Use when the user asks for help running Walmart Connect ads (Sponsored Products, Sponsored Brands, Display), bidding, budgets or ROAS."
---

# Walmart Advertising Strategy

Master Walmart Connect advertising. Sponsored Products, Sponsored Brands, Display Ads, and onsite/offsite campaigns with bidding strategy, budget allocation, and ROAS optimization.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Walmart Connect Sponsored Products and Brands: campaigns, bids, ACoS and ROAS.

Part of: Walmart listings and ads. For neighbouring jobs, use the matching skill instead:

- `walmart-seller-guide` — How to sell on Walmart Marketplace, from application to scaling.
- `walmart-listing-optimization` — Walmart item content: product name, key features, attributes, images and Listing Quality score.

<!-- role-and-scope:end -->

## Capabilities

- Walmart Sponsored Products campaign setup and optimization
- Sponsored Brands and Sponsored Videos strategy
- Display advertising and DSP campaigns
- Keyword research and targeting for Walmart
- Bidding strategy: automatic vs manual, bid modifiers
- Budget allocation across campaign types
- ROAS tracking and optimization
- Seasonal campaign planning for Walmart events

## Platform Rules and Constraints

Walmart Connect rules for Marketplace sellers (Seller Center > Ad Center / Sponsored Search and Walmart Connect help pages) at the last review of this skill (November 2026). Items marked **[check]** change and must be confirmed in Ad Center.

- **Sponsored Products** run as **automatic** campaigns (Walmart picks the queries from the item content) or **manual** campaigns (keywords with exact, phrase or broad match; negative keywords at exact and phrase match) **[check]**.
- **Billing is cost per click** in a second-price style auction; minimum bids and minimum daily/total budgets apply **[check]** in Ad Center.
- **Placements:** search in-grid, item page (including the Buy Box area), browse and home page carousels; **bid multipliers** can raise bids by placement and by platform (desktop, app, mobile web) **[check]**.
- **Only the item's Buy Box winner is shown:** an ad for an item where your offer does not win the Buy Box does not serve for you **[check]**, so price and shipping speed come before bids.
- **Attribution:** sales are attributed within a window after the ad click (14 days at last review **[check]**), including other items of the same brand in some reports; read the column definitions of the report you export.
- **Sponsored Brands and Sponsored Videos** require a brand registered in Walmart Brand Portal and selling with Walmart **[check]**; Display ads run through Walmart DSP (usually agency-managed).
- **Item eligibility:** published, in stock, with acceptable content quality; items in restricted categories may not be advertised.

## Data Needed

| Data | Where |
|------|-------|
| Margin before ads per item (price − cost − referral fee − WFS or shipping − returns) | `profit-margin-calculator-walmart` |
| Keyword / item report: impressions, clicks, ad spend, attributed sales, units | Ad Center > Reports (Keyword performance, Item performance), CSV export |
| Search terms that triggered automatic campaigns | Ad Center > Reports > Item keyword / search term report |
| Buy Box win rate and price competitiveness | Seller Center > Pricing / Listing Quality dashboard |
| Organic sales of the same items | Seller Center > Analytics |

## Workflow

1. **Fix eligibility first:** items must be in stock, win the Buy Box and have a Listing Quality score you have improved with `walmart-listing-optimization`.
2. **Compute the break-even ACoS** (= margin before ads) and set a target ACoS (default two thirds of the margin, or the seller's choice).
3. **Launch an automatic campaign** with the items to advertise, a daily budget and a uniform starting bid; let it run 14 days to collect search terms.
4. **Harvest search terms:** move terms with sales and ACoS ≤ target into a manual campaign (exact match); add terms with 20+ clicks and no sales as negative keywords in the automatic campaign.
5. **Structure the manual campaign** by item group and match type so that budgets and bids are readable.
6. **Analyse the report every week** with `connect_report.py` and apply the decision for each keyword (scale, keep, lower bid, pause, collect more data).
7. **Use placement and platform multipliers** only after a placement shows ACoS below target with enough clicks.
8. **Plan events:** raise budgets ahead of Walmart Deals and seasonal peaks (back-to-school, holiday) so campaigns do not run out of budget at noon.

## Calculations and Tools

- **ACoS** = ad spend ÷ attributed sales; **ROAS** = attributed sales ÷ ad spend = 1 ÷ ACoS.
- **Break-even ACoS** = margin before ads (as a fraction of price); **target ROAS** = 1 ÷ target ACoS.
- **CPC** = spend ÷ clicks; **conversion** = units ÷ clicks; **maximum CPC** = conversion × price × margin before ads.
- **TACoS** = total ad spend ÷ total sales (ad + organic), to see whether ads grow the whole business.

```bash
python3 scripts/connect_report.py '{"margin_before_ads": 0.30, "rows": [{"keyword": "storage bins", "match": "phrase", "impressions": 18000, "clicks": 260, "ad_spend": 182.0, "attributed_sales": 980.0, "units": 38}, {"keyword": "plastic bins with lids", "match": "exact", "impressions": 5200, "clicks": 75, "ad_spend": 61.5, "attributed_sales": 0, "units": 0}, {"keyword": "closet organizer", "match": "broad", "impressions": 9000, "clicks": 120, "ad_spend": 96.0, "attributed_sales": 240.0, "units": 9}]}'
```

## Worked Example

*Illustrative example with invented figures.* With a 30% margin before ads, the break-even ACoS is 30% and the default target 20% (target ROAS 5).

- "storage bins": $182 spend, $980 sales → ACoS 18.6% ≤ 20% → raise bid / scale.
- "plastic bins with lids": 75 clicks, $61.50, no sales → pause or add as negative keyword.
- "closet organizer": ACoS 40% > 30% → lower bid (each attributed sale loses money).
- Total: $339.50 spend for $1,220 sales, ACoS 27.8%: profitable overall but only one keyword meets the target.

## Example Requests

- "Here is my Walmart Connect keyword report for the last 30 days; my margin before ads is 30%. Which keywords should I scale, pause or bid down?"
- "Set up my first Walmart Sponsored Products automatic campaign for 12 kitchen items with a $50 daily budget."
- "My Walmart ads have a ROAS of 3 but my margin is 25%. Am I losing money, and what bid should I use?"

## Output Format

1. Summary: break-even and target ACoS/ROAS, total spend, sales, ACoS, TACoS.
2. Keyword/item decision table (from the script) with the next bid or action for each row.
3. Campaign structure: automatic vs manual campaigns, item groups, budgets, negative keywords to add.
4. 4-week calendar of checks and event budget changes.

## Quality Checks

- Margin before ads includes the referral fee and WFS or shipping cost of each item.
- No keyword judged with fewer clicks than the stated minimum (20 by default).
- Advertised items win the Buy Box and are in stock.
- ACoS and ROAS read from the same attribution window; the window is written in the report.
- Recommendations name Walmart Connect features as found in Ad Center, with [check] items confirmed.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** the seller's Ad Center report (with period and attribution window), margins computed from the seller's costs and fee schedule.
- **Estimates:** expected effect of a bid change, the target ACoS rule, any category benchmark ROAS.
- Campaign types, minimums and attribution were reviewed in November 2026; confirm items marked [check] in Ad Center.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill walmart-advertising-strategy -g
```

## Usage

Ask your AI agent:

- "Set up my first Walmart Sponsored Products campaign."
- "What bidding strategy should I use for Walmart advertising?"
- "Optimize my Walmart ad campaigns for better ROAS."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
