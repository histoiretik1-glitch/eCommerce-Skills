---
name: shopify-conversion-optimization
description: "Increase Shopify store conversion rates with data-driven optimization. Product pages, checkout flow, trust signals, page speed, mobile UX, and A/B testing for higher revenue per visitor. Use when the user asks for help increasing a Shopify store's conversion rate (product pages, checkout, trust signals, mobile UX, speed)."
---

# Shopify Conversion Optimization

Increase Shopify store conversion rates with data-driven optimization. Product pages, checkout flow, trust signals, page speed, mobile UX, and A/B testing for higher revenue per visitor.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** CRO on a Shopify store: theme, apps, product pages, Shopify checkout.

Part of: Conversion and landing pages, Shopify setup, analytics and conversion. For neighbouring jobs, use the matching skill instead:

- `conversion-rate-optimization` — Platform-independent CRO: funnel analysis, heuristics and testing roadmap.
- `ecommerce-landing-page` — Auditing an existing landing or product page for conversion.
- `shopify-landing-page-builder` — Building a new campaign or seasonal landing page on Shopify.
- `shopify-store-setup` — Launching a new Shopify store: plan, payments, theme, products, shipping, taxes, domain.
- `shopify-analytics-guide` — Reading Shopify reports and KPIs: sales definitions, funnel, AOV, repeat customers, cohorts.
- `shopify-ab-testing` — Running A/B tests on a Shopify store with Shopify tools and apps.

<!-- role-and-scope:end -->

## Capabilities

- Conversion funnel analysis and drop-off identification
- Product page optimization: images, descriptions, social proof
- Checkout flow streamlining and friction reduction
- Trust signal implementation (reviews, badges, guarantees)
- Mobile-first UX optimization
- Page speed impact on conversion and fixes
- Urgency and scarcity tactics (ethical implementation)
- Post-purchase upsell and cross-sell setup

## Platform Rules and Constraints

Shopify constraints that shape conversion work, at the last review of this skill (November 2026). Items marked **[check]** must be confirmed in the Shopify Help Center.

- **Funnel data:** Shopify Analytics' conversion rate breakdown reports sessions, sessions with *added to cart*, *reached checkout* and *completed checkout*; this is the reference funnel for a Shopify store.
- **Checkout is Shopify-hosted:** layout changes are made through checkout settings and Checkout Extensibility (checkout UI extensions, Shopify Functions for discounts, delivery and payment customisations). Extensions on the information, shipping and payment steps require Shopify Plus **[check]**; on other plans, work on settings: express checkout (Shop Pay, Apple Pay, Google Pay, PayPal), customer accounts, required fields, address autocomplete, tipping, shipping rates.
- **Theme changes** go through the theme editor (sections, blocks, app blocks) or code; work on a duplicate theme and publish after QA.
- **Apps:** each storefront app can add scripts that slow the page; prefer app blocks / theme app extensions and remove apps you no longer use (uninstalling may leave code in the theme).
- **Honest urgency only:** stock counters must show real inventory, countdowns must end when stated; fake scarcity and fake reviews are deceptive practices (FTC rules in the US, including the 2024 rule on fake reviews **[check]**; UCPD in the EU).
- **Reviews:** Shopify product reviews come from apps (e.g. Judge.me, Okendo, Yotpo; examples); only display reviews from real buyers and include negative ones.
- **Accessibility:** product pages and checkout must stay usable with keyboard and screen readers; Shopify's checkout is built to WCAG, theme customisations are your responsibility.

## Data Needed

| Data | Where |
|------|-------|
| Conversion rate breakdown (4–8 weeks) overall, by device and by traffic source | Analytics > Reports > Conversion rate breakdown, Sessions by device/referrer |
| Top landing pages and product pages by sessions, add-to-cart rate | Reports > Sessions by landing page, Product analytics |
| AOV and revenue per session | Analytics > Overview |
| Abandoned checkouts with the step reached | Orders > Abandoned checkouts |
| Speed (Core Web Vitals, mobile) | Online Store > Themes speed report, PageSpeed Insights, Search Console |
| Qualitative evidence | Session recordings/heatmaps, on-site survey, support tickets, reviews |

