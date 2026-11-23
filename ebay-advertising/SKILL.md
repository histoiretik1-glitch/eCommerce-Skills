---
name: ebay-advertising
description: "Master eBay advertising — Promoted Listings Standard, Advanced, and Offsite Ads. Campaign setup, bidding strategy, budget allocation, and ROI optimization for eBay sellers. Use when the user asks for help setting up or optimizing eBay Promoted Listings (Standard, Advanced, Offsite), ad rates, budgets or ROAS."
---

# eBay Advertising

Master eBay advertising — Promoted Listings Standard, Advanced, and Offsite Ads. Campaign setup, bidding strategy, budget allocation, and ROI optimization for eBay sellers.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Paid eBay Promoted Listings (General, Priority, Offsite): ad rates, bids, break-even and ROAS.

Part of: eBay research, search and ads. For neighbouring jobs, use the matching skill instead:

- `ebay-seller-guide` — How to sell on eBay, from first listing to Top Rated Seller.
- `ebay-product-research` — Deciding what to sell on eBay from sold listings: sell-through rate, sold prices, net per sale.
- `ebay-seo` — Ranking eBay listings in Best Match search: titles, item specifics, category, identifiers.

<!-- role-and-scope:end -->

## Capabilities

- Promoted Listings Standard: ad rate strategy by category
- Promoted Listings Advanced: CPC bidding and keyword targeting
- Offsite Ads opt-in analysis and fee calculation
- Campaign structure and listing selection
- Budget allocation across Promoted Listings types
- Performance metrics: ROAS, impression share, click-through rate
- Seasonal campaign planning
- A/B testing promoted vs organic performance

## Platform Rules and Constraints

Summary of eBay Advertising rules (Seller Hub > Marketing > Advertising dashboard and eBay Advertising help pages) at the last review of this skill (November 2026). eBay renamed *Promoted Listings Standard* to **General** and *Advanced* to **Priority**; both names appear in older reports. Items marked **[check]** must be confirmed on the current help page.

- **General strategy (cost per sale):** you choose an ad rate (a % of the sale total); you pay it only when a promoted listing sells after a buyer clicked the ad within the attribution window **[check: 30 days, click-based]**. Ad rate range 2%–100% **[check]**. A dynamic rate option follows eBay's suggested rate, with a cap you set.
- **What the rate applies to:** the total amount of the sale (item price, shipping and other charges; check whether taxes are included on your site **[check]**). The ad fee is charged **in addition to** the final value fee.
- **Priority strategy (cost per click):** daily budget, keyword or smart targeting, bids per click, eligible for top-of-search placements. You pay for clicks whether or not the item sells.
- **Offsite ads:** cost per click on external sites (e.g. Google) with a daily budget **[check]**.
- **Eligibility:** promoted listing campaigns require an account in good standing (not Below Standard) and recent selling activity **[check]**; some categories (e.g. vehicles) are excluded.
- **Suggested ad rates** shown by eBay are based on similar items; they are not a break-even rate for your margins.

## Data Needed

| Data | Where the seller finds it |
|------|---------------------------|
| Item cost, shipping label cost, typical sale total | Seller's own records; Seller Hub > Orders |
| Final value fee rate and per-order fee for the category | eBay fee page for the seller's site and store subscription |
| Impressions, clicks, sold quantity, ad sales, ad fees per listing | Seller Hub > Marketing > Advertising > Reports (Listing / Campaign report, CSV) |
| Organic (non-promoted) sales of the same listings | Seller Hub > Performance > Sales, compared with ad-attributed sales |
| Click-to-sale conversion rate | Report: sold ÷ clicks over at least 30 days |

## Workflow

