#!/usr/bin/env python3
"""
Brand Protection Templates - Complaint & Legal Templates
Brand ProtectionTemplate - Complaint and legal document templates

Packagecontain:
- Brand Registry Complaint Templates
- Cease & Desist StopInfringementLetter
- Test Buy Operation guide
- MAP Violation notice
- LegalLetterTemplate

Shared by brand-protection-{amazon,ebay,shopify,tiktok,walmart}. The file is
identical in every skill folder; the platform comes from --platform=<name> or,
by default, from the skill folder name. Amazon output is unchanged.

Version: 2.0.0
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from datetime import datetime

SUPPORTED_PLATFORMS = ("amazon", "ebay", "shopify", "tiktok", "walmart")

# Enforcement channel per platform. Program names are stable; exact forms and
# URLs move, so the steps tell the seller where to look rather than hard-coding links.
PLATFORM_PROFILES = {
    "amazon": {
        "name": "Amazon", "marketplace": "Amazon.com", "id_label": "ASIN",
        "program": "Amazon Brand Registry",
    },
    "ebay": {
        "name": "eBay", "marketplace": "eBay", "id_label": "eBay Item ID",
        "program": "eBay VeRO (Verified Rights Owner) Program",
        "report": "VeRO Notice of Claimed Infringement (NOCI)",
        "policy": "eBay's VeRO and counterfeit item policies",
        "message": "eBay messaging (Contact seller)",
        "steps": [
            "Join the eBay VeRO Program as the rights owner (one-time, requires proof of IP ownership)",
            "Open the VeRO reporting tool / NOCI form from the VeRO Program page in eBay Help",
            "Select the reason code (e.g. counterfeit, trademark in listing, unauthorized image use)",
            "Enter each eBay Item ID and paste the complaint text below",
            "Submit and keep the reference number; eBay usually removes listings within days",
        ],
        "buyer": "Use a separate eBay buyer account (not linked to your seller account)",
    },
    "shopify": {
        "name": "Shopify", "marketplace": "a Shopify-hosted online store", "id_label": "Store / product URL",
        "program": "Shopify intellectual property infringement report",
        "report": "IP infringement report to Shopify + DMCA / trademark notice to the store's host and registrar",
        "policy": "Shopify's Acceptable Use Policy and intellectual property policies",
        "message": "the store's contact form or published email",
        "steps": [
            "Confirm the store runs on Shopify (e.g. myshopify.com domain, Shopify checkout)",
            "Open Shopify's 'report intellectual property infringement' form from the Shopify Legal / Help Center pages",
            "Choose trademark or copyright, enter the store URL and each infringing product URL",
            "Paste the complaint text below and attach proof of your rights",
            "In parallel: send a DMCA notice (copyright) to the domain registrar, and report ads to Meta/Google if the store advertises",
        ],
        "buyer": "Order with a personal email and card not linked to your brand",
    },
    "tiktok": {
        "name": "TikTok Shop", "marketplace": "TikTok Shop", "id_label": "TikTok Shop Product ID",
        "program": "TikTok Shop Intellectual Property Protection Center (IPPC)",
        "report": "IP infringement report in the TikTok Shop IP Protection Center",
        "policy": "TikTok Shop's Intellectual Property Protection Policy and prohibited products policy",
        "message": "TikTok Shop chat with the seller",
        "steps": [
            "Register your brand and upload trademark certificates in the TikTok Shop IP Protection Center",
            "Create an infringement report: choose trademark, copyright or patent",
            "Add each Product ID (and LIVE or video links if the infringement is in content)",
            "Paste the complaint text below and upload evidence",
            "Track the case in the IP Protection Center and reply to any seller counter-notice",
        ],
        "buyer": "Use a separate TikTok buyer account (not linked to your shop)",
    },
    "walmart": {
        "name": "Walmart", "marketplace": "Walmart Marketplace (Walmart.com)", "id_label": "Walmart Item ID",
        "program": "Walmart Brand Portal",
        "report": "IP claim in Walmart Brand Portal (or Walmart's infringement report form)",
        "policy": "Walmart Marketplace's Intellectual Property and Prohibited Products policies",
        "message": "Walmart's seller contact options (if available)",
        "steps": [
            "Enroll in Walmart Brand Portal with your registered trademark",
            "Open 'Report infringement' and choose the claim type (counterfeit, trademark, copyright)",
            "Enter each Walmart Item ID and seller name",
            "Paste the complaint text below and attach evidence",
            "Submit and follow the case in Brand Portal",
        ],
        "buyer": "Use a separate Walmart.com customer account (not linked to your seller account)",
    },
}


def detect_platform(default: str = "amazon") -> str:
    """Platform implied by the skill folder name (brand-protection-<platform>)."""
    folder = Path(__file__).resolve().parent.parent.name.lower()
    for platform in SUPPORTED_PLATFORMS:
        if folder.endswith("-" + platform):
            return platform
    return default


def adapt_to_platform(text: str, platform: str) -> str:
    """Rewrite Amazon-specific wording of a template for another platform."""
    if platform == "amazon":
        return text
    pr = PLATFORM_PROFILES[platform]
    replacements = [
        ("on Amazon.com, specifically on ASIN:", f"on {pr['marketplace']}, specifically on {pr['id_label']}:"),
        ("Violation of Amazon's Anti-Counterfeiting Policy", f"Violation of {pr['policy']}"),
        ("Report to Amazon Brand Registry for listing removal", f"Report via {pr['report']} for listing removal"),
        ("Send via Amazon Buyer-Seller Messaging (if available)", f"Send via {pr['message']}"),
        ("Create a separate Amazon buyer account (not linked to seller account)", pr["buyer"]),
        ("Submit via Brand Registry", f"Submit via {pr['program']}"),
        ("Amazon review period", f"{pr['name']} review period"),
        ("Report to Amazon for policy violation", "Notify the marketplace / remove the reseller from your authorized list"),
        ("| Product | ASIN |", f"| Product | {pr['id_label']} |"),
        ("Amazon", pr["name"]),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


@dataclass
class ComplaintInfo:
    """ComplaintInformation"""
    brand_name: str
    trademark_number: Optional[str] = None
    asin: str = ""
    seller_name: str = ""
    seller_id: str = ""
    violation_type: str = ""
    evidence: str = ""
    contact_email: str = ""
    company_name: str = ""


# ============================================================
# Complaint Templates
# ============================================================

def generate_brand_registry_complaint(info: ComplaintInfo) -> str:
    """Generate Brand Registry Complaint Templates"""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 BRAND REGISTRY COMPLAINT TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Platform**: Amazon Brand Registry Portal
**URL**: https://brandregistry.amazon.com/

---

## Report Details

**Brand Name**: {info.brand_name}
**Trademark Number**: {info.trademark_number or "N/A"}
**ASIN**: {info.asin}
**Infringing Seller**: {info.seller_name} ({info.seller_id})
**Violation Type**: {info.violation_type}

---

## Complaint Text (Copy & Paste)

```
I am the brand owner of {info.brand_name} (Trademark #{info.trademark_number or "[YOUR TRADEMARK NUMBER]"}).

The seller "{info.seller_name}" (Seller ID: {info.seller_id}) is selling unauthorized/counterfeit products on ASIN {info.asin}.

Evidence:
{info.evidence or "[Describe your evidence here - screenshots, test buy results, etc.]"}

This seller is NOT an authorized reseller of our products. We request immediate removal of this seller from our listing.

Contact: {info.contact_email or "[YOUR EMAIL]"}
Company: {info.company_name or "[YOUR COMPANY NAME]"}
```

---

## Steps to Submit

1. Log into Brand Registry: https://brandregistry.amazon.com/
2. Click "Report a Violation"
3. Select violation type
4. Enter ASIN and seller information
5. Paste complaint text above
6. Upload evidence (screenshots, invoices, test buy photos)
7. Submit and note case ID

---

## Evidence Checklist

☐ Screenshots of listing showing unauthorized seller
☐ Invoice/order confirmation from test buy
☐ Photos comparing authentic vs suspected counterfeit
☐ Trademark registration certificate
☐ Authorization letter (showing seller is NOT authorized)
"""


