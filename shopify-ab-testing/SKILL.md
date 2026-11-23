---
name: shopify-ab-testing
description: "Run data-driven A/B tests on your Shopify store. Test product pages, pricing, images, copy, checkout flow, and marketing campaigns with proper statistical methodology. Use when the user asks for help running A/B tests on a Shopify store (product pages, pricing, images, copy, checkout) with statistical rigor."
---

# Shopify A/B Testing

Run data-driven A/B tests on your Shopify store. Test product pages, pricing, images, copy, checkout flow, and marketing campaigns with proper statistical methodology.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Running A/B tests on a Shopify store with Shopify tools and apps.

Part of: A/B testing, Shopify setup, analytics and conversion. For neighbouring jobs, use the matching skill instead:

- `ecommerce-ab-testing` — A/B testing method for any channel: hypotheses, sample size, significance, Amazon experiments, ads and email tests.
- `shopify-store-setup` — Launching a new Shopify store: plan, payments, theme, products, shipping, taxes, domain.
- `shopify-analytics-guide` — Reading Shopify reports and KPIs: sales definitions, funnel, AOV, repeat customers, cohorts.
- `shopify-conversion-optimization` — CRO on a Shopify store: theme, apps, product pages, Shopify checkout.

<!-- role-and-scope:end -->

## Capabilities

- A/B testing tool selection for Shopify (native and third-party)
- Test hypothesis formulation and prioritization (ICE/PIE)
- Product page element testing: images, titles, prices, descriptions
- Checkout and cart page optimization tests
- Statistical significance calculation and sample size planning
- Test duration and traffic allocation
- Multi-variate testing for high-traffic stores
- Results interpretation and implementation workflow

## Platform Rules and Constraints

Shopify-specific constraints on experiments, at the last review of this skill (November 2026). Items marked **[check]** must be confirmed in the Shopify Help Center or the app's documentation.

- **Native testing is limited:** Shopify's admin does not randomise visitors between product page versions. Shopify has introduced theme experiments (Rollouts) in recent Editions **[check: availability on your plan]**; most stores use apps from the Shopify App Store (theme/content tests, price and shipping tests, e.g. Shoplift or Intelligems; examples, not endorsements).
- **Previewing a duplicate theme is not an A/B test:** it gives no random split and no control group.
- **Checkout:** checkout customisation goes through Checkout Extensibility (checkout UI extensions, Shopify Functions); checkout.liquid is retired **[check]**. Checkout UI extensions on the information, shipping and payment steps require Shopify Plus **[check]**, so checkout tests on other plans are limited to what apps and settings allow (express buttons, discounts, shipping rates).
- **Price tests must charge the price shown.** A price-test app has to apply the tested price to the cart and checkout; the price in Google Merchant Center and other feeds must match the landing page, or products can be disapproved.
- **Consumer protection:** show each visitor one consistent price during the session; fake scarcity or countdowns that reset are deceptive (FTC guidance in the US, UCPD in the EU).
- **Speed:** client-side test scripts add load time and can cause flicker; check Core Web Vitals in Online Store > Themes > speed report or PageSpeed Insights before and during the test.
- **Shopify Analytics sessions** are the reference for conversion rate (sessions that completed checkout ÷ sessions); the testing app's own counts can differ (bots, consent banners), so read results in one tool.

## Data Needed

| Data | Where |
|------|-------|
| Baseline conversion rate of the page or funnel step | Shopify Analytics > Reports > Conversion rate breakdown (last 4 weeks) |
| Daily sessions reaching the tested page | Analytics > Reports > Sessions by landing page |
| AOV and revenue per session | Analytics > Overview |
| Test results per variant: sessions, orders (and revenue) | The testing app's report or exported data |
| Traffic split configured | Testing app settings |
| Changes, promotions or campaigns during the test | Marketing calendar |

## Workflow

