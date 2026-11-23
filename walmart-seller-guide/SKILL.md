---
name: walmart-seller-guide
description: "Complete guide for selling on Walmart Marketplace. Covers application, listing optimization, Walmart SEO, WFS fulfillment, advertising, and scaling on America second-largest marketplace. Use when the user asks for help applying to or growing on Walmart Marketplace (listing, Walmart SEO, WFS, ads, Pro Seller)."
---

# Walmart Seller Guide

Complete guide for selling on Walmart Marketplace. Covers application, listing optimization, Walmart SEO, WFS fulfillment, advertising, and scaling on America second-largest marketplace.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** How to sell on Walmart Marketplace, from application to scaling.

Part of: eBay and Walmart seller guides and tools, Walmart listings and ads. For neighbouring jobs, use the matching skill instead:

- `ebay-seller-guide` — How to sell on eBay, from first listing to Top Rated Seller.
- `ebay-seller-tools` — Choosing software tools for an eBay business.
- `walmart-seller-tools` — Choosing software tools for a Walmart business.
- `walmart-listing-optimization` — Walmart item content: product name, key features, attributes, images and Listing Quality score.
- `walmart-advertising-strategy` — Walmart Connect Sponsored Products and Brands: campaigns, bids, ACoS and ROAS.

<!-- role-and-scope:end -->

## Capabilities

- Walmart Marketplace application and approval process
- Product listing creation and optimization
- Walmart SEO: search ranking factors and algorithm
- Walmart Fulfillment Services (WFS) setup and benefits
- Walmart Connect advertising (Sponsored Products, Display)
- Buy Box and pricing strategy
- Pro Seller Badge requirements
- Walmart+ customer targeting and visibility

## Platform Rules and Constraints

Walmart Marketplace (US) rules at the last review of this skill (November 2026), from Walmart Marketplace Learn, the Seller Center performance pages and the referral fee guide. Items marked **[check]** change and must be confirmed.

- **Application and approval:** Walmart reviews each application. It asks for a US business tax ID (EIN; some non-US businesses are accepted with conditions **[check]**), W-9 or W-8, proof of marketplace or e-commerce history, product catalogue information and the integration method. Approval is not guaranteed.
- **Fees:** no monthly subscription; a **referral fee** per sale, by category, mostly 15% at last review with lower rates in some categories (e.g. 8% for some electronics and grocery tiers) **[check: Walmart referral fee guide]**. WFS adds fulfilment and storage fees.
- **Seller performance standards [check: Seller Center > Performance]:** on-time delivery, valid tracking rate (about 99%), seller response rate within 48 hours (about 95%), cancellation rate (about 2% maximum), refund rate (about 6% maximum). Sellers below standard can be warned, have items unpublished, or be suspended.
- **Pricing rules:** Walmart may unpublish items whose price is far above prices found elsewhere (*reasonable price* rule) or that look like price gouging **[check]**.
- **Buy Box:** several sellers share one item page; Walmart chooses the featured offer mainly from total price (item + shipping), delivery speed and seller performance.
- **WFS (Walmart Fulfillment Services):** Walmart stores, picks, ships and handles returns; WFS items get 2-day shipping tags and Walmart+ eligibility **[check]**.
- **Pro Seller badge:** granted monthly to sellers meeting performance, listing quality, shipping speed and returns criteria **[check: Seller Center > Pro Seller]**.
- **Returns:** sellers must follow Walmart's return policy (including Walmart's return window for the category) and process refunds in time.

## Data Needed

| Data | Where |
|------|-------|
| Business documents (EIN, W-9, marketplace history), catalogue size, GTINs | Seller's records |
| Product costs, dimensions and weights | Supplier data |
| Referral fee rate per category | Walmart referral fee guide |
| WFS fulfilment and storage fee rates | WFS fee page / WFS calculator in Seller Center |
| Performance metrics (on-time delivery, valid tracking, response, cancellation, refund) | Seller Center > Performance dashboard |
| Buy Box status, Listing Quality, price competitiveness | Seller Center > Listing Quality and Pricing |

## Workflow

