---
name: api-monitoring
description: "API and webhook monitoring for e-commerce integrations. Inventories the APIs and webhooks a store depends on (payments, marketplaces such as Amazon SP-API, Shopify, inventory, shipping, ERP), defines health checks, latency and error-rate SLOs, rate-limit and webhook-failure alerts, and computes availability, error budget and MTTR with a script. Use when orders, stock or prices stop syncing between systems, webhooks fail, or a team asks how to monitor integrations and report on SLAs."
nexscope:
  name: "API Monitoring"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "api"
    - "webhook"
    - "monitoring"
    - "integration"
    - "ecommerce"
  model: "any"
  tokens: "~2000"
  keywords:
    - "api monitoring"
---

# API Monitoring

AI-powered API and webhook monitoring skill for e-commerce integrations. Designs health check systems, alerting strategies, SLA reporting templates, and integration validation for e-commerce API endpoints.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Health, latency and error monitoring of the APIs and webhooks behind the store (payments, inventory, marketplaces, shipping), with SLOs and error budgets.

Part of: Store reliability and technical quality. For neighbouring jobs, use the matching skill instead:

- `synthetic-monitoring` — Scripted checks of the critical shopper journeys (home, search, product, add to cart, checkout) with alerts and performance baselines.
- `domain-monitoring` — Domain expiry, DNS, SSL/TLS certificates and email authentication (SPF, DKIM, DMARC) monitoring.
- `file-integrity-monitoring` — Detecting unauthorized changes to store files, code and payment-page scripts.
- `visual-regression-testing` — Screenshot comparison to catch layout and UI breakages before and after releases.
- `localization-testing` — Testing translations, currencies, prices, taxes, shipping and legal information per country.
- `public-status-page` — Telling customers and partners about incidents and uptime through a public status page.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| List of integrations: endpoint, direction, purpose, owner | Architecture notes, app list, middleware |
| Response codes, latency and error logs | API gateway, app logs, monitoring tool |
| Webhook delivery history and failures | Platform admin (e.g. Shopify app/webhook logs, Stripe dashboard), queue metrics |
| Rate limits per API | Each provider's documentation (Shopify, Amazon SP-API, carriers) |
| Incidents with start/end times | Incident notes, status pages of providers |
| Target SLO / contractual SLA | Contracts, internal targets |

## Workflow

1. **Map dependencies**: for each integration note what breaks for customers or operations if it fails (orders not imported, stock not updated, labels not printed).
2. **Health checks**: a lightweight authenticated call or a heartbeat per integration every 1-5 minutes; check content, not only status code.
3. **Golden signals**: error rate (4xx/5xx, timeouts), latency p95, throughput, saturation (rate-limit headers, 429 responses, queue backlog).
4. **Webhooks**: alert on failed deliveries, growing retry queues and subscriptions disabled after repeated failures (each platform retries for a limited time; check its documentation). Add a reconciliation job (e.g. compare orders in the platform and in the ERP every hour).
5. **SLOs**: set availability and latency targets per integration; compute error budgets and review burn weekly with the script below.
6. **Alerting**: page on customer-impacting failures (payments, order import), ticket for the rest; include links to dashboards and runbooks.
7. **Report**: monthly SLA report per integration (availability, incidents, MTTR, top causes).

## Calculations and Tools

`scripts/uptime.py` computes availability, error budget, MTTR and latency percentiles from exported checks and incidents:

```bash
python3 scripts/uptime.py '{"period_days": 30, "slo": 0.999, "incidents": [{"start": "2026-11-03T10:00:00", "end": "2026-11-03T10:22:00", "service": "payments API"}], "checks": [{"ok": true, "latency_ms": 180}, {"ok": true, "latency_ms": 240}, {"ok": false, "latency_ms": null}]}'
```

- Error budget (minutes) = (1 − SLO) × days × 1,440 → 99.9% over 30 days = 43.2 minutes.
- MTTR = average incident duration; percentiles use the nearest-rank method.

## Example Requests

- "Orders from Amazon sometimes don't reach our ERP. How do we monitor that integration?"
- "Our Shopify inventory webhook failed overnight. Set up alerts and a reconciliation check."
- "Compute our payment API availability and error budget from these incidents."

## Output Format

```
API & WEBHOOK MONITORING — [Store]
| Integration | Direction | Health check | SLO | Alert rule | Runbook link |
SLA report (period): availability, downtime, error budget used, incidents, MTTR, p95 latency
Top causes and fixes
```

## Quality Checks

- Every integration that touches orders, payments or stock has a check and an owner.
- Alerts were tested; no secret or token appears in check definitions shared in the report.
- Webhook monitoring includes a reconciliation, not only delivery success.
- SLA figures state the data source and period; incidents without an end time are flagged, not guessed.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: logs, delivery histories, incident timestamps and the computed metrics derived from them.
- **Estimates**: business impact per minute, rate-limit headroom when headers are not logged, provider-side incidents not visible in your logs.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill api-monitoring -g
```

## Usage

**Input:**
API endpoints, webhook URLs, SLA requirements, integration architecture

**Output:**
Health check framework, alerting rules, SLA report templates, integration validation checklist

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up api monitoring for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
