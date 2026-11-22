---
name: etsy-review-strategy
description: "Etsy review strategy. Increases honest reviews within Etsy's rules (packaging inserts, follow-up messages, delivery experience), responds to negative reviews and uses review themes to fix listings. Use when an Etsy seller asks how to get more reviews, improve their rating or handle a bad review."
metadata:
  nexscope:
    category: etsy
---

# Etsy Review Strategy

Etsy review generation — thank you cards, follow-up messages, photo review incentives.

Earn more honest Etsy reviews, keep the rating high, and use reviews to improve products and listings.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Getting more honest Etsy reviews and handling bad ones.

Part of: Etsy pricing, traffic and operations. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-pricing-strategy` — Setting Etsy prices from costs, Etsy fees and competition.
- `etsy-shipping-strategy` — Etsy shipping profiles, prices, processing times and free shipping.
- `etsy-advertising` — Etsy Ads on Etsy search (budgets, listings, ROAS).
- `etsy-offsite-ads` — Etsy Offsite Ads fees, attribution and the opt-out decision.
- `etsy-social-media-marketing` — Bringing outside traffic to an Etsy shop from Pinterest, Instagram and TikTok.
- `etsy-seasonal-strategy` — Preparing an Etsy shop for holidays and seasonal peaks.
- `etsy-custom-orders` — Personalized and made-to-order items on Etsy.
- `etsy-digital-products` — Selling digital downloads on Etsy.
- `etsy-print-on-demand` — Print-on-demand products on Etsy with a production partner.

<!-- role-and-scope:end -->

## When to Use

- New listings with few reviews
- Rating or share of 5-star reviews falling (affects `etsy-star-seller`)
- A negative review needs an answer

## Policy Boundaries (confirm in Etsy's policies)

Do not offer discounts, gifts or refunds in exchange for reviews or for changing a review, and do not ask only happy buyers. Buyers can usually leave a review for a limited time after delivery (commonly around 100 days); sellers can post a public response.

## Inputs to Collect

Review count and average rating, last 50 reviews, recent negative reviews, delivery and message history for those orders, current packaging insert and follow-up messages.

## Workflow

1. **Delivery first**: on-time shipping, accurate photos and descriptions prevent most bad reviews.
2. **Ask everyone, neutrally**: a thank-you card and, where appropriate, one friendly message after delivery inviting honest feedback and asking the buyer to get in touch if anything is wrong.
3. **Intercept problems**: answer messages fast; offer a fix before the buyer reviews.
4. **Respond to negative reviews** publicly: thank, acknowledge, explain the fix, invite to contact the shop; never argue.
5. **Mine reviews**: group themes (quality, size, color, delivery, packaging) and fix the listing or product; `product-review-analysis` can structure a larger set.
6. **Use positive reviews**: show real buyer photos and quotes accurately in listing images or descriptions.

## Templates

```
Thank-you card: "Thank you for supporting my small shop! If anything isn't right,
message me and I'll make it right. Honest reviews help other buyers find us."

Public response: "Thank you for your feedback. I'm sorry the [issue]. I've
[fix]. Please message me so I can help with your order."
```

## Output Format

1. Review health snapshot and Star Seller impact
2. Main complaint themes and fixes
3. Insert and follow-up message copy
4. Replies to current negative reviews

## Example Requests

- "A buyer left a 2-star review about delivery. How do I answer and avoid it next time?"
- "Help me with etsy review strategy for my Etsy shop"
- "What are the best practices for etsy review strategy?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-review-strategy -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