def generate_cease_desist(info: ComplaintInfo) -> str:
    """GenerateStopInfringementLetterTemplate"""
    today = datetime.now().strftime("%B %d, %Y")
    
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 CEASE AND DESIST LETTER TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Date**: {today}

---

**CEASE AND DESIST NOTICE**

To: {info.seller_name}
Seller ID: {info.seller_id}
Re: Unauthorized Sale of {info.brand_name} Products

---

Dear {info.seller_name},

This letter serves as formal notice that you are engaging in unauthorized sale of products bearing the {info.brand_name}® trademark (Registration No. {info.trademark_number or "[TRADEMARK NUMBER]"}) on Amazon.com, specifically on ASIN: {info.asin}.

**YOU ARE NOT AN AUTHORIZED RESELLER** of {info.brand_name} products. Your unauthorized sale of these products constitutes:

1. Trademark infringement under 15 U.S.C. § 1114
2. False designation of origin under 15 U.S.C. § 1125(a)
3. Violation of Amazon's Anti-Counterfeiting Policy

**DEMAND**

We hereby demand that you:

1. Immediately cease and desist all sales of {info.brand_name} products
2. Remove all {info.brand_name} product listings from your seller account
3. Provide a written confirmation of compliance within 5 business days

**CONSEQUENCES OF NON-COMPLIANCE**

