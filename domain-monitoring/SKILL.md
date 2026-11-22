---
name: domain-monitoring
description: "Domain, DNS, SSL/TLS certificate and email authentication monitoring for a store. Checks domain registration expiry, DNS records, certificate expiry and chain, and SPF, DKIM and DMARC for transactional and marketing email, with commands to verify them and alert thresholds. Use when a store asks how to avoid an expired domain or certificate, why emails land in spam, or how to monitor its DNS and domain security."
nexscope:
  name: "Domain Monitoring"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "domain"
    - "ssl"
    - "security"
    - "monitoring"
    - "ecommerce"
  model: "any"
  tokens: "~2000"
  keywords:
    - "domain monitoring"
    - "ssl monitoring"
---

# Domain Monitoring

AI-powered domain and SSL certificate monitoring skill. Designs domain health checks, SSL expiry alerts, DNS anomaly detection, and security rating assessments for e-commerce websites.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Domain expiry, DNS, SSL/TLS certificates and email authentication (SPF, DKIM, DMARC) monitoring.

Part of: Store reliability and technical quality. For neighbouring jobs, use the matching skill instead:

- `synthetic-monitoring` — Scripted checks of the critical shopper journeys (home, search, product, add to cart, checkout) with alerts and performance baselines.
- `api-monitoring` — Health, latency and error monitoring of the APIs and webhooks behind the store (payments, inventory, marketplaces, shipping), with SLOs and error budgets.
- `file-integrity-monitoring` — Detecting unauthorized changes to store files, code and payment-page scripts.
- `visual-regression-testing` — Screenshot comparison to catch layout and UI breakages before and after releases.
- `localization-testing` — Testing translations, currencies, prices, taxes, shipping and legal information per country.
- `public-status-page` — Telling customers and partners about incidents and uptime through a public status page.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Domains and subdomains in use (store, email, CDN, landing pages) | Registrar, DNS provider, platform domain settings |
| Registrar, renewal date, auto-renew status, registrar lock | Registrar account |
| DNS provider and records (A/CNAME, MX, TXT) | DNS provider |
| Certificates and who renews them | Platform (Shopify and most hosts renew automatically), CDN, hosting |
| Email senders (store notifications, ESP, helpdesk) | Platform and ESP settings |

## Workflow

1. **Inventory domains** and who controls them; enable auto-renew and registrar lock; use an account with two-factor authentication.
2. **Registration expiry**: alert at 60, 30 and 7 days before expiry.
3. **DNS**: record the expected values; alert on unexpected changes to A/CNAME, MX and TXT records.
4. **Certificates**: check expiry and chain for every hostname; alert at 30 and 7 days. Hosted platforms usually renew automatically; custom subdomains and CDNs often do not. Public certificate lifetimes are being shortened in stages (CA/Browser Forum decision, starting 2026), so renewal must be automated.
5. **Email authentication**: SPF includes every sender, DKIM is enabled for each sender, DMARC is published (start with `p=none` and reports, then move to `quarantine`/`reject`). Large mailbox providers require SPF/DKIM/DMARC for bulk senders.
6. **Lookalike domains**: optional watch for typo domains used for phishing (see `brand-protection-shopify`).
7. **Monthly review** of the checks and DMARC reports.

## Calculations and Tools

Commands to verify (replace `example.com`):

```bash
# Certificate expiry date
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -enddate
# SPF and DMARC records
dig +short TXT example.com
dig +short TXT _dmarc.example.com
# Mail servers
dig +short MX example.com
# Registration expiry (format varies by registry)
whois example.com | grep -i expir
```

Days left = expiry date − today; alert thresholds as in the workflow.

## Example Requests

- "Our store certificate expired last year on a subdomain. Set up domain and SSL monitoring."
- "Order confirmation emails go to spam. Check our SPF, DKIM and DMARC setup."
- "Which DNS records should we monitor for our Shopify store and Klaviyo emails?"

## Output Format

```
DOMAIN HEALTH — [Brand]
| Domain/host | Registrar expiry | Auto-renew | Certificate expiry | Issuer | Status |
| Email sender | SPF | DKIM | DMARC policy | Action |
Alerts: [check → threshold → channel]
Fixes: [...]
```

## Quality Checks

- Every domain used by the store or its emails is listed, including subdomains.
- Dates come from the commands or provider dashboards, with the date they were checked.
- DMARC changes to `reject` only after reports show all legitimate senders pass.
- No DNS change is recommended without the exact record to add or edit.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: values returned by the commands, registrar and DNS dashboards at the time of checking.
- **Estimates / to confirm**: provider requirements and certificate lifetime rules (they change; confirm in current provider documentation).

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill domain-monitoring -g
```

## Usage

**Input:**
Domain name(s), current SSL provider, DNS configuration

**Output:**
Domain health check plan, SSL expiry alert setup, DNS monitoring rules, security rating assessment

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up domain monitoring for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
