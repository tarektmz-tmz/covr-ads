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


---
# Advance Watch Co (Tarek, Dubai watches) - SEPARATE PROJECT. Everything below applies only to this section.

New Rolex and luxury watches. Shopify advancewatchco.ae. Instagram @advance_watchco (Windsor account 17841447657748130). Most work files live on branch `claude/relaxed-curie-4cx06p` (stories queue, reel covers, shop/WATCH_LISTING_TEMPLATE.md, reels/MUST_DO_*.md). Private memory also in unpublished Shopify pages: awc-handoff-private, awc-reel-quality-rules-private.

## His rules
- Minimum words. Copy his examples and wording EXACTLY, add nothing of your own, grammar fixes only (say so). Soften guarantees ("100% viral").
- Plain words before any permission box. Warn before spending HeyGen credits or starting big builds. Verify a file exists and delivery is confirmed before saying "sent".
- Instagram crop: stay inside the safe zone (x 90-990, y 230-1700 on 1080x1920); the grid shows the centre 3:4 band. Overlay-check before sending.
- Every video gets a swipe-style POST COVER: 4:5 (1080x1350), boutique background, round Rolex logo top right, small logo above the title, his hook title, nothing else; posted as a carousel (cover, then video).
- Blur serial numbers; no phone numbers on images; never invent specs or prices; other dealers' posts are references only (own script, visuals, store prices).

## IDs and settings
- HeyGen: Tarek Selfie look 95af2eefceb34bee8989f7ffa642573e, beige look a638485bd6a2c700b4047403ac969ee8; voice 1802f0d2ffc84b868c07e11288abca8b, speed 1.1, starfish, 9:16 1080p. No artificial pauses; music via reels/tools/mix_music.sh VOL 0.05.
- Teachable course "The AI Content Machine", USD 199: https://luxurywatchesguide.teachable.com/p/the-ai-content-machine-1099226
- New watch listing: category TaxonomyCategory/aa-6-11 BEFORE shopify.* metafields; 16 metafields; image 1920x1920 transparent square (watch ~97% height); publish to Online Store 117694201927, POS 117694234695, Google 213112913991.

## Done
Authentication reel v8 posted; stories 19 and 21 Nov plus 7 custom watch stories posted; Teachable course live with licence; Oyster Perpetual 41 134300 Celebration listed (AED 75,000); swipe cover for the Top 5 first Rolex reel made.

## Pending
- Not posted: selfie reel v4, course reel v6, launch and explainer stories, Top 5 reel carousel.
- Daily 12:17 Dubai stories routine must be created from the chat that holds the Instagram tools. Info-story days paused until he picks a series.
- Reference reel sent on 25 Nov: recreate in our own style, skip watches we do not have (not started). Metricool timezone untested. Scripts C1-C5 await approval.

## Gotchas
- A routine that starts its own session has no Instagram/Shopify tools.
- Shopify: use featuredMedia, productUpdate(media:), fileDelete; set category before standard metafields.
- Git-excluded folders (course/, reels/private_drafts/, stories/auto/) vanish in a new session; HeyGen keeps renders.

## Update 25 Nov 2026 (site speed + theme)
- More rules: very short answers; don't ask him questions, decide and do; NO HeyGen credits without explicit approval; no routine automation messages; publish theme changes; comment replies natural (don't agree, disagree, argue or apologize).
- LIVE theme 162148483143 "Advance Watch – Filters + reviews loop Nov 24": its agent workspace has stale commits that can't publish. Don't edit it.
- NEW theme 162195505223 "AWC main (AVIF)": all latest work, NOT yet published. Tarek must publish it manually (Online Store → Themes → Publish); agent publish is refused. Edit this one from now on.
  - Has: theme images webp→avif; product-page founder photo like home page (square, "10,000+ Clients served at Rolex" badge covers his watch): sections/awc-why-trust.liquid + assets/awc-product.css (selectors prefixed `.awc-wt__grid`, awc-home.css loads later).
- All 751 products use AVIF media only (old webp kept in Files). AVIFs hosted in repo `a/` on branch claude/relaxed-curie-4cx06p, added via productUpdate with raw GitHub URLs. Reason: Shopify CDN serves alpha .webp to Safari as heavy PNG.
- Speed (phone, before → now): Home 193.8MB → 1.9MB, load 3.7s → 1.3–2.2s; Product 214.1MB → 2.1MB, 2.5s → 1.5s; Day-Date collection 8.8MB → 2.3MB. Re-test after the AVIF theme is published.
- Theme tools: theme_bash / theme_commit (themeId, script, description) / theme_publish (userConfirmed:true). Windsor Instagram: execute_action reply_to_comment, create_story.
- Pending: Tarek publishes "AWC main (AVIF)" then re-test speed; Patek import when Excel arrives (Twenty~4, Aquanaut, Nautilus, Cubitus, Golden Ellipse); faceless reels when footage arrives; optional 8th handover slot; optional delete zz-fmt-test files.