Failure to comply with this demand will result in:
- Report to Amazon Brand Registry for listing removal
- Legal action seeking injunctive relief and monetary damages
- Report to law enforcement if counterfeit goods are involved

This letter is not intended to be a complete statement of the facts or law applicable to this matter, and nothing herein should be construed as a waiver of any rights or remedies.

Sincerely,

{info.company_name or "[YOUR COMPANY NAME]"}
{info.contact_email or "[YOUR EMAIL]"}

---

## Sending Instructions

1. Send via Amazon Buyer-Seller Messaging (if available)
2. Send via seller's contact email (find in storefront)
3. Keep copies of all correspondence
4. Set 5-day deadline for response
5. Escalate to legal action if no response
"""


def generate_test_buy_guide() -> str:
    """Generate Test Buy Operation guide"""
    return """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 TEST BUY PROCEDURE GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Purpose

Test Buy is the process of purchasing products from suspected counterfeit/unauthorized sellers to collect physical evidence for your complaint.

---

## Step-by-Step Process

### 1. Preparation

☐ Create a separate Amazon buyer account (not linked to seller account)
☐ Use a different shipping address if possible
☐ Prepare camera for documentation
☐ Have authentic product ready for comparison

### 2. Purchase

☐ Select the suspected seller's offer (not Buy Box)
☐ Screenshot the product page showing seller name and price
☐ Screenshot checkout page with seller info
☐ Complete purchase and save order confirmation
☐ Note Order ID: ________________

### 3. Documentation Upon Arrival

☐ Photograph unopened package (showing shipping label)
☐ Video record unboxing process
☐ Photograph product from multiple angles
☐ Compare with authentic product side-by-side:
   - Packaging differences
   - Label/printing quality
   - Product quality/finish
   - Weight comparison
   - Serial number verification
☐ Keep all packaging materials

### 4. Evidence Organization

Create folder with:
```
test_buy_evidence/
├── 01_listing_screenshots/
├── 02_order_confirmation/
├── 03_package_photos/
├── 04_unboxing_video/
├── 05_product_comparison/
└── 06_notes.txt
```

