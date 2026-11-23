---
name: ecommerce-branding
description: "Build and strengthen your e-commerce brand identity. Brand positioning, messaging, visual identity guidelines, and brand consistency across sales channels and marketing touchpoints. Use when a store owner asks how to position their brand, define brand voice and messaging, create visual identity guidelines or keep branding consistent across channels."
metadata:
  nexscope:
    emoji: "🎨"
    category: ecommerce
---

# E-Commerce Branding 🎨

Build and strengthen your e-commerce brand identity. Brand positioning, messaging, visual identity guidelines, and brand consistency across sales channels and marketing touchpoints.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Brand positioning, voice, visual identity and trademark clearance across channels.

Part of: Brand and business planning. For neighbouring jobs, use the matching skill instead:

- `ecommerce-business-plan` — Business plan for a new online business: market sizing, unit economics, cash flow.
- `ecommerce-growth-strategy` — Growth priorities for an existing business: unit economics, growth levers and roadmap.
- `tiktok-shop-branding` — Building a recognizable brand on TikTok: identity, content pillars, community.
- `etsy-shop-branding` — Shop identity on Etsy: name, banner, logo, About section, photo style and packaging.

<!-- role-and-scope:end -->

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-branding -g
```

## Usage

```
Help me build a brand identity for my new eco-friendly cleaning products line. I want to sell on Amazon and Shopify. Target: environmentally conscious millennials.
```

## Capabilities

- Brand positioning statement development
- Target audience persona creation
- Brand voice and messaging framework
- Visual identity guidelines (colors, typography, imagery style)
- Brand consistency audit across channels
- Packaging and unboxing experience design
- Brand story crafting for About pages and A+ content

## Principles and Constraints

Cross-channel branding rules, as known at the last review of this skill (November 2026). Items marked **[check]** must be confirmed with the trademark office, regulator or marketplace.

- **Clear the name before designing anything:** search the trademark registers of each selling country (USPTO trademark search, EUIPO eSearch/TMview, UKIPO) in the relevant classes, plus marketplace and domain availability. A logo is worthless if the name must change.
- **Marketplace brand programmes need a trademark:** Amazon Brand Registry accepts registered or, in many countries, pending text or image marks **[check]**; Walmart Brand Portal and TikTok Shop brand authorization have similar requirements. The brand name on packaging must match the mark.
- **Claims must be substantiated:** environmental claims fall under the FTC Green Guides in the US and the EU rules on empowering consumers for the green transition (generic claims like "eco-friendly" restricted from 2026 **[check]**); "natural", "organic", "clinically proven" need evidence or certification.
- **One identity, adapted formats:** the positioning and voice stay identical everywhere; assets are adapted to each channel's format (marketplace main images on white, A+ content modules, social video).
- **Positioning comes before visuals:** a brand is the promise and the proof; colours and logo carry it, they do not create it.
- **Neighbouring skills:** TikTok-native brand building `tiktok-shop-branding`, Etsy shop identity `etsy-shop-branding`, product-level differentiation `product-differentiation-shopify` (Amazon, eBay and TikTok variants exist).

## Data Needed

| Data | Where |
|------|-------|
| Target customer: needs, language, alternatives they use | Customer interviews, reviews of competing products, surveys |
| Competitor brands: promise, price position, visual codes | Competitor stores and marketplace listings |
| Product proof points: materials, tests, certifications, origin | Supplier documents, lab reports |
| Price position vs category | `competitor-price-analysis` or own research |
| Trademark search results and domain/handle availability | Trademark office databases, registrars, social platforms |
| Current assets on each channel | Store, marketplace listings, social profiles, packaging |

## Workflow

1. **Collect customer language:** read 100+ reviews of competing products (3-star reviews show unmet needs) and note recurring words, frustrations and desired outcomes.
2. **Map competitors** on two axes that matter to buyers (e.g. price and performance, or "clinical" vs "natural") and find an open, credible position.
3. **Write the positioning statement:** For [target] who [need], [brand] is the [category] that [main benefit] because [proof]. Unlike [alternative], we [differentiator].
4. **Define the voice:** 3–4 traits with "we are / we are not" pairs and example sentences for a product title, a customer reply and a social caption.
5. **Clear the name and mark,** then design the visual identity: logo variations, palette (with contrast checked for accessibility), typography, photography style, packaging rules.
6. **Write the brand story** in three lengths (one line, one paragraph, About page) using real proof points only.
7. **Roll out by channel:** marketplace listings and A+ content, store pages, social bios, packaging and inserts; keep a brand guide with do/don't examples.
8. **Audit consistency** every quarter with the scorecard below and track brand signals (branded search, direct traffic, repeat rate, price premium).

## Calculations and Tools

- **Consistency score** = checks passed ÷ checks applied across channels (same name and logo, same promise line, same voice, compliant claims, image style respected).
- **Branded search share** = searches for the brand name ÷ (brand + top generic category terms) in the same tool and period.
- **Price premium** = your average selling price ÷ category median price − 1; a brand that holds a premium with stable conversion is working.
- **Direct and returning traffic share** = (direct + returning sessions) ÷ sessions, as a trend.
- **Review theme match** = share of reviews mentioning the promised benefit (a proof that the positioning is felt).

## Worked Example

*Illustrative example with invented details.* A refillable cleaning-concentrate brand selling on Amazon and Shopify, aimed at renters in small apartments.

- Reviews of competing sprays repeat "strong smell", "plastic waste", "takes space under the sink".
- Positioning: "For renters who clean small homes, [Brand] is the refill cleaning system that fits in one drawer and leaves no chemical smell, because each tablet makes a full bottle. Unlike supermarket sprays, you buy the bottle once."
- Claim check: "plastic-free" rejected (bottle is plastic); "reusable bottle, 90% less packaging per refill" kept with the packaging weight calculation filed as proof.
- First audit: 7 of 10 checks passed (70%); fixes: Amazon title uses an old name, Instagram voice too technical.

## Example Requests

- "Build a brand identity for my eco cleaning products for Amazon and Shopify, aimed at environmentally conscious millennials."
- "Audit how consistent my brand is across my Shopify store, Amazon listings and Instagram, and give me a fix list."
- "Write a positioning statement and brand voice guide for my premium dog accessories brand."

## Output Format

1. Customer insight summary with quoted review language.
2. Competitor map and chosen position.
3. Positioning statement, voice guide (traits, do/don't, sample lines) and brand story in three lengths.
4. Visual identity brief (logo uses, palette with contrast ratios, typography, photo style, packaging).
5. Trademark and claim checklist with status per country and claim.
6. Channel roll-out plan and quarterly consistency scorecard.

## Quality Checks

- Positioning backed by customer language and a real proof point.
- Trademark search done in each selling country before any design work is approved.
- Every product claim has evidence on file; no generic green claims.
- Palette passes WCAG contrast for text; assets adapted to each channel's rules.
- Scorecard uses the same checks each quarter.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** quoted reviews with source, trademark search results with date, the brand's own sales and search data.
- **Estimates:** expected price premium, branded search growth, perception of a new name.
- Trademark and claims rules were reviewed in November 2026; confirm items marked [check] (this is not legal advice).

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
