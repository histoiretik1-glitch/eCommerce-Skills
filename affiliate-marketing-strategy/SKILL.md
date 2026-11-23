---
name: affiliate-marketing-strategy
description: "Build and scale affiliate marketing programs for e-commerce stores. Covers program setup, commission structures, affiliate recruitment, tracking, and optimization for Shopify, Amazon, and independent stores. Use when the user asks for help launching, structuring or scaling an affiliate program, setting commissions, or recruiting and tracking affiliates."
---

# Affiliate Marketing Strategy

Build and scale affiliate marketing programs for e-commerce stores. Covers program setup, commission structures, affiliate recruitment, tracking, and optimization for Shopify, Amazon, and independent stores.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Commission-based affiliate programmes: commission ceiling, terms, networks, incrementality.

Part of: Affiliate and creator partnerships. For neighbouring jobs, use the matching skill instead:

- `influencer-outreach` — Finding, contacting and contracting influencers on any platform.
- `tiktok-shop-affiliate-program` — Setting up the TikTok Shop affiliate program: open and targeted collaborations, commission rates, samples.

<!-- role-and-scope:end -->

## Capabilities

- Affiliate program platform selection (ShareASale, Impact, Refersion)
- Commission structure design by product category
- Affiliate recruitment strategy and outreach
- Creative asset library for affiliates
- Performance tracking and attribution
- Fraud detection and quality control
- Top performer incentive programs
- Amazon Associates vs own affiliate program comparison

## Principles and Constraints

Rules and standards that apply whatever the store platform, as known at the last review of this skill (November 2026). Items marked **[check]** change and must be confirmed with the network or regulator.

- **Disclosure is the affiliate's legal duty and the brand's responsibility to enforce.** In the US the FTC Endorsement Guides (16 CFR Part 255, revised 2023) require a clear and conspicuous disclosure of the material connection; in the EU and UK, unfair commercial practice rules require the same. Put it in the affiliate terms and audit it.
- **Pay on validated sales only.** Set a locking period at least as long as your return window so commissions on returned or cancelled orders are reversed.
- **Write the forbidden practices into the terms:** bidding on your brand name in search ads, coupon codes not issued to the affiliate, cookie stuffing, incentivised or self-referred purchases, trademark misuse in domains.
- **Networks and platforms** (examples): Impact, Awin (ShareASale's programmes moved to Awin **[check]**), CJ, Refersion or app-based programmes for Shopify stores. Networks charge setup and/or a commission override on top of affiliate payouts **[check each network's current pricing]**.
- **Amazon Associates is a different model:** you are the affiliate earning Amazon's category rates (short cookie window **[check]**), not the merchant controlling commissions. For Amazon sellers, Amazon's own brand referral programmes are handled in Seller Central.
- **Attribution:** most networks pay last click within a cookie window (often 30 days, set by you). Coupon and cashback sites tend to win the last click on purchases that would have happened anyway, so measure incrementality.
- **Platform programmes have their own rules:** for TikTok Shop creator commissions use `tiktok-shop-affiliate-program`; for one-to-one creator deals use `influencer-outreach`.

## Data Needed

| Data | Why |
|------|-----|
| Contribution margin per product before marketing (price − COGS − fees − shipping) | Ceiling for any commission |
| AOV, return rate and return window | Commission base and locking period |
| Current CAC by channel (paid social, search) | Affiliates must beat it to be worth adding |
| Share of new vs returning customers in affiliate orders | Commission tiers and incrementality |
| Affiliate report: clicks, orders, revenue, commissions, reversals per partner and type | Performance review |
| Coupon codes in circulation and where they leak | Leakage control |

## Workflow

