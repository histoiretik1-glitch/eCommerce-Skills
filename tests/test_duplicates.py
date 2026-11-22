"""Duplicate detection and content preservation across the 162 skills (LOT 3)."""
import itertools
import json
import re
import subprocess
import sys
import unittest
from collections import Counter

from content_lines import candidate_lines
from helpers import GOLDEN, ROOT
from similarity import content_lines, cosine, description, tokens, vectors

REGISTRY = json.loads((ROOT / "tools" / "skill_groups.json").read_text(encoding="utf-8"))["groups"]
PLATFORMS = ("amazon", "ebay", "shopify", "tiktok", "walmart", "etsy", "woocommerce")

# Skills that still have almost no content of their own (template text only).
# This list may only shrink: enrich a skill, then remove it from here.
KNOWN_THIN = set()  # emptied in LOT 4 (was 16 skills in 1.3.0, 56 before LOT 3)
MIN_SPECIFIC_LINES = 8          # lines not found in 5+ other SKILL.md files
MAX_SHARED_SPECIFIC = 0.5        # share of specific lines two skills may have in common
MAX_GROUP_DESCRIPTION_SIM = 0.5  # TF-IDF cosine between descriptions of the same group


def family(name):
    """Platform variants of the same tool share a family (brand-protection-ebay ~ brand-protection-tiktok)."""
    return "-".join(w for w in name.split("-") if w not in PLATFORMS)


def load_texts():
    return {p.parent.name: p.read_text(encoding="utf-8") for p in ROOT.rglob("SKILL.md")
            if ".git" not in p.parts and "node_modules" not in p.parts}


TEXTS = load_texts()


def specific_lines():
    lines = {k: content_lines(v) for k, v in TEXTS.items()}
    spread = Counter(l for s in lines.values() for l in s)
    return {k: {l for l in v if spread[l] < 5} for k, v in lines.items()}


