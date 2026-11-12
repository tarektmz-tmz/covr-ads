# Viral template (approved style, Nov 12 2026)

Full-screen speaker (HeyGen twin, beige shirt), pause cuts with alternating punch zoom, animated title per
section, floating watch cutouts with labels in the band above the head, word-by-word gold captions on the chest,
light-leak transitions, soft whoosh sound design, progress bar, end card.

Pipeline: HeyGen video -> whisper medium word timings -> silence cuts (ffmpeg concat, 30 fps) -> frames
-> page.html (scenes, words, bounds in data.js) -> render3.js (Playwright) -> ffmpeg mux + whoosh + loudnorm.
Scenes, watches and word times are set at the top of page.html (SC array, built from the script words).
Rules: no price/investment claims, no phone number on screen, WhatsApp link in bio.

## v2 changes (Nov 12 2026, after feedback)
- Pauses are fast-forwarded with motion blur (tmix) instead of cut, so the body never jumps (max frame jump 5.96 vs 13.1 with hard cuts; original footage 4.63).
- Work at the source frame rate (25 fps), no 25->30 conversion (it caused duplicate-frame stutter).
- Slow zoom instead of per-cut punch zooms.
- Watches bigger (about 400 px tall) in the band above the head; titles smaller; captions 74 px at y 1500.
