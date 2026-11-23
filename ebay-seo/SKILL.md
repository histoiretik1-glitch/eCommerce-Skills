---
name: ebay-seo
description: "Optimize eBay listings for Cassini search algorithm. Master item specifics, title optimization, category selection, and seller performance factors that drive search visibility. Use when the user asks for help improving eBay search ranking (Cassini), optimizing titles, item specifics or category selection."
---

# eBay SEO

Optimize eBay listings for Cassini search algorithm. Master item specifics, title optimization, category selection, and seller performance factors that drive search visibility.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Ranking eBay listings in Best Match search: titles, item specifics, category, identifiers.

Part of: eBay research, search and ads. For neighbouring jobs, use the matching skill instead:

- `ebay-seller-guide` — How to sell on eBay, from first listing to Top Rated Seller.
- `ebay-product-research` — Deciding what to sell on eBay from sold listings: sell-through rate, sold prices, net per sale.
- `ebay-advertising` — Paid eBay Promoted Listings (General, Priority, Offsite): ad rates, bids, break-even and ROAS.

<!-- role-and-scope:end -->

## Capabilities

- Cassini search algorithm ranking factors
- Title optimization: keyword placement and character limits
- Item specifics completion for maximum visibility
- Category and subcategory selection strategy
- Listing quality score improvement
- Seller performance metrics that affect search rank
- Best Match algorithm optimization
- Promoted Listings integration with organic SEO

## Platform Rules and Constraints

Rules as published in eBay Seller Center and eBay Help (search, listing and item specifics pages) at the last review of this skill (November 2026). Items marked **[check]** change from time to time: confirm them on the named eBay page before quoting them to a seller.

- **Title:** up to 80 characters on eBay.com **[check]** (Help > Listing titles). Write it for buyers: brand, model, product type, key attributes. No ALL CAPS, repeated words, "L@@K"-style filler, or brand names that are not the item: these fall under the *search and browse manipulation* policy.
- **Item specifics:** the listing form flags required and recommended specifics for the category. Missing required specifics block listing; recommended ones feed the search filters (Brand, Size, Color...). Choose values from eBay's dropdown where one exists: a free-text spelling may not match the filter.
- **Product identifiers:** new branded items in most categories need UPC/EAN/ISBN or Brand + MPN **[check]** (Help > Product identifiers). Use "Does not apply" only for items that really have none (handmade, vintage, unbranded).
- **Category:** list in the category that matches the item; listing in an unrelated category to gain exposure is a policy breach. Use eBay's suggested category and the category of comparable sold items.
- **Duplicate listings:** several identical fixed-price listings for the same item by one seller are not allowed (*duplicate listings policy*); use one listing with quantity or variations.
- **Best Match ranking (Cassini):** eBay publicly names relevance to the search, item specifics, price including shipping, shipping speed and cost, returns policy, listing quality and seller performance as factors. eBay does not publish weights: never present a factor weight as known.
- **Seller performance:** a *Below Standard* seller level reduces visibility in search (Seller Hub > Performance > Seller level).
- **Description:** no active content (JavaScript, Flash) in item descriptions; keep it mobile-readable. Keywords in the description do not replace keywords in the title.

## Data Needed

| Data | Where the seller finds it |
|------|---------------------------|
| Current title, category path, condition | The listing (Seller Hub > Listings > Active) |
| Item specifics filled vs recommended | Revise listing > Item specifics (required / recommended / additional) |
| Impressions, click-through rate, page views, sales conversion rate per listing | Seller Hub > Performance > Traffic (download the listing traffic report) |
| Buyer search terms | eBay search autocomplete, titles of sold listings (Sold items filter or Seller Hub > Research / Terapeak) |
| Price + shipping of comparable sold items | Sold items filter or Terapeak, last 90 days |
| Seller level and defect / late shipment rates | Seller Hub > Performance > Service metrics and Seller level |

## Workflow

