# COVR Facebook ads: step-by-step guide

This repo already has everything from your store: `data/products.json` lists all 11 active products with prices, stock, descriptions and **59 photo links**, pulled from your Shopify admin. You run two scripts on your own computer: one downloads the photos, the other turns any photo into ready-to-upload Facebook/Instagram ads.

---

## Part 1: One-time setup (about 15 minutes)

### 1. Install the tools
| Tool | Why | Get it |
|---|---|---|
| **Git** | to download this repo | https://git-scm.com/downloads |
| **Python 3** | runs the scripts | https://www.python.org/downloads (Windows: tick **"Add Python to PATH"**) |
| **Claude Code** | lets you ask for ads in plain English | https://claude.ai/code → install for Mac/Windows, or in a terminal: `npm install -g @anthropic-ai/claude-code` |

Check they work: open **Terminal** (Mac) or **PowerShell** (Windows) and type:
```bash
git --version
python3 --version     # on Windows: python --version
```

### 2. Get this repo onto your computer
```bash
cd Desktop
git clone https://github.com/tarektmz-tmz/covr-ads.git
cd covr-ads
git checkout claude/shopify-padelcovr-ad-images-zpmwq7
pip install pillow    # image library the ad script needs
```

### 3. Download all your product photos
```bash
python3 scripts/download_images.py
```
You now have a folder `images/` with one subfolder per colour (`images/total-black/`, `images/navy/`, ...). These are your full-resolution originals (up to 4000px).

---

## Part 2: Make ads with one command

```bash
python3 scripts/make_ads.py images/total-black/04_20251111131525217.jpg \
  --headline "All black. Nothing catches the light." \
  --sub 'Total Black padel racket cover · $199' \
  --name total-black-player
```
(Windows PowerShell: put it all on one line, without the `\`.)

This creates three files in `ads/`:

| File | Size | Where Facebook uses it |
|---|---|---|
| `total-black-player_portrait.jpg` | 1080×1350 | Facebook & Instagram feed (**best on mobile, use this first**) |
| `total-black-player_square.jpg` | 1080×1080 | feed, Marketplace, right column |
| `total-black-player_story.jpg` | 1080×1920 | Stories & Reels (text kept clear of the reply bar) |

If the crop cuts off the cover, add `--focus 0.3` (moves the crop up) or `--focus 0.7` (moves it down).
To use your own brand font: `--font path/to/font.ttf`.

### About the "Total Black players photo"
You don't need to send it. It's already in your store, and the download script saves it:
- `images/total-black/04_20251111131525217.jpg`: player holding the Total Black cover
- `images/total-black/06_IMG_5961_JPG.jpg`: two players at a stone wall
- `images/total-black/07_IMG_6008_JPG.jpg`: two players, black + baby pink covers
- `images/total-black/08_IMG_6009_JPG.jpg`: two players sitting

Ready-made Total Black set:
```bash
python3 scripts/make_ads.py images/total-black/04_20251111131525217.jpg --headline "All black. No compromise." --sub 'Total Black · handmade padel racket cover · $199' --name tb-player
python3 scripts/make_ads.py images/total-black/07_IMG_6008_JPG.jpg --headline "Pick your side." --sub 'Total Black or Baby Pink · $199' --name tb-duo
python3 scripts/make_ads.py images/total-black/01_7.jpg --headline "Black leather. Black hardware. Black crest." --sub 'Waterproof lining · front zip pocket · $199' --name tb-packshot
```
> Total Black shows **stock: 1** in Shopify. Restock it before you spend money on it, or the ads will send people to a sold-out page. Mocha and the ball pouch are at 0.

---

## Part 3: Use Claude Code to do it for you (the easy way)

1. In the `covr-ads` folder, type `claude` and press Enter.
2. Log in the first time (use your Claude account).
3. Just ask in plain English. Claude reads `CLAUDE.md` (your brand voice + rules) and `data/products.json` automatically. Examples:

```
Download all product images.
```
```
Make 3 ad variations for Ginger: one packshot, one lifestyle on court, one close-up detail.
Write the headlines in our brand voice and show me the results.
```
```
For every colour with stock above 2, make a portrait ad from its best lifestyle photo.
```
```
Write 5 Facebook primary texts and 5 headlines for the Navy cover, testing different angles:
protection, style, gift, handmade quality.
```
```
Make a carousel: one square image per colour, same headline style, in the order Navy, Latte, Ginger, Baby Pink, Sky Denim.
```

**Tips for working with Claude Code**
- Be specific: which product, which photo type, which size, what feeling.
- Say "show me" and Claude will open the image so you can judge it, then say "make the headline smaller" or "use a different photo".
- When you like a result, say "commit this", and it's saved in GitHub.
- Press `Shift+Tab` to let it work without asking permission each step.

### Connect these apps (claude.ai → Settings → Connectors)
| Connector | What it does for you |
|---|---|
| **Shopify** (already connected) | Reads products, stock, sales. Ask "which colour sold best last 30 days?" to choose what to advertise. |
| **Canva** (already connected) | Makes polished designs from your photos and brand kit, resizes to every Meta format, exports PNG. Best when you want more design than the script gives. |
| **Meta Ads / Facebook** (search the connector list) | If available for your account: read campaign results so Claude can tell you which ad wins. |
| **Google Drive** | Store the final ad folder to share with a designer or ad manager. |

---

## Part 4: Upload to Facebook Ads (Meta Ads Manager)

1. Go to **business.facebook.com → Ads Manager → + Create**.
2. Objective: **Sales**. Choose your Shopify catalog/pixel (install the **Facebook & Instagram** app in Shopify if you haven't).
3. Ad set: start with **Advantage+ audience**, location = your markets, budget around $15–30/day per ad set.
4. Ad: **Single image** → upload the `_portrait.jpg`, then under *Placements* choose **Customize asset per placement** → Stories/Reels → upload the `_story.jpg`.
5. Text:
   - **Primary text**: 1–2 lines from `data/products.json` → `lead` (or ask Claude for variations).
   - **Headline**: product name + price, e.g. "Total Black Racket Cover · $199".
   - **Link**: the product's `url` from products.json (link to the product page, not the homepage).
   - **CTA button**: Shop Now.
6. Test **3–5 different images** in the same ad set. After 4–7 days, turn off the ones with high cost per purchase and make new variations of the winner.

### What usually wins for a product like COVR
- **Lifestyle on court** (player carrying the cover) > plain packshot for cold audiences.
- **Packshot on clean background** works well for retargeting people who visited the site.
- **Close-ups** (leather zip pull, crest, lining) sell the "handmade premium" story and justify $199.
- **Two players / two colours** photos are great for "pick your colour" and gift angles.
- Keep text on the image short; put details in the primary text.