1. **Compute profit before ads per sale** = sale total − item cost − final value fee − per-order fee − shipping label − packaging. If the fees are not known, compute them with `sold_analysis.py` from `ebay-product-research` (it prints the eBay fees at the median sold price).
2. **Compute the break-even ad rate** (General) = profit before ads ÷ sale total, and the maximum CPC (Priority) = conversion rate × profit before ads. Run `promoted_listings.py`.
3. **Choose listings to promote.** Start with listings that already convert organically (sales in the last 30 days) and have margin; skip listings whose break-even rate is below eBay's minimum rate.
4. **Set the General ad rate** at or below a target rate (for example half the break-even rate when you want a margin after ads); compare it with eBay's suggested rate and note the gap.
5. **Use Priority only for listings with tested demand**, with a daily budget you accept to lose in a test week; start bids below the maximum CPC.
6. **Run for at least 30 days** (the attribution window) before judging a General campaign.
7. **Read the listing report**: CTR, conversion, ROAS, ad cost of sale, profit after ads; apply the action from the script (pause, lower rate, keep, scale).
8. **Check incrementality.** Compare total sales of promoted listings with the 30 days before promotion; ad-attributed sales include buyers who would have bought organically.

## Calculations and Tools

- **Break-even ad rate (General)** = profit before ads ÷ sale total.
- **Maximum CPC (Priority)** = click-to-sale conversion × profit before ads.
- **ROAS** = ad sales ÷ ad fees; **ad cost of sale** = ad fees ÷ ad sales (the inverse).
- **Profit after ads** = sold × profit before ads − ad fees.
- **Incremental sales** ≈ sales of the promoted listings during the campaign − sales of the same listings in an equal period before (seasonality caveat).

```bash
python3 scripts/promoted_listings.py '{"price_total": 45.0, "profit_before_ads": 9.5, "conversion_rate": 0.02, "listings": [{"listing": "Vintage lens 50mm", "campaign": "general", "ad_rate": 0.06, "impressions": 12000, "clicks": 240, "sold": 6, "sales": 270.0, "ad_fees": 16.2}, {"listing": "Lens hood", "campaign": "priority", "impressions": 3000, "clicks": 60, "sold": 0, "sales": 0, "ad_fees": 9.0}]}'
```

## Worked Example

*Illustrative example with invented figures.* An item sells for $45 total; after item cost, eBay fees and shipping the profit before ads is $9.50.

- Break-even General rate = 9.50 ÷ 45 = **21.1%**. eBay suggests 8%: promoting at 8% leaves $9.50 − $3.60 = $5.90 per attributed sale.
- With a 2% click-to-sale conversion, the maximum Priority CPC is 0.02 × 9.50 = **$0.19**; a $0.35 bid would lose money on average.
- A listing that took $9 of Priority clicks and sold nothing is flagged "pause or fix the listing".

## Example Requests

- "My eBay item sells for $45 and I make $9.50 before ads. What General ad rate can I afford, and is eBay's suggested 8% rate worth it?"
- "Here is my Promoted Listings report CSV for October: which listings should I pause, and which ad rates should I lower?"
- "Should I use Priority cost-per-click campaigns for my vintage camera lenses, and what maximum bid makes sense at a 2% conversion rate?"

## Output Format

1. Break-even table per product: sale total, profit before ads, break-even rate, chosen rate, profit per attributed sale.
2. Listing performance table from the report: CTR, conversion, ROAS, ad cost of sale, profit after ads, action.
3. Campaign plan: listings in General / Priority / not promoted, rates or bids, daily budgets, review date (after 30 days).
4. Incrementality note comparing sales before and during promotion.

## Quality Checks

- Profit before ads includes the final value fee and per-order fee for the seller's category and store level.
- No General ad rate above the break-even rate unless the seller explicitly accepts a loss (e.g. to clear stock), and this is written down.
- No Priority bid above conversion × profit; budgets stated per day.
- Campaigns are judged on at least 30 days of data and the full report, not a single day.
- ROAS and ad cost of sale are not confused (ROAS 5 = ad cost of sale 20%).
- Rates and fees marked [check] are confirmed on eBay's current pages.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** figures from the seller's Promoted Listings report and fee invoices, with the report period.
- **Estimates:** eBay's suggested ad rate (a market indicator, not a profit rule), expected conversion of a new campaign, incrementality.
- Programme names, rate ranges and attribution rules were reviewed in November 2026; eBay changes them, so confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ebay-advertising -g
```

## Usage

Ask your AI agent:

- "Set up Promoted Listings campaigns for my top eBay products."
- "What ad rate should I use for Promoted Listings Standard?"
- "Compare my eBay ad ROAS against category benchmarks."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
