---
name: walmart-price-tracker
description: "Walmart price tracking and Buy Box price positioning with a tested script: landed prices (price plus shipping) of competing offers, price index against the lowest and median offer, rank and price changes, and repricing rules within margin limits (Walmart Repricer, reasonable-price checks). Use whenever a Walmart seller compares prices with other sellers, lost the Buy Box, or sets Walmart repricing rules, even for a few items."
nexscope:
  name: "Walmart Price Tracker"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "walmart"
    - "price-tracking"
    - "monitoring"
    - "competitor-analysis"
  model: "any"
  tokens: "~2000"
  keywords:
    - "walmart price tracker"
---

# Walmart Price Tracker

AI-powered Walmart price tracking and competitive pricing skill. Analyzes Walmart marketplace pricing trends, competitor price positioning, and generates repricing strategies for Walmart sellers.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Walmart-specific price tracking and repricing.

Part of: Pricing. For neighbouring jobs, use the matching skill instead:

- `competitor-price-analysis` — One-off analysis of competitor prices and positioning.
- `competitor-price-tracker` — Ongoing tracking of competitor prices with alerts.
- `competitive-pricing-strategy` — Price architecture and response rules against competitors.
- `dynamic-pricing-ecommerce` — Automated repricing rules with floors, ceilings and guardrails.
- `price-optimization-tool` — Choosing a price from unit economics, elasticity and price tests.
- `minimum-advertised-price` — MAP policy and enforcement: policy document, violation checks across channels and escalation steps.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| My items, prices and shipping | Walmart Seller Center (Items, Pricing) |
| Competing offers on the same item (seller, price, shipping) | Item page on Walmart.com ("other sellers"), Seller Center pricing insights |
| Price history | Seller's own exports or repeated snapshots |
| Cost, fees and minimum margin | `profit-margin-calculator-walmart` |
| Buy Box status per item | Seller Center reports |

## Workflow

1. **Collect** landed prices for every competing offer on the same day (and the same ZIP code if shipping varies).
2. **Compute** the price index, rank and changes with the script below.
3. **Price floor** per item from cost, Walmart referral fee, fulfillment and minimum margin (`profit-margin-calculator-walmart`); never reprice below it.
4. **Diagnose Buy Box losses**: price is one factor; Walmart also considers shipping speed and seller performance and does not publish the exact formula. Check delivery promise and metrics before cutting price.
5. **Reasonable price**: Walmart may unpublish items whose price it considers unreasonable compared with other offers or other sites; check Seller Center alerts for affected items.
6. **Repricing rules**: Walmart's Repricer in Seller Center or a third-party repricer, with floor, ceiling and strategy (e.g. match lowest landed price within margin); review rules weekly.
7. **Track** daily or weekly; record changes and their effect on Buy Box and sales.

## Calculations and Tools

`scripts/price_index.py`:

```bash
python3 scripts/price_index.py '{"items": [{"item_id": "559912345", "name": "Storage bins", "my_price": 24.99, "my_shipping": 0, "competitors": [{"seller": "BinsCo", "price": 23.49, "shipping": 0}, {"seller": "HomeGoods", "price": 22.99, "shipping": 2.99}]}]}'
```

- Landed price = item price + shipping.
- Index vs lowest = my landed ÷ lowest competing landed × 100; index vs median likewise.
- Position band (default 97-103 = "at market") is a policy choice.

## Example Requests

- "We lost the Buy Box on 12 Walmart items this week. Compare our prices with the other sellers."
- "Set repricing rules for my Walmart catalog without going below a 15% margin."
- "Track price changes of competitors on my top 20 Walmart items."

## Output Format

```
WALMART PRICE POSITION — [date]
| Item | My landed | Lowest | Median | Index vs lowest | Rank | Position | Last change | Floor |
Buy Box losses: [item → likely cause: price / shipping speed / performance]
Repricing rules: | Item group | Strategy | Floor | Ceiling |
```

## Quality Checks

- All prices in one comparison were collected the same day and include shipping.
- No recommendation goes below the margin floor.
- Buy Box conclusions are stated as hypotheses unless confirmed by Seller Center data.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: collected prices, Seller Center reports.
- **Estimates / unknowns**: Buy Box weighting (not published by Walmart), expected sales impact of a price change.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill walmart-price-tracker -g
```

## Usage

**Input:**
Product URL, category, or competitor list on Walmart

**Output:**
Price trend analysis, competitor price comparison, price band analysis, repricing strategy recommendations

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up walmart price tracker for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
