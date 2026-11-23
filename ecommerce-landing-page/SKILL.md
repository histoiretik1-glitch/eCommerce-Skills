---
name: ecommerce-landing-page
description: "Landing page conversion audit for any store. Reviews an existing product, collection or campaign page section by section (message match, CTA, trust signals, copy, layout, speed) and lists prioritized fixes and A/B test ideas. Use when a seller wants an existing page reviewed or asks why a page converts poorly (to build a new Shopify page use `shopify-landing-page-builder`)."
metadata:
  nexscope:
    emoji: "🖥️"
    category: ecommerce
---

# E-Commerce Landing Page 🖥️

Audit and optimize e-commerce landing pages for conversion. CTA placement, trust signals, page structure, copy optimization, and A/B testing strategy for product pages, collection pages, and campaign landing pages.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Auditing an existing landing or product page for conversion.

Part of: Conversion and landing pages. For neighbouring jobs, use the matching skill instead:

- `conversion-rate-optimization` — Platform-independent CRO: funnel analysis, heuristics and testing roadmap.
- `shopify-conversion-optimization` — CRO on a Shopify store: theme, apps, product pages, Shopify checkout.
- `shopify-landing-page-builder` — Building a new campaign or seasonal landing page on Shopify.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-landing-page -g
```

## Usage

```
Audit my Shopify landing page for our summer collection launch. Conversion rate is 0.8%. I'm driving traffic from Meta ads.
```

## Capabilities

- Landing page conversion audit (CTA, fold, trust signals, friction)
- Hero section optimization (headline, subheadline, CTA, hero image)
- Social proof placement strategy (reviews, testimonials, press mentions)
- Mobile conversion optimization
- Page speed impact analysis
- Copy optimization framework (benefit-driven, objection-handling)
- A/B testing plan with hypothesis prioritization

## Principles and Constraints

Audit standards for an existing landing or product page on any platform, as known at the last review of this skill (November 2026).

- **Message match:** the headline, offer and visual must continue the promise of the ad, email or search query that brought the visitor; mismatches cause most paid-traffic bounces.
- **One page, one goal:** a campaign landing page has one primary action; secondary links are limited (navigation can stay on product pages).
- **Speed thresholds (Google Core Web Vitals, "good" at the 75th percentile of real users):** LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. Paid social traffic is mostly mobile and in-app browsers, so measure on mobile.
- **Ad platform policies apply to the page:** Meta, Google and TikTok review destination pages (no misleading claims, working page, disclosed pricing and policies); a disapproved page stops the campaign.
- **Claims and social proof must be real:** reviews from real buyers, accurate "as seen in" logos, truthful urgency.
- **Scope:** this skill audits an existing page. Building a new Shopify page is `shopify-landing-page-builder`; the store-wide funnel is `conversion-rate-optimization`.

## Data Needed

| Data | Where |
|------|-------|
| Page URL, screenshots on mobile and desktop | The page |
| Traffic source of the page and the ad/email creatives sending traffic | Ad manager, email tool, UTM report |
| Sessions, engagement, add-to-cart / lead / purchase rate, RPV for the page | Analytics filtered on the landing page |
| CPC/CPM and CPA of the campaign | Ad platform |
| Core Web Vitals field data for the URL (or origin) | PageSpeed Insights / CrUX, Search Console |
| Scroll depth, heatmaps, recordings, on-page survey | Behaviour analytics tool |

## Workflow

1. **Confirm the page's job:** traffic source, audience temperature (cold, warm, retargeting), primary action and the number that defines success.
2. **Check message match:** put the ad and the page side by side; the headline must restate the ad's promise and offer within the first screen.
3. **Run a 5-second test** (or ask 5 people): what is it, for whom, what to do next. Wrong answers point to the hero section.
4. **Audit the first screen on mobile:** headline (benefit), sub-headline (proof or how), product visual, price/offer, primary CTA visible without scrolling, one trust element.
5. **Audit the body in the order objections arise:** how it works, proof (reviews with photos, numbers, guarantees), comparison, FAQ that answers the top support questions, repeat CTA.
6. **Measure speed** and fix the largest elements (hero image weight, scripts, fonts) until mobile LCP is under 2.5 s.
7. **Read behaviour data:** where visitors stop scrolling, what they click that is not a link, survey answers.
8. **Score the page** with the audit scorecard, list fixes, and prepare A/B tests for the highest-impact uncertain changes (`ecommerce-ab-testing`).

## Calculations and Tools

- **Landing page conversion rate** = primary actions ÷ landing sessions; **RPV** = revenue ÷ landing sessions.
- **Cost per acquisition** = CPC ÷ conversion rate; **break-even conversion rate** = CPC ÷ (AOV × contribution margin %).
- **Message match score** (this skill's checklist): headline restates the ad promise, same offer, same visual, same product, CTA wording consistent → 0–5.
- **Audit scorecard:** 20 checks across message match, clarity, proof, friction, speed, mobile (pass/fail), reported as passes ÷ 20.
- **Scroll reach** = share of sessions reaching each section; a key section below 30% reach should move up (working rule).

## Worked Example

*Illustrative example with invented figures.* A summer-collection page receives Meta traffic at $0.90 CPC; AOV $72, contribution margin 45%; conversion 0.8%.

- CPA = 0.90 ÷ 0.008 = **$112.50**; break-even conversion = 0.90 ÷ (72 × 0.45) = **2.8%**: the campaign loses money at 0.8%.
- Audit: ad promises "linen sets under $80", page headline says "Summer Collection" with no prices above the fold (message match 2/5); mobile LCP 4.1 s (2.3 MB hero video).
- Fixes: headline "Linen sets under $80 — free returns", price grid in first screen, compressed hero image; test the new hero vs old.

## Example Requests

- "Audit my landing page for our summer collection. Conversion is 0.8% from Meta ads."
- "Compare my Google Ads text and the landing page it sends to: is the message consistent, and what should change?"
- "What conversion rate do I need on this page to break even with a $0.90 CPC and a $72 AOV?"

## Output Format

1. Page context: source, audience, goal, current metrics, break-even conversion rate.
2. Scorecard (20 checks) with pass/fail and evidence.
3. Speed report (LCP, INP, CLS on mobile) and the elements to fix.
4. Prioritised fix list (ship now vs test) with rewritten headline, sub-headline and CTA options.
5. Test plan for the top uncertain change.

## Quality Checks

- Audit done on a real phone and in the in-app browser of the traffic source.
- Ad and page compared side by side; message match scored.
- Break-even conversion computed from the seller's own CPC, AOV and margin.
- Social proof and urgency elements verified as genuine.
- Speed figures from field data where available, lab data labelled as such.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** analytics and ad platform figures for stated dates, measured Core Web Vitals.
- **Estimates:** expected conversion after fixes, industry landing-page benchmarks.
- Thresholds and policies were reviewed in November 2026.

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
