---
name: online-reputation-management
description: "Online reputation management for e-commerce brands. Audits ratings and reviews across marketplaces, Google, Trustpilot and social media, computes how many positive reviews a rating recovery needs, sets monitoring and response rules and prepares templates and a crisis playbook within platform rules on fake reviews. Use whenever a brand's rating dropped, it asks how many good reviews it needs, or negative reviews or posts pile up."
nexscope:
  name: "Online Reputation Management"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "reputation"
    - "brand-monitoring"
    - "crisis-management"
    - "review-management"
  model: "any"
  tokens: "~2000"
  keywords:
    - "online reputation management"
---

# Online Reputation Management

AI-powered online reputation management skill for e-commerce brands. Builds reputation monitoring frameworks, negative review response strategies, rating recovery plans, and crisis communication templates.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Brand-level reputation: monitoring framework, rating recovery and crisis communication.

Part of: Reviews, feedback and reputation. For neighbouring jobs, use the matching skill instead:

- `product-review-analysis` — Deep analysis of product reviews: pain points, praise, feature requests, sentiment.
- `customer-feedback-analysis` — Analysis of all customer feedback channels (reviews, surveys, tickets) into improvement priorities.
- `review-monitoring` — Ongoing review monitoring: alerts on new or negative reviews and the response workflow.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Ratings and review counts per platform (Amazon, Walmart, Etsy, TikTok Shop, Shopify reviews app, Google, Trustpilot) | Platform dashboards |
| Recent negative reviews and posts | Platforms, `review-monitoring`, `social-media-monitor` |
| Mentions and sentiment trends | `brand-monitoring` |
| Root causes behind complaints | `customer-feedback-analysis`, support data |
| Spokesperson, approval chain, legal contact | Team |

## Workflow

1. **Audit**: rating, count and trend per platform; top complaint themes; search results for the brand name (first page).
2. **Monitoring**: alerts for new negative reviews and spikes in mentions (`review-monitoring`, `brand-monitoring`).
3. **Response rules**: who answers, within what time, tone, what to offer, when to take the conversation private; reply to negative reviews factually, never argue.
4. **Fix the cause**: link each recurring complaint to an owner (product, shipping, service); responses without fixes do not recover ratings.
5. **Recovery plan**: compute the reviews needed (below); increase honest review volume through allowed requests to all customers (no incentives for positive reviews, no review gating, no fake reviews; these breach platform rules and consumer-protection rules such as the FTC rule on fake reviews in the US).
6. **Crisis playbook**: severity levels, first statement within an agreed time, holding statements, approval chain, channels, follow-up.
7. **Report** monthly: rating trends, response time, theme changes.

## Calculations and Tools

- **Rating recovery**: with N reviews at average A, the number n of new 5-star reviews needed to reach target T is n = N × (T − A) ÷ (5 − T).
  Example: 400 reviews at 3.9 → 4.3 needs 400 × 0.4 ÷ 0.7 ≈ 229 five-star reviews (more if new reviews are not all 5 stars: replace 5 by the expected average of new reviews).
- **Response rate** = negative reviews answered ÷ negative reviews; **response time** = median hours to first reply.
- **Negative share** = 1-2 star reviews ÷ all reviews in the period.

## Example Requests

- "Our Amazon rating fell from 4.4 to 3.9 in two months. Build a recovery plan."
- "A viral TikTok video says our product is unsafe. What do we say in the next 24 hours?"
- "Write response templates for negative reviews about late delivery and damaged items."

## Output Format

```
REPUTATION REPORT — [Brand, period]
| Platform | Rating | Reviews | Trend | Negative share | Top complaint |
Recovery math: current → target, reviews needed, timeline at current review rate
Response rules and templates; crisis playbook (levels, statements, approvals)
```

## Quality Checks

- No tactic involves fake, incentivized-for-positive or selectively requested reviews, or removing legitimate reviews.
- Templates are factual, apologize where appropriate and never disclose customer data.
- Recovery timelines use the brand's actual review rate.
- Crisis statements avoid admissions or claims not approved by legal.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: ratings, counts and reviews from the platforms on the stated date.
- **Estimates**: future review rate, timeline to target, impact on sales. Legal points are to confirm with counsel.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill online-reputation-management -g
```

## Usage

**Input:**
Brand name, product name, or store URL

**Output:**
Reputation monitoring plan, negative review response templates, rating recovery roadmap, crisis response playbook

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up online reputation management for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
