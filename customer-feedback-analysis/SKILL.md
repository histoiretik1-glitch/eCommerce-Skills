---
name: customer-feedback-analysis
description: "Voice-of-customer analysis across every feedback source. Merges survey and NPS answers, support tickets, chats, return reasons, social comments and reviews into one theme map scored by frequency, severity and trend, with NPS/CSAT, and an improvement roadmap. Use when a business wants to understand all its customer feedback together or prioritize what to fix from many sources (for product reviews only use `product-review-analysis`)."
nexscope:
  name: "Customer Feedback Analysis"
  category: "Reviews & Reputation"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "reviews"
    - "sentiment-analysis"
    - "customer-feedback"
    - "product-improvement"
  model: "any"
  tokens: "~2000"
  keywords:
    - "customer feedback analysis"
    - "review sentiment analysis"
---

# Customer Feedback Analysis

AI-powered customer feedback and review sentiment analysis skill. Extracts pain points, feature requests, and improvement priorities from customer reviews across e-commerce platforms.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Analysis of all customer feedback channels (reviews, surveys, tickets) into improvement priorities.

Part of: Reviews, feedback and reputation. For neighbouring jobs, use the matching skill instead:

- `product-review-analysis` — Deep analysis of product reviews: pain points, praise, feature requests, sentiment.
- `review-monitoring` — Ongoing review monitoring: alerts on new or negative reviews and the response workflow.
- `online-reputation-management` — Brand-level reputation: monitoring framework, rating recovery and crisis communication.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Survey and NPS/CSAT answers (score + comment) | Survey tool exports |
| Support tickets and chats (category, text, resolution) | Helpdesk exports |
| Return and refund reasons | Platform or returns app reports |
| Reviews (Amazon, Shopify, Etsy, TikTok Shop, Walmart) | Review exports or `product-review-analysis` output |
| Social comments and DMs | Social tools |
| Period, product/SKU, channel and customer segment for each item | Same exports |

## Workflow

1. **Collect and clean**: one table with source, date, product, channel, segment, score and text; remove duplicates and spam; anonymize personal data.
2. **Build a theme codebook**: 10-25 themes (e.g. sizing, shipping delay, damaged item, price, quality, ease of use, customer service), each with a definition and examples.
3. **Code each item** to one or more themes and a sentiment (negative / neutral / positive); check consistency on a sample.
4. **Count** themes by source, product and period; compute NPS and CSAT where scores exist.
5. **Prioritize** with frequency × severity (impact on returns, refunds, ratings or churn) and trend.
6. **Root cause** for the top 5 themes, using ticket details and return data.
7. **Roadmap**: owner, fix, expected effect and the metric that will show it worked; feed back to listings, product, packaging or service.

## Calculations and Tools

- **NPS** = % promoters (9-10) − % detractors (0-6), on answers from the same period.
- **CSAT** = satisfied answers (e.g. 4-5 on a 5-point scale) ÷ all answers.
- **Theme share** = items coded to the theme ÷ all coded items (per source and overall).
- **Priority score** = theme share × severity weight (e.g. 3 = causes returns/refunds, 2 = lowers ratings, 1 = annoyance); weights are a team choice to state.
- **Trend** = theme share this period − previous period; ignore changes on very small samples.

## Example Requests

- "Here are 2,000 support tickets and 500 survey answers from Q3. What should we fix first?"
- "Combine our Amazon reviews, return reasons and NPS comments into one priority list."
- "Build a feedback codebook for our apparel brand and code these comments."

## Output Format

```
VOICE OF CUSTOMER — [period]
Sources: | Source | Items | Period |    NPS: X (n=…)   CSAT: X% (n=…)
| Theme | Share | Trend | Severity | Priority score | Example quote | Root cause | Owner |
Roadmap: top 5 fixes with metric to watch
```

## Quality Checks

- Every number shows its sample size and period; no percentage on fewer than ~30 items without a warning.
- Quotes are real, short and anonymized.
- The codebook is included so the coding can be repeated.
- Feedback from different sources is not double-counted (one customer, one issue).

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: counts and scores computed from the exports.
- **Estimates**: severity weights, expected impact of fixes, sentiment coding (judgment-based; spot-check a sample).

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill customer-feedback-analysis -g
```

## Usage

**Input:**
Product reviews, customer feedback data, brand/ASIN

**Output:**
Sentiment analysis report, pain point extraction, feature request ranking, improvement priority matrix

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up customer feedback analysis for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
