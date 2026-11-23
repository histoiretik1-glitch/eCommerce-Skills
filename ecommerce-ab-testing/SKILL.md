---
name: ecommerce-ab-testing
description: "Master A/B testing for e-commerce across all platforms. Test product pages, pricing, ads, emails, and checkout flows with statistical rigor to maximize conversion and revenue. Use when the user asks for help designing or analyzing A/B tests on product pages, prices, ads, emails or checkout, including sample size and significance."
---

# E-Commerce A/B Testing

Master A/B testing for e-commerce across all platforms. Test product pages, pricing, ads, emails, and checkout flows with statistical rigor to maximize conversion and revenue.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** A/B testing method for any channel: hypotheses, sample size, significance, Amazon experiments, ads and email tests.

Part of: A/B testing. For neighbouring jobs, use the matching skill instead:

- `shopify-ab-testing` — Running A/B tests on a Shopify store with Shopify tools and apps.

<!-- role-and-scope:end -->

## Capabilities

- A/B testing methodology for e-commerce
- Platform-specific testing: Amazon Experiments, Shopify, Google Optimize
- Test prioritization frameworks (ICE, PIE, RICE)
- Statistical significance and sample size calculators
- Product page element testing hierarchy
- Price testing methodology and guard rails
- Ad creative A/B testing (Meta, Google, TikTok)
- Email and SMS A/B testing best practices

## Principles and Constraints

Channel-independent experimentation rules, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed in each tool's documentation.

- **Pick the primary metric before the test:** conversion rate, revenue per visitor (RPV), or contribution per visitor. Revenue metrics need larger samples because order values vary.
- **Fixed horizon or sequential, not peeking:** with a classic (fixed-horizon) test, decide the sample size first and read once; checking every day and stopping at the first p < 0.05 inflates false winners. Tools with sequential or Bayesian statistics allow monitoring under their own rules.
- **Several variants = more false positives:** correct the threshold (Bonferroni: alpha ÷ number of comparisons) or limit tests to one challenger.
- **Check the split (SRM)** before reading results; a broken split invalidates the test.
- **Channel tools and their limits [check]:**
  - Amazon **Manage Your Experiments** (Brand Registry): tests title, main image, bullets, description or A+ content on eligible ASINs with enough traffic, typically for 4–10 weeks, with Amazon's own Bayesian read-out.
  - **Google Optimize was shut down in September 2023**; website tests now need a third-party tool or server-side testing.
  - **Meta** and **Google Ads** have built-in experiments that split audiences or campaigns; results are in their attribution model.
  - **Email/SMS** platforms split recipients; use a holdout to measure incremental revenue, not only opens or clicks.
- **Price tests:** every visitor must be charged the price they were shown; keep feeds consistent and avoid unequal prices by protected characteristics; some jurisdictions restrict personalised pricing (disclose where required **[check]**).
- **Scope:** Shopify set-up and Shopify apps are in `shopify-ab-testing`; what to test comes from `conversion-rate-optimization`.

## Data Needed

| Data | Where |
|------|-------|
| Baseline conversion rate and RPV of the tested page, email or ad | Analytics / channel reports, last 4–8 weeks |
| Traffic (sessions, recipients, impressions) per day reaching the test | Same source |
| Order-level revenue (to compute the standard deviation of revenue per visitor) | Order export joined to sessions, or the testing tool |
| Results per variant: visitors, conversions, revenue, revenue standard deviation | Testing tool export |
| Calendar of promotions and releases during the test | Marketing and dev calendars |

## Workflow