## Workflow

1. **Measure the funnel** for the last 4–8 weeks: sessions → added to cart → reached checkout → completed, by device and traffic source.
2. **Find the leak:** compare each step rate with the store's own previous periods and between devices; a mobile step rate far below desktop is a UX problem, a paid-social segment far below others is a traffic-quality problem.
3. **Collect evidence on the leaking step:** recordings and heatmaps of top product pages, survey "What stopped you from buying today?", abandoned-checkout step, support questions.
4. **Audit the product page:** price and total cost (shipping shown early), delivery date, return policy, photos and video, variant picker clarity, reviews, sticky add-to-cart on mobile, payment icons and express checkout buttons.
5. **Audit cart and checkout settings:** express checkout enabled, unexpected costs removed, required fields minimised, discount field behaviour, shipping options and free-shipping threshold.
6. **Check speed:** mobile Largest Contentful Paint and Interaction to Next Paint on the top templates; remove unused apps, compress hero media (`shopify-page-speed`).
7. **Prioritise fixes** with ICE scores and the revenue-impact formula; ship low-risk fixes directly, test risky ones (`shopify-ab-testing`).
8. **Re-measure** the funnel 2–4 weeks after each release against the same period and traffic mix.

## Calculations and Tools

- **Step rates:** add-to-cart rate = added to cart ÷ sessions; checkout rate = reached checkout ÷ added to cart; checkout completion = completed ÷ reached checkout.
- **Revenue per session (RPS)** = conversion rate × AOV.
- **Revenue impact of a fix** ≈ sessions per month × (new step rate − current step rate) × downstream rates × AOV; label it an estimate.
- **Free-shipping threshold** test: threshold ≈ 1.2–1.3 × current AOV is a common starting point (a heuristic, not a rule); check that margin on the extra items covers the shipping cost.
- **ICE score** = impact × confidence × ease (1–10 each).

## Worked Example

*Illustrative example with invented figures.* 40,000 sessions a month, AOV $62: added to cart 6.0%, reached checkout 45% of carts, completed 52% of checkouts → conversion 1.40%, RPS $0.87.

- Mobile add-to-cart is 4.1% vs desktop 9.8%; recordings show the variant picker hidden below a tall image gallery.
- Fix: move the variant picker and sticky add-to-cart above the fold on mobile.
- Estimated impact if mobile add-to-cart reaches 5.0% on 28,000 mobile sessions: 28,000 × 0.009 × 0.45 × 0.52 × $62 ≈ **$3,660/month** (estimate, to be verified with a test).

## Example Requests

- "My Shopify store converts at 1.4% with 40,000 sessions a month. Find where the funnel leaks and give me a prioritised fix list."
- "Mobile add-to-cart is 4% vs 10% on desktop on my Shopify product pages. What should I change in the theme?"
- "Half my Shopify checkouts are abandoned at the shipping step. Which settings and offers should I change?"

## Output Format

1. Funnel table (overall, mobile, desktop, top sources) with step rates and the main leak.
2. Evidence summary for the leaking step (recordings, survey, abandoned checkouts).
3. Fix list: issue, page/setting, fix, ICE score, estimated monthly impact (estimate), ship-directly vs test.
4. Measurement plan: metric, baseline, re-measure date.

## Quality Checks

- Funnel rates computed from Shopify's conversion rate breakdown for a stated period, split by device.
- Every fix is linked to evidence, not only to a best-practice list.
- No fake urgency, fake reviews or hidden costs in recommendations.
- Checkout recommendations respect the seller's Shopify plan (Plus-only features flagged).
- Impact figures labelled as estimates; winners confirmed by test or before/after with the same traffic mix.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** the store's Shopify funnel, device and source reports, abandoned checkout counts, measured speed scores, for stated dates.
- **Estimates:** revenue impact of fixes, free-shipping threshold effect, industry conversion benchmarks.
- Plan-dependent checkout features were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-conversion-optimization -g
```

## Usage

Ask your AI agent:

- "Audit my Shopify store conversion rate and give me a fix list."
- "How do I reduce cart abandonment on my Shopify store?"
- "Optimize my product pages for higher conversion."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