### 5. Submit Complaint

☐ Compile all evidence
☐ Write detailed complaint (use template)
☐ Submit via Brand Registry
☐ Include Order ID in complaint
☐ Upload photos/video

---

## Evidence Checklist

**Screenshots**
☐ Listing page with seller
☐ Seller storefront
☐ Order confirmation
☐ Shipping confirmation
☐ Delivery confirmation

**Photos**
☐ Package exterior (4+ angles)
☐ Shipping label close-up
☐ Product in packaging
☐ Product removed
☐ Side-by-side with authentic
☐ Close-up of differences

**Documents**
☐ Invoice from test buy
☐ Authentication certificate (if available)
☐ Trademark registration

---

## Timeline

Day 1: Place order
Day 3-7: Receive package
Day 7-8: Document and compare
Day 8-10: Compile and submit complaint
Day 10-21: Amazon review period

---

## Cost Tracking

| Item | Cost |
|------|------|
| Test Buy Product | $_____ |
| Shipping | $_____ |
| Return Shipping | $_____ |
| Total | $_____ |

*Note: May be recoverable in legal action*
"""


def generate_map_violation_notice(info: ComplaintInfo, violation_price: float, map_price: float) -> str:
    """Generate MAP Violation notice"""
    today = datetime.now().strftime("%B %d, %Y")
    discount = (map_price - violation_price) / map_price * 100
    
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 MAP VIOLATION NOTICE TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Date**: {today}

---

**MINIMUM ADVERTISED PRICE (MAP) VIOLATION NOTICE**

To: {info.seller_name}
Re: MAP Policy Violation - {info.brand_name}

---

Dear {info.seller_name},

This notice is to inform you that your current advertised price for {info.brand_name} products violates our Minimum Advertised Price (MAP) policy.

**Violation Details:**

| Product | ASIN | Your Price | MAP Price | Violation |
|---------|------|------------|-----------|-----------|
| {info.brand_name} | {info.asin} | ${violation_price:.2f} | ${map_price:.2f} | -{discount:.1f}% |

**MAP Policy Terms:**

As an authorized/unauthorized reseller of {info.brand_name} products, you are required to maintain advertised prices at or above the Minimum Advertised Price. This policy ensures:

- Fair competition among resellers
- Brand value protection
- Quality customer experience

**Required Action:**

Please adjust your advertised price to ${map_price:.2f} or higher within **48 hours** of receiving this notice.

**Consequences of Non-Compliance:**

Continued violation of our MAP policy may result in:
- Removal from authorized reseller program
- Report to Amazon for policy violation
- Supply chain restrictions

Please confirm compliance by replying to this notice.

Sincerely,
{info.company_name or "[YOUR COMPANY NAME]"}
{info.contact_email or "[YOUR EMAIL]"}
"""


# ============================================================
#  in textTemplate
# ============================================================

def generate_brand_registry_complaint_zh(info: ComplaintInfo) -> str:
    """Generate Brand Registry Complaint Templates ( in text)"""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 BRAND REGISTRY Complaint Templates
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Platform**: Amazon Brand Registry Portal
**URL**: https://brandregistry.amazon.com/

---

## ComplaintInformation

**BrandName**: {info.brand_name}
**TrademarkRegisternumber**: {info.trademark_number or "N/A"}
**ASIN**: {info.asin}
**InfringementSeller**: {info.seller_name} ({info.seller_id})
**InfringementCategoryType**: {info.violation_type}

---

## ComplaintText (CopyPaste)

```
I is  {info.brand_name} BrandOwner (TrademarkRegisternumber: {info.trademark_number or "[youTrademarknumber]"})。

Seller "{info.seller_name}" (Seller ID: {info.seller_id}) positive in  ASIN {info.asin} Selling unauthorized on/CounterfeitProduct。

Evidence:
{info.evidence or "[Describe your evidence here - Screenshot、TestPurchaseResult etc]"}

 should Sellernot is WeProductAuthorized distributor of。WeRequestImmediately will  this Seller from We Listing  in Remove。

Contact info: {info.contact_email or "[Your email]"}
CompanyName: {info.company_name or "[youCompanyname]"}
```

