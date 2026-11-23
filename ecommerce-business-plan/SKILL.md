---
name: ecommerce-business-plan
description: "Create a comprehensive e-commerce business plan. Market analysis, financial projections, marketing strategy, operations planning, and milestone roadmap for new or growing e-commerce businesses. Use when someone needs a business plan for a new online store or e-commerce brand, financial projections, or a plan for investors or a loan."
metadata:
  nexscope:
    emoji: "📑"
    category: ecommerce
---

# E-Commerce Business Plan 📑

Create a comprehensive e-commerce business plan. Market analysis, financial projections, marketing strategy, operations planning, and milestone roadmap for new or growing e-commerce businesses.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Business plan for a new online business: market sizing, unit economics, cash flow.

Part of: Brand and business planning. For neighbouring jobs, use the matching skill instead:

- `ecommerce-branding` — Brand positioning, voice, visual identity and trademark clearance across channels.
- `ecommerce-growth-strategy` — Growth priorities for an existing business: unit economics, growth levers and roadmap.
- `tiktok-shop-branding` — Building a recognizable brand on TikTok: identity, content pillars, community.
- `etsy-shop-branding` — Shop identity on Etsy: name, banner, logo, About section, photo style and packaging.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-business-plan -g
```

## Usage

```
I want to start an e-commerce business selling premium dog accessories. Budget: $15,000. Help me create a business plan.
```

## Capabilities

- Market opportunity sizing and TAM/SAM/SOM estimation
- Competitive landscape analysis
- Business model definition (DTC, marketplace, hybrid)
- Financial projections (revenue, costs, break-even, cash flow)
- Marketing strategy outline with CAC and LTV targets
- Operations plan (fulfillment, supply chain, technology)
- Milestone roadmap (3-month, 6-month, 12-month)

## Principles and Constraints

Planning standards that hold for any online business model, as known at the last review of this skill (November 2026).

- **Bottom-up beats top-down:** market size from "number of buyers you can reach × purchase frequency × price" is more useful than a percentage of a global market report.
- **Unit economics first:** a plan only works if contribution per order (after product, fees, fulfilment, returns and payment costs) pays for customer acquisition with a margin left.
- **Cash is not profit:** inventory is paid weeks or months before it sells; marketplace payouts come days after the sale. Model cash month by month, including inventory deposits and lead times.
- **Scenarios, not one number:** base, low and high cases with stated assumptions; the low case must still be survivable with the money available.
- **Channel economics differ:** marketplace referral fees and fulfilment fees vs D2C payment fees and ad costs; use the platform profit calculators (`profit-margin-calculator-amazon`, `profit-margin-calculator-shopify`, `profit-margin-calculator-walmart`, `profit-margin-calculator-tiktok`) for exact fee structures.
- **Compliance costs are real costs:** business registration, sales tax/VAT registration, product safety testing and certification, insurance; list them in start-up costs.
- **Neighbouring skills:** opportunity finding `market-gap-analysis`, growth of an existing business `ecommerce-growth-strategy`, sourcing and logistics `supply-chain-optimization-shopify` (Amazon, Walmart and TikTok variants exist).

## Data Needed

| Data | Where |
|------|-------|
| Target customer and reachable audience size | Keyword volumes, marketplace category data, social audience tools |
| Price points of comparable products | Marketplace and competitor store research |
| Landed product cost (quotes incl. freight, duties) and MOQ | Supplier quotes, freight forwarder |
| Channel fees and fulfilment costs | Marketplace fee pages, 3PL quotes, payment processor |
| Expected CAC by channel (tests or reasoned assumptions) | Ad platform tests, similar-business data |
| Budget available and timeline | Founder |

## Workflow

1. **Define the offer and customer** in one paragraph: product line, price range, target buyer, channels (D2C, marketplace, hybrid).
2. **Size the market bottom-up:** reachable buyers per year × share you can win in year 1 (SOM) × orders per buyer × AOV; show TAM/SAM only as context.
3. **Analyse competition:** 5–10 competitors, their prices, ratings, review counts and positioning; note the entry barrier (reviews, brand, capital).
4. **Build unit economics per channel:** price, COGS landed, fees, fulfilment, returns allowance, payment fees → contribution per order; then contribution after a target CAC.
5. **Plan marketing** with CAC targets by channel and an LTV estimate (orders per customer × contribution); LTV:CAC ≥ 3 is a common target, payback within 6–12 months for a bootstrapped business.
6. **Plan operations:** supplier, MOQ, lead time, fulfilment model (self, 3PL, FBA/WFS), tech stack and monthly tool costs.
7. **Project 12–24 months** of P&L and cash flow by month, with inventory purchases at their real payment dates; compute break-even and lowest cash point.
8. **Set milestones** at 3, 6 and 12 months with go/no-go metrics (e.g. contribution margin after ads, repeat rate, review count).

## Calculations and Tools

- **SOM (year 1 revenue)** = reachable buyers × expected share × orders per buyer × AOV.
- **Contribution per order** = price − landed COGS − channel fees − fulfilment − returns allowance − payment fees.
- **Break-even orders per month** = fixed monthly costs ÷ (contribution per order − CAC per order).
- **Inventory cash need** = units ordered × landed unit cost, paid at deposit and balance dates; **cash conversion cycle** = days of inventory + days to receive payouts − days payable to supplier.
- **Lowest cash point** = minimum of cumulative cash over the projection; the budget must cover it plus a buffer (e.g. 2 months of fixed costs).
- **LTV:CAC** = (orders per customer over 12 months × contribution per order) ÷ CAC.

## Worked Example

*Illustrative example with invented figures.* Premium dog accessories, $15,000 budget, Shopify + Amazon.

- Hero product: $45 price, $12 landed cost, D2C fees and fulfilment $7.50, returns allowance $1.35 → contribution **$24.15** per order.
- Target CAC $16 → $8.15 left per order; fixed costs $1,400/month → break-even = 1,400 ÷ 8.15 ≈ **172 orders/month**.
- Cash before any sales income: $15,000 − first stock order 600 × $12 ($7,200, 30% at order and 70% before shipping, 60-day lead time) − launch ads $3,000 − start-up costs $1,500 (samples, registration, photos) − two months of fixed costs $2,800 = **$500**: too thin a buffer.
- Options: first order of 400 units ($4,800, frees $2,400), or ads only after the stock lands; the plan's go/no-go is CAC ≤ $16 over the first 300 orders.

## Example Requests

- "I want to start an e-commerce business selling premium dog accessories with a $15,000 budget. Help me create a business plan."
- "Build a 12-month cash flow for my first inventory order of 600 units with a 60-day lead time and 30% deposit."
- "Is a $45 product with $12 landed cost viable on Amazon and Shopify if my CAC is around $16?"

## Output Format

1. Executive summary (offer, customer, channels, money needed, break-even month).
2. Market sizing (bottom-up SOM, with TAM/SAM context) and competitor table.
3. Unit economics per channel and CAC/LTV targets.
4. Operations plan (supplier, lead time, fulfilment, tools, compliance costs).
5. Monthly P&L and cash-flow projection (base/low/high), break-even and lowest cash point.
6. Milestones with go/no-go metrics and the main risks with mitigations.

## Quality Checks

- Every assumption is listed with its source or marked as an estimate.
- Unit economics include fees, fulfilment, returns and payment costs per channel.
- Cash flow places inventory payments on their real dates; the low case does not run out of cash.
- Market size is bottom-up and consistent with the marketing budget.
- Compliance and registration costs included.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** supplier quotes, fee schedules, the founder's budget, observed competitor prices and review counts with dates.
- **Estimates:** market share, CAC before tests, conversion rates, repeat purchase rates, all projections.
- This plan is a decision tool, not financial or legal advice; reviewed November 2026.

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
