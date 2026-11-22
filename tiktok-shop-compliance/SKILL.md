---
name: tiktok-shop-compliance
description: "TikTok Shop policy and compliance check. Reviews products against prohibited and restricted product rules and category approval requirements, listings and videos against content and claim rules, and IP risks, then explains the violation and appeal process. Use when a TikTok Shop seller asks whether they can sell a product, why a listing or video was removed, how to handle a violation or penalty points, or how to avoid account suspension."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Compliance

Keep a TikTok Shop account, its listings and its creator content within platform policy, and handle violations when they happen.

## When to Use

- Before listing a new product or entering a new category
- After a listing, video or LIVE is removed or restricted
- When the shop receives a violation, penalty points or a warning
- Before briefing creators on claims they may make

## Inputs to Collect

Product type and ingredients/materials, target region, the exact listing text and images, the video or LIVE script, the violation notice wording (if any), the seller's documents (certificates, test reports, trademark or authorization letters).

## Compliance Checklist

**1. Product eligibility**
- Is the product prohibited in the region (weapons, drugs, many supplements or medical devices, counterfeit goods, etc.)?
- Is it restricted, requiring category approval or documents (e.g. beauty, health, food, children's products, electronics)?
- Are certificates or test reports needed for the region (safety marks, lab tests)?

**2. Listing accuracy**
- Title, images and attributes match the real product; no misleading claims, fake discounts or exaggerated results.
- No brand names or trademarks the seller is not authorized to use.

**3. Content and claims (videos, LIVE, creator content)**
- No medical, cure, guaranteed weight-loss or before/after claims that the policy prohibits.
- Required disclosures for paid or gifted creator content.
- No redirecting buyers off TikTok Shop.

**4. Intellectual property**
- Trademark, copyright (music, images) and design rights; authorization from the brand owner for branded goods.

**5. Operations**
- Shipping and customer-service performance thresholds, because poor performance also triggers penalties (see `tiktok-shop-fulfillment` and `tiktok-shop-customer-service`).

## Handling a Violation

1. Read the notice: policy name, affected listing or content, penalty (removal, points, restriction).
2. Identify the root cause; fix every similar listing, not only the flagged one.
3. Appeal only with evidence (documents, invoices, authorization letters) and a short factual explanation.
4. Track the shop's violation points or account health status in Seller Center and the date points expire.

## Output Format

```
COMPLIANCE REVIEW — [Product / Listing]
Eligibility: Allowed / Restricted (needs: ...) / Prohibited
Listing issues: [issue → fix]
Content and claim issues: [claim → allowed rewrite]
IP risk: [low / medium / high + why]
Documents to prepare: [...]
If already penalized: appeal plan + evidence list
```

Always tell the seller to confirm the current policy page in Seller Center, as rules differ by region and change frequently.

## Related Skills

`brand-protection-tiktok` (IP enforcement against others), `tiktok-shop-listing-optimization`, `tiktok-shop-content-strategy`.

## Status

🔶 **Beta** — full workflow added in plugin version 1.1.0. Review figures marked "confirm in Seller Center" before acting.

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
