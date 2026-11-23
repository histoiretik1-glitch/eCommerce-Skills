---
name: conversion-rate-optimization
description: "Systematic CRO for e-commerce stores. Audit conversion funnels, identify drop-off points, implement fixes, and run experiments to increase revenue per visitor across all platforms. Use when the user asks for help diagnosing a low conversion rate, auditing a funnel, finding drop-off points or building a CRO testing roadmap."
---

# Conversion Rate Optimization

Systematic CRO for e-commerce stores. Audit conversion funnels, identify drop-off points, implement fixes, and run experiments to increase revenue per visitor across all platforms.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Platform-independent CRO: funnel analysis, heuristics and testing roadmap.

Part of: Conversion and landing pages. For neighbouring jobs, use the matching skill instead:

- `shopify-conversion-optimization` — CRO on a Shopify store: theme, apps, product pages, Shopify checkout.
- `ecommerce-landing-page` — Auditing an existing landing or product page for conversion.
- `shopify-landing-page-builder` — Building a new campaign or seasonal landing page on Shopify.

<!-- role-and-scope:end -->

## Capabilities

- Conversion funnel mapping and analysis
- Heuristic evaluation frameworks (LIFT, ResearchXL)
- User behavior analysis: heatmaps, session recordings, surveys
- Product page CRO checklist (images, copy, social proof, CTA)
- Cart and checkout optimization
- Mobile conversion optimization
- Page speed impact on conversions
- CRO testing roadmap and prioritization

## Principles and Constraints

Platform-independent CRO standards, as known at the last review of this skill (November 2026).

- **Optimise revenue per visitor, not conversion rate alone:** a discount can raise conversion and lower profit. Track RPV and contribution per session.
- **Research before ideas:** use a structured process such as ResearchXL (heuristic review, technical checks, analytics, mouse tracking, surveys, user testing) and a heuristic model such as LIFT (value proposition, relevance, clarity, anxiety, distraction, urgency).
- **Measure with a consistent event model:** in GA4 the recommended e-commerce events are `view_item`, `add_to_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info`, `purchase`; the same funnel must be used before and after a change. Consent banners reduce tracked sessions, so compare like periods.
- **Test only where traffic allows it:** pages with too few conversions cannot reach significance in a reasonable time; ship research-backed fixes there and monitor.
- **No dark patterns:** fake timers, fake stock, pre-ticked add-ons and hidden fees are deceptive practices (FTC in the US, UCPD in the EU) and erode trust.
- **Accessibility counts:** WCAG 2.2 AA issues (contrast, focus, labels) block some customers from buying; the European Accessibility Act applies to many e-commerce sites from June 2025.
- **Scope:** this skill is the platform-independent method (WooCommerce, BigCommerce, Magento, custom sites, multichannel). Shopify-specific changes are in `shopify-conversion-optimization`; landing page audits in `ecommerce-landing-page`; test statistics in `ecommerce-ab-testing`.

## Data Needed

| Data | Where |
|------|-------|
| Funnel by step, device, traffic source and new/returning (8 weeks) | GA4 funnel exploration or the platform's analytics |
| Revenue, orders, AOV, sessions | Analytics + order system |
| Page-level data for top templates (home, category, product, cart, checkout) | Analytics landing page / page path reports |
| Speed and Core Web Vitals (field data) | Search Console, CrUX / PageSpeed Insights |
| Qualitative data: surveys, chat logs, support tickets, reviews, session recordings | Survey/recording tools, help desk |
| Previous tests and changes log | Team records |

## Workflow

1. **Check tracking first:** compare analytics orders with the order system for the same period (gap above 5–10% means tracking must be fixed before analysis).
2. **Map the funnel** by device and source and compute step rates and RPV; locate the step and segment with the largest revenue loss (formula below).
3. **Run a heuristic review** of the templates on that step (LIFT model), on a real phone, as a new visitor.
4. **Collect qualitative evidence:** exit or post-purchase survey ("What almost stopped you?"), session recordings of drop-offs, support questions, negative reviews.
5. **Check technical issues:** errors in the browser console, broken forms, slow templates, payment method failures, browser/device-specific drop-offs.
6. **Write hypotheses** (evidence → change → expected metric) and prioritise them with PXL or ICE.
7. **Decide test vs ship:** test where traffic supports the sample size; ship clear bug fixes and research-backed low-risk changes with before/after monitoring.
8. **Keep a CRO log** (hypothesis, evidence, change, result) and re-run the funnel every month.

## Calculations and Tools

- **Step rate** = sessions reaching step n+1 ÷ sessions reaching step n.
- **RPV** = revenue ÷ sessions = conversion rate × AOV.
- **Revenue at stake for a step** = sessions at the step × (best comparable segment's step rate − current step rate) × downstream rates × AOV (comparable segment = e.g. desktop vs mobile, or last year's same period).
- **Testable?** weekly conversions per variant needed: use the sample-size formula in `ecommerce-ab-testing`; if the test would exceed 8 weeks, do not test that change on that page.
- **PXL score**: binary questions (above the fold? noticeable within 5 seconds? backed by user testing / analytics / surveys? easy to implement?) summed.

## Worked Example

*Illustrative example with invented figures, WooCommerce store.* 60,000 sessions/month, AOV $85. Mobile (70% of sessions): product → cart 5.2%, cart → checkout 38%, checkout → purchase 41%; desktop: 7.9%, 52%, 58%.

- Mobile conversion = 0.052 × 0.38 × 0.41 = 0.81%; desktop 2.38%.
- Revenue at stake at mobile checkout → purchase: 42,000 × 0.052 × 0.38 × (0.58 − 0.41) × $85 ≈ **$11,990/month** (estimate, upper bound).
- Recordings show a forced account-creation step on mobile: enable guest checkout (bug-level fix, ship) and monitor the step rate for 4 weeks.

## Example Requests

- "Audit my WooCommerce store's conversion funnel and tell me which step loses the most revenue."
- "Give me a prioritised CRO roadmap for the next quarter from my GA4 funnel data and customer survey."
- "Which of these 15 CRO ideas should I test and which should I just implement, given 3,000 sessions a day?"

## Output Format

1. Tracking check result (analytics vs order system).
2. Funnel table by device and source, with step rates, RPV and revenue at stake per step.
3. Findings by source: heuristic, technical, quantitative, qualitative (each with evidence).
4. Prioritised hypothesis backlog (PXL/ICE), each marked "test" or "ship and monitor".
5. CRO log template and monthly review plan.

## Quality Checks

- Tracking validated before conclusions are drawn.
- Every recommendation cites its evidence (data point, recording, survey answer).
- RPV or contribution is the success metric, not conversion rate alone.
- Tests are only proposed where traffic allows the required sample in ≤ 8 weeks.
- No deceptive urgency or hidden costs; accessibility issues listed as defects.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** funnel, revenue and speed data from the store's analytics for stated dates; survey answers quoted as given.
- **Estimates:** revenue at stake, expected uplift, industry conversion benchmarks (vary widely by category and traffic mix).
- Standards (GA4 events, accessibility law) were reviewed in November 2026.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill conversion-rate-optimization -g
```

## Usage

Ask your AI agent:

- "Audit my store's conversion funnel and identify the biggest drop-offs."
- "Give me a CRO checklist for my product pages."
- "What is a good conversion rate for my industry and how do I improve mine?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
