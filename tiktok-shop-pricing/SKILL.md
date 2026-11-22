---
name: tiktok-shop-pricing
description: "TikTok Shop pricing strategy. Builds a price from unit economics (referral fee, creator commission, shipping, returns, promotions), sets a price ladder for list price, everyday discount and campaign price, and checks price competitiveness against other channels. Use when a TikTok Shop seller asks what price to charge, how much discount or creator commission they can afford, how to price bundles, or why a price change hurt sales."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Pricing

Price TikTok Shop products so they survive creator commissions, platform discounts and campaign pricing, while staying competitive with the same product elsewhere.

## When to Use

- Setting the launch price of a new product
- Deciding how much room there is for creator commission, vouchers or Flash Deals
- Building bundle or multi-buy prices
- Diagnosing a drop in sales after a price change

## Inputs to Collect

Ask for what is missing, then state assumptions explicitly:

| Input | Why it matters |
|-------|----------------|
| Landed product cost per unit | Base of the margin |
| Fulfillment cost (FBT fee or own pick/pack + label) | Often the second-largest cost |
| Referral fee rate for the category | From Seller Center; ~6-8% for most US categories (5% jewelry), changed in 2026, so confirm |
| Creator commission rate and share of orders from creators | Can exceed the referral fee |
| Expected return/refund rate | Impulse categories return more |
| Planned discounts (seller vouchers, Flash Deals, campaign price) | Discounts reduce price before fees |
| Same product's price on Amazon, own site and competitors' shops | Price competitiveness |

## Workflow

1. **Unit economics first.** Run the calculator of the `profit-margin-calculator-tiktok` skill (same plugin, folder `profit-margin-calculator/profit-margin-calculator-tiktok/`):
   ```bash
   python3 profit-margin-calculator/profit-margin-calculator-tiktok/scripts/calculator.py '{"selling_price": 24.99, "product_cost": 6, "fulfillment_fee": 3.5, "affiliate_commission_rate": 0.15, "affiliate_order_share": 0.6, "return_rate": 0.08, "return_processing_fee": 2.5}'
   ```
   (path relative to the plugin root; pass `referral_fee_rate` when the seller knows their rate). Without the tool, compute: price − cost − fulfillment − referral fee − (commission × creator share) − returns − ads.
2. **Floor price.** The break-even price, plus the minimum margin the seller accepts (e.g. 15% net).
3. **Price ladder.** Define three prices and check each against the floor:
   - *List price*: the reference shown before discounts.
   - *Everyday price*: list price minus a permanent product discount.
   - *Campaign price*: the deepest price for Flash Deals or mega campaigns; must stay above the floor after commission.
4. **Competitiveness check.** Compare with the same item on other channels. If TikTok is noticeably more expensive, expect lower conversion and less platform promotion; if much cheaper, check channel conflict and MAP agreements.
5. **Psychology and structure.** Charm pricing ($19.99), anchoring with a visible list price, bundles that raise basket size (2-pack at a lower unit price), and free-shipping thresholds just above the average order value.
6. **Test and review.** Change one lever at a time and compare conversion rate, GMV and margin per order over 7-14 days.

## Rules of Thumb

- Creator commission is calculated on the price the buyer pays; a 20% commission on a discounted price can wipe out the margin of a campaign.
- Keep the campaign price above break-even *with* the highest commission you pay.
- Products under ~$10 rarely carry FBT/shipping costs plus commission: bundle them.

## Output Format

```
TIKTOK SHOP PRICING PLAN — [Product]
Unit economics: cost $X | fulfillment $X | referral X% | commission X% on X% of orders
Break-even price: $X   Minimum acceptable price (X% net): $X

| Price level | Price | Net margin | Max commission it supports |
| List        | $X    | X%         | X%                         |
| Everyday    | $X    | X%         | X%                         |
| Campaign    | $X    | X%         | X%                         |

Competitiveness: [vs Amazon / own site / top 3 shops]
Recommendations: 1. ... 2. ... 3. ...
Test plan: [lever, duration, success metric]
```

## Related Skills

`profit-margin-calculator-tiktok` (calculator), `tiktok-shop-promotions` (discount mechanics), `tiktok-shop-affiliate-program` (commission strategy), `competitive-pricing-strategy`.

## Status

🔶 **Beta** — full workflow added in plugin version 1.1.0. Review figures marked "confirm in Seller Center" before acting.

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
