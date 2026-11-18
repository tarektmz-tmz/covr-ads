# New story system (preview, nothing is posted)

Two stories a day instead of the old batch: one KNOWLEDGE story, one AVAILABLE NOW story. The daily stories task is unchanged until the owner approves.

## Files
- `previews/sheet_available_now.jpg`, `previews/sheet_knowledge.jpg`: the two preview sheets; single images in `previews/`.
- `templates/*.html`: the 8 templates (1080x1920, content inside y 250 to 1580), rendered by `render_templates.py`.
- `pool.json`: all 244 active store products ranked for AVAILABLE NOW; `rotation.md`: 28-day plan; `build_pool.py`: ranking rules.
- `assets/`: transparent watch cutouts taken from the store's own product images.

## Rules built in
- AED price exactly as the store lists it (minimum variant price); Patek shows no number, only REQUEST PRICE ON WHATSAPP.
- Never a phone number: WHATSAPP IN BIO. Tiny "not affiliated with Rolex" line on Rolex stories.
- Knowledge facts only from `reels/scripts/script-bank.md` and the confirmed notes (no investment claims).
- Wait times and sourcing time are the owner's confirmed approximate figures and carry "approximate" wording.

## Animated variant idea (not built)
A 4 to 6 second MP4 story: the watch drops in, the gold rays spin, the price pill pops, the HIGH DEMAND badge pulses. Built with the same HTML pages and the same frame renderer used for the reels (about 25 fps frames, 4 parallel Chromium workers, ffmpeg encode), so no new tool and no credits. Cost: roughly 3 to 5 minutes of rendering per story. Hosting: Windsor's `create_story` takes a public video URL (MP4 or MOV, 3 to 60 s, under 100 MB), so the files would be committed to the repo like the images, or stored in the store's Files; unposted stories should live in a private place, not the public repo. Best used for the AVAILABLE NOW story only, 2 to 3 a week, to keep rendering light.
