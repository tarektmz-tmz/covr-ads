# CLAUDE.md

Main points carried over from earlier chats. **This repo is public:** never add emails, personal photos, client data, bank, ID or company-registration details, or anything else private.

## User's rules
- Keep answers short and direct, with no emotional filler.
- Verify first: check official sources and read every page of every document before answering or recommending. Don't guess.
- Never publish the user's personal email on a store.
- Hide client contact details, IDs and watch serials in anything shared with third parties.
- Never commit customer or personal data. Keep generated documents such as invoices and NOCs out of the repo.
- Commit only to the branch you were given, unless the user says otherwise.

## Repo
- `research/store-build-prompt.md`: reusable A-to-Z Shopify store build prompt.
- `research/product-research-notes.md`: product research.
- `store-kit/`: reusable store kit (theme snippets, page templates, tools, news-ticker announcement bar).
- Working branch from earlier sessions: `claude/kind-rubin-xk7wv4`.

## Key IDs and settings
- Advance Watch Co (advancewatchco.com):
  - Live theme "Advance Watch – Bank-ready Nov 7", id `161379319879`.
  - Previous theme id `160810303559`, kept as a backup.
- Edited theme files: `sections/awc-faq.liquid`, `main-article.liquid`, `main-page.liquid`, `footer.liquid`.

## Done
- Ceylora Shopify store built and themed.
- Meta ad creatives made.
- Store kit and build prompt committed.
- Advance Watch theme made bank-ready:
  - Liquid `replace` filters reduce the payment wording to bank transfer and card only. This also covers the FAQ JSON-LD.
  - Added a company-operator line to the footer.
  - Verified live.
- Sale invoices and an employer NOC draft prepared, kept outside the repo.

## Pending
- Business bank account:
  - Finish the remaining ID step of the current application.
  - Get the NOC signed.
  - Try UAE banks next.
- Check two open items on the invoices: a small price gap (was it a discount?) and the missing client names.
- Wispr Flow voice-input setup on the user's computer.

## Gotchas
- **Shopify MCP:**
  - `themeFilesUpsert` is refused on the live theme. Duplicate the theme, edit the copy, and have the user publish it.
  - `bulkOperationRunMutation` is blocked.
- **Checking the storefront:**
  - curl to the shop is blocked by the proxy.
  - Use Firecrawl with `?preview_theme_id=<id>` and `maxAge: 0` instead.
- **Choosing a bank or payment provider:**
  - Check its prohibited-business list before recommending it. USD fintechs (Slash/Bridge) ban watches and luxury goods.
  - Mercury requires a US-formed company.
- **Forms:** some reject dots in licence numbers. Enter digits only.
- **Computer use** (installing apps on the user's PC) works only in a normal Claude desktop-app chat with Computer use on. It does not work in cloud Claude Code sessions.
