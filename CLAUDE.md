# COVR ad workspace

Brand: COVR (padelcovr.com). Handmade padel racket covers, $249 (price from Oct 2026), plus a $29 clip-on ball pouch.
Voice: calm, understated, premium. Short declarative lines ("All black. No compromise."). No hype, no emojis, no ALL-CAPS shouting.
Palette: cream (#F5F0E6) text on photos, black, natural canvas tones.

- Product facts, prices, stock and every image URL: `data/products.json` (pulled from the Shopify Admin API). Never invent features that aren't in that file.
- `python3 scripts/download_images.py` downloads all photos into `images/<colour>/`.
- `python3 scripts/make_video.py --slide "photo|text" ... --end "headline|sub"` makes a 1080x1920 video ad (needs ffmpeg).
- `python3 scripts/make_ads.py <photo> --headline ... --sub ... --name ...` makes 1080x1080, 1080x1350 and 1080x1920 ads in `ads/`.
- Don't advertise colours with stock 0 (check `stock` in products.json); in the Oct 2026 pull that was Mocha. The ball pouch is available (stock just not entered in Shopify).
- Keep text on images short (headline under ~8 words). Put the longer selling copy in the Facebook primary text instead.

## Designed ads (creative/)
- `node creative/build.js` renders every ad in `creative/ads.js` (HTML/CSS layouts) to `ads/creative/*.png` at 1080x1350. `node creative/build.js <id>` renders one.
- Ads are grouped TOFU (t*), MOFU (m*), BOFU (b*). Helpers: `frame()` crops a photo region into a box, `circle()` makes detail close-ups.
- Fonts: Montserrat (bold billboard type), Instrument Serif (editorial), Inter (body) in `creative/fonts/`. Colours in `creative/base.css`.
- Facts must come from products.json or padelcovr.com. No invented reviews, offers, countdowns or certifications. See `creative/VIDEO-SHOTS.md` for formats that need real footage.

## Pricing & promos (set Oct 2026)
- Every cover: **$249** full price.
- Promos: **20% off** or a **$50 voucher** (both ≈ $199). Edit `OFFER` in `creative/ads6.js` (was/now/pct/voucher/code/when); all promo ads read it.
- **Live now:** Shopify prices set to $249 on all 10 active covers (12 Oct 2026). Code **COV20** = 20% off covers only ($199.20), all customers, 12 Oct → 26 Oct 2026 (HKT). Pouch excluded.
- **Next (after 26 Oct):** $50 voucher shown as a store pop-up ("Claim your $50 now"), used at checkout. Not created yet; confirm $50 fixed amount (not 50%) before building it.
- Ads that say "48 hours" / countdowns are only valid near the real end date.
