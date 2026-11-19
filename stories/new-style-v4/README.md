# Story system, round 4 (previews only, nothing is posted, no scheduled task changed)

Font: Inter (the store theme's heading font). Palette: the store's navy #0b1a33 / #112448, gold #c9a24b / #e3c47a, cream #f6f2ea. Knowledge stories copy the website's look (small gold letter-spaced eyebrow, big heading, white and cream rounded cards, gold pill button).

## Available Now: one style per day, never four styles in one day
Six styles, each used for a whole day (3 stories, 3 different watches; the pair style shows 2 watches per story): hero, cream, pair, the full set (box/papers/tag icons), editorial, gallery plaque. The next day uses the next style. The full watch is always inside the frame (a text and image safe-zone check runs on every render: key content y 250 to 1580, nothing within 40 px of the sides).
Every Rolex story carries: **Full set: official Rolex box, papers and tag**. Patek and AP stories do not carry it (see notes.md), and Patek always shows "PRICE ON REQUEST".

## Urgency, rare and truthful
- **HIGH DEMAND PIECE · DM TO SOURCE YOURS NOW** (gold band): 1 watch on every second day, 2 watches every eighth day. It makes no stock claim.
- **ONLY ONE AVAILABLE · DM TO SOURCE YOURS NOW**: OFF. It is applied only to watches whose store handle you list in `only_one_available.json` (empty now). The store does not track stock, so an automatic "only one" on every watch would be a claim nobody has verified, which can mislead customers and get noticed.

## Knowledge library
`knowledge_library.py`: 43 different stories, 10 layouts (myth vs fact, checklist, big number, Q&A, comparison table, steps, timeline, quote card, ladder, do and don't). Facts only from your confirmed notes; 9 are flagged `confirm: True` (years of waiting, timing rules, the unpublished consultation line). Rendered images are in `library/`.

## Rotation
`rotation.md` / `rotation.json`: 30 days. Run `python3 rotation.py`. `python3 build_v4.py` renders previews, `python3 build_v4.py library` renders all knowledge stories. Available Now days are rendered from the rotation (cutouts come from each listing's own product image, so image and price always match).
