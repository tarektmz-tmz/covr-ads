# Merchant Center fix: Advance Watch (UAE only)

## Why the two warnings appear
- Your Google & YouTube channel feeds each product once per target country (244 x 2 = 488).
- The Shopify "International" market includes Hong Kong, but the only delivery zone is the UAE.
- Google sees Hong Kong with no shipping, no return policy and no Buy button, so it flags it.

## Fix 1: stop selling to Hong Kong (5 minutes, in Shopify admin)
1. Sales channels > Google & YouTube > Settings > Target countries.
2. Remove everything except United Arab Emirates. Save.
3. Settings > Markets > International > deactivate it (or remove Hong Kong from its regions).
   Keep the "United Arab Emirates" market active.

## Fix 2: return policy (Merchant Center)
Merchant Center > Settings (gear) > Shipping and returns > Returns tab > add policy:
- Country: United Arab Emirates
- Returns: "Not accepted / final sale" (matches the store's Refund policy: all watch sales are final)
- Policy URL: https://advancewatchco.com/policies/refund-policy
Then Shipping tab: UAE, free standard shipping, 1-2 days handling+transit (24-48 hours).

## Fix 3: shipping policy text (paste into Shopify > Settings > Policies > Shipping policy)
See below. It removes the Canada / UK / EU boilerplate.

---
**Shipping policy**

Advance Watch delivers within the United Arab Emirates only.

**Delivery time:** 24-48 hours after your order is confirmed and the deposit is received.

**Shipping cost:** Free standard shipping on all orders in the UAE.

**Tracking:** You'll receive a message with delivery details once your watch is on its way.

**Delivery:** Every watch is insured in transit. Someone must be available to receive it and show ID.

**Outside the UAE:** We don't currently ship outside the UAE.

**Questions:** advancewco@gmail.com or WhatsApp +971 56 185 3856.
---
(Check "insured in transit" and "show ID" are true for how you deliver before pasting; delete those lines if not.)

## After you do the above
Merchant Center > Products > Diagnostics: warnings clear within 24-72h. Deadline Nov 29, 2026.
