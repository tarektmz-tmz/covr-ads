# Notes and things to confirm

## 'Full set' claim
- The homepage says "Brand New · Full Set · Same-Day Delivery in Dubai" and "100% Authentic Full Set, Box & Papers"; the approved carousel captions say "Brand new | Full set". So the line is applied to every Rolex story as the owner asked.
- The product descriptions in the store do NOT mention box, papers or tag for any watch checked (about 300 listings read), so the claim rests on the site-wide wording, not on each listing. For Patek and AP the line is left OFF (set `fullset` to True in rotation.py if the owner confirms). Pre-owned or discontinued pieces (the notes say these are said clearly) should not use the line unless they truly come with the full set.

## Store listing problems found while reading the descriptions (not changed)
- At least 18 product descriptions still contain leftover chat text, for example "ChatGPT said:" at the start (Datejust 36, Datejust 31, Sky-Dweller 336934 and 336933 listings) and "If you'd like, I can now create a unified format..." at the end of an Audemars Piguet Royal Oak Chronograph 26240BA description. Customers can read this on the product pages.

## Duplicate listings, same title, different price (confirm which is current)
- GMT-Master II Pepsi 126710BLRO: AED 115,000 (used) and AED 99,000
- GMT-Master II Bruce Wayne 126710GRNR: AED 84,000 (used) and AED 75,000
- GMT-Master II Sprite 126720VTNR: AED 69,000 (used) and AED 67,000
- Datejust 41 126300 and 126334 white dial: two identical-price listings each

## Other
- The store does not track stock (inventory 0), so "available" means "can be sourced". Buttons say "DM to order", never "reserve".
- Knowledge stories flagged 'confirm' are marked in rotation.md with a warning sign; the course lessons L11 and L15 (made-up stories for salespeople), the investment lesson and the 'NEEDS CAREFUL WORDING' queue ideas were not used.

## STRICT owner rule (22 Nov 2026)
One design per day: all stories of that day use the SAME design; the design changes day to day (rotate the 6). After the month, make 7 NEW designs (one per weekday) and rotate those. Never mix designs within one day.

## STRICT (23 Nov 2026): verify before posting
Before posting any story day, open the day's images and check each watch photo matches its title (dial colour, bracelet) and that no pair shows the same photo twice. Bug fixed: photo cache names were cut to 40 characters, so same-model listings overwrote each other.
