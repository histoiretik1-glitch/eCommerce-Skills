---
name: etsy-shipping-strategy
description: "Etsy shipping strategy. Sets up shipping profiles, processing times, free shipping or built-in shipping costs, international shipping and tracking for an Etsy shop. Use when an Etsy seller asks how to charge for shipping, whether to offer free shipping, or how to reduce shipping problems."
metadata:
  nexscope:
    category: etsy
---

# Etsy Shipping Strategy

Shipping strategy — free shipping vs markup, shipping profiles, international shipping, tracking.

Set Etsy shipping so buyers see fair, fast delivery and the shop does not lose money on postage.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Etsy shipping profiles, prices, processing times and free shipping.

Part of: Etsy pricing, traffic and operations, Shipping and returns. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-pricing-strategy` — Setting Etsy prices from costs, Etsy fees and competition.
- `etsy-advertising` — Etsy Ads on Etsy search (budgets, listings, ROAS).
- `etsy-offsite-ads` — Etsy Offsite Ads fees, attribution and the opt-out decision.
- `etsy-social-media-marketing` — Bringing outside traffic to an Etsy shop from Pinterest, Instagram and TikTok.
- `etsy-seasonal-strategy` — Preparing an Etsy shop for holidays and seasonal peaks.
- `etsy-review-strategy` — Getting more honest Etsy reviews and handling bad ones.
- `etsy-custom-orders` — Personalized and made-to-order items on Etsy.
- `etsy-digital-products` — Selling digital downloads on Etsy.
- `etsy-print-on-demand` — Print-on-demand products on Etsy with a production partner.
- `ecommerce-shipping-rates` — Parcel costs on any carrier: dimensional weight, zones, surcharges, free-shipping threshold.
- `ecommerce-returns-management` — Returns on any channel: cost per return, reasons, policy, grading and fraud controls.
- `tiktok-shop-returns` — TikTok Shop returns and refunds.
- `tiktok-shop-shipping` — Shipping templates, carriers, shipping prices and delivery promise.

<!-- role-and-scope:end -->

## When to Use

- Setting up shipping profiles for a new shop or product
- Deciding on free shipping
- Late deliveries, lost parcels or shipping complaints

## Inputs to Collect

Packed weight and size per product, ship-from location, carriers used, average order value and items per order, share of international orders, current processing times.

## Etsy Specifics (confirm in the Seller Handbook)

- **Shipping profiles** apply the same rules to many listings; create one per size/weight class.
- **Processing time** is part of the delivery estimate buyers see: set what the shop can always meet.
- Etsy has given **search priority to US listings with free shipping on orders of $35 or more**; check whether this still applies to the shop's market.
- **Etsy shipping labels** can be cheaper than retail postage and add tracking automatically (helps `etsy-star-seller`).

## Workflow

1. Weigh and measure each packed product; group into shipping profiles.
2. Compare label costs (Etsy labels vs. carrier accounts) for the main destinations.
3. Choose a pricing model:
   - **Charge actual shipping**: transparent, lower item price.
   - **Free shipping, cost in the item price**: better conversion and search; raise the item price by the average label cost.
   - **Free over a threshold** (e.g. $35): encourages multi-item orders.
4. International: decide countries, customs information, longer processing estimates.
5. Set processing times per profile and upgrades (express) if worthwhile.
6. Monitor late deliveries and complaints; adjust carriers or processing times.

## Output Format

1. Shipping profiles table (profile, products, weight range, domestic and international price, processing time)
2. Free-shipping recommendation with the price change it requires
3. Carrier and label recommendation
4. Packaging checklist

## Example Requests

- "Should I offer free shipping on Etsy for my $28 prints?"
- "Help me with etsy shipping strategy for my Etsy shop"
- "What are the best practices for etsy shipping strategy?"

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-shipping-strategy -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
