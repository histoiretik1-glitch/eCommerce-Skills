---
name: etsy-custom-orders
description: "Etsy custom and personalized order management. Sets up personalization fields and custom order requests, quote and pricing rules, message templates, proof approval, production times and return rules for made-to-order items. Use when an Etsy seller offers personalized or custom products and asks how to price them, manage requests or avoid disputes."
metadata:
  nexscope:
    category: etsy
---

# Etsy Custom Orders

Custom order management — communication templates, pricing, delivery timelines, return policies.

Sell personalized and made-to-order items on Etsy without endless back-and-forth, underpricing or disputes.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Personalized and made-to-order items on Etsy.

Part of: Etsy pricing, traffic and operations. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-pricing-strategy` — Setting Etsy prices from costs, Etsy fees and competition.
- `etsy-shipping-strategy` — Etsy shipping profiles, prices, processing times and free shipping.
- `etsy-advertising` — Etsy Ads on Etsy search (budgets, listings, ROAS).
- `etsy-offsite-ads` — Etsy Offsite Ads fees, attribution and the opt-out decision.
- `etsy-social-media-marketing` — Bringing outside traffic to an Etsy shop from Pinterest, Instagram and TikTok.
- `etsy-seasonal-strategy` — Preparing an Etsy shop for holidays and seasonal peaks.
- `etsy-review-strategy` — Getting more honest Etsy reviews and handling bad ones.
- `etsy-digital-products` — Selling digital downloads on Etsy.
- `etsy-print-on-demand` — Print-on-demand products on Etsy with a production partner.

<!-- role-and-scope:end -->

## When to Use

- Offering personalization (names, dates, photos, colors) or fully custom pieces
- Too much time spent on messages and proofs
- Disputes about custom work

## Inputs to Collect

Types of customization offered, extra time and material per option, current process (messages, proofs), production time, return policy, common mistakes and disputes.

## Etsy Tools (names may vary; check the listing editor)

- **Personalization field** on the listing, with instructions and a character limit.
- **Variations** with their own prices for options (size, color, material).
- **Custom order requests** through messages, then a private custom listing for the buyer.

## Workflow

1. **Standardize** the most common custom requests into variations and a personalization field; reserve full custom work for a separate, higher-priced process.
2. **Price options**: each option's extra materials and minutes, at the shop's hourly rate (`etsy-pricing-strategy`); add a design fee for fully custom work.
3. **Clear instructions** in the personalization box and description: format, what is possible, what is not, examples (`etsy-product-description`).
4. **Proof process** (if needed): one proof, one revision included, response deadline, then production starts.
5. **Production times**: add custom work time to processing times; show order-by dates for events.
6. **Policy**: personalized items are often not returnable; state it clearly in shop policies (Etsy allows sellers to exclude custom items from returns, but they must still resolve problems such as defects).
7. **Templates** for messages: request received, proof, approval reminder, shipped.

## Output Format

1. Options and pricing table
2. Personalization instructions text
3. Proof and approval workflow with message templates
4. Policy wording for custom items

## Example Requests

- "I get too many custom requests by message. How do I set up personalization properly?"
- "Help me with etsy custom orders for my Etsy shop"
- "What are the best practices for etsy custom orders?"

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-custom-orders -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