1. **Write the hypothesis:** "Because [evidence from analytics, recordings or reviews], changing [element] for [page/audience] will increase [metric]". One change per test.
2. **Prioritise** candidate tests with ICE or PIE scores; start with high-traffic templates (product template, cart).
3. **Size the test** with `ab_test.py` plan mode: baseline rate, the smallest lift worth detecting, 95% confidence, 80% power, daily sessions. If it needs more than 6–8 weeks, test a bigger change or a higher-traffic page.
4. **Choose the tool:** Shopify theme experiments if available, otherwise an app that randomises at the visitor level, applies prices in checkout for price tests, and loads without flicker.
5. **QA before launch:** both variants on mobile and desktop, add to cart and checkout work, prices and feeds match, analytics events fire.
6. **Run full weeks** (at least 14 days) without stopping early when the result "looks significant"; avoid launching during a sale unless the sale is the test.
7. **Analyse** with `ab_test.py` analyze mode: SRM check first, then p-value and confidence interval; also compare revenue per session, not only conversion.
8. **Ship or discard** and log the result (hypothesis, dates, numbers, decision) in a test log so it is not retested.

## Calculations and Tools

- **Sample size per variant** n = (z₁₋α/₂·√(2p̄(1−p̄)) + z₁₋β·√(p₁(1−p₁) + p₂(1−p₂)))² ÷ (p₂ − p₁)².
- **Duration** = total sessions needed ÷ daily sessions on the page, at least 14 days.
- **Two-proportion z-test** z = (p₂ − p₁) ÷ √(p̄(1−p̄)(1/n₁ + 1/n₂)); two-sided p-value.
- **Sample ratio mismatch (SRM):** chi-square test of the observed split against the configured split; p < 0.001 means the split is broken and results are invalid.
- **Revenue per session** = conversion rate × AOV, to catch a variant that converts more but sells cheaper.

```bash
python3 scripts/ab_test.py '{"mode": "plan", "baseline_rate": 0.025, "min_relative_lift": 0.15, "daily_sessions": 1800}'
```

```bash
python3 scripts/ab_test.py '{"mode": "analyze", "control": {"sessions": 10400, "orders": 262}, "variant": {"sessions": 10350, "orders": 301}}'
```

## Worked Example

*Illustrative example with invented figures.* A product page converts at 2.5% with 1,800 sessions a day. Detecting a 15% relative lift (2.5% → 2.875%) needs about 29,000 sessions per variant, about 33 days at 50/50: acceptable.

Partway through (about a third of the planned sample), control has 262 orders / 10,400 sessions (2.52%) and the variant 301 / 10,350 (2.91%), a +15.4% lift. The analyze command above prints p = 0.085 and a 95% confidence interval of −0.05 to +0.83 points, with no SRM (p = 0.73): **not significant yet**. Each variant has about 10,400 of the 29,193 sessions planned, so the right decision is to keep the test running to the planned size, not to ship the variant on a promising lift.

## Example Requests

- "My Shopify product page converts at 2.5% with 1,800 sessions a day. How long must I run an A/B test to detect a 15% lift?"
- "Control had 262 orders from 10,400 sessions, the new product template 301 from 10,350. Is the result significant on Shopify, and can I trust the split?"
- "I want to test a $34 vs $39 price on Shopify without breaking my Google Shopping feed. How do I set it up?"

## Output Format

1. Test plan: hypothesis, page/template, variant description, primary metric, sample size, duration, tool.
2. QA checklist results (devices, checkout, prices, feeds, tracking).
3. Results table: sessions, orders, conversion, revenue per session per variant, p-value, confidence interval, SRM check.
4. Decision (ship / discard / extend with a pre-stated reason) and the test log entry.

## Quality Checks

- One variable changed per test; the hypothesis is written before launch.
- Sample size and duration computed before launch and respected (no early stopping on a peek).
- SRM check passed before reading the lift.
- Price tests charge the displayed price in checkout and keep feeds consistent.
- Revenue per session reported next to conversion rate.
- Results come from one analytics source for both variants.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** sessions and orders per variant from the test app or Shopify Analytics for stated dates.
- **Estimates:** baseline rate used for sizing, expected lift, annualised revenue impact of a winning variant.
- Shopify feature availability (theme experiments, checkout extensions by plan) was reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-ab-testing -g
```

## Usage

Ask your AI agent:

- "Set up A/B tests for my Shopify product pages."
- "What should I test first to improve my conversion rate?"
- "Calculate how long I need to run my A/B test for significance."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
