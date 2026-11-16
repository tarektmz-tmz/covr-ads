# Script writing rules for HeyGen (Tarek, Nov 16 2026)
Tarek found why the avatar pauses: punctuation. Every . , ; : ! ? - ' < > and every comma inside a number makes the voice stop.
1. Send HeyGen ONE continuous line: no punctuation marks, no symbols, no line breaks. Words back to back.
2. Write numbers as words: 58,100 dollars becomes "fifty eight thousand one hundred dollars", 172% becomes "one hundred seventy two percent", 2020 becomes "twenty twenty".
3. Contractions written out (it is, that is). Hyphens become spaces (Sky Dweller, GMT Master).
4. Keep the sentences short and packed: full information in the shortest way. No filler.
5. Use `python3 reels/tools/flow_script.py script.txt` to convert an approved script, then check the result before sending it.
6. After generating: measure pauses with ffmpeg silencedetect (-38dB, 0.35 s). If long pauses remain, use `reels/tools/smooth_cut_50.py` (cuts pauses, no speed-up).
7. On screen: every number shown must be a number he says. A card appears when the watch NAME starts. Count-ups last as long as he takes to say the number.
8. No sound effects, except the cash sounds on profit reels when Tarek asks (R3 Nov 16).

## Instagram safe zone (Tarek, Nov 16 2026): EVERYTHING must fit inside what Instagram shows
On a phone Instagram crops about 54 px off each side of the 1080x1920 video and covers the top (status bar, about 115 px) and the bottom (buttons, about 100 px).
- Keep ALL text, numbers, boxes and watches between x 90 and x 990, and between y 230 and y 1700. Nothing important outside it.
- Watches smaller, set lower, tighter to the middle. Price boxes narrower, towards the middle. No logo or text at the very top.
- Standard way: build the layout, then wrap everything except the background and the avatar in a container scaled to 88% (see reels/tools/safe_wrap.js). Avatar corner: right edge at x 1040 or less.
- ALWAYS check a test frame with the crop zones marked before rendering a whole reel.