---

## SubmitStep

1. Login Brand Registry: https://brandregistry.amazon.com/
2. Click "Report a Violation" (ReportInfringement)
3. ChoiceInfringementCategoryType
4. Input ASIN AndSellerInformation
5. PasteAboveComplaintText
6. UploadEvidence (Screenshot、Invoice、Test Buy Photo)
7. SubmitandRecord Case ID

---

## EvidenceList

☐ Show notAuthorizedSeller Listing Screenshot
☐ Test Buy Invoice/OrderConfirm
☐ Authentic vs suspected counterfeitComparisonPhoto
☐ Trademark registration certificate
☐ Authorizedbook (Proof should SellerNot obtainedAuthorized)
"""


def generate_test_buy_guide_zh() -> str:
    """Generate Test Buy Operation guide ( in text)"""
    return """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 TEST BUY Operation guide
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## item

Test Buy (TestPurchase) Is fromSuspiciousCounterfeit/notAuthorizedSeller at PurchaseProduct，Process of collecting physical evidence for complaint。

---

## Operation process

### 1. Preparation work

☐ CreateIndependent Amazon BuyerAccount (not need  and SellerAccountAssociate)
☐ Use different deliveryAddress
☐ Prepare camera for recording
☐ Prepare authentic product forComparison

### 2. Purchase

☐ ChoiceSuspiciousSellerQuote (not need select Buy Box)
☐ ScreenshotProductPage，DisplaySellerNameAndPrice
☐ ScreenshotSettlementPage，PackagecontainSellerInformation
☐ CompletePurchaseandSaveOrderConfirm
☐ RecordOrdernumber: ________________

### 3. Receive after Record

☐ Photo of unopened package (Show shipping label)
☐ Video record unboxing process
☐  many angleDegreePhotoProduct
☐  and AuthenticSide by sideComparison:
   - PackagingDifference
   - Tag/Print quality
   - ProductQuality/Workmanship
   -  heavy quantityComparison
   - Serial number verification
☐ Keep all packaging materials

### 4. EvidenceOrganize

CreateFolder:
```
test_buy_Evidence/
├── 01_listingScreenshot/
├── 02_OrderConfirm/
├── 03_Package photo/
├── 04_UnboxingVideo/
├── 05_ProductComparison/
└── 06_Notes.txt
```

### 5. SubmitComplaint

☐ Organize all evidence
☐ Write detailed complaint (UseTemplate)
☐ Pass Brand Registry Submit
☐ Include in complaintOrdernumber
☐ Upload photo/Video

---

## Timeline

number 1 days:  below single
number 3-7 days: Receive
number 7-8 days: RecordandComparison
number 8-10 days: Organize and submit complaint
number 10-21 days: Amazon ReviewPeriod

---

## CostTrack

| Itemitem | Fee |
|------|------|
| Test Buy Product | $_____ |
| Shipping | $_____ |
| ReturnShipping | $_____ |
| Total | $_____ |

*note: Can be recovered in legal proceedings*
"""


def generate_platform_complaint(info: ComplaintInfo, platform: str = "amazon") -> str:
    """Complaint template for the platform's own enforcement channel."""
    if platform == "amazon":
        return generate_brand_registry_complaint(info)
    pr = PLATFORM_PROFILES[platform]
    steps = "\n".join(f"{i}. {s}" for i, s in enumerate(pr["steps"], 1))
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 {pr['name'].upper()} IP COMPLAINT TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Platform**: {pr['program']}
**Channel**: {pr['report']}

---

## Report Details