1. **Set the commission ceiling** per product line from contribution margin and the CAC you accept (formula below); a commission above the ceiling buys revenue at a loss.
2. **Choose the model:** network (reach, recruiting, compliance tools) vs in-house app (lower fees, you recruit); write down the expected monthly volume to compare total costs.
3. **Design the commission plan:** base rate, higher rate or bonus for new customers, tiers for top partners, lower rate or flat fee for coupon/cashback sites, no commission on gift cards and shipping.
4. **Write the terms:** disclosure requirement, prohibited practices, locking period, payment schedule, brand-bidding ban, code ownership.
5. **Recruit by partner type:** content publishers and reviewers in your niche, creators already mentioning you, loyalty/cashback sites last; prepare a creative kit (product images, copy, landing pages, unique codes).
6. **Track correctly:** server-side or network pixel on the order confirmation, deduplication with other channels, unique codes per partner.
7. **Review monthly** per partner: EPC, conversion rate, AOV, reversal rate, new-customer share, effective CAC; act on outliers (fraud signals, leaked codes).
8. **Test incrementality** every 6 months: pause or lower rates for coupon sites in a test period and compare total sales, not affiliate-attributed sales.

## Calculations and Tools

- **Commission ceiling (%)** = (contribution margin per order − minimum profit per order) ÷ order value.
- **Effective CAC of the programme** = (commissions + network fees + bonuses + tool costs) ÷ new customers from affiliates.
- **EPC (earnings per click, partner view)** = commissions paid ÷ clicks; a low EPC makes partners drop your programme.
- **Reversal rate** = reversed commissions ÷ commissions generated; compare with the store return rate.
- **Coupon leakage share** = orders with a partner's code not coming from that partner's link ÷ orders with that code.
- **Incremental revenue** ≈ total revenue in test period − expected revenue without the partner (prior trend); label it an estimate.

## Worked Example

*Illustrative example with invented figures.* A skincare store: AOV $64, contribution margin before marketing $28 per order, minimum profit $8 → commission ceiling = (28 − 8) ÷ 64 = **31%**. Paid social CAC is $35.

- Plan: 15% base (= $9.60 per order), 20% on new customers, coupon sites 5%, network override of 20% of commissions (to verify on the network's pricing).
- Month 1 report: 120 affiliate orders, 70 new customers, commissions $1,420 + override $284 + $300 creative bonuses → effective CAC = 2,004 ÷ 70 = **$28.63**, below the $35 paid-social CAC.
- 38% of orders came from one coupon site with 80% returning customers: lower its rate and test incrementality.

## Example Requests

- "Set up an affiliate programme for my skincare brand: commission rates, terms and the network to use, with a $64 AOV and $28 margin per order."
- "My affiliate report shows one coupon site drives 40% of affiliate sales. Is it incremental, and how should I change its commission?"
- "Write affiliate terms that ban brand bidding and require FTC-compliant disclosure."

## Output Format

1. Commission ceiling table by product line and the chosen commission plan (base, new-customer, partner-type rates).
2. Programme model comparison (network vs in-house) with total monthly cost at expected volume.
3. Affiliate terms checklist (disclosure, prohibited practices, locking period, payments).
4. Recruitment plan by partner type with the creative kit list.
5. Monthly partner scorecard: clicks, EPC, orders, AOV, reversal rate, new-customer share, effective CAC, action.

## Quality Checks

- No commission rate above the ceiling computed from the store's own margins.
- Locking period ≥ return window; reversals tracked.
- Terms include disclosure duty, brand-bidding ban and code ownership.
- Effective CAC compared with other channels using the same definition of new customer.
- Coupon and cashback partners evaluated on incrementality, not on attributed sales alone.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** the store's margins, return rate, network report figures for a stated period, network fees from the signed contract.
- **Estimates:** expected affiliate volume, incremental share, "typical" commission rates in the niche.
- Legal and network points were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill affiliate-marketing-strategy -g
```

## Usage

Ask your AI agent:

- "Set up an affiliate program for my Shopify store."
- "What commission rates should I offer for my product category?"
- "Create a recruitment plan to find quality affiliates."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
