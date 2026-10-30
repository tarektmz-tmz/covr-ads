# Store Build Prompt (A to Z, hands-off)

Paste everything inside the box into a new Claude Code session on this repository
(`tarektmz-tmz/covr-ads`) with the Shopify and Canva connectors on.
Fill in the `[brackets]` first. Photos are optional: drop yours in a folder and name it below,
or leave it empty and it will create them.

---

```
Build my complete Shopify store from A to Z, fully on your own, and upload everything
directly to the store. I don't want to touch anything until it's finished. Don't ask me
questions; make sensible choices, test everything, and only stop for the things on the
"Only I can do" list at the end.

Reuse the kit in this repo: read store-kit/README.md first. It has the finished homepage,
product page and footer layouts, the bundle cards code, the site styles, the Why/FAQ/description
templates, and the tools for infographics, bundle photos, ads and live testing. Copy the FORMAT
and layout exactly; write NEW text for my product and use MY brand, prices and photos.

## My details
- Product: [product, e.g. Magnesium Glycinate 400mg capsules]
- Supplier / app: [CJdropshipping / other]. Delete every supplier photo.
- Brand name: [brand] (one spelling everywhere: store name, logo text, bag, ads, footer)
- Competitor to model: [competitor homepage URL], [competitor product page URL]
- Shopify store: [xxxx.myshopify.com], currency [AED/USD/...]
- Sell and ship to: [countries]
- Brand colours: [dark #.., main #.., light #..]; fonts: [e.g. Poppins headings, Plus Jakarta body]
- Bundles (variants): [Buy 1 = price / compare-at], [Buy 2 Get 1 Free (3) = price / compare-at],
  [Buy 3 Get 2 Free (5) = price / compare-at]
- 4 main benefits / pain points: [1], [2], [3], [4]
- Guarantee: [90-day money-back]   Free shipping: [yes/no, from which bundle]
- Current sale for banner + ads: [e.g. Fall Sale, up to 70% off, ends Nov 30]
- People in photos: [e.g. families and older couples at home]
- My photos (optional): [folder or "none, create them"]
- Support email for the store (not my personal one): [support@...]

## Rules
- Act straight away, short updates only, no long explanations.
- Never edit the live theme: duplicate it, build in the copy, test, then publish the copy
  yourself once every test passes (I approve this in advance).
- Test in a real browser (Firecrawl + store-kit/tools/livetest.js) on desktop 1440px AND phone
  390px after every phase. Fix problems before moving on.
- Never cover faces, hands or the product with text, notes or stickers. When an older person
  is the hero of an ad, add some benefits to the image without covering them.
- Health products: "supports healthy ..." wording, FDA disclaimer in footer, no star ratings
  until real reviews exist, no claims that can't be true yet.
- All text on images is added in code, never by AI.

## 1. Research
- Scrape the competitor homepage and product page: section order, offers, bundles, comparison
  table, guarantee, FAQ, footer. Note what their ads push (Meta Ad Library landing pages).

## 2. Store settings
- Theme: install/duplicate Horizon; set colour palette and fonts to my brand.
- Logo text, favicon (simple brand icon), announcement bar: "[sale] · Up To X% Off Bundles ·
  Ends [date]" + guarantee message.
- Menus: Main = Home, Shop [product], Why [product], FAQ, Contact. Footer/Help = Shop, FAQ,
  Contact, Search.
- Policies (Settings > Policies via API): refund policy matching the guarantee, shipping
  policy, terms, privacy, contact information. Support email, never my personal one.
- Shipping zones include every country above; free shipping rule if I said yes.

## 3. Product
- Title "[Brand] [product] [key spec]", vendor = brand, clean handle, SEO title/description,
  product type, tags.
- Variants = the 3 bundles with prices and compare-at prices. Keep the supplier's SKUs.
- Description = store-kit/pages/product-description.html format: one intro line, then closed
  tabs that open on click and slide out on hover (Studied Benefits, Key Ingredients, How It
  Works, 5 Reasons [Brand] Is Different, What to Expect Week by Week, Guarantee, FAQ).
- If the product has a templateSuffix, every product template change goes into that template.

## 4. Photos (use mine if given, otherwise create realistic AI photos with Canva)
- Transparent cut-out of the product pack (remove background) for all composites.
- Lifestyle: kitchen family breakfast (hero), older couple cooking with the pack, couple
  walking outdoors, person taking one capsule/softgel with water, product on a wooden table with
  ingredients, ingredient close-up, one "science" image for the main benefit (e.g. cells).
- Infographics with store-kit/tools: key benefits panel (person holding pack), take 1 daily,
  pack + badges, inside the formula, daily routine (all square for the gallery).
- Bundle photos: 1 / 3 / 5 packs, same background (bundles_compose.py).
- Graphics: Us vs Other Brands table (6 rows, pack on our column), scalloped money-back seal,
  4 round benefit icons, "[us] vs [cheap alternative]" comparison, guarantee + packs image.
- Upload all to Shopify Files with clear names; product gallery = 9 square images.

## 5. Homepage (store-kit/templates/index.json format, in this order)
1. Hero: photo ~44% width; brand label pill; big headline; one line; 4 benefit cards with
   icons in a 2x2 grid; button + guarantee line next to it.
2. 3 Reasons [Brand] Is Different (REASON 1/2/3 pills on photo cards).
3. [Brand] vs. Other Brands (brown gradient, table image, 4 checks, white button).
4. "Not All [product] Is the Same" education section.
5. Made for Real, Everyday Life: 4 lifestyle cards (4 different photos, no repeats).
6. What to Expect, Week by Week: intro + 4 white cards (WEEK 1-2 / 3-4 / 5-6 / 7-8+),
   4 bullets each.
7. Money-back guarantee (gradient, centred seal, white title, white pill button).
8. FAQ accordion (6 questions).
9. Footer (store-kit/templates/footer-group.json): brand + tagline, contact rows, Quick Links,
   Help, Join Our Email List + Sign Up, disclosure, payment icons, copyright, policies.

## 6. Product page (store-kit/templates/product.json format)
- Gallery left (sticky, max ~720px), thumbnails. Right: title, price, 4 benefit points with
  icons, bundle cards block (store-kit/theme/blocks), quantity, Add to cart, Shop Pay,
  guarantee line, description tabs.
- Below: 3 trust columns, "Why This Formula Works" 4 cards, key benefits image + text,
  benefit accordion cards with thumbnails, what's inside, week-by-week timeline with the
  daily routine image, Us vs Other Brands, guarantee banner.
- Add the site styles snippet (store-kit/theme/snippets) and render it from layout/theme.liquid.

## 7. Pages
- "Why [product]" (store-kit/pages/why-page.html format): 7 numbered benefits, one photo each,
  offer box, disclaimer.
- FAQ (store-kit/pages/faq.html format) with real answers, no placeholders.
- Contact page with the theme's contact form.

## 8. Test (real browser, desktop + phone) and fix
- Every section renders; no broken images; nothing overlaps; nothing covers people; no
  placeholder text; no stray asterisks; names spelled the same everywhere.
- Each bundle card selects the right variant; each ?variant= URL shows the right price;
  Add to cart enabled.
- Tabs open/close and slide on hover; footer shows; all menu links work; Why/FAQ/Contact load.
- Then publish the tested theme.

## 9. Meta ads (1080x1350, store-kit/tools/ads.js + ads2.js formats, my brand/prices/photos)
- 5 angle tests: problem/solution, did-you-know, us-vs-them, 4 benefits, offer.
- 14 proven formats: brown-header claim + badges, price offer card, product with 4 benefit
  callouts, older person + sticky notes + benefit bar, what's inside checklist, first 90 days
  timeline, price anchor with 5 packs + cost per day, notes-app "3 things to know",
  "Buy 2 Get 1 Free so you can feel the difference", "We're Sorry" letter, "We owe you an
  apology" note, "X% Off Ends at Midnight" low stock, "Last Chance For Our Best Deal",
  "Buy 2 Get 1 Free, Sale Ends Tonight". Use free shipping only if it's on in the store.
- Check every ad at full size before sending; then send me all of them.
- Write primary text + headline for each ad.

## 10. Final report (short)
- Store link, list of everything built, test results, ads.
- "Only I can do" list: activate payments (cards), paid plan, domain, connect Meta Pixel /
  Facebook & Instagram app, order a sample, install a reviews app, confirm supplier shipping
  times and pack claims (non-GMO, lab tested).
```
