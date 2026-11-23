---
name: review-monitoring
description: "Set up systematic review monitoring across e-commerce platforms. Track new reviews, detect negative review spikes, monitor competitor reviews, and automate review response workflows. Use when a seller wants alerts on new or negative reviews, to track competitor reviews, or a process to respond to reviews."
metadata:
  nexscope:
    emoji: "👁️"
    category: ecommerce
---

# Review Monitoring 👁️

Set up systematic review monitoring across e-commerce platforms. Track new reviews, detect negative review spikes, monitor competitor reviews, and automate review response workflows.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Ongoing review monitoring: alerts on new or negative reviews and the response workflow.

Part of: Reviews, feedback and reputation. For neighbouring jobs, use the matching skill instead:

- `product-review-analysis` — Deep analysis of product reviews: pain points, praise, feature requests, sentiment.
- `customer-feedback-analysis` — Analysis of all customer feedback channels (reviews, surveys, tickets) into improvement priorities.
- `online-reputation-management` — Brand-level reputation: monitoring framework, rating recovery and crisis communication.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill review-monitoring -g
```

## Usage

```
Set up a review monitoring system for my products. I sell on Amazon (3 ASINs) and Etsy (15 listings). I want to catch negative reviews within 24 hours.
```

## Capabilities

- Multi-platform review monitoring setup (Amazon, Etsy, Walmart, Shopify)
- Negative review alert framework and response templates
- Review velocity tracking and anomaly detection
- Competitor review monitoring strategy
- Review response best practices by platform
- Review solicitation compliance guide (per platform rules)

## Principles and Constraints

Review monitoring and response rules across channels, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed with each channel.

- **Never suppress, filter or buy reviews:** the FTC rule on consumer reviews (in force since October 2024) bans review suppression, fake reviews and conditional incentives; marketplaces have similar bans.
- **Channel response options differ [check]:** Amazon does not let sellers reply publicly to product reviews or contact reviewers outside Buyer-Seller Messaging rules (brand owners can see reviews in brand tools and contact for some negative reviews where Amazon offers it); Etsy lets the seller reply once publicly to a review; Walmart, Shopify review apps, Google Business Profile and Trustpilot allow public replies.
- **Report, don't argue:** report reviews that break the channel's guidelines (wrong product, abusive, seller feedback in product review) through the official form; reply factually to genuine criticism.
- **Speed matters for issues, not for vanity:** a defect, safety or allergy mention needs action within 24 hours; star averages move slowly.
- **Privacy:** replies must not reveal order details or personal data.
- **Scope:** this skill is the alerting and response system. Deep analysis of review themes is `product-review-analysis`; combining reviews with surveys and tickets `customer-feedback-analysis`; brand-level crisis handling `online-reputation-management`.

## Data Needed

| Data | Where |
|------|-------|
| Products/listings to monitor per channel with IDs | Catalogue |
| Review feeds or exports: date, rating, text, verified purchase | Channel review pages/reports, review apps, monitoring tools |
| Historical weekly review counts and average rating per product | Same sources, 12+ weeks |
| Order volume per product per week | Sales reports |
| Response templates and escalation owners | Customer service |

## Workflow

1. **Inventory sources** per channel and the access method (native notifications, brand tools, review app webhooks, third-party monitor).
2. **Set the cadence:** near real-time for 1–2-star reviews and alert keywords; daily digest for all; weekly trend report.
3. **Define alert rules:** rating ≤ 2, safety/defect keywords ("burn", "broke", "allergic", "leak", "fake"), rolling rating drop, velocity anomaly.
4. **Route alerts** to owners with an SLA: safety/defect → product/quality within 24 h; delivery/service → customer service within 24 h; general criticism → reply within 48 h where replies are allowed.
5. **Respond** with channel-appropriate templates: acknowledge, fact, fix, path to help (no order details, no requests to change the review).
6. **Report policy-violating reviews** through official channels and log the outcome.
7. **Track trends weekly:** rolling average, review velocity per 100 orders, negative share, top themes; hand recurring themes to `product-review-analysis`.
8. **Close the loop:** record the fix (listing change, supplier action) and watch the theme frequency afterwards.

## Calculations and Tools

- **Rolling average rating (last 30 or 90 days)** = mean of ratings in the window (more sensitive than the lifetime average).
- **Review rate** = reviews ÷ orders × 100 for the same weeks (lag of 1–3 weeks after delivery).
- **Negative share** = 1–2-star reviews ÷ reviews in the window.
- **Velocity anomaly** (z-score) = (this week's count − mean of the previous 8 weeks) ÷ standard deviation; |z| > 3 flags a spike or a drop (possible review attack, listing merge or a fault).
- **Response SLA compliance** = alerts handled within SLA ÷ alerts.

## Worked Example

*Illustrative example with invented figures.* 3 Amazon ASINs and 15 Etsy listings. ASIN B's previous 8 weeks had 6, 5, 7, 6, 4, 6, 5, 7 reviews (mean 5.75, standard deviation ≈ 1.04).

- This week: 14 reviews, 9 of them 1-star mentioning "leaks" → z = (14 − 5.75) ÷ 1.04 ≈ **8.0**: alert.
- Rolling 30-day rating falls from 4.5 to 3.9; negative share 64% this week vs 8% before.
- Actions within 24 h: quality check of the current batch (lid seal), pause ads on ASIN B, add a "how to close the lid" image, reply on Etsy listings that mention it; on Amazon use only the options Amazon provides.

## Example Requests

- "Set up review monitoring for 3 Amazon ASINs and 15 Etsy listings so I catch negative reviews within 24 hours."
- "Write response templates for negative reviews on Etsy, Walmart and our Shopify review app."
- "We suddenly received 10 one-star reviews in two days. Is it an attack or a product problem, and what can we do?"

## Output Format

1. Source inventory and access method per channel.
2. Alert rules, keyword list, routing and SLAs.
3. Response templates per channel and situation.
4. Weekly trend report template (rolling rating, review rate, negative share, z-score, themes).
5. Incident log template (alert, cause, action, outcome).

## Quality Checks

- No tactic that filters, suppresses or incentivises reviews.
- Replies follow each channel's rules and contain no personal or order data.
- Alerts tested on past data (would they have fired on known incidents?).
- Rates computed per orders to separate volume effects from quality effects.
- Every safety/defect alert has an owner and a closing note.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** review data exported or observed with dates, order volumes.
- **Estimates:** causes of a spike before investigation, sentiment from automated tools, benchmark review rates.
- Channel rules were reviewed in November 2026; confirm items marked [check].

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