1. **Write the hypothesis and primary metric** (conversion, RPV or contribution per visitor) plus guardrail metrics (refund rate, AOV, unsubscribe rate for email).
2. **Size the test:** for conversion use the two-proportion formula; for RPV use the means formula below with your measured standard deviation; convert to days with traffic, minimum two full weeks.
3. **Choose the channel tool** (site testing tool, Amazon Manage Your Experiments, ad platform experiments, email split) and note its statistical method.
4. **QA the variants** on devices and check the tracking of both arms.
5. **Launch and leave it alone:** no changes to the page, prices or traffic sources mid-test; log external events.
6. **At the planned end, check SRM**, then read conversion and RPV results with `revenue_test.py` (Bonferroni for several variants).
7. **Decide:** ship only if the primary metric wins and guardrails hold; "no significant difference" is a result — keep the simpler version.
8. **Record** in the test log and plan a confirmation or follow-up test for big wins (novelty effects fade).

## Calculations and Tools

- **Sample size for a conversion test** (per variant): n = (z₁₋α/₂√(2p̄(1−p̄)) + z₁₋β√(p₁(1−p₁)+p₂(1−p₂)))² ÷ (p₂−p₁)².
- **Sample size for an RPV test** (per variant): n = 2 (z₁₋α/₂ + z₁₋β)² σ² ÷ Δ², where σ = standard deviation of revenue per visitor and Δ = smallest RPV difference worth detecting.
- **Welch test on RPV:** z = (m₂ − m₁) ÷ √(s₁²/n₁ + s₂²/n₂) (normal approximation for large n).
- **Bonferroni:** compare each variant to control at alpha ÷ (k − 1).
- **Holdout uplift (email/SMS):** (revenue per recipient − revenue per holdout member) × recipients.

```bash
python3 scripts/revenue_test.py '{"variants": [{"name": "control", "visitors": 12000, "conversions": 312, "revenue": 18720.0, "revenue_sd": 14.2}, {"name": "B", "visitors": 11950, "conversions": 345, "revenue": 19320.0, "revenue_sd": 13.6}, {"name": "C", "visitors": 12030, "conversions": 360, "revenue": 21240.0, "revenue_sd": 15.1}]}'
```

## Worked Example

*Illustrative example with invented figures.* A product page test with two challengers, about 12,000 visitors each. The command above prints:

- Control: conversion 2.60%, RPV $1.560, AOV $60.
- B: conversion +11.0% (p = 0.174), RPV +3.6% (p = 0.752) → no significant difference.
- C: conversion +15.1% (p = 0.065), RPV +13.2% (p = 0.277) → no significant difference at the Bonferroni threshold 0.025.
- With σ ≈ $14.5, detecting a $0.20 RPV difference at 80% power needs about 2 × (1.96 + 0.84)² × 14.5² ÷ 0.20² ≈ **82,000 visitors per variant**: the test was far too small for a revenue decision. Decide on conversion with a pre-registered single challenger, or run longer.

## Example Requests

- "Create an A/B testing roadmap for my store, Amazon listings and email campaigns for next quarter."
- "How do I use Amazon Manage Your Experiments to test my main image, and how long should it run?"
- "My variant converts 15% better but revenue per visitor is not significant. Should I ship it?"

## Output Format

1. Test plan per channel: hypothesis, primary and guardrail metrics, tool and its statistical method, sample size, duration.
2. QA checklist and change-freeze rules.
3. Results table: conversion, RPV, AOV per variant, p-values with the corrected threshold, confidence interval of the RPV difference, SRM check.
4. Decision and test log entry; follow-up test proposal.

## Quality Checks

- Primary metric and sample size fixed before launch; no early stopping on a peek.
- Multiple comparisons corrected; SRM checked.
- Revenue conclusions use RPV with its own variance, not conversion alone.
- Channel tool limits respected (eligibility, attribution model, minimum duration).
- Price tests charge the displayed price and keep feeds consistent.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** visitors, conversions and revenue per variant from the testing tool or channel for stated dates.
- **Estimates:** standard deviation used for sizing before data exists, expected lift, annualised impact.
- Tool capabilities were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-ab-testing -g
```

## Usage

Ask your AI agent:

- "Create an A/B testing roadmap for my e-commerce store."
- "How do I use Amazon Manage Your Experiments for listing tests?"
- "Calculate the sample size needed for my price test."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
