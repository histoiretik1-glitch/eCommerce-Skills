---
name: shoppable-video
description: "Create and optimize shoppable video content for e-commerce. Strategy for TikTok Shop, Instagram Reels, YouTube Shorts, and Amazon Live with product tagging, CTAs, and conversion optimization. Use when the user asks for help creating shoppable videos or live shopping on TikTok Shop, Instagram Reels, YouTube Shorts or Amazon Live."
---

# Shoppable Video

Create and optimize shoppable video content for e-commerce. Strategy for TikTok Shop, Instagram Reels, YouTube Shorts, and Amazon Live with product tagging, CTAs, and conversion optimization.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Shoppable and live-shopping video with product tagging on several platforms.

Part of: Video commerce. For neighbouring jobs, use the matching skill instead:

- `ecommerce-video-marketing` — Overall video marketing strategy across channels.
- `tiktok-live-selling` — Planning and running TikTok Shop LIVE sessions.

<!-- role-and-scope:end -->

## Capabilities

- Shoppable video format selection by platform
- Product tagging and linking best practices
- Script frameworks for product demonstration videos
- Thumbnail and hook optimization for scroll-stopping
- CTA placement and conversion optimization
- Live shopping event planning and execution
- UGC shoppable content strategy
- Video analytics: view-to-purchase rate, engagement, ROAS

## Principles and Constraints

Rules for shoppable and live-shopping video across platforms, as known at the last review of this skill (November 2026). Platform programmes change often: items marked **[check]** must be confirmed in each platform's current help pages.

- **Tagging depends on a connected catalogue:** TikTok Shop video product links need a TikTok Shop and approved products; Instagram/Facebook product tags need a Meta catalogue and a commerce-eligible account **[check]**; YouTube Shopping needs a connected store or the YouTube Shopping affiliate programme with its eligibility rules **[check]**; on your own site, shoppable video apps (examples: Tolstoy, Firework, Videowise) link videos to product pages.
- **Price and stock shown must be accurate:** tagged products pull price and availability from the catalogue; sync errors create mismatches and policy issues.
- **Disclosure and claims:** creator and affiliate videos need disclosure; product claims follow advertising law and platform policies (no medical or "guaranteed" claims).
- **Live shopping events** run on platform tools (TikTok LIVE, YouTube Live with product shelves **[check]**) or site apps; each has moderation and prohibited-product rules.
- **Measure purchases, not just views:** view-to-purchase depends on attribution windows of each platform; compare platforms with the same metric definitions.
- **Scope:** this skill covers shoppable formats across platforms. TikTok Shop LIVE operations in detail are in `tiktok-live-selling`; overall video strategy `ecommerce-video-marketing`; TikTok Shop short-video planning `tiktok-shop-content-strategy`.

## Data Needed

| Data | Where |
|------|-------|
| Catalogue connection status per platform (store sync, approved products, errors) | Commerce Manager, TikTok Shop Seller Center, YouTube Studio, site app |
| Video library and rights status (own, creator, UGC) | Content team |
| Video metrics: views, product tag/link clicks, add to carts, purchases, revenue | Platform analytics, site app analytics |
| Product margins and AOV | Finance |
| Audience location and active hours | Platform analytics |

## Workflow

1. **Check eligibility and catalogue sync** per platform; fix disapproved or out-of-sync products first.
2. **Choose formats per platform:** short tagged videos (TikTok, Reels, Shorts), product carousels on site pages (PDP, homepage), scheduled live events.
3. **Script for the tag:** show the product in the first seconds, demonstrate one outcome, say the product name the tag will show, call to action that matches the tap ("tap the bag below").
4. **Tag correctly:** one to three products per video, the main product first, variants matching what is shown.
5. **Publish to own site too:** shoppable video on the PDP and collection pages, lightweight embeds that do not hurt LCP.
6. **Plan live events** (if used): product line-up, offers, host script, moderator, stock check; follow platform live rules.
7. **Measure per video and platform:** product click rate, click-to-purchase, revenue per 1,000 views; compare with untagged equivalents.
8. **Iterate:** reuse top videos as ads (with rights), retire low performers, refresh hooks monthly.

## Calculations and Tools

- **Product click rate** = product tag/link clicks ÷ views.
- **Click-to-purchase rate** = purchases ÷ product clicks.
- **View-to-purchase rate** = purchases ÷ views; **revenue per 1,000 views** = revenue ÷ views × 1,000.
- **Contribution per 1,000 views** = revenue per 1,000 views × contribution margin − content cost per 1,000 views.
- **On-site video lift** = conversion of PDP sessions with the shoppable player vs a holdout without it (test), checking page speed impact.

## Worked Example

*Illustrative example with invented figures.* A beauty brand posts the same 25-second serum demo, tagged, on TikTok and Instagram Reels.

- TikTok: 84,000 views, 2,100 product clicks (2.5%), 63 purchases (3.0% of clicks), $1,890 revenue → **$22.50 per 1,000 views**.
- Reels: 31,000 views, 400 clicks (1.3%), 9 purchases (2.3%), $270 → $8.71 per 1,000 views.
- On the PDP, the same video in a shoppable player is tested against a holdout for 3 weeks before rolling out.

## Example Requests

- "Create a shoppable video strategy for my beauty brand on TikTok, Instagram and my Shopify product pages."
- "What makes a high-converting product video for social commerce, and how should I tag products?"
- "Plan a live shopping event for my product launch on YouTube and TikTok."

## Output Format

1. Eligibility and catalogue status per platform with fixes.
2. Format plan per platform and page (with specs and tag rules).
3. Scripts with tag moments and CTAs.
4. Live event plan (if relevant).
5. Measurement table per video/platform: click rate, click-to-purchase, revenue and contribution per 1,000 views.

## Quality Checks

- Catalogues synced; tagged prices and stock correct.
- Product appears and is named in the first seconds; tag matches the variant shown.
- Rights and disclosures recorded for creator content.
- Platforms compared with the same metric definitions and periods.
- Site embeds tested for speed impact.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** platform analytics and site app data for stated dates.
- **Estimates:** expected click and purchase rates before posting, platform benchmark rates.
- Platform programmes were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill shoppable-video -g
```

## Usage

Ask your AI agent:

- "Create a shoppable video strategy for my beauty brand on TikTok."
- "What makes a high-converting product video for social commerce?"
- "Plan a live shopping event for my product launch."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
