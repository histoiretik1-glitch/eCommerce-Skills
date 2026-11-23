---
name: ecommerce-video-marketing
description: "Create video marketing strategy for e-commerce brands. Product videos, unboxing, tutorials, UGC, live streams, and platform-specific video optimization for Amazon, TikTok, YouTube, and Instagram. Use when the user asks for help planning product videos, UGC, unboxing, tutorials or platform-specific video strategy (Amazon, TikTok, YouTube, Instagram)."
---

# E-Commerce Video Marketing

Create video marketing strategy for e-commerce brands. Product videos, unboxing, tutorials, UGC, live streams, and platform-specific video optimization for Amazon, TikTok, YouTube, and Instagram.

<!-- role-and-scope:start (generated from tools/skill_groups.json) -->
## Role and Scope

**This skill:** Overall video marketing strategy across channels.

Part of: Video commerce. For neighbouring jobs, use the matching skill instead:

- `shoppable-video` — Shoppable and live-shopping video with product tagging on several platforms.
- `tiktok-live-selling` — Planning and running TikTok Shop LIVE sessions.

<!-- role-and-scope:end -->

## Capabilities

- Video content strategy by funnel stage (awareness, consideration, purchase)
- Product demo and tutorial video frameworks
- UGC collection and repurposing workflow
- Platform-specific video specs and best practices
- Amazon product video and A+ content video
- Short-form video strategy (Reels, TikTok, Shorts)
- Video SEO: titles, descriptions, tags, thumbnails
- Video production workflow on a budget

## Principles and Constraints

Cross-channel video rules, as known at the last review of this skill (November 2026). Items marked **[check]** change often and must be confirmed on each platform's specs page.

