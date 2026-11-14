# Reel template v6 (use this one)
- Full-frame, no zoom, natural HeyGen audio, 50 fps (minterpolate mci on source), captions at belly height.
- Visuals are small and sit BELOW the iPhone/Instagram top zone: nothing important above y=230 or below y=1690 (1080x1920).
- No logo at the very top, no footer handle (Instagram shows the username/caption bar there).
- Looks to use: beige shirt (a638485bd6a2c700b4047403ac969ee8) and green shirt (5accb4bd2f7ccfc4ca0ccf99bc52a832) ONLY. No black t-shirt.
- Steps: download HeyGen mp4 -> tr.py (whisper words) -> cfg json (scenes) -> ffmpeg minterpolate 50 fps (name_v50.mp4) -> build5.sh (4-core render + encode).
