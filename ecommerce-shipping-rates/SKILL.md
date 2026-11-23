---
name: ecommerce-shipping-rates
description: "Compare and optimize shipping rates across carriers and fulfillment methods. UPS, FedEx, USPS, DHL rate comparison, zone optimization, and shipping strategy to maximize margins. Use when a seller wants to compare carriers, cut shipping costs, set shipping prices or decide on free-shipping thresholds."
metadata:
  nexscope:
    emoji: "🚚"
    category: ecommerce
---

# E-Commerce Shipping Rates 🚚

Compare and optimize shipping rates across carriers and fulfillment methods. UPS, FedEx, USPS, DHL rate comparison, zone optimization, and shipping strategy to maximize margins.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Parcel costs on any carrier: dimensional weight, zones, surcharges, free-shipping threshold.

Part of: Shipping and returns. For neighbouring jobs, use the matching skill instead:

- `ecommerce-returns-management` — Returns on any channel: cost per return, reasons, policy, grading and fraud controls.
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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-shipping-rates -g
```

## Usage

```
I ship about 200 orders/month from my Shopify store. Average package is 1.5 lbs. Currently using USPS Priority. Is there a cheaper option?
```

## Capabilities

- Multi-carrier rate comparison (USPS, UPS, FedEx, DHL)
- Shipping zone optimization strategy
- Free shipping threshold calculation (impact on AOV vs margin)
- Dimensional weight pricing analysis
- International shipping rate comparison
- Shipping insurance and tracking recommendations
- Shipping cost reduction strategies (negotiated rates, regional carriers)

## Principles and Constraints

Parcel pricing rules that apply to most carriers, as known at the last review of this skill (November 2026). Items marked **[check]** change each year (carriers publish new rates and surcharges, usually in January) and must be confirmed in the carrier's current rate guide.

- **Billable weight = the greater of actual and dimensional weight,** rounded up. Common divisors: 139 (in/lb) for UPS and FedEx daily rates, 166 for USPS on larger parcels (USPS applies dim weight above 1 cubic foot) **[check]**, 5000 or 6000 (cm/kg) for many international and European carriers.
- **Zones** depend on the distance from origin to destination (US zones 1–8/9); shipping from two locations can cut average zones.
- **Surcharges add up:** fuel (weekly %), residential delivery, delivery area, additional handling/oversize, peak/demand surcharges in Q4 **[check]**. Compare total landed cost per parcel, not base rates.
- **US services change names:** USPS Ground Advantage replaced First-Class Package and Parcel Select Ground in July 2023; check current service names in your shipping software.
- **Negotiated or platform rates** (Shopify Shipping, eBay labels, Pirate Ship, ShipStation) are often below retail; compare with the same parcel profile.
- **International:** duties and taxes (DDP vs DAP), customs documents, EU IOSS for consignments ≤ €150 **[check]**, restricted items (lithium batteries, liquids).
- **Neighbouring skills:** shipping profiles in Shopify `shopify-store-setup`, Etsy shipping profiles `etsy-shipping-strategy`, TikTok Shop shipping rules `tiktok-shop-shipping`, cross-border operations `cross-border-ecommerce`.

## Data Needed

| Data | Where |
|------|-------|
| Orders per month and parcel profile: weight and box dimensions per SKU or order type | Order system, packing station |
| Destination distribution (zones or countries) | Order export by ZIP/country |
| Current carrier, service, invoices with surcharges | Carrier invoices, shipping software |
| Rate tables for candidate carriers/services (and negotiated rates) | Carrier rate guides, shipping software quotes |
| AOV, contribution margin, current shipping charged to customers | Store analytics, finance |
| Delivery time requirements (promise, marketplace badges) | Channel requirements |

## Workflow

1. **Build the parcel profile:** the 3–5 most common box/weight combinations covering 80% of orders, and the zone mix.
2. **Check dimensional weight** for each profile with each carrier's divisor; find boxes that push parcels into a higher billable weight.
3. **Right-size packaging:** choose boxes or mailers that keep volume under the dim-weight threshold (the script prints the largest box volume without dim weight).
4. **Quote each profile** across carriers and services with surcharges, using `shipping_quote.py` with the rate rows from each carrier's current guide for the relevant zone.
5. **Compute the weighted average cost per order** using the zone and profile mix; compare with what customers pay.
6. **Set the customer offer:** free shipping, flat rate, threshold or calculated rates; choose the free-shipping threshold with the formula below and test it.
7. **Negotiate or switch:** use volume and the quotes to negotiate, or use a platform's discounted labels; consider a second fulfilment location if many orders go to far zones.
8. **Review monthly** invoices for surcharges and dim-weight adjustments (carriers re-measure parcels).

## Calculations and Tools

- **Dimensional weight** = L × W × H ÷ divisor; **billable weight** = max(actual, dimensional), rounded up.
- **Largest box without dim weight** = rounded actual weight × divisor (cubic inches or cm³).
- **Weighted shipping cost per order** = Σ (share of orders in profile/zone × cost).
- **Shipping as % of order value** = shipping cost ÷ AOV.
- **Free-shipping threshold (first test):** basket increase needed to pay for the shipping you absorb = average shipping cost ÷ contribution margin %; start the threshold at about current AOV + that increase, then test it (e.g. $9.85 ÷ 55% ≈ $17.90 → threshold ≈ $48 + $18 = $66).
- **Second warehouse value** = orders shifted × (cost from far zones − cost from nearer zones) − extra fixed costs.

```bash
python3 scripts/shipping_quote.py '{"package": {"length": 14, "width": 10, "height": 6, "weight": 2.2, "unit": "in/lb"}, "order_value": 48.0, "carriers": [{"name": "Carrier A Ground", "dim_divisor": 139, "rates": [[1, 8.10], [2, 9.05], [3, 9.85], [5, 11.40], [10, 15.20]]}, {"name": "Carrier B Economy", "dim_divisor": 166, "rates": [[1, 7.60], [2, 8.70], [3, 9.90], [5, 12.30], [10, 16.80]]}]}'
```

The rates in this command are **invented placeholders**: replace them with the rows of each carrier's current guide for your zone.

## Worked Example

*Illustrative example with the placeholder rates above.* A 2.2 lb product in a 14 × 10 × 6 in box (840 in³): dimensional weight is 6.04 lb with a 139 divisor and 5.06 lb with 166, so the parcel is billed at 7 lb and 6 lb instead of 3 lb; shipping costs 31.7% of a $48 order with carrier A.

- The largest box billed at 3 lb is 417 in³ (divisor 139) or 498 in³ (166): a 12 × 8 × 4 in box (384 in³) keeps the parcel at 3 lb → $9.85 instead of $15.20 with carrier A, a saving of $5.35 per order.

## Example Requests

- "I ship 200 orders a month, 1.5 lb average, with USPS Priority. Is there a cheaper option?"
- "Compare UPS, FedEx and a regional carrier for my three box sizes, including dimensional weight and surcharges."
- "What free-shipping threshold should I set with a $48 AOV and 55% contribution margin?"

## Output Format

1. Parcel profile and zone mix.
2. Quote table per profile and carrier: dim weight, billable weight, price with surcharges, % of order value.
3. Packaging recommendations (box sizes that avoid dim weight).
4. Weighted cost per order today vs proposed; annual saving estimate.
5. Customer shipping offer (threshold or rates) and test plan.

## Quality Checks

- Every rate traced to a carrier guide or quote with its date and zone.
- Dim weight computed with each carrier's own divisor.
- Surcharges included; invoices checked for re-measurement adjustments.
- Free-shipping threshold justified by margin, then tested.
- International quotes state DDP/DAP and customs requirements.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** carrier rates and invoices with dates, the seller's parcel and zone data.
- **Estimates:** savings projections, AOV effect of a threshold, future surcharges.
- Carrier rules were reviewed in November 2026; confirm items marked [check] in current rate guides.

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
