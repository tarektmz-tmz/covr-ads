# COVR Ads – Claude notes

COVR = padel racket covers (Bali). Site: padelcovr.com. Shopify store: `znv4f0-th.myshopify.com`.

## My rules
- Keep answers short. Be very specific with click-by-click steps.
- Group reports: plain words, copy-paste ready, use "I" not "we". Format:
  `Ads update day N` → visitors from Bali, by source → most visited pages → spent / clicks / add to cart / sales.
- Keep my original ad designs. No dark panels, no new headlines unless I ask.
- Don't save, commit or push anything until I say so.
- Confirm the plan before spending credits. Don't waste Adspirer credits (failed calls count too).
- Use free Shopify analytics (ShopifyQL) for reports when possible.

## Key IDs & settings
- Meta ad account: `969524312328512`
- Campaign: `120249949986890296` (Traffic → website, Bali only, ends Oct 28)
- Ad set A (Latte + other ads): `120249949987040296` – Instagram only, optimizes Landing Page Views
- Ad set B (Vanilla Cream / padel girls): `120249950036820296` – best performer
- Budget: ~Rp100K/day total (started Rp200K). Prepaid balance + 11% VAT on ad spend.
- Ad images hosted on Shopify Files: `covr-ad1-grip-breathe.jpg`, `covr-ad2-did-you-know.jpg`, `covr-ad3-unboxing.jpg`, `covr-ad4-padel-girls.jpg` (1080x1350).
- Margin: cost ~Rp1.2M, price ~Rp3M ($249), shipping $10–20. Break-even ~Rp750K per sale (with 20% off). Target ≤ Rp450–500K per sale.

## Done
- Adspirer connected to Meta (needs a Facebook profile with Page Full control + ad account access).
- Campaign live with 4 ads, all traffic to website. Ad1 turned off. Facebook placements removed from ad set A.
- Results Oct 14–18: ~89K reach, 1,735 link clicks, Rp555,688 spent, 1 add to cart, 0 sales.
- Vanilla Cream: ~Rp603 per visit vs ~Rp1,019 for ad set A.

## Pending
- Check if Bali visitors see prices in USD or Rupiah (likely conversion blocker).
- Suggested: Rp60K/day Vanilla, Rp40K/day A. Confirm ad set B is Instagram only.
- Decision rule: ~4 days at Rp100K/day → keep going if ≥3 add to carts or 1 sale, else stop and fix the website.
- Add funds about weekly.
- Idea not started: COVR AI system (/ad-report, /new-ad-idea, /ad-learning).

## Gotchas
- Adspirer free plan = 15 actions/month (used up; resets Nov 11). Plus plan $49/mo if continuing. `get_tool_schema` / `search_tools` are free.
- Meta: campaign, ad set AND ad must all be ON. New ad sets come in PAUSED.
- Advantage+ audience: age max must be 65.
- "Missing Page permission" → give the Facebook profile Full control of the COVR Page, then reconnect Adspirer.
- Portfolio invite errors → open the invite in an Incognito window (browser was logged in as the wrong account).
- Shopify connector can point at another store → always check shopDomain is `znv4f0-th.myshopify.com`, use switch-shop if not.
- Meta "link clicks" ≫ Shopify visitors is normal-ish; compare with landing page views + Shopify sessions by landing page.

## Website work (Nov 2026)
Rules:
- Only real facts and real colours. Don't alter the product in AI images.
- AI photos: COVR shoot style (half body, hands or legs), one image per prompt, with real shoot photos as reference. Keep the strap off the cover front.
- Anything I must paste goes in a code block.
- I publish themes myself. Never edit the live theme: duplicate it (themeDuplicate) and edit the copy.

Store state:
- **Signature:** $249, collection `padel-racket-covers`, retitled "Signature".
- **Essential:** collection `essential`, 40% launch price, template suffix `essential`, no free pouch.
  - Colours: Vanilla Cream, Sky Denim, Ash.
  - Product IDs: Vanilla 15491458465882, Ash 15491458334810, Sky Denim 15491458433114.
- **Shipping:**
  - Essential profile 104618721370: free in Indonesia, $50 international.
  - General profile: free "International 20-30 days" plus DHL $19.99.
- **Pop-ups** (`covr-offer-popup`, `show_on` setting):
  - Signature: $50 scratch card, code **COVR50**, $249 minimum. /pages/offer shows the code on screen after sign-up, so no email is needed.
  - Essential pages: "40% off, no code".
- **Menu** `main-menu-collections`: Signature and Essential, shown as photo cards.
- **Source copies:** `store/theme/`, `store/essential-pdp/`, `store/popup-v2/`. AI photos are in `store/essential/ai/` (branch `claude/shopify-padelcovr-ad-images-zpmwq7`).

Pending:
- Publish the theme "COVR code on offer page 2026-11-08". It holds all the changes above.
- Optional: send COVR50 to the 28 earlier pop-up sign-ups (tag `popup-offer-20`). The automation draft is off.

Gotchas:
- Shopify API 2026-10:
  - Use fileDelete, not productDeleteMedia.
  - collectionUpdate takes `collection:`.
  - Discounts take `context:{all:ALL}`.
  - Use discountNode.
  - fileUpdate with originalSource replaces an image and keeps its ID.
- themeFilesUpsert: send the body as TEXT (the URL type silently does nothing). It is refused on the MAIN theme.
- Liquid: no filters inside `[]` lookups. Assign the value to a variable first.
- Canva media and export URLs are blocked locally. Export the design and let Shopify fetch the export URL.
- Shopify MCP says "sign in again": reconnect it in claude.ai Connectors (with COVR selected in Shopify admin), then start a new chat.