- **Format per placement:** vertical 9:16 for TikTok, Reels, Shorts and Stories; 4:5 or 1:1 for social feeds; 16:9 for YouTube long-form and many site players. Keep text and key product shots inside the safe zones (platform UI covers the edges).
- **Sound-off by default:** most feed video starts muted; burn in captions and show the product in the first seconds.
- **Length limits** differ: YouTube Shorts up to 3 minutes **[check]**, TikTok uploads up to 60 minutes **[check]**, ad placements often perform best under 30 seconds.
- **Marketplace video:** Amazon lets brand-registered sellers add videos to listings and A+ content (review and content guidelines apply: no pricing, no off-Amazon links, no unverifiable claims) **[check]**; Walmart and other marketplaces have their own rich-media rules.
- **Rights:** written permission for UGC reuse and paid usage (duration, channels, whitelisting); commercially licensed music only (platform commercial music libraries for ads); release forms for people on camera.
- **Disclosure:** paid creator content must be labelled (#ad / platform paid-partnership tools) under FTC and EU/UK rules.
- **Scope:** this skill is the overall video strategy. LIVE selling is `tiktok-live-selling`; shoppable and tagged video is `shoppable-video`; short-video plans for TikTok Shop `tiktok-shop-content-strategy`; creator sourcing `influencer-outreach`.

## Data Needed

| Data | Where |
|------|-------|
| Products, key benefits, top objections and questions | Reviews, Q&A, support tickets |
| Channels and placements where video will run | Marketing plan |
| Existing video performance: impressions, 3-second views, ThruPlays/completions, CTR, conversions | Ad managers, YouTube/TikTok/Meta analytics |
| Product page performance with/without video | Store analytics, tests |
| Budget, in-house skills, UGC available and its rights status | Team |

## Workflow

1. **Map video jobs to the funnel:** awareness (hook-led short videos), consideration (demo, comparison, how-to, reviews), purchase (product page video, objection busters), post-purchase (setup/care tutorials that cut returns and tickets).
2. **Write a hook bank** from customer language: 20 opening lines (problem, result, surprising fact, "POV"), tested in the first 1–3 seconds.
3. **Script with a fixed structure:** hook (0–3 s), problem or desire, product in use, proof (result, review, test), offer and call to action; one message per video.
4. **Produce efficiently:** batch-shoot several hooks and endings per session; phone, natural light, external mic; capture B-roll for reuse.
5. **Source UGC and creators** with written usage rights; brief them with the hook bank and the must-show product moments.
6. **Adapt per placement:** aspect ratio, length, captions, safe zones, on-screen text; upload marketplace videos per their guidelines.
7. **Test systematically:** vary one element (hook, length, proof) per test; read hook rate and hold rate before CTR and CPA.
8. **Measure the business effect:** product page conversion with vs without video (test), return-rate change for tutorial videos, CPA by creative; retire fatigued creatives.

## Calculations and Tools

- **Hook rate** = 3-second views ÷ impressions; **hold rate** = ThruPlays (or 15-second views) ÷ 3-second views.
- **Cost per acquisition per creative** = spend ÷ conversions; **creative fatigue** when frequency rises and CTR falls by 30%+ from its first week (working rule).
- **Video page lift** = conversion of sessions that played the video vs a holdout without video (test, not correlation: buyers watch more videos).
- **Production cost per usable asset** = production spend ÷ videos published (all cuts and formats).
- **Rights calendar**: usage end date = start + licensed duration per creator asset.

## Worked Example

*Illustrative example with invented figures.* A water-bottle brand tests three hooks on the same 20-second demo in Meta ads, $300 each.

- Hook A "Still drinking lukewarm water at 3 pm?": 41,000 impressions, 12,300 3-second views (hook rate 30.0%), 2,950 ThruPlays (hold 24.0%), 19 purchases → CPA $15.79.
- Hook B (product name first): hook rate 17.5%, CPA $27.27. Hook C (temperature test): hook rate 26.2%, CPA $18.75.
- Decision: scale A, reuse C's temperature test as proof inside A; repeat the test with the winning hook on TikTok in 9:16 with native captions.

## Example Requests

- "Create a video marketing plan for my product launch across TikTok, Instagram, YouTube and Amazon."
- "What types of product videos convert best on Amazon and what are the content rules?"
- "Build a UGC video collection strategy with usage rights for my brand."

## Output Format

1. Funnel-to-video map with formats and placements.
2. Hook bank and 3–5 scripts using the fixed structure.
3. Production and UGC plan with rights checklist.
4. Placement spec sheet (ratio, length, captions, safe zones) per channel.
5. Test plan and creative scorecard (hook rate, hold rate, CTR, CPA, fatigue).

## Quality Checks

- Each video has one message and shows the product within the first seconds.
- Captions burned in; specs match each placement's current requirements.
- Usage rights, music licences and disclosures documented per asset.
- Creative decisions based on hook/hold/CPA from tests, not views alone.
- Marketplace videos follow the marketplace's content rules.

## Data Reliability

Label every figure in the deliverable as **[verified]** (with its source and date) or **[estimate]** (with the assumption behind it). Never present an estimate or a benchmark as the seller's own data.

- **Verified:** ad and video analytics for stated periods, test results.
- **Estimates:** expected hook rates or CPAs before tests, benchmark completion rates.
- Platform specs were reviewed in November 2026; confirm items marked [check].

## Installation

Part of the **`ecommerce-skills`** Claude Code plugin (all 162 skills). In Claude Code:

```
/plugin marketplace add histoiretik1-glitch/eCommerce-Skills
/plugin install ecommerce-skills@ecommerce-skills
```

This skill only, with the Skills CLI (Claude Code, Cursor, Codex and other agents):

```bash
npx skills add histoiretik1-glitch/eCommerce-Skills --skill ecommerce-video-marketing -g
```

## Usage

Ask your AI agent:

- "Create a video marketing plan for my product launch."
- "What types of product videos convert best on Amazon?"
- "Build a UGC video collection strategy for my brand."

---

*Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — AI-powered e-commerce tools for sellers worldwide.*
