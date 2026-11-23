---
name: ebay-seller-guide
description: "Complete guide for selling on eBay — auction and fixed-price strategies, listing optimization, eBay SEO, shipping setup, seller ratings, and scaling from casual seller to Top Rated Seller. Use when the user asks for help starting or growing an eBay business, choosing auction vs Buy It Now, shipping setup or reaching Top Rated Seller."
---

# eBay Seller Guide

Complete guide for selling on eBay — auction and fixed-price strategies, listing optimization, eBay SEO, shipping setup, seller ratings, and scaling from casual seller to Top Rated Seller.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** How to sell on eBay, from first listing to Top Rated Seller.

Part of: eBay and Walmart seller guides and tools, eBay research, search and ads. For neighbouring jobs, use the matching skill instead:

- `ebay-seller-tools` — Choosing software tools for an eBay business.
- `walmart-seller-guide` — How to sell on Walmart Marketplace, from application to scaling.
- `walmart-seller-tools` — Choosing software tools for a Walmart business.
- `ebay-product-research` — Deciding what to sell on eBay from sold listings: sell-through rate, sold prices, net per sale.
- `ebay-seo` — Ranking eBay listings in Best Match search: titles, item specifics, category, identifiers.
- `ebay-advertising` — Paid eBay Promoted Listings (General, Priority, Offsite): ad rates, bids, break-even and ROAS.

<!-- role-and-scope:end -->

## Capabilities

- Account setup and seller level progression
- Listing format strategy: auction vs Buy It Now vs Best Offer
- eBay SEO: item specifics, titles, and Cassini search algorithm
- Photography and description best practices
- Shipping and returns policy optimization
- eBay Promoted Listings strategy
- Top Rated Seller requirements and benefits
- International selling and Global Shipping Program

## Platform Rules and Constraints

eBay.com (US) seller standards and selling rules at the last review of this skill (November 2026), from the *Seller performance standards* and *Top Rated seller* help pages. Other eBay sites use different thresholds. Items marked **[check]** change and must be confirmed.

