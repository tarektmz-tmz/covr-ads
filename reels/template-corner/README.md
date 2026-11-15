# Corner template (you bottom-right, visuals on main screen, faded boutique background)
- Crop of the avatar video: x 90, y 600, 900x1058 -> 460x541 bottom-right, soft edge, no frame.
- Hook text first (no watches), cards timed to the spoken names (cfg with s/e per card), progress dots per model family, CTA at the end.
- Build: HeyGen mp4 -> minterpolate 50fps -> frames -> render.js in 4 parallel ranges -> ffmpeg crf 15.
