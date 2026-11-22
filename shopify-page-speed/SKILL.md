---
name: shopify-page-speed
description: "Shopify Core Web Vitals diagnosis. Explains LCP, INP and CLS from Shopify's web performance report and PageSpeed Insights against Google's thresholds (75th percentile), and finds which templates and elements cause slow loading, slow clicks or layout shifts. Use whenever a Shopify store owner shares speed scores or Core Web Vitals, asks what they mean or which pages are slow (for the fix plan use `shopify-speed-optimization`)."
nexscope:
  name: "Shopify Page Speed"
  category: "Site Performance"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "shopify"
    - "page-speed"
    - "performance"
    - "core-web-vitals"
  model: "any"
  tokens: "~2000"
  keywords:
    - "shopify page speed"
---

# Shopify Page Speed

AI-powered Shopify page speed optimization skill. Diagnoses performance bottlenecks, provides Core Web Vitals improvement plans, and recommends theme and app optimizations for faster Shopify stores.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Measuring Core Web Vitals and diagnosing which pages and elements are slow.

Part of: Shopify store speed. For neighbouring jobs, use the matching skill instead:

- `shopify-speed-optimization` — Full speed audit of a Shopify store and the prioritized fix plan (apps, images, scripts, theme).
- `shopify-theme-optimization` — Choosing and tuning the Shopify theme itself: Liquid code, sections, mobile UX.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Core Web Vitals from real users (LCP, INP, CLS) | Shopify admin web performance report; PageSpeed Insights "field data" / Chrome UX Report |
| Lab diagnostics per page | PageSpeed Insights or Lighthouse on mobile |
| URLs per template (home, collection, product, cart) | Store |
| Recent changes (theme updates, new apps) | Theme and app history |

## Workflow

1. **Use field data first**: Core Web Vitals are assessed on real users at the 75th percentile; lab scores (the 0-100 performance score) help diagnose but are not the metric itself.
2. **Per template**: collect LCP, INP and CLS for home, collection, product and cart (mobile first).
3. **Classify** each metric with Google's thresholds (below).
4. **Diagnose** with PageSpeed Insights audits:
   - LCP: which element is the LCP (often hero image or product image), its size, whether it is lazy-loaded by mistake, render-blocking resources.
   - INP: long tasks from apps, chat widgets, tag managers; heavy JavaScript on interaction.
   - CLS: images without dimensions, late-loading banners or app widgets, web fonts swapping.
5. **Attribute** each issue to a source: theme, a specific app, an image, a third-party script.
6. **Hand over** the prioritized findings to `shopify-speed-optimization` (fix plan) or `shopify-theme-optimization` (theme code).
7. **Re-measure**: field data is a 28-day rolling window, so improvements show progressively.

## Calculations and Tools

Google's Core Web Vitals thresholds (75th percentile of page loads; published by Google at web.dev):

| Metric | Good | Needs improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤ 2.5 s | 2.5-4.0 s | > 4.0 s |
| INP (Interaction to Next Paint) | ≤ 200 ms | 200-500 ms | > 500 ms |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | 0.1-0.25 | > 0.25 |

A page passes when all three are "good".

## Example Requests

- "My Shopify speed report says LCP 4.2 s on mobile. What is slowing it down?"
- "Explain our Core Web Vitals per template and what each number means."
- "Our CLS got worse after installing a reviews app. How do we confirm the cause?"

## Output Format

```
CORE WEB VITALS DIAGNOSIS — [Store, date, data source]
| Template | LCP | INP | CLS | Status | Main cause | Source (theme/app/image/script) |
Findings handed to the fix plan: [...]
```

## Quality Checks

- Field data and lab data are clearly separated; the data source and date are stated.
- Each finding names the element or script responsible, not only the metric.
- Mobile is analyzed before desktop.
- Thresholds are Google's published values, cited as such.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: field metrics from Shopify's report / Chrome UX Report, lab audits from PageSpeed Insights, Google's thresholds.
- **Estimates**: expected gains from a fix before re-measurement; sales impact of speed changes.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shopify-page-speed -g
```

## Usage

**Input:**
Shopify store URL, current theme, installed apps

**Output:**
Speed diagnostic report, Core Web Vitals improvement plan, theme optimization guide, app performance audit

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up shopify page speed for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
