# Store Build Prompt (reusable)

Copy everything inside the box below into a new Claude session. Fill in the `[brackets]` first.
This is the full process used to build the Ceylora store in one day, in the order that worked.

---

```
You are building a complete Shopify dropshipping store for me, end to end, and uploading
everything directly to the store. Work fast and act straight away, but TEST everything in a
real browser before you tell me it's done.

## My details
- Product: [product name, e.g. Ceylon Cinnamon 7,200mg softgels with MCT oil]
- Supplier: [CJdropshipping / other] (supplier photos are low quality: replace ALL of them)
- Brand name: [brand] (use the same spelling everywhere: store name, header, bag, ads)
- Competitor to model the layout on: [competitor homepage URL] and [competitor product page URL]
- Store: [xxxx.myshopify.com], currency [AED/USD], ships to [countries]
- Brand colours: [e.g. brown #9a3d14 / cream #f6eee5] fonts: [e.g. Poppins]
- Bundles: [e.g. Buy 1 / Buy 2 Get 1 Free (3) / Buy 3 Get 2 Free (5)] with prices [..] and
  compare-at prices [..]
- Main pain points / benefits to push: [4 benefits]
- Target customer for photos: [e.g. families and older couples at home]

## How to work with me
- Short, simple answers. Show me results, not long explanations.
- Never edit the live theme: duplicate it, edit the copy, give me the preview link, I publish.
  Before editing a copy, check I didn't change the live theme in the editor.
- After every change: open the real store (preview link) in a browser, screenshot desktop
  (1440px) AND phone (390px), and fix anything broken before reporting.
- In every image or ad: never cover a face, hands, or the product with text, notes or stickers.
- Health products: use "supports healthy ..." wording, never "cures/restores/treats". Keep one
  FDA disclaimer in the footer. No fake star ratings until real reviews exist.

## Phase 1: Research (15 min)
1. Scrape the competitor homepage + product page (layout, section order, offers, bundle cards,
   comparison table, guarantee, FAQ). Copy the METHOD and layout, never their photos or text.
2. Check their Meta Ad Library landing pages to see which angle gets the most ads.

## Phase 2: Product setup
1. Rename the product, set vendor = brand, clean URL handle, SEO title.
2. Variants = bundles (1 / 3 / 5 bags) with compare-at prices.
3. Description: one intro line, then closed click-to-open tabs (details/summary) that slide out
   on hover: Studied Benefits, Key Ingredients, How It Works, 5 Reasons We're Different,
   What to Expect Week by Week, Guarantee, FAQ. FDA disclaimer at the end.

## Phase 3: Photos (upload straight to Shopify, delete all supplier photos)
1. Generate realistic AI photos (Canva generate-image, use the product pouch as reference):
   [target customer] at home: kitchen family breakfast, older couple cooking, couple walking,
   person taking one softgel, product with ingredients on a wooden table, a "science" image
   (e.g. blood cells) for the metabolic benefit card.
2. Make a clean transparent cut-out of the pouch (remove-background) to reuse everywhere.
3. Put ALL text on images with code (HTML rendered to PNG), never AI text, so spelling is right.
4. Product gallery (all square): hero, key benefits panel, take 1 softgel daily, pouch + badges,
   inside the formula, daily routine, lifestyle photos.
5. Bundle photos: same background, 1 bag / 3 bags / 5 bags from the cut-out.
6. Extra graphics: "Us vs Other Brands" table (6 rows, pouch on our column), scalloped
   90-day money-back seal, 4 round benefit icons, Cassia-vs-Ceylon style comparison.

## Phase 4: Homepage (in this order)
1. Hero: photo ~44% left; right side = small brand label, big headline, one line, 4 benefit
   cards with icons (2x2), "Shop Now" button + guarantee line next to it.
2. "3 Reasons [brand] Is Different" cards with REASON 1/2/3 labels.
3. "[Brand] vs. Other Brands": brown gradient, table image left, 4 check points, white
   "Try Risk-Free Today" button right.
4. "Not All [product] Is the Same" education section with comparison image.
5. "Made for Real, Everyday Life": 4 lifestyle photo cards (no repeats).
6. "What to Expect, Week by Week": intro + 4 white cards (WEEK 1-2 / 3-4 / 5-6 / 7-8+),
   4 bullets each.
7. 90-Day Money Back Guarantee: brown gradient, centred seal, white title, white pill button.
8. FAQ accordion.
9. Full footer: brand + tagline, contact rows with icons, Quick Links, Help menu,
   "Join Our Email List" + Sign Up, FDA disclosure, payment icons.

## Phase 5: Product page
1. Gallery left, sticky while scrolling, max ~720px wide. Title, price, 4 benefit points with
   icons (2x2, one per row on phone).
2. Custom bundle cards block (photo, label, per-bag price, % saved, Recommended/Best Value
   badges) that drives the hidden variant picker. Test each card changes the price and adds the
   right variant to cart.
3. Add to cart, Shop Pay, guarantee line, description tabs.
4. Below: 3 trust columns, "Why This Formula Works" cards, key benefits image + text,
   benefit accordion cards with photo thumbnails, what's inside, week-by-week timeline,
   Us vs Other Brands, 90-day guarantee banner.

## Phase 6: Pages
- "Why [product]" landing page: 7 numbered benefits, a photo for each, offer box, disclaimer.
- FAQ page with REAL answers (no placeholders like "[add delivery time]").
- Contact page with form. Never publish my personal email.

## Phase 7: Test everything (real browser, desktop + phone)
- Every section renders, no broken images, nothing overlaps, no leftover "*".
- Each bundle URL shows the right price; add to cart enabled.
- Tabs open/close; footer visible; menus work; FAQ/Contact/Why pages load.
- Report what's broken and fix it before saying done.

## Phase 8: Meta ads (1080x1350)
Make at least 14 static ads in the brand style, using our photos and bundle prices:
1. Brown header claim ("Supports Healthy [benefit]") + badge row + bottom offer bar
2. Price offer card (Save up to X%, Buy 3 Get 2 Free, price + crossed price, checklist, seal)
3. Product centre with 4 benefit callouts + "Buy 2 Get 1 Free" sticker
4. Older person holding the product + sticky notes (flash sale / up to X% / Buy 2 Get 1 /
   money back) in their own column + benefit icon bar under the hands
5. "What's inside?" checklist + product + lifestyle strip
6. First 90 days timeline (30 / 60 / 90 days)
7. Price anchor with 5 bags + cost per day
8. Notes-app style "3 things to know before you buy"
9. "Buy 2 Get 1 Free, so you can actually feel the difference" (3 bags + FREE sticker)
10. "We're Sorry" apology letter (sale reopened for a short time) + X% OFF sticker
11. "We owe you an apology" playful note
12. "X% Off Ends at Midnight" low-stock alert
13. "Last Chance For Our Best Deal" dark ad with free shipping / bundle / guarantee
14. "Buy 2 Get 1 Free, Sale Ends Tonight" with guarantee + free shipping icons
Plus 5 simple angle tests: problem/solution, did-you-know, us-vs-them, 4 benefits, offer.
Rules: whenever an older person is the hero, add benefits to the image without covering them.
Make the store banner match the ad deadline (rotate urgency ads daily).

## Phase 9: Launch checklist (tell me what's still missing)
- Shipping zones include every country I advertise to; free shipping turned on if ads say it.
- Refund policy (matches the guarantee), shipping policy, privacy, terms.
- Payments set up (cards, not only PayPal); paid plan active.
- Store name spelled the same everywhere.
- Reviews app installed before showing any stars.
- Order a sample and confirm claims on the pouch (non-GMO, lab tested, etc.).
```
