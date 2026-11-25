# COVR ad workspace

Brand: COVR (padelcovr.com). Handmade padel racket covers, $249 (price from Oct 2026), plus a $29 clip-on ball pouch.
Voice: calm, understated, premium. Short declarative lines ("All black. No compromise."). No hype, no emojis, no ALL-CAPS shouting.
Palette: cream (#F5F0E6) text on photos, black, natural canvas tones.

- Product facts, prices, stock and every image URL: `data/products.json` (pulled from the Shopify Admin API). Never invent features that aren't in that file.
- `python3 scripts/download_images.py` downloads all photos into `images/<colour>/`.
- `python3 scripts/make_video.py --slide "photo|text" ... --end "headline|sub"` makes a 1080x1920 video ad (needs ffmpeg).
- `python3 scripts/make_ads.py <photo> --headline ... --sub ... --name ...` makes 1080x1080, 1080x1350 and 1080x1920 ads in `ads/`.
- Don't advertise colours with stock 0 (check `stock` in products.json); in the Oct 2026 pull that was Mocha. The ball pouch is available (stock just not entered in Shopify).
- Ad requests: make ONE image only, vertical 4:5 at 1080x1350 (no separate story/square versions unless asked).
- Use the photo exactly as it is (no zoom-out, no blurred/mirrored extensions). Only a light fade behind the text at the top and bottom, no heavy dark gradients.
- Keep text on images short (headline under ~8 words). Put the longer selling copy in the Facebook primary text instead.

## Designed ads (creative/)
- `node creative/build.js` renders every ad in `creative/ads.js` (HTML/CSS layouts) to `ads/creative/*.png` at 1080x1350. `node creative/build.js <id>` renders one.
- Ads are grouped TOFU (t*), MOFU (m*), BOFU (b*). Helpers: `frame()` crops a photo region into a box, `circle()` makes detail close-ups.
- Fonts: Montserrat (bold billboard type), Instrument Serif (editorial), Inter (body) in `creative/fonts/`. Colours in `creative/base.css`.
- Facts must come from products.json or padelcovr.com. No invented reviews, offers, countdowns or certifications. See `creative/VIDEO-SHOTS.md` for formats that need real footage.

## Pricing & promos (set Oct 2026)
- Every cover: **$249** full price.
- Promos: **20% off** or a **$50 voucher** (both ≈ $199). Edit `OFFER` in `creative/ads6.js` (was/now/pct/voucher/code/when); all promo ads read it.
- **Live now:** Shopify prices set to $249 on all 10 active covers (12 Oct 2026). Code **COV20** = 20% off ($199.20 per cover), all customers, 12 Oct → 26 Oct 2026 (HKT). COV20 combines with the automatic "Free ball pouch with every cover". COV20 is an order-level 20% (applies to all items) because Shopify drops the free pouch when the cover itself has a product discount; result: cover $199.20 + free pouch. Side effect: extra paid pouches also get 20%.
- **Next (after 26 Oct):** $50 voucher shown as a store pop-up ("Claim your $50 now"), used at checkout. Not created yet; confirm $50 fixed amount (not 50%) before building it.
- Ads that say "48 hours" / countdowns are only valid near the real end date.

## Owner's rules (always)
- Short answers, low usage. Anything the owner must paste goes in a code block.
- Only real facts. No fake reviews, offers or claims. Don't alter the product in AI images; use only real colours.
- AI lifestyle photos: COVR shoot style (half body, hands or legs), one image per prompt, real shoot photos as reference. The strap never sits on the cover front.
- The owner publishes themes. Never edit the live theme: duplicate it (themeDuplicate) and edit the copy.
- Before any Shopify write, check `shop{name}` is the COVR store (the owner has more than one store).

## Store state (Nov 2026)
- Two lines: **Signature** ($249; collection handle `padel-racket-covers`, retitled "Signature") and **Essential** (collection `essential`, 40% launch price, template suffix `essential`). Colours: Vanilla Cream, Sky Denim, Ash.
- Essential product IDs: Vanilla 15491458465882, Ash 15491458334810, Sky Denim 15491458433114. Each has a white shot plus 3 lifestyle photos. No free pouch on Essential.
- Shipping: Essential profile 104618721370 is free in Indonesia, $50 international. The General profile has free "International 20-30 days" plus DHL $19.99.
- Pop-ups (footer group, `covr-offer-popup`, `show_on` setting): Signature gets a $50 scratch card (code **COVR50**, $249 minimum). After sign-up, /pages/offer shows the code on screen, so no email is needed. Essential pages get a "40% off, no code" message.
- Menu `main-menu-collections`: Signature and Essential under Padel Racket Covers, shown as photo cards.
- Homepage arches: file `covr-line-essential-arch.jpg` (strap hanging at the side).
- Source copies of the theme edits: `store/theme/`, `store/essential-pdp/`, `store/popup-v2/`. AI photos: `store/essential/ai/`.

## Pending
- The owner needs to publish the theme "COVR code on offer page 2026-11-08" (it holds all the changes above).
- Optional: send COVR50 to the 28 earlier pop-up sign-ups (customer tag `popup-offer-20`). The automation draft is off.

## Gotchas
- Shopify API 2026-10:
  - Use fileDelete, not productDeleteMedia.
  - collectionUpdate takes `collection:`.
  - Discounts take `context:{all:ALL}`.
  - Use discountNode, not codeDiscountNode.
  - fileUpdate with originalSource replaces an image in place and keeps its ID.
- themeFilesUpsert: send the body as TEXT. The URL body type silently does nothing. It is refused on the MAIN theme.
- Liquid: no filters inside `[]` lookups. Assign the value to a variable first.
- Canva media and export URLs are blocked locally. For full-size images, export the design and let Shopify fetch the export URL.
- If the Shopify MCP says "sign in again", the owner must reconnect it in claude.ai Connectors (with COVR selected in Shopify admin) and start a new chat.
