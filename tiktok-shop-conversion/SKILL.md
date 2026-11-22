---
name: tiktok-shop-conversion
description: "TikTok Shop conversion rate optimization. Diagnoses the funnel from video or LIVE view to product click, product page view, add to cart and paid order, then fixes hooks, product detail pages, price display, reviews, vouchers and checkout friction. Use when a TikTok Shop seller has views but few sales, a low click-through or conversion rate, high add-to-cart abandonment, or wants to improve GPM."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Conversion

Turn TikTok Shop traffic into orders by finding where buyers drop off between the video and the payment.

## When to Use

- Many views or clicks but few orders
- Conversion rate falling after a price, image or content change
- Comparing products or creators with very different conversion rates

## Inputs to Collect

From Seller Center analytics (last 7-30 days, per product and per traffic source: videos, LIVE, product card, search, shop tab): impressions, views, product clicks, product page views, add-to-carts, orders, GMV, GPM. Plus the product page (title, images, video, price, reviews) and 2-3 competitor products.

## Funnel Diagnosis

| Stage | Metric | If weak, look at |
|-------|--------|------------------|
| Content → product click | Click-through rate on the product link/anchor | Hook in the first 2 seconds, product shown early, clear call to action, pinned product in LIVE |
| Product page → add to cart | Page-to-cart rate | Main image, video on the page, price and visible discount, reviews and rating, variants, shipping time |
| Cart → paid order | Checkout completion | Unexpected shipping cost, payment options, delivery estimate, voucher not applied |
| Overall | Conversion rate, GPM | Mismatch between what the video promises and the page shows |

Compare each stage with the seller's own best product and with category benchmarks shown in Seller Center, rather than fixed industry numbers.

## Workflow

1. Locate the weakest stage, split by traffic source (a product can convert well from LIVE and badly from videos).
2. List 3-5 hypotheses for that stage (e.g. "the main image does not show the product in use").
3. Prioritize by impact and effort; fix the cheapest high-impact item first.
4. Change one element at a time and compare 7 days before/after with similar traffic.

## Product Page Checklist

- Main image: product clearly visible, readable on a phone, no clutter
- 5+ images: in use, scale, details, packaging, benefits
- Short product video on the page
- Title: what it is + key benefit + key attribute (see `tiktok-shop-listing-optimization`)
- Price: visible discount from a credible reference price; bundles shown
- Reviews: enough ratings and photo reviews (see `tiktok-shop-reviews`)
- Delivery: realistic shipping time; free-shipping threshold if relevant

## Output Format

1. Funnel table with the weak stage highlighted
2. Hypotheses ranked by impact × effort
3. Exact changes to make (copy, image brief, price display, voucher)
4. Test plan and success metric

## Related Skills

`tiktok-shop-listing-optimization`, `tiktok-shop-content-strategy`, `tiktok-live-selling`, `tiktok-shop-reviews`, `tiktok-shop-analytics`.

## Status

🔶 **Beta** — full workflow added in plugin version 1.1.0. Review figures marked "confirm in Seller Center" before acting.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-conversion -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