1. **Check eligibility and prepare the application:** EIN, W-9, marketplace history, catalogue with GTINs (GS1 barcodes), and an integration method (Seller Center bulk templates, API, or an approved solution provider).
2. **Confirm unit economics per item** before listing: price − product cost − referral fee − fulfilment (WFS or own shipping) − returns allowance. Use `profit-margin-calculator-walmart`.
3. **Set up the account:** shipping templates and fulfilment centers, return settings, tax settings, payment details.
4. **List items** via bulk templates or API; follow `walmart-listing-optimization` for content and the Listing Quality score.
5. **Choose fulfilment per item** with the WFS-vs-self comparison below (cost per unit and delivery speed).
6. **Win the Buy Box:** keep total price competitive and use Walmart's Repricer in Seller Center with a floor price that protects the margin.
7. **Monitor performance weekly** (the 5 standards) and fix causes (carrier cut-off times, stock sync, response time).
8. **Scale:** Walmart Connect ads (`walmart-advertising-strategy`), Pro Seller badge, seasonal events, new item lines that pass the margin test.

## Calculations and Tools

- **Referral fee** = referral rate × total sale price (item price + shipping charged).
- **Contribution per unit (self-fulfilled)** = price − product cost − referral fee − label cost − packaging − returns allowance.
- **Contribution per unit (WFS)** = price − product cost − referral fee − WFS fulfilment fee − monthly storage share − inbound freight per unit − returns allowance.
- **Valid tracking rate** = orders with valid tracking ÷ orders shipped; **cancellation rate** = seller-cancelled orders ÷ orders.
- **Buy Box gap** = your total price − featured offer total price; keep it ≤ 0 or offer faster delivery.

## Worked Example

*Illustrative example with invented figures.* A $29.99 storage set costs $9.00, weighs 2.5 lb, referral fee 15%.

- Referral fee = $4.50. Self-fulfilled with a $7.80 label and $0.60 packaging: contribution = 29.99 − 9.00 − 4.50 − 7.80 − 0.60 − 0.90 (3% returns allowance) = **$7.19**.
- WFS with a fulfilment fee to be read from the current WFS fee table (say $5.75, to verify) plus $0.40 storage and $0.70 inbound: 29.99 − 9.00 − 4.50 − 5.75 − 0.40 − 0.70 − 0.90 = **$8.74**, with 2-day delivery tags.
- Decision: WFS for this item if the fee table confirms the rate.

## Example Requests

- "I sell kitchen storage on Amazon. What do I need to apply to Walmart Marketplace and how long will approval take?"
- "Compare WFS and self-fulfilment for my $29.99, 2.5 lb storage set with a 15% referral fee."
- "My Walmart valid tracking rate is 97.5% and my cancellation rate 2.4%. What is at risk and how do I fix it?"

## Output Format

1. Readiness checklist (documents, GTINs, integration method) with status.
2. Unit economics table per item: price, fees, fulfilment option, contribution.
3. Performance table: each standard, seller value, threshold (with check date), action.
4. 90-day plan: setup, first listings, fulfilment choice, Buy Box and Repricer settings, ads start date.

## Quality Checks

- Referral rates and WFS fees taken from Walmart's current fee pages with the check date.
- Every item listed has a positive contribution after referral fee, fulfilment and returns.
- GTINs belong to the brand (GS1), no reused or purchased barcodes of unknown origin.
- Performance thresholds compared with the seller's own dashboard values.
- No advice to bypass Walmart rules (off-platform contact with buyers, price gouging).

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** the seller's costs and performance dashboard, fee rates copied from Walmart's fee guide with date.
- **Estimates:** approval time, Buy Box share, returns allowance, sales uplift from WFS or Pro Seller.
- Rules and thresholds were reviewed in November 2026; items marked [check] must be re-confirmed on Walmart's current pages.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill walmart-seller-guide -g
```

## Usage

Ask your AI agent:

- "Help me apply and set up my Walmart Marketplace seller account."
- "Optimize my Walmart product listings for better search ranking."
- "Should I use WFS or self-fulfill on Walmart?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
