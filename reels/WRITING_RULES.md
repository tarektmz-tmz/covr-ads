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
