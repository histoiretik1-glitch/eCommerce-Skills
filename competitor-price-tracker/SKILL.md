---
name: competitor-price-tracker
description: "Set up competitor price tracking and monitoring workflows. Track price changes, detect promotions, analyze pricing patterns, and get alerts for competitive price movements. Use when a seller wants to monitor competitor prices over time, detect promotions or price drops, or decide how to respond to a price war (for one-off pricing analysis use `competitor-price-analysis`)."
metadata:
  nexscope:
    emoji: "📊"
    category: ecommerce
---

# Competitor Price Tracker 📊

Set up competitor price tracking and monitoring workflows. Track price changes, detect promotions, analyze pricing patterns, and get alerts for competitive price movements.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Ongoing tracking of competitor prices with alerts.

Part of: Pricing. For neighbouring jobs, use the matching skill instead:

- `competitor-price-analysis` — One-off analysis of competitor prices and positioning.
- `competitive-pricing-strategy` — Price architecture and response rules against competitors.
- `dynamic-pricing-ecommerce` — Automated repricing rules with floors, ceilings and guardrails.
- `price-optimization-tool` — Choosing a price from unit economics, elasticity and price tests.
- `walmart-price-tracker` — Walmart-specific price tracking and repricing.
- `minimum-advertised-price` — MAP policy and enforcement: policy document, violation checks across channels and escalation steps.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill competitor-price-tracker -g
```

## Usage

```
Help me track pricing for 10 competitor products on Amazon. I want to know when they change prices or run promotions so I can respond quickly.
```

## Capabilities

- Competitor price monitoring setup methodology
- Price change detection and alert framework
- Promotional pricing pattern analysis (frequency, depth, timing)
- Price war detection and response strategy
- MAP violation monitoring setup
- Historical price trend analysis methodology

## Principles and Constraints

Cross-channel rules for ongoing competitor price tracking, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed with the data source.

- **Compare like with like:** match products by GTIN/UPC/EAN or brand + MPN, same pack size and condition; compare **landed price** (item + shipping − instant coupons) because marketplaces rank and buyers choose on it.
- **Collect data lawfully:** use official APIs and feeds where they exist (for example Amazon SP-API competitive pricing for your own listings, Google Merchant Center price competitiveness reports **[check availability]**), reputable price-intelligence tools, or manual checks. Scraping must respect the site's terms and robots.txt; never scrape behind a login.
- **Price changes are observations at a time:** record the timestamp, location/ZIP (marketplace prices and delivery fees vary by region) and the seller who holds the featured offer.
- **Respond with rules, not reflexes:** every automatic response needs a floor price from your costs; competition law forbids agreeing prices with competitors, and MAP policies may limit advertised prices (`minimum-advertised-price`).
- **Scope:** this skill is the ongoing monitoring system. A one-off price positioning study is `competitor-price-analysis`; Walmart Buy Box price tracking is `walmart-price-tracker`; automated repricing rules are `dynamic-pricing-ecommerce`.

## Data Needed

| Data | Where |
|------|-------|
| Your SKU list with GTIN/MPN, price, cost and floor price | Catalogue and finance |
| Competitor listings matched to each SKU (URL or ID per channel) | Manual matching, then tool or API |
| Price snapshots: timestamp, competitor, SKU, price, shipping, coupon/strike-through, stock status | Tracking tool export, API, manual log |
| Your sales and conversion per SKU over the same period | Store / marketplace reports |
| Promotional calendar (yours and known competitor events) | Marketing calendar |

## Workflow

1. **Select the SKUs to track:** top revenue SKUs and SKUs where you lose the featured offer or conversion; usually 20–100, not the whole catalogue.
2. **Match competitors** for each SKU (3–5 direct competitors per channel) and record the match key (GTIN or brand + MPN).
3. **Set the cadence:** daily for marketplace featured-offer products, weekly for D2C sites; more often during events (Prime Day, Black Friday).
4. **Collect snapshots** with the chosen method into one table with the fields above.
5. **Compute indicators** per SKU and week: price index, number and depth of changes, promotion frequency, stock-outs.
6. **Define alert rules:** competitor landed price drops more than X% (e.g. 5%), goes below your floor, starts a promotion, or goes out of stock (opportunity to hold price).
7. **Define response playbooks** per alert: hold, match down to the floor, respond with value (bundle, faster shipping) or wait 48 hours to see if the move holds.
8. **Review monthly** whether price moves explain sales changes (index vs conversion) and adjust rules.

## Calculations and Tools

- **Landed price** = item price + shipping − instant coupon.
- **Price index** = your landed price ÷ median competitor landed price × 100 (100 = at market).
- **Promotion frequency** = days with a promotion ÷ days observed; **promotion depth** = (regular − promo) ÷ regular.
- **Volatility** = number of price changes per SKU per week.
- **Price war signal** (this skill's rule): 3 or more successive undercuts between the same sellers within 7 days.
- **Response floor** = unit cost + fees + shipping + minimum profit; never alert-match below it.

## Worked Example

*Illustrative example with invented figures.* A 2-pack of stainless water bottles sells at $34.99 + free shipping. Three competitors in week 46: $32.99 + $0, $29.99 + $4.99, $33.49 + $0 (strike-through from $39.99).

- Landed prices: 32.99, 34.98, 33.49 → median 33.49 → index = 34.99 ÷ 33.49 × 100 = **104.5**.
- Competitor C is on promotion (depth 16%); its promotions ran 9 of the last 28 days (frequency 32%).
- Floor = $27.40 from costs. Rule: no match while the index stays below 105 and conversion holds; if index > 108 for 3 days, match to $33.49.

## Example Requests

- "Track 10 competitor products on Amazon and alert me when they change prices or start promotions."
- "Design a weekly price tracking sheet for my 40 best-selling SKUs across Amazon, Walmart and my Shopify store."
- "Two sellers keep undercutting me every day on the same product. Is this a price war and how should I respond?"

## Output Format

1. Tracking scope: SKU list, matched competitors, match keys, channels, cadence, data source per channel.
2. Snapshot table template and the weekly indicator table (index, changes, promo frequency and depth, stock-outs).
3. Alert rules with thresholds and the playbook for each.
4. Monthly review: price index vs sales/conversion per SKU, rule changes.

## Quality Checks

- Every match uses a product identifier; mismatched pack sizes are excluded.
- Landed prices include shipping and instant coupons; timestamp and region recorded.
- Data collection method respects each site's terms.
- Each automated response has a floor price from the seller's costs.
- Conclusions about sales impact compare the same periods and account for your own promotions.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** price snapshots with timestamp and source, the seller's costs and sales.
- **Estimates:** competitor costs or margins, expected sales effect of a price move, missing snapshots filled by interpolation.
- Data-source availability was reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
