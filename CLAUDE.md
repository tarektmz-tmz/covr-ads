# CLAUDE.md: context for future Claude sessions

This file records what has been done and decided across earlier chats, so a new session can pick up without re-deriving it.
Client personal data (names, phones, emails, IDs, watch serials), bank account numbers, IBANs and passport numbers are deliberately left out. **Never commit them to this repo.**

## How to work with this user

- Keep answers short and direct.
- **Verify before answering.** Search or read the source (provider policy pages, licence documents) first. Never guess or recommend something without checking. (Slash was recommended before its banking partner's prohibited list was checked, and that wasted the user's time.)
- Give no emotional filler ("this is disappointing"), only facts, reasons and next steps.
- Read every page of every document. Page 2 of the trade licence was missed once.
- Never publish the user's personal email on any store.
- Hide client contact details, IDs and serials in anything sent to banks.

## Repo layout

- `research/product-research-notes.md`: product research notes.
- `research/store-build-prompt.md`: reusable A-to-Z Shopify store build prompt.
- `store-kit/`: reusable store kit (theme snippets, page templates, tools, news-ticker announcement bar).
- `IMG_*.JPG`: product photos.
- Development branch: `claude/kind-rubin-xk7wv4`.

## Projects

### 1. Ceylora (Shopify store, modelled on metabolae.com)

- Store built and themed; v5 theme changes are noted in the commit history.
- Meta ad creatives were made in earlier sessions. They were scratch files and are not in the repo.

### 2. Advance Watch Co (Shopify, advancewatchco.com)

- Pre-owned luxury watch dealer, operated by MAI MURI L.L.C-FZ.
- Live theme: **"Advance Watch – Bank-ready Nov 7"** (id 161379319879), a duplicate of the old live theme 160810303559. The old themes are kept.
- **Bank-ready edits:**
  - `sections/awc-faq.liquid`: a Liquid `replace` rewrites the payment answer to "Bank transfer and credit/debit cards". This covers both the visible text and the JSON-LD.
  - `sections/main-article.liquid` and `sections/main-page.liquid`: `replace` filters remove the "cash or crypto" and "cash on delivery" wording.
  - `sections/footer.liquid`: "Advance Watch Co is operated by MAI MURI L.L.C-FZ, Meydan Free Zone, Dubai, UAE · Licence No. 2654973.01".
  - Verified live: no cash or crypto mentions remain.
- **Tooling quirks:**
  - The Shopify MCP refuses `themeFilesUpsert` on the live (MAIN) theme. Duplicate the theme, edit the copy, and have the user publish it.
  - `bulkOperationRunMutation` is blocked.
  - Direct curl to the shop is blocked by the proxy. Use Firecrawl with `?preview_theme_id=` and `maxAge: 0` to verify.

## Company banking: MAI MURI L.L.C-FZ (main open task)

**Company facts:**
- Meydan Free Zone LLC.
- Licence 2654973.01, issued 12/10/2026, expires 11/10/2027. Some forms reject the dot, so enter `2654973`.
- Activities: Sports Wear Trading, Handbags & Leather, Watches & Clocks & Spare Parts Trading, **and E-Commerce (4790.00, on page 2 of the licence)**.
- Shareholding 92% (owner and manager) / 8% (minority partner).
- AMOA clause 6.3.1 lets managers open and operate bank accounts "jointly or singly".
- Office: shared desk at Meydan Grandstand.

**The goal:** get accepted honestly. Present the business accurately and say only what's relevant. Do not disguise the watch business as generic e-commerce. Transaction RFIs ask for invoices, and KYB checks the website, so it gets caught and the account can be frozen.

**Results so far (verified):**

| Provider | Result | Verified reason |
|---|---|---|
| Slash (USD via Bridge) | Rejected | Bridge's prohibited activities list includes "Precious metals, Jewelry, **Watches**, Luxury goods". |
| Mercury | Not eligible | Requires a US-formed company. Syria is also on its prohibited list by residence. |
| Wio Business (13 Oct application) | Rejected in about 31 minutes (automated) | No published reason. Likely factors: the partner was then 50%, non-UAE-resident and without a UAE ID; there was no employer NOC; E-Commerce was only on page 2. Wio's unsupported list (jewelry/bullion, money exchange, crypto, gambling, etc.) **does not include watches**. |

**Current Wio application:**
- All steps and documents are done. Only the ID step is left (Emirates ID or passport plus selfie). Do it from the UAE if possible, with no VPN.
- Waiting for a reply from Wio care.

**Documents prepared (kept outside the repo):**
- Sale invoices in the user's invoice template, showing real sale dates, prices and bank payment references. Client contact details, IDs and serials are withheld, with a note: "Full records available on request."
- Draft NOC from the user's employer, Cinegenic Event Management. It allows the user to be shareholder and manager of MAI MURI and to operate its bank accounts. The founder needs to date, sign and stamp it.
- An employer salary certificate also exists.

**Recommended path:**
1. Finish Wio, where watches are allowed.
2. Get the NOC signed.
3. Ask the user's current personal bank about an SME account.
4. Contact the Meydan Free Zone banking desk and Mashreq NEO BIZ.
5. Use USD fintechs (Slash, Mercury, etc.) only for non-watch businesses such as Ceylora.

**Open questions:**
- Was the AED 725 gap on one invoice a discount? If so, update that invoice.
- Full names are still needed for two clients.
- What "P24" means. Possibly a 2024 warranty card.
- The Slash rejection reply should be sent from the Advance Watch Gmail. The connected Gmail connector is a different account.

## Other notes

- **Voice input:** the user uses Wispr Flow (dictation into any app).
- **Installing it for the user:** this needs Computer use in a normal Claude desktop-app chat (Settings → This computer → Computer use). Cloud Claude Code sessions cannot control the user's computer.