**Brand Name**: {info.brand_name}
**Trademark Number**: {info.trademark_number or "N/A"}
**{pr['id_label']}**: {info.asin}
**Infringing Seller / Store**: {info.seller_name} ({info.seller_id})
**Violation Type**: {info.violation_type}

---

## Complaint Text (Copy & Paste)

```
I am the owner of the {info.brand_name} trademark (Registration #{info.trademark_number or "[YOUR TRADEMARK NUMBER]"}).

The seller "{info.seller_name}" ({info.seller_id}) is offering unauthorized/counterfeit {info.brand_name} products on {pr['marketplace']} ({pr['id_label']}: {info.asin}).

Evidence:
{info.evidence or "[Describe your evidence here - screenshots, test buy results, etc.]"}

This seller is NOT authorized to sell our products or use our trademark. Under {pr['policy']}, we request removal of the infringing listing(s).

Contact: {info.contact_email or "[YOUR EMAIL]"}
Company: {info.company_name or "[YOUR COMPANY NAME]"}
```

---

## Steps to Submit

{steps}

---

## Evidence Checklist

☐ Screenshots of the listing/store with URL and date visible
☐ Invoice/order confirmation from test buy
☐ Photos comparing authentic vs suspected counterfeit
☐ Trademark registration certificate
☐ Authorization list (showing the seller is NOT authorized)
"""


# ============================================================
# CLI
# ============================================================

def main():
    import sys
    
    # DemoData
    info = ComplaintInfo(
        brand_name="TechGadget",
        trademark_number="US12345678",
        asin="B08XXXXXX1",
        seller_name="CheapDeals123",
        seller_id="X9Y8Z7W6V5U4T3",
        violation_type="Unauthorized Sale / Suspected Counterfeit",
        evidence="Test buy received product with different packaging and lower quality than authentic product.",
        contact_email="legal@techgadget.com",
        company_name="TechGadget Inc.",
    )
    
    lang = "zh" if "--zh" in sys.argv else "en"
    platform = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--platform=")), None) or detect_platform()
    platform = platform.lower()
    if platform not in SUPPORTED_PLATFORMS:
        print(f"Error: unknown platform '{platform}' (expected one of {', '.join(SUPPORTED_PLATFORMS)})")
        sys.exit(1)
    if platform != "amazon":
        lang = "en"  # Chinese templates exist for Amazon only
        info.asin = {"ebay": "1234567890", "shopify": "https://example-store.com/products/techgadget-pro",
                     "tiktok": "1729000000000000000", "walmart": "123456789"}[platform]
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    template_type = args[0] if args else "all"
    # Sub-command names used in the platform SKILL.md files
    aliases = {
        "vero": "complaint", "dmca": "complaint", "platform-report": "complaint",
        "ip-report": "complaint", "seller-complaint": "complaint", "content-takedown": "complaint",
        "brand-portal": "complaint", "brand-registry": "complaint",
        "cease-desist": "cease", "test-buy": "testbuy", "map-notice": "map",
    }
    template_type = aliases.get(template_type, template_type)
    if template_type not in ("all", "complaint", "cease", "testbuy", "map"):
        print(f"Error: unknown template '{args[0]}'. Use: complaint, cease, testbuy, map or all "
              f"(aliases: {', '.join(sorted(aliases))})")
        sys.exit(1)
    
    if template_type == "complaint" or template_type == "all":
        if lang == "zh":
            print(generate_brand_registry_complaint_zh(info))
        else:
            print(generate_platform_complaint(info, platform))
    
    if template_type == "cease" or template_type == "all":
        print(adapt_to_platform(generate_cease_desist(info), platform))
    
    if template_type == "testbuy" or template_type == "all":
        if lang == "zh":
            print(generate_test_buy_guide_zh())
        else:
            print(adapt_to_platform(generate_test_buy_guide(), platform))
    
    if template_type == "map" or template_type == "all":
        print(adapt_to_platform(generate_map_violation_notice(info, 18.99, 29.99), platform))


if __name__ == "__main__":
    main()
