---
name: synthetic-monitoring
description: "Synthetic monitoring of an online store's critical shopper journeys. Designs scripted checks (home, search, product page, add to cart, checkout up to payment in test mode) with Playwright or a monitoring service, sets run frequency, locations, performance baselines and alert rules, and defines the response runbook. Use when a store wants to know before customers do that checkout, cart or search is broken or slow, or asks how to set up uptime and journey monitoring."
nexscope:
  name: "Synthetic Monitoring"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "monitoring"
    - "checkout"
    - "uptime"
    - "testing"
    - "ecommerce"
  model: "any"
  tokens: "~2000"
  keywords:
    - "synthetic monitoring"
---

# Synthetic Monitoring

AI-powered synthetic monitoring skill for e-commerce websites. Designs automated user journey tests for add-to-cart, checkout, and payment flows with alerting rules and performance baselines.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Scripted checks of the critical shopper journeys (home, search, product, add to cart, checkout) with alerts and performance baselines.

Part of: Store reliability and technical quality. For neighbouring jobs, use the matching skill instead:

- `api-monitoring` — Health, latency and error monitoring of the APIs and webhooks behind the store (payments, inventory, marketplaces, shipping), with SLOs and error budgets.
- `domain-monitoring` — Domain expiry, DNS, SSL/TLS certificates and email authentication (SPF, DKIM, DMARC) monitoring.
- `file-integrity-monitoring` — Detecting unauthorized changes to store files, code and payment-page scripts.
- `visual-regression-testing` — Screenshot comparison to catch layout and UI breakages before and after releases.
- `localization-testing` — Testing translations, currencies, prices, taxes, shipping and legal information per country.
- `public-status-page` — Telling customers and partners about incidents and uptime through a public status page.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Critical journeys and URLs (home, top collection, top product, cart, checkout) | Store analytics: top landing pages and conversion paths |
| Test account, test product, test payment method | Payment provider test mode (e.g. Shopify Bogus Gateway / test mode, Stripe test cards) |
| Current monitoring tools and alert channels | Team (email, Slack, on-call) |
| Traffic by country and device | Analytics, to choose check locations and mobile/desktop |
| Past incidents and their impact | Incident notes, support tickets |

## Workflow

1. **List journeys by revenue impact**: checkout and add-to-cart first, then search, product pages, login, store locator.
2. **Choose the tool**: a hosted synthetic monitoring service (Datadog, Checkly, Better Stack, Pingdom...) or Playwright tests run on a schedule (GitHub Actions, cron).
3. **Script each journey** with stable selectors and explicit assertions (price shown, "Add to cart" enabled, cart count increments, checkout page loads payment step). Never place real orders: stop before payment or use test mode.
4. **Frequency and locations**: checkout every 5-15 minutes from the main customer regions; less critical pages every 30-60 minutes.
5. **Baselines**: record normal step durations for 1-2 weeks, then alert on failures and on sustained slowdowns (e.g. 3 consecutive runs above baseline × 2).
6. **Alerts and runbook**: who is paged, first checks (status of payment provider, recent deploys, app changes), escalation, customer communication (`public-status-page`).
7. **Review monthly**: false alarms, missed incidents, journeys to add after site changes.

## Calculations and Tools

- **Availability of a journey** = successful runs ÷ total runs over the period; error budget and MTTR with the `api-monitoring` calculator (`python3 api-monitoring/scripts/uptime.py` from the plugin root).
- **Alert on consecutive failures** (2-3) rather than one failed run, to filter network noise.
- **Example Playwright check** (adapt URLs and selectors):

```javascript
// checkout-journey.spec.js — run with: npx playwright test
const { test, expect } = require('@playwright/test');
test('add to cart reaches checkout', async ({ page }) => {
  await page.goto('https://example-store.com/products/test-product');
  await page.getByRole('button', { name: /add to cart/i }).click();
  await page.goto('https://example-store.com/cart');
  await expect(page.getByText(/subtotal/i)).toBeVisible();
  await page.getByRole('button', { name: /check ?out/i }).click();
  await expect(page).toHaveURL(/checkout/);
});
```

## Example Requests

- "My Shopify checkout broke for 3 hours last month and nobody noticed. Set up monitoring so it can't happen again."
- "Write Playwright checks for search, add to cart and checkout on our WooCommerce store."
- "How often should we run synthetic checks and when should they alert?"

## Output Format

```
SYNTHETIC MONITORING PLAN — [Store]
| Journey | Steps & assertions | Frequency | Locations | Alert rule | Owner |
Tool: [...]   Test data: [test product, test payment mode]
Baselines: [step: normal duration]
Runbook: [first checks → escalation → status page]
```

## Quality Checks

- Every check stops before a real payment or uses test mode; no real orders, no real card data.
- Each journey has at least one business assertion (not only "page returned 200").
- Alert rules require consecutive failures; a test alert has been sent end to end.
- Selectors do not depend on text that changes with promotions.
- Checks cover mobile viewport for mobile-heavy stores.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: run results, durations and failures from the monitoring tool.
- **Estimates**: revenue at risk per minute of downtime (average revenue per minute from analytics is an approximation); baselines before 2 weeks of data.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill synthetic-monitoring -g
```

## Usage

**Input:**
Website URL, critical user flows, SLA targets

**Output:**
Synthetic test suite design, alerting rules, performance baselines, incident response procedures

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up synthetic monitoring for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
