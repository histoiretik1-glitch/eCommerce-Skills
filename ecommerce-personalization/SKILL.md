---
name: ecommerce-personalization
description: "Design personalization strategies for e-commerce stores. Product recommendations, dynamic content, customer segmentation, and personalized email/SMS based on browsing and purchase behavior. Use when a store wants product recommendations, personalized content or emails, or customer segments to show different offers to different shoppers."
metadata:
  nexscope:
    emoji: "🎯"
    category: ecommerce
---

# E-Commerce Personalization 🎯

Design personalization strategies for e-commerce stores. Product recommendations, dynamic content, customer segmentation, and personalized email/SMS based on browsing and purchase behavior.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Personalising site content and recommendations by segment, with consent and holdouts.

Part of: Retention, loyalty and personalization. For neighbouring jobs, use the matching skill instead:

- `ecommerce-customer-retention` — Retention from order data: cohorts, RFM segments, lifecycle flows with holdouts.
- `shopify-loyalty-program` — Loyalty and rewards programmes on Shopify.
- `shopify-upsell-cross-sell` — Upsell and cross-sell offers on a Shopify store.
- `shopify-email-flows` — Setting up the core automated email flows of a Shopify store.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-personalization -g
```

## Usage

```
I run a Shopify store with 5,000 customers. How do I set up personalization? I want to show different products to different customer segments.
```

## Capabilities

- Customer segmentation framework (RFM, behavioral, demographic)
- Product recommendation engine strategy (collaborative, content-based, hybrid)
- Dynamic content personalization for homepage, PDP, and checkout
- Personalized email/SMS strategy by customer segment
- A/B testing framework for personalization
- Privacy-compliant data collection strategy
- Tool and app recommendations by platform (Shopify, WooCommerce)

## Principles and Constraints

Personalization rules for any store platform, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed for the seller's jurisdictions (this is not legal advice).

- **Consent and transparency:** behavioural tracking cookies need prior consent in the EU/UK (ePrivacy + GDPR); profiling must be disclosed in the privacy notice. In California (CCPA/CPRA) sharing data for cross-context behavioural advertising requires a "Do Not Sell or Share" option and honouring Global Privacy Control **[check]**. Other US states have similar laws.
- **Prefer first- and zero-party data:** purchase history, on-site behaviour with consent, quiz answers and stated preferences are more reliable and more defensible than bought third-party data.
- **No sensitive inferences:** do not personalise on health, religion, sexuality or other special categories without explicit consent; avoid personalised prices that could discriminate (and disclose personalised pricing where required **[check]**).
- **Start with rules, then algorithms:** rule-based personalization (new vs returning, location, last category viewed) works with little data; collaborative filtering needs enough interactions per product (cold start for new items and visitors).
- **Measure incrementality:** keep a holdout that sees the non-personalized experience; "revenue from recommendations" attributed by a widget overstates impact.
- **Neighbouring skills:** upsell/cross-sell offers on Shopify `shopify-upsell-cross-sell`, lifecycle email and SMS `ecommerce-customer-retention`, Shopify automations `shopify-email-flows`.

## Data Needed

| Data | Where |
|------|-------|
| Customers, orders and products bought (12+ months) | Store order export |
| Browsing events (product views, add to cart) with consent status | Analytics / CDP / personalization tool |
| Catalogue attributes (category, price band, style, compatibility) | Product catalogue / feed |
| Traffic split: new vs returning, device, country, source | Analytics |
| Current personalization tools and their reported results | App/tool dashboards |
| Consent rate of the cookie banner | Consent management platform |

## Workflow

1. **Check the data foundation:** consent rate, identity (logged-in share, email capture), catalogue attributes complete; personalization quality is capped by these.
2. **Segment:** start with 4–6 actionable segments (first-time visitor, returning non-buyer, first-time buyer, repeat buyer, VIP by RFM, lapsed) with sizes.
3. **Choose placements by traffic and value:** home page hero, collection sorting, product page recommendations, cart cross-sell, post-purchase email, search results.
4. **Define rules per segment and placement** (e.g. returning visitors see the last category viewed; first-time buyers see complementary items to their first purchase; lapsed customers see new arrivals since their last order).
5. **Pick the recommendation logic:** "frequently bought together" (co-purchase), "similar items" (content-based on attributes), "trending in category"; hybrid when data is enough; fall back to bestsellers for cold starts.
6. **Implement with a holdout** of 10% of eligible traffic per placement.
7. **Measure** CTR on recommendations, attach rate, AOV and RPV vs holdout for 4+ weeks.
8. **Iterate:** remove placements without incremental lift (they add page weight), extend winning rules to email and SMS.

## Calculations and Tools

- **Segment size and value** = customers and revenue share per segment (RFM quintiles as in `ecommerce-customer-retention`).
- **Co-purchase lift (A → B)** = P(B | A) ÷ P(B) from order data; recommend B with A when lift > 1 and P(B | A) is based on enough orders (e.g. 30+).
- **Recommendation CTR** = clicks on recommended items ÷ widget impressions; **attach rate** = orders containing a recommended item ÷ orders.
- **Incremental RPV** = RPV of personalized group − RPV of holdout; incremental revenue = incremental RPV × personalized sessions.
- **Minimum test duration** from the sample-size rules in `ecommerce-ab-testing`.

## Worked Example

*Illustrative example with invented figures.* 5,000 customers, 2,400 orders in 6 months. 380 orders contain a pour-over kettle (A); 120 of those also contain filters (B); 300 of all 2,400 orders contain filters.

- P(B | A) = 120 ÷ 380 = 31.6%; P(B) = 300 ÷ 2,400 = 12.5% → lift **2.5**: show filters on the kettle page and in the cart.
- Holdout after 5 weeks: RPV $2.31 personalized vs $2.19 holdout → incremental RPV $0.12 on 40,000 sessions ≈ **$4,800** over the period (check significance with `ecommerce-ab-testing` before scaling).

## Example Requests

- "I run a store with 5,000 customers. How do I set up personalization to show different products to different customer segments?"
- "Which products should I recommend together? Here is my order export."
- "Our recommendation app claims 18% of revenue. How do I know how much it really adds?"

## Output Format

1. Data readiness check (consent rate, identity, catalogue attributes) with gaps.
2. Segment table with rules, sizes and value.
3. Placement plan: placement, segment, logic, fallback, holdout size.
4. Co-purchase pairs with lift and support.
5. Measurement plan and results template (CTR, attach rate, AOV, RPV vs holdout).
6. Privacy checklist (consent, notice, opt-outs, sensitive data exclusions).

## Quality Checks

- Personalization uses only data collected with valid consent and disclosed in the privacy notice.
- Every placement has a fallback for new visitors and new products.
- Product pairs are based on enough co-purchases (support stated).
- Impact measured against a holdout, not from the tool's attributed revenue.
- No personalization on sensitive categories or prices that could discriminate.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** order-based pair statistics, segment sizes and holdout results from the store's data for stated dates.
- **Estimates:** expected uplift before tests, vendor case-study figures.
- Privacy rules were reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
