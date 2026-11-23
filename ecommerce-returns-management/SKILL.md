---
name: ecommerce-returns-management
description: "Optimize e-commerce returns process and reduce return rates. Returns policy design, reverse logistics, root cause analysis, and customer retention through better returns experience. Use when a seller asks how to reduce return rates, write a return policy, handle reverse logistics or find out why customers return products."
metadata:
  nexscope:
    emoji: "📥"
    category: ecommerce
---

# E-Commerce Returns Management 📥

Optimize e-commerce returns process and reduce return rates. Returns policy design, reverse logistics, root cause analysis, and customer retention through better returns experience.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Returns on any channel: cost per return, reasons, policy, grading and fraud controls.

Part of: Shipping and returns. For neighbouring jobs, use the matching skill instead:

- `ecommerce-shipping-rates` — Parcel costs on any carrier: dimensional weight, zones, surcharges, free-shipping threshold.
- `tiktok-shop-returns` — TikTok Shop returns and refunds.
- `tiktok-shop-shipping` — Shipping templates, carriers, shipping prices and delivery promise.
- `etsy-shipping-strategy` — Etsy shipping profiles, prices, processing times and free shipping.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-returns-management -g
```

## Usage

```
My return rate is 22% on Amazon (clothing category). Industry average is 15-20%. Help me analyze why and reduce it.
```

## Capabilities

- Returns rate benchmarking by category
- Return reason analysis and root cause identification
- Returns policy optimization (balancing customer satisfaction vs cost)
- Reverse logistics workflow design
- Return cost calculation (shipping, restocking, loss)
- Product listing improvements to reduce returns (size guides, photos, descriptions)
- Customer retention strategies post-return

## Principles and Constraints

Returns rules and standards across channels, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed for the seller's country and marketplace.

- **Legal minimums come first:** EU and UK consumers have a 14-day right of withdrawal for distance sales (the seller may charge the return shipping only if this was disclosed before purchase) **[check]**; US returns are mostly governed by the seller's stated policy and state rules on posting it.
- **Marketplaces impose their own policies:** Amazon's return policy and prepaid label rules, Walmart's return windows, eBay's return options and TikTok Shop's return process override your store policy on those channels **[check each]**. Amazon also shows a "frequently returned item" notice on some product pages **[check]**, so high return rates hurt conversion there.
- **Restocking fees must be disclosed** before purchase and are not allowed in all cases (e.g. not for EU withdrawal of unopened goods) **[check]**.
- **Returned products are not free stock:** inspection, cleaning, repackaging and grading cost money; some items (hygiene, opened cosmetics, damaged) cannot be resold.
- **Fight causes, not customers:** most returns come from fit, expectation gaps (photos, descriptions) and damage; returns fraud (wardrobing, empty-box) needs specific controls without punishing honest buyers.
- **Neighbouring skills:** TikTok Shop return handling `tiktok-shop-returns`, review and feedback analysis `product-review-analysis`, `customer-feedback-analysis`.

## Data Needed

| Data | Where |
|------|-------|
| Units sold and returned per SKU and period | Order system and marketplace return reports |
| Return reasons (customer-selected and free text) and condition on receipt | Return reports, warehouse inspection log |
| Return shipping cost, processing cost per return, share resellable | Carrier invoices, warehouse/3PL invoices |
| Price, unit cost per SKU | Catalogue and finance |
| Current returns policy per channel | Store policy page, marketplace settings |
| Reviews and questions mentioning size, quality, mismatch | Reviews, Q&A, support tickets |

## Workflow

1. **Compute return rate and cost per SKU** with `returns_cost.py`; rank SKUs by returns cost, not only by rate.
2. **Analyse reasons:** group free-text reasons into causes (size/fit, not as described, quality/defect, damaged in transit, changed mind, late delivery) and match them with warehouse condition notes.
3. **Read the evidence for top SKUs:** reviews, Q&A and photos of returned items to find the exact expectation gap.
4. **Fix the listing causes:** size charts with body measurements and fit notes, true-colour photos, scale photos, material details, compatibility tables.
5. **Fix product and packaging causes:** supplier quality checks for defect reasons, packaging tests (drop tests) for damage reasons.
6. **Design the policy and process per channel:** window, who pays shipping, exchange-first option, returnless refunds for low-value items where return cost exceeds recoverable value, inspection grades (A resell, B outlet, C liquidate, D destroy/recycle).
7. **Add fraud controls** proportionate to risk: serial-number/ tag checks, photos on receipt, account-level return limits on your own store.
8. **Track monthly** return rate, cost per return and reasons per SKU; confirm that fixes reduce the targeted reason.

## Calculations and Tools

- **Return rate** = units returned ÷ units sold (same sale period; returns lag sales).
- **Cost per return** = return shipping + processing + (1 − resellable share) × unit cost.
- **Net margin after returns** = kept units × (price − unit cost) − returns cost.
- **Returnless refund threshold**: refund without return when price × resellable share × recovery rate < return shipping + processing (working rule).
- **Reason share** = returns for a reason ÷ total returns of the SKU.

```bash
python3 scripts/returns_cost.py '{"return_rate_alert": 0.10, "skus": [{"sku": "DRESS-M", "units_sold": 400, "units_returned": 72, "price": 59.0, "unit_cost": 18.0, "return_shipping": 7.5, "processing_cost": 3.0, "resellable_share": 0.8, "reasons": {"too small": 30, "not as pictured": 18, "changed mind": 24}}, {"sku": "SCARF-1", "units_sold": 250, "units_returned": 10, "price": 29.0, "unit_cost": 8.0, "return_shipping": 5.0, "processing_cost": 2.0, "resellable_share": 0.95, "reasons": {"changed mind": 7, "damaged": 3}}]}'
```

## Worked Example

*Illustrative example with invented figures.* The command above reports for DRESS-M: return rate 18.0%, cost per return $14.10 (7.50 + 3.00 + 20% × $18), returns cost $1,015.20, net margin $12,432.80 vs $16,400 before returns; "too small" is 41.7% of its returns. SCARF-1 returns 4.0% at $7.40 each.

- Action for DRESS-M: add a size chart in cm/in with model measurements and "runs small: order one size up" if reviews confirm; recheck the "too small" share after 6 weeks of sales.

## Example Requests

- "My return rate is 22% on Amazon in clothing. Analyse why and how to reduce it."
- "Calculate the real cost of returns per SKU from this data, including items I cannot resell."
- "Should I offer free returns on my Shopify store, and when should I refund without asking for the item back?"

## Output Format

1. Returns table per SKU: return rate, cost per return, returns cost, net margin, top reason.
2. Reason analysis with evidence (reviews, inspection notes) for the top SKUs.
3. Fix list by cause (listing, product, packaging, policy) with owner and target reason share.
4. Policy and process per channel (window, shipping, exchanges, returnless threshold, grading).
5. Monthly tracking sheet.

## Quality Checks

- Return rate uses returns of the same sale cohort or a stated lag.
- Cost per return includes non-resellable losses.
- Policies comply with each channel's rules and consumer law in each selling country.
- Fixes target a measured reason and have a follow-up metric.
- Fraud controls do not block legal returns.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** returns, reasons and costs from the seller's reports and invoices for a stated period.
- **Estimates:** resellable share before inspection data exists, expected reduction from fixes, industry return-rate benchmarks.
- Legal and marketplace rules were reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
