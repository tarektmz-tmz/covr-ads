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

---
# Chat history, 14–22 Nov 2026 (reels, stories, AI course). Saved from the long first chat.

## Working style (strict, Tarek never wants to repeat these)
- Minimum words. Copy his examples and wording EXACTLY; add nothing of your own; grammar fixes only and say so. Soften any guarantee or false claim ("100% go viral", "10x faster") and tell him in one line.
- Before a permission box: say in plain words what approve/deny does. Warn before big credit use (HeyGen credits and long background builds that burn his daily Claude allowance). Verify a file exists and delivery is confirmed before saying "sent" (SendUserFile).
- Instagram crop: the stricter safe zone above (x 90–990, y 230–1700) wins; the old chat also used 54 px sides / 115 top / 100 bottom. Profile grid shows only the centre 3:4 band (y 240–1680 on 1920). Overlay-check before sending and say "crop check done". Notes: reels/MUST_DO_INSTAGRAM_CROP.md.
- **Swipe-style POST COVER for every video** (strict): 4:5 (1080x1350) like the aviationtrack example: boutique background, round Rolex logo top right, small logo above the title, big hook title ("FORMER ROLEX EMPLOYEE REVEALING THE 5 TOP PICKS FOR YOUR FIRST ROLEX"). Nothing else on it. Posted as a carousel (cover first, video second). Notes: reels/MUST_DO_SWIPE_POST_COVERS.md; example reels/drafts/r5_top5_first_rolex/post_cover_swipe_4x5.jpg.
- Serial numbers always blurred; no phone numbers on images ("WhatsApp in bio"); no AI mention in watch captions; AI-system content says it is AI and uses Instagram's AI label. Reel quality rules are in the private Shopify page awc-reel-quality-rules-private (also awc-handoff-private).
- Other dealers' reels/photos are references only: recreate the concept with our own script, visuals and store prices; never reuse their footage, photos, voice or prices.

## HeyGen settings (when approved)
Avatar looks: beige a638485bd6a2c700b4047403ac969ee8, green 5accb4bd2f7ccfc4ca0ccf99bc52a832, Tarek Selfie 95af2eefceb34bee8989f7ffa642573e (motionPrompt gives more expression). Voice 1802f0d2ffc84b868c07e11288abca8b, speed 1.1, engine starfish, 9:16 1080p, about 0.33 credit/s. Never add artificial pauses; use his own punctuation; shorten pauses over 0.3 s to about 0.2 s with smooth cuts, never speed up.

## Reel pipeline that worked
HeyGen render → faster-whisper timings → minterpolate to 50 fps → Playwright frames of HTML visuals → ffmpeg; quiet music via reels/tools/mix_music.sh at VOL 0.05. He likes slow readable pop-ups (2–3 s holds), big visuals, real photos (Unsplash, sources in reels/private_drafts/selfie_reel/assets/SOURCES.md, git-excluded), phone-mockup demos, pointer rings. He dislikes tiny visuals, everything in the same place, AI-looking photos, extra labels. Private work folders (git-excluded, lost in a new session): course/, reels/private_drafts/, stories/auto/.

## Posted / live as of 22 Nov
- Instagram: authentication reel v8 (normal Reel, cover thumb_report_B); consultation reel v1 (weak); Available Now stories 19 and 21 Nov; 7 custom watch stories from his reference list.
- Teachable course "The AI Content Machine" LIVE at USD 199 (Starter plan monthly, Stripe connected, refund 7 days, personal licence in the zip and PDF): sales page https://luxurywatchesguide.teachable.com/p/the-ai-content-machine-1099226 , checkout https://luxurywatchesguide.teachable.com/purchase?product_id=6924570 . Interest = comment AUTOMATED/SYSTEM; he does the DMs.
- Shopify listing template for new watches: shop/WATCH_LISTING_TEMPLATE.md (category aa-6-11 BEFORE the shopify.* metafields, 16 metafields, 1920x1920 transparent square image ~97% height, publish to Online Store 117694201927 / POS 117694234695 / Google 213112913991). Example: Oyster Perpetual 41 134300 Celebration Dial, AED 75,000.

## Not posted yet / open
- Selfie reel v4 (same system, different topics; HeyGen da79f9a884eb55d86afba5c5490ebdd6; phone demo uses his Bluewater Villas PDF), course reel "This isn't really me" v6, launch story, explainer story, top-5 first Rolex reel (carousel not built: 4:5 video on blurred background).
- Daily 12:17 Dubai stories routine must be created from the chat that holds the Instagram tools (a routine that starts its own session has no tools). Stories: stories/new-style-v4/queue/<date>_1..5.jpg on Available Now days (every second day from 2026-11-21 to 2026-12-17). Info-story days paused until he picks from stories/new-style-v4/examples_info.
- Save-reel scripts C1–C5 (reels/scripts/batch2_save_reels_v2.md) awaiting approval; Metricool timezone (Singapore) and test schedule; MyChatBot Instagram link blocked by Meta cleanup; a reference reel he sent on 25 Nov (copy the concept in our own style, skip watches we do not have) was not started.
