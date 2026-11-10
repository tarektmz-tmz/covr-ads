# Reel template (approved style, Nov 10 2026)

Look: framed speaker window (big at the start, small top-right after the intro), gold lower-third,
animated watch showcases (spotlight, reflection, float, tilt), spec chips, reference labels,
gold light-sweep transitions, word-by-word captions, @advance_watchco footer.

Pipeline (all local):
1. Cut the talking video (ffmpeg), export 30 fps frames to `vf/f_0001.jpg ...` and the audio.
2. Word timings from faster-whisper (medium model, HF_HUB_DISABLE_XET=1) -> `words.json` / `words.js`.
3. Edit `SCENES` in `page.html` (title, spec chips, watch cutouts + labels, start/end times).
4. `node render.js 0 <frames>` (Playwright/Chromium) writes `out/f_XXXX.jpg`.
5. ffmpeg: frames + audio -> mp4 (loudnorm, crf 21, yuv420p).

Rules: no price/investment claims, no phone number on screen ("WhatsApp link in bio"),
no "authorised dealer", AI avatar clips labelled as AI when posted.
Spec chips must come from public facts about the exact reference.
