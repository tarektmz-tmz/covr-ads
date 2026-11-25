# Advance Watch Co — project memory (read first)

Client: Tarek, Advance Watch Co, Dubai. Pre-owned luxury watches (Rolex focus, Patek coming).
- Shopify: advancewatchco.ae
- Instagram: @advance_watchco (Windsor account 17841447657748130)
- This repo is PUBLIC: never commit personal photos, emails or private data.

## Rules (from Tarek)
- Very short answers. Don't ask questions — decide and do.
- Never invent facts. Verify everything.
- Warn before spending any credits. NO HeyGen credits without explicit approval.
- No routine automation messages.
- Theme changes: publish them (approved "do for everything").
- Instagram safe zone: x 90–990, y 230–1700 (1080x1920).
- Comment replies: natural; don't agree, disagree, argue or apologize.

## Shopify state (2026-11-25)
- LIVE theme: 162148483143 "Advance Watch – Filters + reviews loop Nov 24". Its agent workspace has stale commits that can't publish (conflict on 2 templates) — don't edit it.
- NEW theme: 162195505223 "AWC main (AVIF)" — all latest work, NOT yet published. Tarek must publish manually (Online Store → Themes → Publish); agent publish is refused for this theme. After it's live, edit that one.
  - Contains: theme images webp→avif (lighter on iPhone/Safari), product-page founder photo matching home page (square photo, "10,000+ Clients served at Rolex" badge covering the watch) — sections/awc-why-trust.liquid + assets/awc-product.css (selectors prefixed `.awc-wt__grid` because awc-home.css loads later).
- Products: all 751 use AVIF media only (old webp kept in Files). AVIFs hosted in this repo under `a/`, added via productUpdate with raw GitHub URLs.
- Why AVIF: Shopify CDN serves alpha .webp to Safari as heavy PNG.

## Speed (phone, first test → now)
- Home: 193.8MB → 1.9MB, load 3.7s → 1.3–2.2s
- Product: 214.1MB → 2.1MB, load 2.5s → 1.5s
- Day-Date collection: 8.8MB → 2.3MB
- Re-test after "AWC main (AVIF)" is published.

## Tools / gotchas
- Shopify theme tools: theme_bash / theme_commit (themeId, script, description) / theme_publish (userConfirmed:true). themeFilesUpsert on live theme is blocked.
- Windsor Instagram: get_data, execute_action (reply_to_comment, create_story).
- Daily stories scheduled task runs (logs in stories/auto/). Replied comment ids: stories/auto/replied_comments.txt.

## Pending
- Tarek to publish "AWC main (AVIF)", then re-run speed test.
- Patek import when Excel arrives (Twenty~4, Aquanaut, Nautilus, Cubitus, Golden Ellipse).
- Faceless reels when footage arrives.
- Optional: 8th handover slot; delete zz-fmt-test files.
