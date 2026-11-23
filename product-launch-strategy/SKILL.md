---
name: product-launch-strategy
description: "Plan and execute e-commerce product launches. Pre-launch, launch day, and post-launch playbooks for Amazon, Shopify, and multi-channel sellers. Covers inventory, pricing, advertising, and review strategy. Use when a seller is preparing to launch a new product and needs a pre-launch, launch-day and post-launch plan."
metadata:
  nexscope:
    emoji: "🚀"
    category: ecommerce
---

# Product Launch Strategy 🚀

Plan and execute e-commerce product launches. Pre-launch, launch day, and post-launch playbooks for Amazon, Shopify, and multi-channel sellers. Covers inventory, pricing, advertising, and review strategy.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Planning a product launch on any channel: timeline, stock, pricing, compliant reviews, launch ads.

Part of: Product research and launch. For neighbouring jobs, use the matching skill instead:

- `dropshipping-product-research` — Screening dropshipping products: supplier quotes, landed cost, max CPA, delivery time, policy checks.
- `shopify-dropshipping` — Running a dropshipping store on Shopify: apps, supplier connections and order flow.
- `tiktok-shop-product-research` — Scoring and validating a product idea for TikTok Shop.
- `ebay-product-research` — Deciding what to sell on eBay from sold listings: sell-through rate, sold prices, net per sale.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill product-launch-strategy -g
```

## Usage

```
I'm launching a new kitchen gadget on Amazon next month. Help me create a launch plan. Budget: $2,000 for launch. I have 500 email subscribers.
```

## Capabilities

- Pre-launch checklist (listing, inventory, pricing, imagery)
- Launch timeline creation (4-8 week plan)
- Launch pricing strategy (introductory pricing, coupons, deals)
- Review generation plan (compliant strategies per platform)
- Launch advertising playbook (PPC ramp-up schedule)
- Social proof and influencer seeding strategy
- Post-launch optimization workflow (days 7, 14, 30)

## Principles and Constraints

Launch rules that apply on marketplaces and D2C stores, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed in the channel's current help pages.

- **Reviews must be earned honestly:** the FTC rule on consumer reviews and testimonials (in force since October 2024) bans fake reviews, buying reviews and suppressing negative ones; marketplaces ban incentivised reviews. On Amazon, the compliant routes are Amazon Vine (brand-registered sellers, limited units per parent ASIN, enrolment fee **[check]**) and the Request a Review button (4–30 days after delivery **[check]**). Never ask only happy customers for reviews.
- **Reference prices must be real:** strike-through and "was" prices need a genuine prior price under marketplace rules and consumer law (EU Omnibus: lowest price in the prior 30 days **[check]**).
- **Pre-orders:** US Mail Order Rule requires shipping within the stated time (or 30 days) and notifying delays with a cancellation option **[check]**.
- **Stock-outs kill launches:** marketplaces reduce visibility of out-of-stock items, and ads stop; plan stock for the launch ramp plus lead time.
- **Paid traffic needs a converting listing first:** finish images, content and reviews strategy before spending on ads.
- **Neighbouring skills:** keyword map `ecommerce-keyword-research`, titles `product-title-optimization`, viability `ecommerce-business-plan`, TikTok Shop launches with creators `tiktok-shop-affiliate-program`, video assets `ecommerce-video-marketing`.

## Data Needed

| Data | Where |
|------|-------|
| Product readiness: images, video, content, compliance documents, barcodes | Product and listing team |
| Stock on hand, inbound dates, supplier lead time | Inventory and supplier |
| Unit economics and break-even ACoS/ROAS per channel | Profit calculators |
| Launch budget and existing audiences (email list, followers, past customers) | Marketing |
| Competitor launch benchmarks: prices, review counts, deals | Marketplace research |
| Keyword map for the product | `ecommerce-keyword-research` |

## Workflow

1. **T−8 to T−6 weeks — readiness:** final samples approved, compliance documents, barcodes, listing content and images, keyword map, video; landing page or waitlist for D2C.
2. **T−6 to T−4 — stock and pricing:** inbound stock booked so it is live (and checked in at FBA/WFS) before launch; launch price and real reference price defined; coupons/deals planned within channel rules.
3. **T−4 to T−2 — audience warm-up:** waitlist/email teasers, creator seeding with disclosure, Vine enrolment if eligible.
4. **T−1 — QA:** listing live check on mobile, variations, price, coupon display, tracking links and codes, ad campaigns built and paused.
5. **Launch week:** email the list with a launch offer, start ads (auto/broad discovery + exact match on top keywords), creators post, monitor stock daily.
6. **Days 7 and 14 — first optimisation:** search terms → negatives and exact match; conversion vs category; price/coupon adjustment; respond to first reviews and questions.
7. **Day 30 — review:** sales vs plan, ACoS vs break-even, review count and rating, stock cover; decide scale, fix or stop.
8. **Days 31–90 — move from launch to steady state:** lower launch discounts gradually, shift budget to profitable terms, plan the next restock.

## Calculations and Tools

- **Launch stock** = forecast daily sales × (days until next stock arrives + safety days); compare with MOQ and cash.
- **Launch ad budget** = target daily clicks × expected CPC × launch days; cap by acceptable loss.
- **Launch ACoS allowance** = break-even ACoS + planned investment (e.g. break-even 25% + 15 points for 30 days), written down with an end date.
- **Review target** = reviews needed to match the median review count of the top 10 competitors' entry level (e.g. the 10th result), reached with compliant methods only.
- **Day-30 contribution** = revenue − COGS − fees − fulfilment − ads − coupon cost.

## Worked Example

*Illustrative example with invented figures.* A kitchen gadget launching on Amazon with a $2,000 launch budget and 500 email subscribers; price $24.99, break-even ACoS 28%.

- Ads: 70 clicks/day × $0.85 CPC × 28 days ≈ **$1,666**; remaining $334 for a launch coupon ($3 off, about 110 redemptions).
- Launch ACoS allowance: 28% + 15 points = 43% until day 30, then back to ≤ 28%.
- Stock: forecast 15/day, next inbound in 50 days, 10 safety days → 15 × 60 = **900 units** needed; the 600 planned would run out around day 40 → move the reorder forward.
- Email: 500 subscribers × an assumed 2–4% purchase rate ≈ 10–20 early orders (estimate) to start sales history.

## Example Requests

- "I'm launching a new kitchen gadget on Amazon next month with a $2,000 budget and 500 email subscribers. Create a launch plan."
- "Build an 8-week launch timeline for a new product on Shopify and TikTok Shop."
- "How many units do I need for launch if I expect 15 sales a day and my next shipment arrives in 50 days?"

## Output Format

1. Launch timeline (T−8 weeks to day 90) with owners.
2. Readiness checklist (content, compliance, stock, tracking).
3. Pricing and promotion plan with reference price evidence.
4. Ad plan: structure, budgets, launch ACoS allowance and end date.
5. Review plan using compliant methods only.
6. Day 7/14/30 review templates and stock cover forecast.

## Quality Checks

- No review tactic outside channel rules and the FTC rule.
- Reference prices documented; coupons and deals within channel rules.
- Stock covers forecast through the next inbound with safety days.
- Launch loss allowance has a limit and an end date.
- Ads start only after the listing passes QA.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** costs, budgets, stock and lead times, actual post-launch sales and ad data.
- **Estimates:** forecasts, CPC, conversion and email purchase rates before launch.
- Channel rules were reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
