---
name: tiktok-shop-product-research
description: "TikTok Shop product research and validation. Scores product ideas on demonstrability in short video, creator appeal, price point, margin after referral fee and creator commission, competition, compliance risk and supply, then gives a go/no-go and a test plan. Use when a seller asks what to sell on TikTok Shop, wants to validate a product idea, compare candidate products, or check whether a product can be profitable with creators."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Product Research

Decide which products are worth launching on TikTok Shop before money goes into stock and samples.

## When to Use

- Choosing a first or next product to sell on TikTok Shop
- Comparing several candidate products
- Validating a supplier product found elsewhere

For spotting what is trending right now, use `tiktok-shop-trending-products`.

## Inputs to Collect

Candidate products (with links if possible), landed cost and supplier lead time, target price, category, evidence of demand (videos, competing shops, search interest), the seller's content and creator capacity.

## Scoring Model (score each 1-5)

| Criterion | 5 = strong | 1 = weak |
|-----------|-----------|----------|
| Demonstrability | Result visible in 3-5 seconds of video | Benefit invisible or slow |
| Creator appeal | Easy for many creators to make content | Needs expertise or special setup |
| Price point | Impulse range for the audience (often ~$10-50) | High-consideration price |
| Unit margin | Healthy net margin after referral fee, ~15-20% creator commission, shipping, returns | Margin disappears with commission |
| Competition | Few shops, room to differentiate | Saturated with identical listings |
| Compliance risk | Clearly allowed | Restricted, needs approval, or claim-heavy |
| Supply | Reliable supplier, short lead time, low MOQ | Long lead time, quality risk |
| Repeat / bundle potential | Consumable or add-on items | One-off purchase |

Weight demonstrability and unit margin double; a product scoring under 3 on compliance is a no-go regardless of the total.

## Workflow

1. Gather evidence for each criterion (videos and their engagement, competitor shops and prices, reviews and complaints).
2. Compute unit economics with `profit-margin-calculator-tiktok` at the target price and at a campaign price.
3. Score, rank and explain the top 3.
4. **Test plan** for the winner: small first order, 5-10 creator samples, 2-3 owned videos, success thresholds (e.g. CTR, conversion, cost per order) and a decision date.

## Output Format

```
PRODUCT RESEARCH — [Shortlist]
| Product | Demo | Creator | Price | Margin | Competition | Compliance | Supply | Repeat | Weighted score |
Top pick: [...] — why
Unit economics at $X: net margin X% (commission X%)
Risks: [...]
Test plan: [first order, samples, videos, thresholds, decision date]
```

## Related Skills

`tiktok-shop-trending-products`, `profit-margin-calculator-tiktok`, `tiktok-shop-compliance`, `dropshipping-product-research`, `market-gap-analysis`.

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-product-research -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
