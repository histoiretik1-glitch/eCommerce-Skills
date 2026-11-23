---
name: market-gap-analysis
description: "Identify underserved market gaps and unmet customer needs in e-commerce. Analyzes competitor blind spots, review pain points, search demand without adequate supply, and emerging customer segments. Use when a seller looks for an underserved niche, unmet customer needs or product ideas that competitors miss."
metadata:
  nexscope:
    emoji: "🎯"
    category: ecommerce
---

# Market Gap Analysis 🎯

Identify underserved market gaps and unmet customer needs in e-commerce. Analyzes competitor blind spots, review pain points, search demand without adequate supply, and emerging customer segments.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Finding underserved needs and niches that competitors miss.

Part of: Competitive visibility. For neighbouring jobs, use the matching skill instead:

- `share-of-shelf` — Measuring a brand's share of marketplace search results against competitors, by keyword and over time.
- `ecommerce-competitor-analysis` — Cross-platform competitor analysis: channel presence, offer, strategy and positioning.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill market-gap-analysis -g
```

## Usage

```
Find market gaps in the home office furniture category on Amazon. What are customers asking for that nobody is providing well?
```

## Capabilities

- Competitor coverage gap identification
- Review-based pain point extraction and opportunity mapping
- Search demand vs supply analysis
- Underserved customer segment identification
- Price gap analysis (price points with no quality options)
- Feature gap mapping across competitor products

## Principles and Constraints

Method rules for finding underserved needs on any marketplace or category, as known at the last review of this skill (November 2026).

- **A gap is demand without a good answer,** not just low competition: confirm buyers search for it or complain about its absence before calling it an opportunity.
- **Reviews are the best free evidence:** 2–3-star reviews describe what buyers wanted and did not get; 1-star reviews often describe defects or shipping issues (useful, but less about product design).
- **Use the channel's own signals:** marketplace search results count, best-seller ranks and their stability, review counts of top results, Q&A, autocomplete; Google Trends and keyword tools for off-marketplace demand. Third-party sales estimates are models: label them.
- **Check the reasons a gap exists:** regulations or certifications (e.g. children's products, electrical safety), patents, freight cost for bulky items, margins too thin; a gap can be a trap.
- **Respect intellectual property:** improving on a product idea is fine; copying protected designs, trademarks or patented features is not.
- **Scope:** this skill finds the gap. Competitor teardown is `ecommerce-competitor-analysis`; making your product different is `product-differentiation-amazon` (or its eBay, Shopify and TikTok variants); checking viability with numbers is `ecommerce-business-plan` (or `dropshipping-product-research` for dropshipping).

## Data Needed

| Data | Where |
|------|-------|
| Top 20–50 products in the category: price, rating, review count, rank, key features | Marketplace search and best-seller pages (date noted) |
| Reviews of the top products (especially 2–3 stars) and Q&A | Product pages, review export tools |
| Search demand for need-based queries | Autocomplete, keyword tools, Brand Analytics if available |
| Price distribution of products with good ratings | Same product sample |
| Community discussions | Reddit, forums, social comments |
| Regulatory and IP constraints for the category | Regulator pages, patent searches |

## Workflow

1. **Define the category and buyer** precisely (e.g. "standing desk converters for small apartments", not "office furniture").
2. **Sample the market:** top 30 products with price, rating, review count, rank and main features in one table.
3. **Mine reviews:** read or export 200–500 reviews (2–3 stars first), code each complaint or wish into themes (size, noise, assembly, durability, missing feature), count frequencies.
4. **Map features vs products:** a matrix of the top 10 products and the 10 most requested features; empty cells with high demand are feature gaps.
5. **Map price bands:** count products and average rating per price band; a band with demand but no product rated ≥ 4.3 is a price/quality gap.
6. **Check search demand** for the need-based phrases found in reviews (e.g. "quiet", "for small spaces") and how well current results match them.
7. **Screen each gap** for regulation, IP, logistics and margin risks.
8. **Score and rank gaps** with the opportunity score; write the top 3 as product briefs (target buyer, must-have features, price band, proof needed).

## Calculations and Tools

- **Theme frequency** = reviews mentioning a theme ÷ reviews read (per product and overall).
- **Unmet-need share** = mentions of a wish or complaint across the top 10 products ÷ their reviews read.
- **Price-band gap** = demand indicator in the band (sum of review counts or search volume) ÷ number of products rated ≥ 4.3 in the band.
- **Opportunity score** (this skill's formula, 0–100) = 40 × demand index + 35 × unmet-need share index + 25 × (1 − competition index), where each index is scaled 0–1 within the sample.
- **Entry barrier** = median review count of the top 10 (reviews needed to compete) and capital needed for the first order.

## Worked Example

*Illustrative example with invented figures.* Home-office standing desk converters, 30 products sampled, 400 reviews read (2–3 stars first).

- Themes: "wobbles when typing" 23% of reviews, "too heavy to lift" 17%, "too deep for small desks" 12%, "keyboard tray too low" 9%.
- Feature matrix: only 1 of the top 10 offers a depth under 50 cm, and it is rated 3.9.
- Price bands: $150–200 holds 9 products, 2 rated ≥ 4.3; $100–150 holds 12 products, 6 rated ≥ 4.3 → the gap is a compact, stable converter at $150–200.
- Screening: no category certification issue found; bulky shipping (dimensional weight) must be checked with `ecommerce-shipping-rates` before sourcing.

## Example Requests

- "Find market gaps in the home office furniture category on Amazon. What are customers asking for that nobody provides well?"
- "Analyse 300 reviews of the top 10 yoga mats and tell me which unmet needs could justify a new product."
- "Which price band in electric kettles has demand but no well-rated products?"

## Output Format

1. Market sample table (top products with price, rating, reviews, rank, features) with the collection date.
2. Review theme table with frequencies and example quotes.
3. Feature gap matrix and price-band table.
4. Risk screening per gap (regulation, IP, logistics, margin).
5. Ranked opportunities with scores and one-page product briefs.

## Quality Checks

- Category and buyer defined narrowly; sample and date stated.
- Review themes coded consistently; counts and example quotes given.
- Each gap backed by both complaint/wish evidence and demand evidence.
- Regulatory, IP and logistics risks screened before recommending.
- Third-party sales or volume estimates labelled with tool and date.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** observed prices, ratings, review counts and quoted reviews with collection date.
- **Estimates:** third-party sales and search volumes, opportunity scores, expected demand for a new product.
- Method reviewed in November 2026.

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
