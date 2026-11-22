---
name: tiktok-shop-shipping
description: "TikTok Shop shipping setup and optimization. Configures shipping templates, carrier choice (TikTok-provided labels vs own carrier), delivery promises, free-shipping thresholds and package dimensions, and reduces shipping cost and late deliveries. Use when a TikTok Shop seller asks how to set shipping fees or templates, offer free shipping profitably, choose carriers, avoid shipping fee adjustments, or fix late or lost deliveries."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Shipping

Set TikTok Shop shipping so buyers see a fast, cheap delivery promise and the shop still makes money on every order.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Shipping templates, carriers, shipping prices and delivery promise.

Part of: TikTok Shop operations. For neighbouring jobs, use the matching skill instead:

- `tiktok-shop-fulfillment` — Choosing and running the fulfillment model (FBT, self, 3PL) and dispatch performance.
- `tiktok-shop-inventory` — Stock planning for viral demand on TikTok Shop.
- `tiktok-shop-returns` — TikTok Shop returns and refunds.
- `tiktok-shop-customer-service` — Buyer messages, disputes and service metrics on TikTok Shop.
- `tiktok-shop-reviews` — Ratings and reviews on TikTok Shop.

<!-- role-and-scope:end -->

## When to Use

- First shipping setup or new warehouse
- Deciding on free shipping or a free-shipping threshold
- Shipping costs or weight adjustments are eating margin
- Late, lost or untracked deliveries

For choosing between FBT and self-fulfillment, see `tiktok-shop-fulfillment`.

## Inputs to Collect

Product weights and packed dimensions, average order value and items per order, ship-from locations, current carriers and costs, delivery-time data, share of orders with shipping complaints.

## Workflow

1. **Packaging and dimensions.** Record accurate packed weight and size per SKU; billed weight is often the larger of actual and dimensional weight. Wrong data leads to shipping fee adjustments.
2. **Carrier option.** Compare TikTok-provided shipping labels (platform rates, integrated tracking) with your own carrier contract on cost, pickup, scan reliability and delivery time.
3. **Shipping templates.** Define regions, handling time and buyer-paid fees; keep handling time to what you can always meet.
4. **Free shipping decision.**
   - Cost per order of free shipping = average label cost (minus any platform shipping subsidy).
   - Profitable if the expected conversion lift × margin per order exceeds that cost.
   - Threshold: set it slightly above the current average order value to push bundles.
5. **Delivery promise.** Ship within the handling time, upload valid tracking immediately, and pick carriers whose first scan happens the same day.
6. **Monitor.** Late deliveries and lost parcels by carrier and region; renegotiate or switch carriers with poor results.

## Output Format

1. Shipping cost per order by product and carrier
2. Recommended template (regions, handling time, fees)
3. Free-shipping recommendation with break-even math
4. Packaging and dimension fixes
5. Delivery KPIs and review cadence

## Related Skills

`tiktok-shop-fulfillment`, `tiktok-shop-pricing`, `ecommerce-shipping-rates`.

## Status

🔶 **Beta** — full workflow added in plugin version 1.1.0. Review figures marked "confirm in Seller Center" before acting.

## Example Requests

- "Should I offer free shipping on my $15 TikTok Shop products?"
- "Set up TikTok Shop shipping templates for two warehouses."
- "We keep getting shipping fee adjustments on TikTok Shop. What's wrong?"

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-shipping -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