- **Seller levels:** Top Rated, Above Standard, Below Standard. eBay evaluates them monthly (around the 20th) over the last 3 months, or the last 12 months for sellers with fewer than 400 US transactions in 3 months **[check]**.
- **Top Rated Seller (US) [check]:** account open at least 90 days; at least 100 transactions and $1,000 sales with US buyers in 12 months; transaction defect rate ≤ 0.5%; cases closed without seller resolution ≤ 0.3%; late shipment rate ≤ 3%; tracking uploaded on time and validated on at least 95% of transactions.
- **Top Rated Plus listings [check]:** a Top Rated seller who offers same or 1-business-day handling and free 30-day (or longer) returns gets the badge and a final value fee discount (10% of the FVF on eBay.com at last review).
- **Below Standard** sellers get lower search visibility and may face selling restrictions; defects are: transactions cancelled by the seller for being out of stock, and cases closed without seller resolution **[check]**.
- **Formats:** auctions (1, 3, 5, 7 or 10 days, optional reserve price for a fee **[check]**), fixed price (Good 'Til Cancelled), Best Offer with auto-accept and auto-decline thresholds.
- **Selling limits** apply to new accounts (count and value per month); request increases in Seller Hub.
- **Shipping and returns:** handling time is a commitment; late shipment is measured against it and the carrier's acceptance scan. eBay International Shipping replaced the Global Shipping Program for US sellers **[check]**.
- **Payments:** eBay manages payments; payouts go to the seller's bank account on the payout schedule chosen in Payments settings.

## Data Needed

| Data | Where |
|------|-------|
| Current seller level, defect rate, late shipment rate, cases closed without resolution | Seller Hub > Performance > Service metrics / Seller level |
| Transactions and sales in the evaluation period | Seller Hub > Performance > Seller level dashboard |
| Handling time, returns policy, shipping options per listing | Business policies (Account > Business policies) |
| Item type, condition, price, sold comparables | Listing drafts; `ebay-product-research` |
| Store subscription and fees | Seller Hub > Payments > Reports / fee invoices |

## Workflow

1. **Set up the account basics:** business vs personal account, payout bank account, business policies for shipping, returns and payment, so every listing reuses them.
2. **Pick the format per item** with the rule below (auction for rare items with uncertain value and strong demand; fixed price + Best Offer for repeatable items).
3. **Create listings** with complete item specifics, 12+ well-lit photos for used items, clear condition notes and accurate weight/size for calculated shipping (see `ebay-seo` for titles).
4. **Fix the handling time you can meet every day** (1 business day if possible) and upload tracking the same day.
5. **Choose a returns policy** (30-day free returns if margin allows, as it is a Top Rated Plus requirement).
6. **Track the service metrics weekly** with the formulas below; act when a metric reaches 50% of its limit.
7. **Plan the path to Top Rated:** count transactions and sales still needed in the evaluation window and the maximum defects allowed.
8. **Scale:** open a Store when listing volume or fee savings justify it (compare invoices), use Promoted Listings selectively (`ebay-advertising`), consider international shipping via eBay International Shipping.

## Calculations and Tools

- **Transaction defect rate** = defects ÷ transactions in the evaluation period.
- **Late shipment rate** = late shipments ÷ transactions with tracking.
- **Defects allowed** before losing Top Rated = floor(0.005 × transactions) − defects already counted.
- **Transactions still needed** = 100 − transactions in 12 months; **sales still needed** = $1,000 − sales in 12 months.
- **Auction vs fixed price:** choose an auction when at least 5 comparable items sold in 90 days and sold prices vary by more than ±30% around the median (uncertain value); otherwise fixed price at or slightly above the sold median, with Best Offer auto-decline at your floor price. (Working rule of this skill.)
- **Top Rated Plus value** = FVF × 10% discount × annual sales − cost of offering free returns (return rate × return shipping cost).

## Worked Example

*Illustrative example with invented figures.* A seller has 380 transactions in the last 12 months, 2 defects and 9 late shipments.

- Defect rate = 2 ÷ 380 = 0.53% (> 0.5% limit for Top Rated); allowed defects = floor(1.9) = 1, so the seller is one defect over.
- Late shipment rate = 9 ÷ 380 = 2.4% (≤ 3%: compliant, but 80% of the limit).
- Action: stop out-of-stock cancellations (sync quantities), set handling to 2 days on items shipped from a second location, recheck on the next evaluation date.

## Example Requests

- "I have 380 transactions, 2 defects and 9 late shipments in the last 12 months on eBay.com. Am I Top Rated, and what must I fix?"
- "Should I sell my signed first-edition book on eBay as an auction or a Buy It Now with Best Offer?"
- "I'm starting to sell used electronics on eBay: set up my shipping, returns and payment business policies step by step."

## Output Format

1. Status table: each service metric, the seller's value, the limit for the target level, headroom.
2. Prioritised action list (account setup, listing, shipping, returns) with owners and dates.
3. Format decision per item (auction / fixed price / Best Offer thresholds) with the sold-data evidence.
4. Path to Top Rated: transactions and sales still needed, defects allowed, next evaluation date.

## Quality Checks

- Thresholds are those of the seller's eBay site and current evaluation period, marked verified with the date of the help page used.
- Metric calculations use the seller's own dashboard numbers, not estimates.
- Handling time and returns policy recommended are ones the seller confirmed they can sustain.
- Format recommendation is backed by sold comparables, not by habit.
- No advice that breaks eBay policy (fee avoidance, off-eBay payments, duplicate listings).

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** the seller's metrics from Seller Hub, thresholds copied from eBay's help pages with date.
- **Estimates:** expected sales uplift from Top Rated Plus or a Store, return rate used in the free-returns cost.
- Thresholds above were reviewed in November 2026 for eBay.com; marked [check] items and other eBay sites must be confirmed.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ebay-seller-guide -g
```

## Usage

Ask your AI agent:

- "Help me set up my eBay store and create optimized listings."
- "What is the best listing strategy for used electronics on eBay?"
- "How do I become a Top Rated Seller on eBay?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
