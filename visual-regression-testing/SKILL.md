---
name: visual-regression-testing
description: "Visual regression testing for e-commerce sites. Captures screenshots of key templates (home, collection, product, cart, checkout start) on desktop and mobile, compares them with approved baselines after theme, app or code changes, masks dynamic areas, sets difference thresholds and a review workflow. Use when a store wants to catch broken layouts, missing buttons or styling bugs before or right after a release, theme update or app install."
nexscope:
  name: "Visual Regression Testing"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "testing"
    - "visual-regression"
    - "QA"
    - "monitoring"
    - "ecommerce"
  model: "any"
  tokens: "~2000"
  keywords:
    - "visual regression testing"
---

# Visual Regression Testing

AI-powered visual regression testing skill for e-commerce websites. Designs screenshot comparison workflows, mobile/desktop visual checks, and change detection alerts to prevent conversion-killing UI bugs.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Screenshot comparison to catch layout and UI breakages before and after releases.

Part of: Store reliability and technical quality. For neighbouring jobs, use the matching skill instead:

- `synthetic-monitoring` — Scripted checks of the critical shopper journeys (home, search, product, add to cart, checkout) with alerts and performance baselines.
- `api-monitoring` — Health, latency and error monitoring of the APIs and webhooks behind the store (payments, inventory, marketplaces, shipping), with SLOs and error budgets.
- `domain-monitoring` — Domain expiry, DNS, SSL/TLS certificates and email authentication (SPF, DKIM, DMARC) monitoring.
- `file-integrity-monitoring` — Detecting unauthorized changes to store files, code and payment-page scripts.
- `localization-testing` — Testing translations, currencies, prices, taxes, shipping and legal information per country.
- `public-status-page` — Telling customers and partners about incidents and uptime through a public status page.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Key templates and example URLs | Store: one URL per template type |
| Viewports to test | Analytics: top devices and screen sizes |
| Release process (staging/preview, deploy times) | Team, theme preview links |
| Dynamic areas (prices, timers, carousels, reviews, ads) | Page inspection |
| Tool preference | Playwright, BackstopJS, Percy, Chromatic, Applitools… |

## Workflow

1. **Pick pages**: one representative URL per template plus high-revenue pages; keep the set small (10-30) so reviews stay fast.
2. **Viewports**: at least one mobile and one desktop size.
3. **Stabilize**: fixed test data, disable animations, wait for fonts and images, mask or hide dynamic regions (prices on sale, countdowns, review widgets, personalized recommendations).
4. **Baselines**: capture approved screenshots from production or staging.
5. **Compare** after every theme/app change: run against the preview or staging URL; fail when the difference exceeds the threshold.
6. **Review**: a person approves intended changes (new baseline) or files a bug.
7. **Schedule** a daily run against production to catch changes made by apps or third-party scripts.

## Calculations and Tools

Playwright built-in screenshot comparison (thresholds are a starting point to tune):

```javascript
// visual.spec.js — first run creates baselines: npx playwright test --update-snapshots
const { test, expect } = require('@playwright/test');
for (const url of ['/', '/collections/all', '/products/test-product', '/cart']) {
  test(`visual ${url}`, async ({ page }) => {
    await page.goto('https://example-store.com' + url);
    await expect(page).toHaveScreenshot({
      fullPage: true,
      maxDiffPixelRatio: 0.01,                       // fail above 1% of pixels changed
      mask: [page.locator('.price, .countdown, .reviews-widget')],
      animations: 'disabled',
    });
  });
}
```

Difference ratio = changed pixels ÷ total pixels; tune per page after a week of runs.

## Example Requests

- "Our theme update broke the mobile product page and we only noticed from customer emails. Set up visual testing."
- "Write Playwright visual tests for home, collection, product and cart pages on desktop and mobile."
- "Too many false alarms from our screenshot tests. How do we mask dynamic content?"

## Output Format

```
VISUAL REGRESSION PLAN — [Store]
| Page | URL | Viewports | Masked regions | Threshold |
Tool & commands: [...]
Workflow: change → run on preview → review diffs → approve baseline / file bug
```

## Quality Checks

- Each tested page has stable test data and masks for dynamic regions.
- Thresholds were tuned on real runs, not left at defaults blindly.
- Baseline updates are approved by a person, never accepted automatically.
- Mobile and desktop are both covered.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: screenshot diffs and their ratios produced by the tool.
- **Estimates**: initial thresholds and which regions are "dynamic" (confirm after the first runs).

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill visual-regression-testing -g
```

## Usage

**Input:**
Website URL, critical pages, device/viewport targets

**Output:**
Visual test suite design, screenshot comparison rules, mobile check checklist, anomaly alerting config

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up visual regression testing for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
