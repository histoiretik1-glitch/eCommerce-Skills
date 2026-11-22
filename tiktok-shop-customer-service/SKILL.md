---
name: tiktok-shop-customer-service
description: "TikTok Shop customer service operations. Sets response-time targets for buyer messages, builds reply templates and auto-replies, handles order issues, disputes and refund requests, and protects shop performance metrics and ratings. Use when a TikTok Shop seller asks how to answer buyers faster, write message templates, handle complaints or disputes, reduce negative reviews, or improve customer-service metrics."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Customer Service

Answer TikTok Shop buyers quickly and consistently, resolve problems before they become disputes or bad reviews, and keep service metrics healthy.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Buyer messages, disputes and service metrics on TikTok Shop.

Part of: TikTok Shop operations. For neighbouring jobs, use the matching skill instead:

- `tiktok-shop-fulfillment` — Choosing and running the fulfillment model (FBT, self, 3PL) and dispatch performance.
- `tiktok-shop-shipping` — Shipping templates, carriers, shipping prices and delivery promise.
- `tiktok-shop-inventory` — Stock planning for viral demand on TikTok Shop.
- `tiktok-shop-returns` — TikTok Shop returns and refunds.
- `tiktok-shop-reviews` — Ratings and reviews on TikTok Shop.

<!-- role-and-scope:end -->

## When to Use

- Message response time or response rate is below target
- Rising disputes, refund requests or negative reviews
- Setting up templates, auto-replies or a support rota
- Preparing for a sales peak

## Inputs to Collect

Current metrics from Seller Center (response rate, response time, dispute or refund rates, ratings), the most common buyer questions and complaints, team size and hours, return/refund policy.

## Service Standards

- Respond within the response-time target shown in Seller Center (commonly 12-24 hours; confirm the current value for the region). Peak periods need extra cover.
- Keep conversations inside TikTok Shop messaging; never ask buyers to move to another channel or to change a review.
- Log every issue with an order ID and a category so the root cause can be fixed.

## Workflow

1. **Classify the top 10 buyer contacts** (where is my order, size/compatibility, damaged item, wrong item, return, discount not applied, product question).
2. **Write templates** for each: acknowledge, give the answer or next step, set a time frame. Keep them short and personal (use the buyer's name and order details).
3. **Auto-replies and FAQ** for pre-sale questions (shipping time, sizes, materials) so buyers get an instant answer.
4. **Resolution rules**: what agents can approve alone (replacement, partial refund up to $X) and what needs escalation.
5. **Disputes**: answer within the deadline, attach evidence (tracking, photos, messages), propose a fair solution early.
6. **Feedback loop**: weekly list of top complaints → listing fixes, packaging changes, supplier issues.

## Template Example

```
Hi [Name], thanks for your message about order [ID]. I'm sorry the [item] arrived [issue].
We can [send a replacement / refund $X] right away — which do you prefer?
You'll get an update from us within [X hours].
```

## Output Format

1. Service-level targets and current gaps
2. Contact categories with templates (and auto-replies)
3. Resolution and escalation rules
4. Dispute handling checklist
5. Weekly KPI tracker (response time, response rate, disputes, refunds, rating)

## Related Skills

`tiktok-shop-returns`, `tiktok-shop-reviews`, `tiktok-shop-fulfillment`.

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
npx skills add histoiretik1-glitch/eCommerce-Skills --skill tiktok-shop-customer-service -g
```

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
