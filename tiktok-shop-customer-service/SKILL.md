---
name: tiktok-shop-customer-service
description: "TikTok Shop customer service operations. Sets response-time targets for buyer messages, builds reply templates and auto-replies, handles order issues, disputes and refund requests, and protects shop performance metrics and ratings. Use when a TikTok Shop seller asks how to answer buyers faster, write message templates, handle complaints or disputes, reduce negative reviews, or improve customer-service metrics."
metadata:
  nexscope:
    category: tiktok-shop
---

# TikTok Shop Customer Service

Answer TikTok Shop buyers quickly and consistently, resolve problems before they become disputes or bad reviews, and keep service metrics healthy.

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

## Limitations

- Strategic guidance from the information the seller shares; no live TikTok Shop API access.
- TikTok Shop policies, fees and thresholds change often and differ by region: confirm current values in Seller Center (Help Center / Academy) before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
