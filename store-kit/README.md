# Store Kit

Everything reusable from the Ceylora build (Shopify, Horizon theme), so a new store can be built
from the same format without starting over. The master prompt that drives it is
`research/store-build-prompt.md`.

## What's here

| Path | What it is | How to reuse |
|---|---|---|
| `theme/blocks/ceylora-bundles.liquid` | Bundle cards (photo, label, per-bag price, % saved, badges). Clicking a card selects the matching variant in the theme's own picker, which stays hidden. | Upload as `blocks/<brand>-bundles.liquid`, add it to the product details above the variant picker, set image/label/bags/badge per bundle. |
| `theme/snippets/ceylora-sizes.liquid` | Site CSS: gallery size + sticky, hero image size, brown gradient sections, pill buttons, description tabs (open on click, slide out on hover), footer links, phone layout for benefit points. | Upload as `snippets/<brand>-styles.liquid` and add `{%- render '<brand>-styles' -%}` in `layout/theme.liquid` right after `{%- render 'color-palette' -%}`. Section rules target `[id$='__section_key']`, so keep the same section keys or update them. |
| `templates/index.json` | Finished homepage layout. | Copy, swap the text and `shopify://shop_images/<file>` names, upload to the duplicated theme. |
| `templates/product.json` | Finished product page layout. | Same. Also write it to the product's own template if it has a `templateSuffix`. |
| `templates/footer-group.json` | Full footer: brand, contact rows, menus, email sign-up, disclosure, payment icons, copyright. | Upload as `sections/footer-group.json`. |
| `pages/product-description.html` | Product description with intro + closed tabs. | `productUpdate` `descriptionHtml`. |
| `pages/why-page.html` | 7-benefit "Why" landing page with a photo per benefit + offer box. | `pageCreate`/`pageUpdate`. |
| `pages/faq.html` | FAQ page. | `pageCreate`/`pageUpdate`. |
| `tools/render.js`, `render2.js` | Product infographics (benefits panel, daily routine, inside the formula, pouch + badges) with text added in code. | `node render.js <bgdir> <outdir> [name]` |
| `tools/compare2.js` | "Us vs Other Brands" table + scalloped 90-day seal (transparent PNG). | `node compare2.js` |
| `tools/badge.js`, `icons4.js` | Round 90-day badge, 4 round benefit icons. | `node badge.js`, `node icons4.js` |
| `tools/bundles_compose.py` | 1 / 3 / 5 bag bundle photos from one transparent pouch cut-out. | `python3 bundles_compose.py` |
| `tools/page_imgs.js` | Cassia vs Ceylon comparison, guarantee + bags images for pages. | `node page_imgs.js` |
| `tools/ads.js`, `ads2.js` | 19 Meta ad templates (1080x1350): angle tests, offers, benefits, sticky notes, notes-app, apology letters, deadline/low stock, bundles. | `node ads.js`, `node ads2.js` |
| `tools/livetest*.js` | Renders the real storefront HTML (scraped with Firecrawl) in a local browser with the real theme assets, screenshots each section, runs bundle/tab/broken-image checks. | `ONLY=section_a,section_b node livetest.js page.html out 1440 sections` |
| `tools/test-bundles.js` | Tests the bundle block logic with liquidjs before upload. | `node test-bundles.js` |

Install tool dependencies: `cd tools && npm install` (Playwright + Chromium must already exist).
Expected folders next to `tools/`: `bg/` (photos, `bag.png` cut-out), `final/`, `ads/`, `ads2/`, `test/`.
Update the brand name, colours, prices and the shop CDN path (`SHOP=` in `livetest.js`,
`ceyllora.myshopify.com` domain) before using.

## Lessons that save hours

**Theme**
- Never write to the live (MAIN) theme. `themeDuplicate`, edit the copy, send the preview link
  `https://<shop>.myshopify.com/?preview_theme_id=<id>`. Before editing a copy of a theme the
  user edited, compare its templates with your last version.
- `themeFilesUpsert` with a TEXT body works on the trial plan (file uploads of non-images don't).
  Send templates as minified JSON.
- Check `product.templateSuffix`: supplier apps (CJ) assign their own product template, so edits
  to `templates/product.json` don't show. Write the same JSON to
  `templates/product.<suffix>.json` (`themeFilesCopy`).
- Horizon blocks used: section, group (row/column, background, border, radius, padding),
  text (presets, custom size, colour, background pill), image (ratio, custom width %), button
  (style_class, custom colours; width only fit-content/custom), icon (image_upload for custom
  icons, width 12–200), accordion + _accordion-row (image thumbnail), carousel + _card,
  email-signup, menu, payment-icons, footer-copyright, footer-policy-list.

**Images**
- Canva hosts are blocked from the sandbox: generate with Canva, put the image on a page of a
  Canva design (`update_fill`), export JPG, then give the export URL straight to Shopify
  `fileCreate`. Download from cdn.shopify.com if you need it locally.
- Local files: `stagedUploadsCreate` → curl multipart POST to the storage URL → `fileCreate`.
- Replace a photo everywhere at once: `fileUpdate` with `originalSource` (same file name/URL).
- Reference files in templates as `shopify://shop_images/<filename>`.
- Never let AI write text on images; render text in HTML with local fonts.
- Gallery images square (1:1). Never cover faces, hands or the product.

**Testing**
- The sandbox can't open `*.myshopify.com` directly. Use Firecrawl `screenshot` (full page)
  and `rawHtml`, then `tools/livetest.js` for section-by-section desktop (1440) and phone (390)
  shots, broken images, bundle clicks and tab behaviour.
- Full-page screenshots miss lazy images and the footer (`content-visibility: auto`); check
  section by section before calling something broken.
- Prices after a bundle click need the store's section API; verify with
  `?variant=<id>` URLs instead.

**Copy**
- "Supports healthy …" wording, one FDA disclaimer in the footer, no star ratings before real
  reviews, no claims that can't be true yet (no customers = no "most people notice").