class Registry(unittest.TestCase):
    def test_members_exist_and_groups_have_several_members(self):
        for gid, group in REGISTRY.items():
            self.assertGreaterEqual(len(group["members"]), 2, gid)
            for name in group["members"]:
                self.assertIn(name, TEXTS, f"{gid}: unknown skill {name}")

    def test_each_skill_has_one_role(self):
        roles = {}
        for group in REGISTRY.values():
            for name, role in group["members"].items():
                self.assertEqual(roles.setdefault(name, role), role, f"{name} has two different roles")
        # Two different skills must not share the same role text
        dupes = [r for r, c in Counter(roles.values()).items() if c > 1]
        self.assertEqual(dupes, [], "identical roles for different skills")

    def test_role_and_scope_sections_up_to_date(self):
        r = subprocess.run([sys.executable, str(ROOT / "tools" / "apply_skill_groups.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)


class Duplicates(unittest.TestCase):
    def test_no_new_template_only_skill(self):
        spec = specific_lines()
        thin = {k for k, v in spec.items() if len(v) < MIN_SPECIFIC_LINES}
        self.assertEqual(sorted(thin - KNOWN_THIN), [],
                         "skill(s) with almost no content of their own (template text)")
        improved = sorted(KNOWN_THIN - thin)
        self.assertEqual(improved, [], "these skills now have content: remove them from KNOWN_THIN")

    def test_no_two_skills_share_most_of_their_content(self):
        spec = specific_lines()
        offenders = []
        for a, b in itertools.combinations(sorted(spec), 2):
            if family(a) == family(b) or not spec[a] or not spec[b]:
                continue
            ratio = len(spec[a] & spec[b]) / min(len(spec[a]), len(spec[b]))
            if ratio >= MAX_SHARED_SPECIFIC:
                offenders.append(f"{a} / {b}: {ratio:.0%} shared lines")
        self.assertEqual(offenders, [])

    def test_descriptions_distinct_within_groups(self):
        vec = vectors({k: description(v) for k, v in TEXTS.items()})
        too_close = []
        for gid, group in REGISTRY.items():
            for a, b in itertools.combinations(sorted(group["members"]), 2):
                sim = cosine(vec[a], vec[b])
                if sim >= MAX_GROUP_DESCRIPTION_SIM:
                    too_close.append(f"{gid}: {a} / {b} = {sim:.2f}")
        self.assertEqual(too_close, [], "descriptions too similar to tell the skills apart")


# Template sentences of the 1.2.0 "Nexscope format" skills; they vary only by category word, so the
# boilerplate filter (lines in 5+ files) misses them. They carry no skill-specific content and were
# replaced by real sections in LOT 4. Only lines matching this pattern may disappear.
REMOVED_TEMPLATE = re.compile(r"^generates actionable .+ frameworks based on your specific business context$")


class ContentPreserved(unittest.TestCase):
    def test_no_functional_line_lost_since_1_2_0(self):
        baseline = json.loads((GOLDEN / "content_baseline_1.2.0.json").read_text(encoding="utf-8"))
        self.assertEqual(set(baseline), set(TEXTS), "skill set changed")
        lost = {}
        for name, lines in baseline.items():
            now = set(candidate_lines(TEXTS[name]))
            missing = [l for l in lines if l not in now and not REMOVED_TEMPLATE.match(l)]
            if missing:
                lost[name] = missing[:3]
        self.assertEqual(lost, {}, "functional lines removed (list items, steps, table rows)")


# (request, expected skill): the expected skill must outrank every other member of its groups
GROUP_REQUESTS = [
    ("How do I open my first Etsy shop and what should I set up before launch?", "etsy-shop-setup"),
    ("Write an About section and banner idea for my Etsy shop brand", "etsy-shop-branding"),
    ("Should I open a second Etsy shop for a different product line?", "etsy-multi-shop"),
    ("Check my numbers for the Star Seller badge: message response and on-time shipping", "etsy-star-seller"),
    ("Explain my Etsy Stats traffic sources and conversion rate drop", "etsy-shop-analytics"),
    ("Score my Etsy listing SEO title tags and description", "etsy-seo"),
    ("What phrases do Etsy buyers search for my product? Find long-tail keywords", "etsy-keyword-research"),
    ("Write the 13 tags and attributes for this Etsy listing", "etsy-seo-tags"),
    ("Write the description text for my Etsy listing with materials and care", "etsy-product-description"),
    ("Plan the thumbnail and photos for my Etsy listing", "etsy-listing-photography"),
    ("Analyze competing Etsy shops in my niche and their reviews", "etsy-competitor-analysis"),
    ("How should I price my handmade items to cover Etsy fees and labor?", "etsy-pricing-strategy"),
    ("Set up Etsy shipping profiles and decide on free shipping", "etsy-shipping-strategy"),
    ("Etsy Ads daily budget and which listings to promote", "etsy-advertising"),
    ("Offsite Ads fee 15 percent opt out decision", "etsy-offsite-ads"),
    ("Pinterest and Instagram plan to drive traffic to my Etsy shop", "etsy-social-media-marketing"),
    ("Holiday calendar: when to list and make stock for Christmas on Etsy", "etsy-seasonal-strategy"),
    ("Get more honest Etsy reviews and reply to a bad review", "etsy-review-strategy"),
    ("Personalization field and proof process for custom Etsy orders", "etsy-custom-orders"),
    ("Sell printable digital downloads on Etsy: files and license", "etsy-digital-products"),
    ("Printify print on demand t-shirts on Etsy with production partner", "etsy-print-on-demand"),
    ("Where do I start to grow my Etsy business overall?", "etsy-seller-guide"),
    ("Which TikTok creator collaboration model fits our launch and how to split the creator budget?", "tiktok-influencer-marketing"),
    ("Hire TikTok creators for paid sponsored videos and negotiate their fees", "tiktok-creator-marketplace"),
    ("Set commission rates and open collaboration in the TikTok Shop affiliate program", "tiktok-shop-affiliate-program"),
    ("Tier my existing TikTok creator roster and track samples", "tiktok-shop-creator-management"),
    ("What do my Shopify Core Web Vitals LCP INP CLS scores mean?", "shopify-page-speed"),
    ("Give me a prioritized plan to make my slow Shopify store faster by removing apps", "shopify-speed-optimization"),
    ("Which Shopify theme should I choose and how do I clean up Liquid code?", "shopify-theme-optimization"),
    ("Configure Shop Pay and checkout extensions in the Shopify checkout", "shopify-checkout-customization"),
    ("Recover abandoned Shopify checkouts with email and SMS", "shopify-cart-abandonment"),
    ("Simplify the checkout of my WooCommerce site with fewer form fields", "ecommerce-checkout-optimization"),
    ("Connect my Shopify store to Merchant Center with the Google & YouTube app", "shopify-google-channel"),
    ("Structure Performance Max campaigns and ROAS targets", "google-shopping-optimization"),
    ("Fix product feed sync errors and missing SKUs across channels", "ecommerce-feed-management"),
    ("Review my existing landing page and tell me why it converts poorly", "ecommerce-landing-page"),
    ("Create a new Shopify page for our product launch campaign", "shopify-landing-page-builder"),
    ("Analyze our product reviews for pain points and feature requests", "product-review-analysis"),
    ("Combine survey answers, support tickets and return reasons into improvement priorities", "customer-feedback-analysis"),
    ("Alert me when a new negative review arrives and set a response workflow", "review-monitoring"),
    ("Our brand reputation is under attack, plan crisis communication", "online-reputation-management"),
    ("Set reorder points and safety stock to avoid stock-outs", "restock-alert"),
    ("Manage stock across Shopify locations and transfers", "shopify-inventory-management"),
    ("Improve our FBA IPI score and warehouse storage costs", "warehouse-optimization"),
    ("Which channels should we sell on and keep one consistent brand experience?", "omnichannel-ecommerce"),
    ("Sync inventory and route orders across Amazon, eBay and Shopify", "multichannel-ecommerce"),
    ("Design the subscription offer and pricing tiers for our coffee brand", "ecommerce-subscription-model"),
    ("Install a subscription app and selling plans on Shopify", "shopify-subscription-setup"),
    ("Write a full email program with copy and an annual campaign calendar", "ecommerce-email-marketing-builder"),
    ("Turn on the welcome and abandoned checkout automations in Shopify Email", "shopify-email-flows"),
    ("Script checks of add to cart and checkout journeys every 10 minutes with alerts", "synthetic-monitoring"),
    ("Our Amazon order webhook to the ERP fails; monitor API error rates and the SLO error budget", "api-monitoring"),
    ("Check SSL certificate expiry and DMARC SPF DKIM records for our domain", "domain-monitoring"),
    ("Detect unauthorized file changes and card skimmer scripts on our Magento checkout", "file-integrity-monitoring"),
    ("Screenshot comparison to catch layout breakages after a theme update", "visual-regression-testing"),
    ("Test translations, currency formats and VAT display for our German market", "localization-testing"),
    ("Status page with incident templates to tell customers checkout is down", "public-status-page"),
    ("What share of marketplace search results does our brand have versus competitors on these keywords?", "share-of-shelf"),
    ("Draft a minimum advertised price policy and check reseller prices for violations", "minimum-advertised-price"),
    ("Compare my Walmart landed prices with other sellers and set Repricer rules", "walmart-price-tracker"),
]


class GroupRouting(unittest.TestCase):
    """Heuristic: the intended skill must rank above its group neighbours for a typical request."""

    def test_intended_skill_beats_its_neighbours(self):
        docs = {k: tokens(description(v)) + tokens(k.replace("-", " ")) * 2 for k, v in TEXTS.items()}
        vec = vectors({k: " ".join(v) for k, v in docs.items()})
        neighbours = {}
        for group in REGISTRY.values():
            for name in group["members"]:
                neighbours.setdefault(name, set()).update(m for m in group["members"] if m != name)
        failures = []
        for request, expected in GROUP_REQUESTS:
            self.assertIn(expected, neighbours, expected)
            q = vectors({"q": request, **{k: " ".join(v) for k, v in docs.items()}})["q"]
            score = lambda s: cosine(q, vec[s])
            beaten = sorted((n for n in neighbours[expected] if score(n) >= score(expected)), key=score, reverse=True)
            if beaten:
                failures.append(f"{request!r}: {expected} ({score(expected):.2f}) beaten by {beaten[:3]}")
        self.assertEqual(failures, [], "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
