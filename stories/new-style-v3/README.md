# Story designs, round 3 (preview only, nothing is posted)

Font: **Inter** (the store theme's heading font is Inter 500) in the store palette: navy #0b1a33 / #112448, gold #c9a24b / #e3c47a, cream #f6f2ea, ink #16181d, muted #5d6370.
Text is big: headlines 104-176 px, secondary 44-68 px, prices 64-104 px, legal line 30 px. Key content sits between y 250 and 1580.

## Directions
Available Now: 1 hero (navy, rays, reflection) / 2 cream (giant navy type, watch bleeding right) / 3 dial close-up (dramatic crop) / 4 pair (two high-demand GMT-Master II).
Knowledge: 1 myth vs fact / 2 three checks (cream) / 3 five-year guarantee (giant numeral).

## Files
build_v3.py (writes templates/*.html, renders previews/*.png and the two sheets), fonts/Inter.ttf (OFL), assets/ (native transparent cutouts of the exact store listings, from src/), notes.md (price check).
Rebuild: `NODE_PATH=/opt/node22/lib/node_modules python3 build_v3.py`
