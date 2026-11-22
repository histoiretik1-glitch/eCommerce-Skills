---
name: public-status-page
description: "Public status page and incident communication for e-commerce businesses. Defines which components to show (storefront, checkout, payments, order tracking, API), status levels, incident and maintenance templates, update cadence, subscriber notifications and uptime reporting, and chooses a status page tool. Use when a store or e-commerce platform wants to communicate outages or maintenance to customers, merchants or partners, or reduce support tickets during incidents."
nexscope:
  name: "Public Status Page"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "status-page"
    - "incident-communication"
    - "transparency"
    - "monitoring"
  model: "any"
  tokens: "~2000"
  keywords:
    - "public status page"
---

# Public Status Page

AI-powered public status page design skill for e-commerce businesses. Creates status page architecture, incident communication templates, subscriber notification systems, and uptime reporting frameworks.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Telling customers and partners about incidents and uptime through a public status page.

Part of: Store reliability and technical quality. For neighbouring jobs, use the matching skill instead:

- `synthetic-monitoring` — Scripted checks of the critical shopper journeys (home, search, product, add to cart, checkout) with alerts and performance baselines.
- `api-monitoring` — Health, latency and error monitoring of the APIs and webhooks behind the store (payments, inventory, marketplaces, shipping), with SLOs and error budgets.
- `domain-monitoring` — Domain expiry, DNS, SSL/TLS certificates and email authentication (SPF, DKIM, DMARC) monitoring.
- `file-integrity-monitoring` — Detecting unauthorized changes to store files, code and payment-page scripts.
- `visual-regression-testing` — Screenshot comparison to catch layout and UI breakages before and after releases.
- `localization-testing` — Testing translations, currencies, prices, taxes, shipping and legal information per country.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Customer-facing components and their dependencies | Architecture, `api-monitoring` inventory |
| Monitoring sources that can update the page | Synthetic and uptime monitors |
| Audience (shoppers, B2B buyers, merchants, partners) | Business model |
| Past incidents and support ticket volume | Incident notes, helpdesk |
| Tool preference and budget | Team |

## Workflow

1. **Components**: 5-10 items customers understand (e.g. Website, Checkout & payments, Order tracking, Customer accounts, API for partners), not internal services.
2. **Status levels**: Operational, Degraded performance, Partial outage, Major outage, Under maintenance; define what each means for customers.
3. **Tool**: hosted (Atlassian Statuspage, Instatus, Better Stack…) or self-hosted/static (e.g. Upptime); host it outside the main infrastructure so it stays up during outages.
4. **Automation**: connect monitors to propose status changes; a person confirms public incidents.
5. **Templates** for each incident stage: Investigating, Identified, Monitoring, Resolved; plus scheduled maintenance.
6. **Cadence**: first post within an agreed time after detection (e.g. 15 minutes), updates at a stated interval until resolved.
7. **Subscribers**: email/SMS/RSS/webhook; link the page from the help center, order emails and checkout error pages.
8. **Post-incident**: public summary for major incidents; monthly uptime per component.

## Calculations and Tools

- **Uptime per component** = 1 − downtime ÷ period; compute from incident start/end times with `python3 api-monitoring/scripts/uptime.py` (plugin root).
- **Time to first update** = first public post − detection time; track it per incident against the target.

## Example Requests

- "Set up a status page for our marketplace so merchants know when checkout is down."
- "Write incident update templates for a payment outage on our store."
- "Which components and status levels should our e-commerce status page show?"

## Output Format

```
STATUS PAGE PLAN — [Business]
Components: | Component | What customers see when it fails | Monitor |
Status levels and definitions
Templates: Investigating / Identified / Monitoring / Resolved / Maintenance
Cadence and owners; subscriber channels; monthly uptime report format
```

Template example:

```
[Investigating] Some customers can't complete checkout. We're investigating and will update by 14:30 UTC.
[Identified] The issue is caused by our payment provider. Orders placed are safe. Next update 15:00 UTC.
[Resolved] Checkout is working again since 14:52 UTC. Orders between 14:05 and 14:52 may need to be retried.
```

## Quality Checks

- Components are named in customer language, without internal jargon.
- Templates never blame a provider without confirmation and never promise times that are not known.
- The page is hosted independently of the store.
- Every update states the next update time.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: incident times and uptime computed from monitoring data.
- **Estimates**: expected reduction in support tickets; do not publish figures that are not measured.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill public-status-page -g
```

## Usage

**Input:**
Services/systems to monitor, audience (customers/partners), SLA targets

**Output:**
Status page architecture, incident template library, notification subscription design, uptime reporting framework

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up public status page for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
