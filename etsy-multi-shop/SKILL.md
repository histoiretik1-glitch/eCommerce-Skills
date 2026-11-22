---
name: etsy-multi-shop
description: "Etsy multi-shop management. Decides when to open a second Etsy shop, how to split categories and brands between shops, and how to run several shops efficiently within Etsy's rules. Use when an Etsy seller asks about opening or managing more than one Etsy shop."
metadata:
  nexscope:
    category: etsy
---

# Etsy Multi-Shop

Multi-shop management — category separation, brand differentiation, efficiency optimization.

Decide whether a second Etsy shop is worth it, and run several shops without doubling the workload or breaking Etsy's rules.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Deciding on and running more than one Etsy shop.

Part of: Etsy selling. For neighbouring jobs, use the matching skill instead:

- `etsy-seller-guide` — Entry point for Etsy: diagnoses where the shop stands across the whole selling lifecycle and routes to the specialist Etsy skills.
- `etsy-shop-setup` — Opening a new Etsy shop: account, policies, payments, first listings and launch checklist.
- `etsy-shop-branding` — Shop identity on Etsy: name, banner, logo, About section, photo style and packaging.
- `etsy-star-seller` — Reaching and keeping the Etsy Star Seller badge (messages, shipping, reviews).
- `etsy-shop-analytics` — Reading Etsy Stats to find what drives or blocks sales.

<!-- role-and-scope:end -->

## When to Use

- The seller sells unrelated product lines in one shop
- Considering a separate shop for a new brand, wholesale-style supplies or digital products
- Already running several shops and struggling with time or consistency

## Inputs to Collect

Current product lines and their sales, buyer types per line, time available per week, branding of each line, tools used for listings and orders.

## Decision Criteria

Open a second shop when most of these are true:

- The product lines target **different buyers** (e.g. wedding decor vs. pet accessories).
- Mixing them **confuses the shop's identity** or its search relevance.
- Each line can reach **enough listings** (ideally 20+) to look established.
- The seller has **time** to answer messages and ship on time for both (each shop has its own Star Seller metrics).

Keep one shop with clear sections when the products share the same buyer or style.

## Rules to Respect

Each shop must follow Etsy's policies on its own; separate shops must not be used to get around a suspension, policy limits or reviews. Confirm the current rules in Etsy's Seller Policy, as account requirements (separate email, etc.) can change.

## Workflow

1. Map product lines to buyers and decide: one shop with sections, or separate shops.
2. For a new shop, plan brand, name and first listings (`etsy-shop-setup`, `etsy-shop-branding`).
3. Share operations: one production calendar, shared shipping supplies, message templates, a weekly routine per shop.
4. Track each shop separately (`etsy-shop-analytics`) and stop the one that does not pay back the time.

## Output Format

1. Recommendation (one shop or several) with reasons
2. Split of product lines between shops
3. Weekly operating routine
4. KPIs per shop and review date

## Example Requests

- "Should I open a second Etsy shop for my digital planners, separate from my jewelry?"
- "Help me with etsy multi-shop strategy for my Etsy shop"
- "What are the best practices for etsy multi-shop strategy?"

## Status

🔶 **Beta** — full workflow added in plugin version 1.3.0.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill etsy-multi-shop -g
```

## Limitations

- Guidance from the information the seller shares; no live Etsy API access.
- Etsy fees, limits and policies change and differ by country: confirm current values in Etsy's Seller Handbook and policies before acting.
- For real-time data, see [Nexscope](https://www.nexscope.ai/?co-from=skill).

---

*Part of the `ecommerce-skills` Claude Code plugin. Original collection built by [Nexscope](https://www.nexscope.ai/?co-from=skill).*
