# COVR Ads – Claude notes

COVR = padel racket covers (Bali). Site: padelcovr.com. Shopify store: `znv4f0-th.myshopify.com`.

## My rules
- Keep answers short. Be very specific with click-by-click steps.
- Group reports: plain words, copy-paste ready, use "I" not "we". Format:
  `Ads update day N` → visitors from Bali, by source → most visited pages → spent / clicks / add to cart / sales.
- Keep my original ad designs. No dark panels, no new headlines unless I ask.
- Don't save, commit or push anything until I say so.
- Confirm the plan before spending credits. Don't waste Adspirer credits (failed calls count too).
- Use free Shopify analytics (ShopifyQL) for reports when possible.

## Key IDs & settings
- Meta ad account: `969524312328512`
- Campaign: `120249949986890296` (Traffic → website, Bali only, ends Oct 28)
- Ad set A (Latte + other ads): `120249949987040296` – Instagram only, optimizes Landing Page Views
- Ad set B (Vanilla Cream / padel girls): `120249950036820296` – best performer
- Budget: ~Rp100K/day total (started Rp200K). Prepaid balance + 11% VAT on ad spend.
- Ad images hosted on Shopify Files: `covr-ad1-grip-breathe.jpg`, `covr-ad2-did-you-know.jpg`, `covr-ad3-unboxing.jpg`, `covr-ad4-padel-girls.jpg` (1080x1350).
- Margin: cost ~Rp1.2M, price ~Rp3M ($249), shipping $10–20. Break-even ~Rp750K per sale (with 20% off). Target ≤ Rp450–500K per sale.

## Done
- Adspirer connected to Meta (needs a Facebook profile with Page Full control + ad account access).
- Campaign live with 4 ads, all traffic to website. Ad1 turned off. Facebook placements removed from ad set A.
- Results Oct 14–18: ~89K reach, 1,735 link clicks, Rp555,688 spent, 1 add to cart, 0 sales.
- Vanilla Cream: ~Rp603 per visit vs ~Rp1,019 for ad set A.

## Pending
- Check if Bali visitors see prices in USD or Rupiah (likely conversion blocker).
- Suggested: Rp60K/day Vanilla, Rp40K/day A. Confirm ad set B is Instagram only.
- Decision rule: ~4 days at Rp100K/day → keep going if ≥3 add to carts or 1 sale, else stop and fix the website.
- Add funds about weekly.
- Idea not started: COVR AI system (/ad-report, /new-ad-idea, /ad-learning).

## Gotchas
- Adspirer free plan = 15 actions/month (used up; resets Nov 11). Plus plan $49/mo if continuing. `get_tool_schema` / `search_tools` are free.
- Meta: campaign, ad set AND ad must all be ON. New ad sets come in PAUSED.
- Advantage+ audience: age max must be 65.
- "Missing Page permission" → give the Facebook profile Full control of the COVR Page, then reconnect Adspirer.
- Portfolio invite errors → open the invite in an Incognito window (browser was logged in as the wrong account).
- Shopify connector can point at another store → always check shopDomain is `znv4f0-th.myshopify.com`, use switch-shop if not.
- Meta "link clicks" ≫ Shopify visitors is normal-ish; compare with landing page views + Shopify sessions by landing page.
