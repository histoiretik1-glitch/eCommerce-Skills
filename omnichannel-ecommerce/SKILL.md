---
name: omnichannel-ecommerce
description: "Plan and execute omnichannel e-commerce strategy. Unify selling across Amazon, Shopify, Walmart, TikTok Shop, eBay, and Etsy with consistent branding, inventory sync, and customer experience. Use when the user asks for help building an omnichannel strategy, choosing channels and unifying brand, inventory and customer experience."
---

# Omnichannel E-Commerce

Plan and execute omnichannel e-commerce strategy. Unify selling across Amazon, Shopify, Walmart, TikTok Shop, eBay, and Etsy with consistent branding, inventory sync, and customer experience.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Strategy: which channels to sell on and how to keep brand and customer experience consistent.

Part of: Selling on several channels. For neighbouring jobs, use the matching skill instead:

- `multichannel-ecommerce` — Operations: inventory sync, order routing and listing syndication across channels.

<!-- role-and-scope:end -->

## Capabilities

- Channel selection matrix by product type and audience
- Inventory synchronization across platforms
- Unified branding and product content management
- Platform-specific listing adaptation
- Order management and fulfillment routing
- Cross-channel pricing strategy
- Customer data unification and CRM integration
- Channel performance comparison and budget allocation

## Principles and Constraints

Strategy rules for choosing channels and keeping one customer experience, as known at the last review of this skill (November 2026).

- **Add a channel for a reason you can measure:** new customers you cannot reach today, better margin, or defensive presence (others are selling your brand there). Each channel adds fees, operations and compliance work.
- **Data ownership differs:** on your own store you own the customer relationship; on marketplaces (Amazon, Walmart, eBay, TikTok Shop) buyer data belongs to the marketplace and cannot be used for your own marketing. Plan retention accordingly.
- **Cannibalisation is real:** a marketplace can take sales from your own store; measure total brand sales and contribution, not channel sales in isolation.
- **Consistency without uniformity:** same brand promise, product facts, prices within policy (MAP) and service standards; formats adapted per channel.
- **Customer data across channels** (online store, POS, email, support) needs consent and a single customer ID; unify only what you are allowed to.
- **Physical retail and pick-up options** (BOPIS, ship-from-store, returns in store) need real-time stock by location.
- **Scope:** this skill is strategy. Running inventory sync, routing and syndication is `multichannel-ecommerce`; growth priorities overall `ecommerce-growth-strategy`; brand consistency work `ecommerce-branding`.

## Data Needed

| Data | Where |
|------|-------|
| Current channel P&L: revenue, contribution, CAC, repeat rate | Finance, `sales-tracking-tool` |
| Customer profile and where they shop and search | Surveys, analytics, marketplace search data |
| Candidate channel requirements and costs: fees, fulfilment, approval, content | Channel seller guides (`walmart-seller-guide`, `ebay-seller-guide`, `tiktok-shop-seller-guide`...) |
| Category demand on each candidate channel | Marketplace search results, best-seller ranks, keyword tools |
| Operational capacity: inventory, team hours, systems | Operations |
| Brand and pricing policies (MAP, authorised resellers) | Brand guide, MAP policy |

## Workflow

1. **Baseline current channels** with contribution after ads per channel and the share of new customers.
2. **List candidate channels** where the target customer already shops for the category (marketplaces, social commerce, wholesale, retail).
3. **Score each candidate** with the channel selection matrix (below) using real fee and demand data.
4. **Model the channel P&L** for 12 months: expected revenue, fees, fulfilment, ads, team time, set-up costs; include cannibalisation of existing channels.
5. **Decide the role of each channel:** acquisition (marketplaces, social), profit and retention (own store), reach (retail, wholesale); set channel-specific KPIs.
6. **Define consistency rules:** product content master, price corridor and MAP, service standards (shipping speed, returns), brand assets per channel.
7. **Plan customer data and experience:** unified customer ID where consented, cross-channel returns, inserts that bring marketplace buyers to brand-owned channels within the marketplace's rules.
8. **Launch in sequence** (one channel at a time), review after 90 days against the model, adjust budget by marginal return.

## Calculations and Tools

- **Channel selection matrix** (this skill's weights, 1–5 scores): demand for the category 30%, contribution margin after fees 25%, audience fit 20%, operational effort (inverse) 15%, brand control and data ownership 10%.
- **Channel contribution** = revenue − COGS − fees − fulfilment − ads − returns − allocated team cost.
- **Incremental contribution of a new channel** = new channel contribution − contribution lost on existing channels (cannibalisation estimate from before/after comparison).
- **Marginal ROAS / CAC** per channel for budget allocation: move budget towards the channel where the next dollar returns the most contribution.
- **Price corridor** = allowed range of channel prices around the reference price (e.g. ±5%), within MAP.

## Worked Example

*Illustrative example with invented scores.* A D2C skincare brand on Shopify and Amazon evaluates Walmart, TikTok Shop and wholesale to boutiques.

| Channel | Demand (30%) | Margin (25%) | Audience fit (20%) | Effort, inverse (15%) | Control (10%) | Score |
|---------|------|------|------|------|------|------|
| TikTok Shop | 4 | 3 | 5 | 3 | 2 | 3.60 |
| Walmart | 3 | 3 | 3 | 3 | 2 | 2.90 |
| Wholesale boutiques | 2 | 2 | 4 | 2 | 4 | 2.60 |

- Decision: launch TikTok Shop first as an acquisition channel with creator affiliates; KPI = new customers and contribution after commissions; revisit Walmart after 90 days.

## Example Requests

- "I sell on Amazon. Which additional channels should I expand to, and in what order?"
- "Create an omnichannel strategy for my DTC brand that keeps pricing and brand consistent."
- "Is Amazon cannibalising my Shopify store? How do I measure it?"

## Output Format

1. Current channel baseline (contribution, CAC, new-customer share).
2. Channel selection matrix with sources for each score.
3. 12-month P&L per candidate channel with cannibalisation assumption.
4. Channel roles and KPIs; consistency rules (content, price corridor, service).
5. Launch sequence and 90-day review plan.

## Quality Checks

- Candidate scores backed by data (fees from channel pages, demand observations with dates).
- Models include fulfilment, ads, team time and cannibalisation.
- Marketplace data-use rules respected in customer experience plans.
- Price corridor compatible with MAP and marketplace pricing rules.
- One channel launched at a time with a review date.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** current channel results, fee schedules with dates, observed demand indicators.
- **Estimates:** new channel revenue, cannibalisation, matrix scores (judgements, with their rationale).
- Method reviewed in November 2026.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill omnichannel-ecommerce -g
```

## Usage

Ask your AI agent:

- "I sell on Amazon. Which additional channels should I expand to?"
- "Create an omnichannel strategy for my DTC brand."
- "How do I sync inventory across Amazon, Shopify, and Walmart?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