1. **Diagnose with the traffic report.** For each listing compute impression click-through rate and sales conversion rate (formulas below). Many impressions but a low click-through rate points to title, main photo or price; few impressions points to relevance: category, item specifics, title keywords.
2. **Collect buyer keywords.** Type the product in eBay search and note autocomplete suggestions; read the titles of the 20 most recent sold listings for the same item and list the words most of them share (model numbers, compatibility, size, condition words).
3. **Confirm the category.** Search the main keyword, open the sold results and check which leaf category most sold items use. Move the listing if it sits elsewhere.
4. **Complete item specifics.** Fill every required and recommended specific with dropdown values; add additional specifics buyers filter on (compatibility, material, era). Run `title_check.py` to list empty recommended specifics.
5. **Rewrite the title.** Order: Brand + model / product line + product type + 2-4 key attributes (size, colour, material, compatibility) + condition qualifier if it matters (e.g. "Tested", "New Sealed"). Front-load the words buyers type first, use the characters available, remove repeated words and filler.
6. **Add product identifiers / catalog match.** Enter UPC/EAN or Brand + MPN; accept the eBay catalog product (ePID) if it matches exactly, so the listing appears on the product page.
7. **Check the offer factors.** Compare price + shipping with the median of comparable sold items (use `ebay-product-research`), set handling time and returns policy you can sustain, offer tracked shipping.
8. **Revise one element at a time and measure.** Log the date and the change, then compare 14 days before and 14 days after (impressions, click-through rate, conversion). Revert changes that do not help.

## Calculations and Tools

- **Impression click-through rate** = clicks from eBay search ÷ search impressions (as shown in the Traffic report).
- **Sales conversion rate** = quantity sold ÷ page views.
- **Specifics completion** = recommended specifics filled ÷ recommended specifics listed for the category.
- **Price position** = (your price + shipping) ÷ median sold total of comparable items; above 1.10 explains low conversion more often than keywords do (a working rule, not an eBay figure).

Title and specifics checker (length, missing buyer keywords, repeated words, ALL CAPS, filler, empty recommended specifics):

```bash
python3 scripts/title_check.py '{"title": "Canon AE-1 Program 35mm SLR Film Camera Body Black Tested", "keywords": ["canon ae-1", "35mm", "film camera"], "specifics": {"Brand": "Canon", "Model": "AE-1 Program", "Type": "SLR", "Color": ""}, "recommended_specifics": ["Brand", "Model", "Type", "Color", "Format"]}'
```

## Worked Example

*Illustrative example with invented figures, not real listing data.* A listing titled "VINTAGE CAMERA canon ae1 program WORKS GREAT!!" (46 characters) had 4,100 impressions, 0.6% click-through rate and 1 sale in 30 days.

- Checker output: missing keywords "35mm" and "film camera", ALL CAPS words, filler symbols, "Color" and "Format" specifics empty, 34 characters unused.
- Revised title: "Canon AE-1 Program 35mm SLR Film Camera Body Black Tested Working" (65 characters); Color = Black, Format = 35mm filled from the dropdown.
- What to report after 14 days: impressions, click-through rate and sales conversion before vs after, with dates. Do not promise a ranking change: Best Match weights are not public.

## Example Requests

- "My eBay listing for a Canon AE-1 gets impressions but almost no clicks. Rewrite the title and tell me which item specifics are missing."
- "Check these 10 eBay titles against the 80-character limit and the keywords buyers use for used iPhone 13 cases."
- "Which eBay category should I use for vintage Pyrex bowls, and which item specifics matter for search filters?"

## Output Format

1. Diagnosis table per listing: impressions, click-through rate, sales conversion rate, likely cause (relevance vs offer).
2. Revised title (with character count) and the keyword evidence behind each word.
3. Item specifics to fill: name, value from the dropdown, required/recommended.
4. Category recommendation with the evidence (category of comparable sold items).
5. Offer fixes (price vs sold median, shipping, returns) and a dated change log template for the 14-day before/after check.

## Quality Checks

- Title ≤ 80 characters (or the limit of the seller's eBay site), no repeated words, no filler, no brand that is not the item.
- Every keyword in the title is backed by sold-listing titles or autocomplete, not guessed.
- Item specific values match the dropdown spelling; no required specific empty.
- Category confirmed by comparable sold items, not by a guess.
- Recommendations never state a Best Match weight or a guaranteed rank.
- Only one change per listing per measurement window, so the effect can be attributed.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** the seller's Traffic report figures, sold-listing titles and prices observed on a stated date, item specifics shown in the seller's listing form.
- **Estimates:** expected effect of a title change, keyword popularity inferred from autocomplete, any industry click-through benchmark.
- eBay limits and policies above were reviewed in November 2026 from eBay's public help pages; items marked [check] must be re-confirmed before use.

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ebay-seo -g
```

## Usage

Ask your AI agent:

- "Optimize my eBay listing titles for better search ranking."
- "What item specifics should I fill in for electronics on eBay?"
- "How does eBay Cassini algorithm rank listings?"

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
