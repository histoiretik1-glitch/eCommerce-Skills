---
name: share-of-shelf
description: "Digital share of shelf measurement for brands on Amazon, Walmart, Target, TikTok Shop or other marketplaces. Defines the keyword set and a repeatable collection method, computes organic, sponsored and position-weighted share of search results by keyword and brand with a script, and tracks competitors over time. Use when a brand asks how visible it is in marketplace search versus competitors, how its share of shelf changed, or which keywords to defend with ads or SEO."
nexscope:
  name: "Share of Shelf"
  category: "Monitoring & Alerts"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "digital-shelf"
    - "visibility"
    - "category-analysis"
    - "monitoring"
  model: "any"
  tokens: "~2000"
  keywords:
    - "share of shelf"
---

# Share of Shelf

AI-powered digital share of shelf analysis skill. Measures brand visibility within product categories, benchmarks against competitors, and tracks shelf position trends across e-commerce platforms.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Measuring a brand's share of marketplace search results against competitors, by keyword and over time.

Part of: Competitive visibility. For neighbouring jobs, use the matching skill instead:

- `ecommerce-competitor-analysis` — Cross-platform competitor analysis: channel presence, offer, strategy and positioning.
- `market-gap-analysis` — Finding underserved needs and niches that competitors miss.

<!-- role-and-scope:end -->

## Data Needed

| Data | Where to find it |
|------|------------------|
| Keyword set (category, generic, brand, competitor terms) | Search term reports (Amazon Brand Analytics if available), `ecommerce-keyword-research` |
| Search result pages per keyword: rank, brand, sponsored or organic | Manual collection or a digital shelf tool, same conditions each time |
| Brand list and brand aliases | Brand and competitor catalogs |
| Collection context: marketplace, location/ZIP, device, logged in or not, date | Collection log |

## Workflow

1. **Keyword set**: 20-100 keywords weighted by importance (search volume or revenue); keep it fixed between snapshots.
2. **Collection protocol**: same marketplace, location, device type, account state and time of day; first page or top N results; record sponsored labels.
3. **Normalize brands** (aliases, sub-brands) and mark the seller's own listings.
4. **Compute** shares with the script; compare organic vs sponsored to see whether visibility is bought or earned.
5. **Segment** by keyword type (generic vs brand vs competitor) and by product line.
6. **Trend**: repeat weekly or monthly with the same protocol; compare like with like.
7. **Act**: keywords with high value and low organic share → SEO/listing work (`product-title-optimization`, platform listing skills); defend with ads where competitors take sponsored slots.

## Calculations and Tools

`scripts/sos.py`:

```bash
python3 scripts/sos.py '{"brand": "Acme", "top_n": 10, "results": [{"keyword": "steel water bottle", "rank": 1, "brand": "Acme", "sponsored": true}, {"keyword": "steel water bottle", "rank": 2, "brand": "Hydra", "sponsored": false}]}'
```

- Share of shelf = brand listings ÷ all listings in the top N.
- Organic / paid share = same within organic / sponsored listings.
- Weighted share uses 1/rank weights so top positions count more (a convention; state it in reports).

## Example Requests

- "What's our share of shelf on Amazon for 'protein powder' keywords compared with the top 3 brands?"
- "Build a monthly share-of-shelf tracker for our Walmart category."
- "Is our visibility organic or bought with ads on these 30 keywords?"

## Output Format

```
SHARE OF SHELF — [Marketplace, date, protocol]
| Keyword | Share | Organic | Paid | Weighted | In top 3 |
| Brand | Share | Weighted | Change vs last snapshot |
Priorities: [keywords to defend / win, with action]
```

## Quality Checks

- The collection protocol is stated and identical across snapshots.
- Sponsored and organic results are separated.
- Brand aliases are normalized; the seller's own listings are verified.
- Changes smaller than the normal variation between days are not presented as trends.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified**: counts from the collected result pages for that date and context.
- **Estimates**: keyword weights from search volume tools, inferred sales impact. Results are personalized and vary by location and time.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill share-of-shelf -g
```

## Usage

**Input:**
Brand name, product category, target marketplace(s), competitor brands

**Output:**
Share of shelf score, category positioning map, competitor visibility comparison, trend tracking framework

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up share of shelf for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce intelligence.*
