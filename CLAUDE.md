# COVR ad workspace

Brand: COVR (padelcovr.com). Handmade padel racket covers, $199, plus a $29 clip-on ball pouch.
Voice: calm, understated, premium. Short declarative lines ("All black. No compromise."). No hype, no emojis, no ALL-CAPS shouting.
Palette: cream (#F5F0E6) text on photos, black, natural canvas tones.

- Product facts, prices, stock and every image URL: `data/products.json` (pulled from the Shopify Admin API). Never invent features that aren't in that file.
- `python3 scripts/download_images.py` downloads all photos into `images/<colour>/`.
- `python3 scripts/make_video.py --slide "photo|text" ... --end "headline|sub"` makes a 1080x1920 video ad (needs ffmpeg).
- `python3 scripts/make_ads.py <photo> --headline ... --sub ... --name ...` makes 1080x1080, 1080x1350 and 1080x1920 ads in `ads/`.
- Don't advertise colours with stock 0 (check `stock` in products.json); in the Oct 2026 pull that was Mocha and the ball pouch.
- Keep text on images short (headline under ~8 words). Put the longer selling copy in the Facebook primary text instead.

## Designed ads (creative/)
- `node creative/build.js` renders every ad in `creative/ads.js` (HTML/CSS layouts) to `ads/creative/*.png` at 1080x1350. `node creative/build.js <id>` renders one.
- Ads are grouped TOFU (t*), MOFU (m*), BOFU (b*). Helpers: `frame()` crops a photo region into a box, `circle()` makes detail close-ups.
- Fonts: Montserrat (bold billboard type), Instrument Serif (editorial), Inter (body) in `creative/fonts/`. Colours in `creative/base.css`.
- Facts must come from products.json or padelcovr.com. No invented reviews, offers, countdowns or certifications. See `creative/VIDEO-SHOTS.md` for formats that need real footage.
