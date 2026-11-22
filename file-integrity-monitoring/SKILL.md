---
name: file-integrity-monitoring
description: "File integrity monitoring for online stores. Baselines store files, code and payment-page scripts, detects unauthorized changes (malware, card skimmers, unexpected theme or plugin edits) with checksums or FIM tools and maps controls to PCI DSS script-integrity requirements. Use when a self-hosted store (WooCommerce, Magento, custom) or a Shopify theme needs tamper detection, after a suspected hack or skimmer, or to prepare payment-page security checks."
nexscope:
  name: "File Integrity Monitoring"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "security"
    - "monitoring"
    - "file-integrity"
    - "ecommerce"
  model: "any"
  tokens: "~2000"
  keywords:
    - "file integrity monitoring"
---

# File Integrity Monitoring

AI-powered file integrity monitoring skill for e-commerce websites. Designs file change detection systems, tamper alerts, security baselines, and recovery procedures to protect online stores.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Detecting unauthorized changes to store files, code and payment-page scripts.

Part of: Store reliability and technical quality. For neighbouring jobs, use the matching skill instead:

- `synthetic-monitoring` — Scripted checks of the critical shopper journeys (home, search, product, add to cart, checkout) with alerts and performance baselines.
- `api-monitoring` — Health, latency and error monitoring of the APIs and webhooks behind the store (payments, inventory, marketplaces, shipping), with SLOs and error budgets.
- `domain-monitoring` — Domain expiry, DNS, SSL/TLS certificates and email authentication (SPF, DKIM, DMARC) monitoring.
- `visual-regression-testing` — Screenshot comparison to catch layout and UI breakages before and after releases.
- `localization-testing` — Testing translations, currencies, prices, taxes, shipping and legal information per country.
- `public-status-page` — Telling customers and partners about incidents and uptime through a public status page.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Platform and hosting (self-hosted vs hosted SaaS) | Hosting account |
| Code locations: core, plugins/extensions, theme, uploads | Server, Git repository |
| Who can deploy or edit files | Hosting users, admin roles, CI/CD |
| Scripts loaded on checkout/payment pages | Browser DevTools, tag manager |
| Backups and their dates | Hosting / backup tool |

## Workflow

1. **Scope by platform**:
   - *Self-hosted* (WooCommerce, Magento, custom): monitor server files.
   - *Hosted* (Shopify): no server access; monitor theme code changes (theme version history, GitHub integration), apps and staff permissions, and scripts on storefront pages.
2. **Baseline**: hash every file of core, plugins and theme from a known-good state (ideally from the Git repository or a clean install).
3. **Detection**: schedule a comparison (daily, or real time with a FIM agent such as Wazuh, OSSEC, AIDE or Tripwire); exclude caches, logs and upload folders that change normally, but watch for executable files in upload folders.
4. **Payment pages**: inventory every script on payment pages, justify each, and detect unauthorized changes to scripts and HTTP headers (PCI DSS v4.0 requirements 6.4.3 and 11.6.1 cover this for in-scope merchants; confirm applicability with your acquirer or QSA).
5. **Alert and triage**: who receives alerts, how to tell a deploy from tampering (compare with the release log).
6. **Response**: isolate, restore from a clean source, rotate credentials, scan, review access logs, notify as required.
7. **Re-baseline** after every legitimate release.

## Calculations and Tools

Checksum baseline and comparison with standard tools (self-hosted):

```bash
# Create a baseline (run from the store root, excluding changing folders)
find . -type f -not -path './var/cache/*' -not -path './wp-content/cache/*' -print0 | sort -z | xargs -0 sha256sum > /secure/baseline.sha256
# Compare later: lists changed or missing files
sha256sum --quiet -c /secure/baseline.sha256
# New files since the baseline
find . -type f -newer /secure/baseline.sha256 -not -path './var/cache/*'
```

Store the baseline outside the web root and outside the server if possible.

## Example Requests

- "We found a card skimmer on our Magento checkout. How do we detect file changes from now on?"
- "Set up file integrity monitoring for our WooCommerce site with daily alerts."
- "How do we monitor changes to our Shopify theme code and checkout scripts?"

## Output Format

```
FILE INTEGRITY PLAN — [Store]
Scope: [paths monitored / excluded]   Tool: [...]   Frequency: [...]
Payment-page script inventory: | Script | Purpose | Owner | Integrity control |
Alert routing and triage steps
Incident response checklist
```

## Quality Checks

- The baseline comes from a known-good source, not from a possibly compromised server.
- Excluded paths are justified; upload folders are checked for executable files.
- Payment-page scripts are all listed with an owner.
- The plan never asks to paste credentials or private keys into the conversation.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: hashes, file lists and script inventories produced by the commands or tools.
- **To confirm**: PCI DSS applicability and scope (depends on the merchant's payment setup, decided with the acquirer or a QSA); this is not a security audit.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill file-integrity-monitoring -g
```

## Usage

**Input:**
Website/server details, critical file paths, security requirements

**Output:**
FIM implementation plan, tamper detection rules, security baseline config, incident recovery procedures

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up file integrity monitoring for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
