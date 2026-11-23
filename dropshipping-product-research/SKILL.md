---
name: dropshipping-product-research
description: "Dropshipping product research on any channel. Screens candidate products with supplier quotes, landed cost including duties, margin, maximum CPA and break-even ROAS, delivery time, return risk and marketplace dropshipping rules, with a scoring script. Use when someone asks what to dropship, wants to validate a dropshipping product or supplier, or compare margins and delivery times of candidates (to set up a Shopify dropshipping store use `shopify-dropshipping`)."
metadata:
  nexscope:
    emoji: "📦"
    category: ecommerce
---

# Dropshipping Product Research 📦

Product research for dropshipping businesses. Identify profitable products with reliable suppliers, healthy margins, and manageable competition. Evaluates shipping times, return risk, and marketing viability.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Screening dropshipping products: supplier quotes, landed cost, max CPA, delivery time, policy checks.

Part of: Product research and launch. For neighbouring jobs, use the matching skill instead:

- `shopify-dropshipping` — Running a dropshipping store on Shopify: apps, supplier connections and order flow.
- `tiktok-shop-product-research` — Scoring and validating a product idea for TikTok Shop.
- `ebay-product-research` — Deciding what to sell on eBay from sold listings: sell-through rate, sold prices, net per sale.
- `product-launch-strategy` — Planning a product launch on any channel: timeline, stock, pricing, compliant reviews, launch ads.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill dropshipping-product-research -g
```

## Usage

```
Help me find dropshipping products in the pet accessories niche. Budget is $2000 to start. I want to sell via Shopify with Meta ads.
```

## Capabilities

- Product viability scoring for dropshipping (margin, weight, fragility, return risk)
- Supplier reliability assessment framework
- Shipping time and cost analysis by origin/destination
- Marketing angle identification (social media, paid ads, SEO)
- Competition analysis specific to dropshipping niches
- Trend validation and longevity assessment

## Principles and Constraints

Rules that decide whether a dropshipping product is viable, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed with the marketplace, customs authority or counsel.

- **Marketplace dropshipping policies [check]:** Amazon allows dropshipping only if you are the seller of record, are identified on packing slips and invoices, remove third-party supplier information and handle returns; buying from another online retailer and having it ship directly to your customer is not allowed. eBay forbids listing an item and having another retailer or marketplace ship it to the buyer (wholesale dropshipping suppliers are allowed). Walmart and TikTok Shop require you to meet their shipping-time and tracking standards.
- **Duties changed in 2025 [check]:** the US suspended the $800 de minimis exemption for low-value parcels (for China and Hong Kong from May 2025, then for all countries from August 2025), so duties and fees now apply to many dropshipped parcels; the EU has charged VAT on all imports since 2021 (IOSS for consignments ≤ €150).
- **Product safety and compliance:** the EU General Product Safety Regulation (since December 2024) requires an EU-based responsible person and traceability information for products sold to EU consumers; children's products, electronics and cosmetics need certificates in most markets.
- **Delivery promises are legal promises:** the US Mail Order Rule requires shipping within the time stated (or 30 days) and notifying delays; long delivery times drive chargebacks and refunds.
- **Intellectual property:** many trending products copy protected designs or brands; check before listing.
- **Neighbouring skills:** Shopify dropshipping set-up and apps `shopify-dropshipping`, TikTok Shop product research `tiktok-shop-product-research`, unmet needs in a niche `market-gap-analysis`.

## Data Needed

| Data | Where |
|------|-------|
| Candidate products: retail price you can charge, competitor prices | Store/marketplace research, ads libraries |
| Supplier price, shipping cost and delivery time to your customers' country | Supplier quotes (several suppliers per product), sample orders |
| Duties and import fees for the destination | Customs tariff tools, supplier/forwarder quotes |
| Return risk factors: size/fit, fragility, electronics, expectations | Product type, competitor reviews |
| Expected CPA from tests or similar products | Ad tests, past campaigns |
| Supplier reliability: order history, ratings, response time, stock levels | Supplier platform, sample orders |

## Workflow

1. **Generate candidates** from demand signals (search trends, marketplace best sellers, ad libraries) and unmet needs (`market-gap-analysis`); avoid products with clear IP owners.
2. **Screen for policy and compliance:** prohibited/restricted on your channels, certificates needed, GPSR responsible person for EU sales, batteries or liquids.
3. **Collect 2–3 supplier quotes per product** with delivery time to your main market, duties/fees included or not, and stock levels.
4. **Order samples** from the shortlisted suppliers: check quality, packaging, branding on parcels and real delivery time.
5. **Run `dropship_score.py`:** landed cost, gross margin, contribution before ads, maximum CPA, break-even ROAS and the stated score.
6. **Check the ad maths:** expected CPA from a small test (or similar products) must be well below the maximum CPA.
7. **Plan operations:** delivery promise per country, tracking, returns address and process, customer service macros for delays.
8. **Test 2–3 products** with a fixed budget and stop rules (e.g. stop if CPA > max CPA after 1.5× max CPA spent without a sale), then scale the winner.

## Calculations and Tools

- **Landed cost** = supplier price + shipping + duties/fees per unit.
- **Contribution before ads** = price − landed cost − payment and platform fees − return allowance.
- **Maximum CPA** = contribution before ads; **break-even ROAS** = price ÷ contribution before ads.
- **Profit per order at expected CPA** = contribution before ads − expected CPA.
- **Stop rule** (this skill's): stop a product test after spending 1.5 × max CPA with no sale, or after 50 clicks with no add-to-cart.
- **Score** (0–100, stated weights): margin 40, delivery speed 25, return risk 20, ad viability 15 (see the script header).

```bash
python3 scripts/dropship_score.py '{"payment_fee_rate": 0.029, "payment_fee_fixed": 0.30, "products": [{"name": "Dog cooling mat", "price": 39.99, "supplier_cost": 11.20, "shipping_cost": 4.80, "shipping_days": 9, "return_risk": "low", "expected_cpa": 14.0}, {"name": "LED dog collar", "price": 24.99, "supplier_cost": 6.10, "shipping_cost": 3.90, "shipping_days": 14, "return_risk": "medium", "expected_cpa": 16.0}]}'
```

## Worked Example

*Illustrative example with invented figures (no duties included: add them for your destination).* The command above compares two pet products sold via Shopify with Meta ads:

- Dog cooling mat: landed $16.00, gross margin 60.0%, max CPA **$21.33**, break-even ROAS 1.87, profit $7.33 at a $14 CPA, score 90 → test.
- LED dog collar: landed $10.00, max CPA $11.97 but expected CPA $16 → loses **$4.03** per order, 14-day delivery, score 55 → test only with a clear angle (e.g. a bundle that raises the price).
- Budget $2,000: test the mat with $600 (stop rule: no sale after $32 spent on an ad set), keep $1,400 for scaling and samples.

## Example Requests

- "Help me find dropshipping products in the pet accessories niche with a $2,000 budget, selling via Shopify with Meta ads."
- "Compare these 5 AliExpress products: margins, maximum CPA and delivery times to the US after the de minimis change."
- "Can I dropship on Amazon and eBay, and what are the rules?"

## Output Format

1. Candidate list with demand evidence and policy/compliance screening.
2. Supplier comparison per product (price, shipping, delivery time, duties, sample results).
3. Economics table (script output) with max CPA, break-even ROAS and verdict.
4. Test plan with budget, stop rules and success criteria.
5. Operations checklist (delivery promise, tracking, returns, customer service).

## Quality Checks

- Channel dropshipping rules and product compliance checked for each candidate.
- Landed cost includes duties and fees for the destination (or states they are excluded).
- Delivery times from sample orders, not supplier claims only.
- Ad viability compares expected CPA with the computed max CPA.
- No product with obvious IP risk recommended.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** supplier quotes, sample-order delivery times, fee rates, test campaign results with dates.
- **Estimates:** expected CPA, return allowances, demand trends, the script's score weights.
- Policies and customs rules were reviewed in November 2026; confirm items marked [check] (not legal advice).

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
