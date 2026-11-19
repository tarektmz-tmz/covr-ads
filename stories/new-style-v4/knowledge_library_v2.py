"""Knowledge library v2: stories that are NEW (no overlap with knowledge_library.py). Facts only from the owner's own published
carousels (families guide, GMT guide, fake-checks part 1 and 2, ten steps), his confirmed scripts (recovered_viral_scripts: v11 complications,
v12 first Rolex, v14 purposes, v2 Day-Date stone dials, New 2 Datejust combos) and well-known public watch facts that are on his slides.
No prices, no market or investment claims. confirm=True means: excluded from the queue until the owner confirms (see confirm.md).
grp: used to spread topics (family, fake, buy, gmt, tech, guide)."""
L = []


def add(id, grp, layout, eyebrow, title, src, confirm=False, **kw):
    L.append(dict(id=id, grp=grp, layout=layout, eyebrow=eyebrow, title=title, src=src, confirm=confirm, **kw))


# ---------------- Rolex families (big_number, one fact per family, from the published families guide)
FAM = [
 ("datejust", "1945", "YEAR", "Datejust", "The first self-winding chronometer wristwatch with the date in a window. The classic Rolex. Sizes 31 to 41 mm."),
 ("daydate", "1956", "YEAR", "Day-Date", "The first wristwatch to spell out the day of the week in full. Made only in gold or platinum, on the President bracelet."),
 ("oyster", "1931", "YEAR", "Oyster Perpetual", "The essential Rolex: waterproof Oyster case and a self-winding rotor, nothing extra. Colourful dials, 28 to 41 mm."),
 ("sub", "1953", "YEAR", "Submariner", "The Rolex diver's watch. Today it is waterproof to 300 metres."),
 ("gmt", "1955", "YEAR", "GMT-Master II", "Made for pilots to follow two time zones at once. The two-colour bezel is its signature."),
 ("daytona", "1963", "YEAR", "Daytona", "The racing chronograph named after Daytona Beach. One of the most wanted Rolex watches."),
 ("skydweller", "2012", "YEAR", "Sky-Dweller", "An annual calendar plus a second time zone, set with the rotating Ring Command bezel."),
 ("airking", "1945", "YEAR", "Air-King", "A tribute to early aviation, with a bold minute scale made for reading the time in flight."),
 ("seadweller", "1967", "YEAR", "Sea-Dweller", "Built for saturation divers, with a helium escape valve. Waterproof to 1,220 metres."),
 ("deepsea", "2008", "YEAR", "Deepsea", "Rolex's ultimate dive watch, waterproof to 3,900 metres."),
 ("yachtmaster", "1992", "YEAR", "Yacht-Master", "The Rolex sailing watch. Precious metals, Oysterflex straps and a bidirectional bezel."),
 ("ym2", "2007", "YEAR", "Yacht-Master II", "A regatta chronograph with a programmable countdown for the start of a race."),
 ("landdweller", "2025", "YEAR", "Land-Dweller", "Rolex's newest watch family, with the new Dynapulse escapement and an integrated bracelet."),
 ("r1908", "2023", "YEAR", "1908", "A modern dress watch named after the year the Rolex name was registered: 1908."),
]
for k, y, u, nm, t in FAM:
    add("fam_" + k, "family", "big_number", f"Rolex family · {nm}", y, "families guide part 1/2", big=y, unit="SINCE", text=t)

# ---------------- how to spot a fake (from fake-checks part 1 and 2, ten steps)
add("fk_engraved", "fake", "qa_card", "Check the dial", "The engraved ring", "daily 06 slide 5",
    q="What is the engraved ring on a Rolex dial?",
    a="The inner ring of the dial is engraved ROLEX. The letters should be sharp, even and lined up. Shallow or crooked is a warning sign.")
add("fk_caseback", "fake", "myth_fact", "Check the back", "The see-through caseback", "daily 06 slide 6",
    myth="You can admire the movement through a Rolex caseback.",
    fact="Rolex does not make see-through casebacks. A plain, solid caseback is correct. If you can see the movement, it is not a Rolex.")
add("fk_weight", "fake", "checklist", "Feel it in your hand", "Weight, bracelet, bezel", "daily 06 slide 7",
    items=[("It feels dense", "A real Rolex has weight."), ("No rattling links", "The bracelet is tight."), ("A clean clasp click", ""), ("A firm, even bezel", "")])
add("fk_glow", "fake", "qa_card", "Check the lume", "Chromalight", "daily 07 slide 2",
    q="What is the blue glow on current Rolex sports models?",
    a="Chromalight: a blue glow that stays bright for hours. A short or patchy glow deserves a closer look.")
add("fk_serial", "fake", "quote_card", "Check the numbers", "Serial and reference", "daily 07 slide 3",
    quote="The numbers on the watch, the card and the papers must match.", note="Necessary, but not enough: numbers can be copied.")
add("fk_price", "fake", "quote_card", "Check the price", "The price tells a story", "daily 07 slide 5",
    quote="If a Daytona is at a big discount, ask why.", note="Popular steel Rolex models rarely sell far below the market.")
add("fk_seller", "fake", "checklist", "Check the seller", "A real dealer is open", "daily 07 slide 6",
    items=[("Open about who they are", ""), ("A trade licence you can ask to see", ""), ("An online history", "And real reviews."), ("Welcomes an independent check", "")])
add("fk_indep", "fake", "steps", "The last step", "Get an independent check", "daily 07 slide 7",
    items=[("Before paying in full", ""), ("Ask a watchmaker or an authentication service", ""), ("A genuine dealer agrees without a fuss", "")])

# ---------------- ten steps to buy safely
add("ts_12", "buy", "steps", "Buying safely · steps 1 and 2", "Decide, then get a quote", "daily 08",
    items=[("Decide the exact watch", "Model, reference, dial and budget."), ("Get a boutique quote", "It is your reference point for every offer.")])
add("ts_34", "buy", "steps", "Buying safely · steps 3 and 4", "Seller, then proof", "daily 08",
    items=[("Choose a seller you can check", "Open about who they are, a trade licence, an online history and real reviews."), ("Ask for proof", "Photos or a video with today's date, showing reference and serial.")])
add("ts_56", "buy", "steps", "Buying safely · steps 5 and 6", "Full set and warranty date", "daily 08",
    items=[("Confirm a full set", "Box, card and papers with matching numbers."), ("Check the warranty date", "A new watch should have a recent, filled-in card.")])
add("ts_78", "buy", "steps", "Buying safely · steps 7 and 8", "Payment order and inspection", "daily 08",
    items=[("Agree the payment order", "Deposit to confirm, balance on receipt."), ("Inspect in person", "Look under good light before paying the balance.")])
add("ts_910", "buy", "steps", "Buying safely · steps 9 and 10", "Check, then keep everything", "daily 08",
    items=[("Get an independent check", "A genuine dealer agrees without a fuss."), ("Keep your paperwork", "Warranty card, papers and messages.")])
add("ts_rule", "buy", "quote_card", "The most important rule", "Never pay in full first", "daily 08 slide 7",
    quote="Never pay in full before you have seen the watch and checked the seller.", note="One rule that avoids most problems.")

# ---------------- GMT-Master II guide (from the GMT guide carousel)
add("gmt_bat", "gmt", "compare_table", "Which GMT are you?", "Batman or Batgirl?", "gmt guide",
    cols=("Batgirl", "Batman"), rows=[("Reference", "126710BLNR", "126710BLNR"), ("Bracelet", "Jubilee", "Oyster"), ("Bezel", "Blue and black", "Blue and black")])
add("gmt_sprite", "gmt", "qa_card", "Which GMT are you?", "Which GMT has a left-hand crown?", "gmt guide + v1",
    q="Which GMT-Master II has the crown on the left?",
    a="The Sprite, reference 126720VTNR, with a green and black bezel. It is the most unusual GMT Rolex has made.")
add("gmt_rootbeer", "gmt", "qa_card", "Which GMT are you?", "What is a Root Beer?", "gmt guide",
    q="What is the Root Beer GMT-Master II?",
    a="The two-tone version in Oystersteel and Everose gold with a brown and black bezel, reference 126711CHNR, on an Oyster bracelet.")
add("gmt_pepsi", "gmt", "compare_table", "Which GMT are you?", "Pepsi or Bruce Wayne?", "gmt guide",
    cols=("Pepsi", "Bruce Wayne"), rows=[("Reference", "126710BLRO", "126710GRNR"), ("Bezel", "Blue and red", "Grey and black"), ("Bracelets", "Jubilee or Oyster", "Jubilee or Oyster")])
add("gmt_two", "gmt", "qa_card", "Which GMT are you?", "A two-tone GMT", "gmt guide",
    q="Is there a gold GMT-Master II?",
    a="Yes. Rolesor versions pair Oystersteel with yellow gold (reference 126713GRNR, Jubilee) or Everose gold (the Root Beer).")
add("gmt_use", "gmt", "qa_card", "Why it exists", "Why a GMT has two time zones", "v14",
    q="Why does the GMT-Master II show two time zones?",
    a="It was made for pilots flying between countries, to read home time and local time at once on one dial.")

# ---------------- what each Rolex was built for (v14)
add("built_sea", "guide", "ladder", "How deep?", "Three dive watches, three depths", "families guide",
    rungs=[("Submariner", "Waterproof to 300 metres."), ("Sea-Dweller", "Waterproof to 1,220 metres, with a helium escape valve."), ("Deepsea", "Waterproof to 3,900 metres.")])
add("built_for", "guide", "ladder", "Built for a purpose", "What each Rolex was made for", "v14",
    rungs=[("Daytona", "Motorsport, timing laps."), ("Submariner", "Diving."), ("GMT-Master II", "Pilots and travel."), ("Explorer", "Extreme conditions.")])
add("built_explorer", "guide", "qa_card", "Built for a purpose", "Explorer and Explorer II", "v14",
    q="What are the Explorer and Explorer II for?",
    a="The Explorer is for adventure: a high-contrast dial, a simple layout, and shock and temperature resistance. The Explorer II adds a day and night indicator, used by cave and polar researchers.")
add("built_dd", "guide", "myth_fact", "Gold only", "Does the Day-Date come in steel?", "families guide",
    myth="You can buy a Day-Date in steel.",
    fact="No. The Day-Date is made only in gold or platinum, on the President bracelet. It is the Rolex that spells out the day in full.")
add("first_rolex", "guide", "ladder", "Top picks for a first Rolex", "From entry to luxury", "v12",
    rungs=[("Datejust", "Green or Wimbledon dial. The everyday classic."), ("Submariner", "Black or green. The ultimate sport Rolex."),
           ("GMT-Master", "Batman or Bruce Wayne. The statement piece."), ("Daytona", "Panda or black dial. The iconic chronograph."), ("Day-Date", "The luxury level, on the President bracelet.")], confirm=True)
add("dj_combos", "guide", "steps", "Datejust", "The three combinations to know", "New 2",
    items=[("Jubilee bracelet, fluted bezel", "The original Datejust, since 1945. The most recognised."), ("Fluted bezel, Oyster bracelet", "Sportier, with a modern feel."), ("Jubilee bracelet, smooth bezel", "Clean, no flash.")])
add("dd_stone", "guide", "qa_card", "Day-Date dials", "What is a stone dial?", "v2",
    q="What is a stone dial on a Day-Date?",
    a="A dial cut from natural stone, such as eisenkiesel, onyx or even meteorite. No two are exactly the same.")

# ---------------- watch knowledge (complications from the owner's reel v11)
add("cx_list", "tech", "checklist", "Watch complications", "7 complications collectors know", "v11",
    items=[("Chronograph", "A stopwatch built into the watch."), ("GMT", "A second time zone."), ("Moon phase", ""), ("Annual calendar", ""), ("Perpetual calendar", ""), ("World timer", ""), ("Tourbillon", "")])
add("cx_chrono", "tech", "qa_card", "Watch complications", "What is a chronograph?", "v11",
    q="What is a chronograph?", a="Simply put, a stopwatch built into your watch. You start it, stop it and measure time. The Daytona is a chronograph.")
add("cx_gmt", "tech", "qa_card", "Watch complications", "What is a GMT?", "v11",
    q="What is a GMT watch?", a="It tracks a second time zone, so travelers can see local time and home time at the same time.")
add("cx_moon", "tech", "myth_fact", "Watch complications", "Moon phase", "v11",
    myth="A moon phase watch is just decoration.", fact="It shows the current phase of the moon on the dial, exactly what it sounds like. It is a complication, a mechanism of its own.")
add("cx_cal", "tech", "compare_table", "Watch complications", "Annual or perpetual calendar?", "v11",
    cols=("Annual", "Perpetual"), rows=[("It tracks", "Day, date and month", "Day, date, month and year"), ("Leap years", "No", "Yes"), ("Corrected", "Once a year, end of February", "Set once, accurate for decades")])
add("cx_world", "tech", "qa_card", "Watch complications", "What is a world timer?", "v11",
    q="What is a world timer?", a="It shows the time across 24 countries around the world all at once. A traveler's dream watch.")
add("cx_tourb", "tech", "qa_card", "Watch complications", "What is a tourbillon?", "v11",
    q="What is a tourbillon?", a="A tiny spinning cage that fights gravity to keep the watch accurate. One of the hardest things to make in watchmaking, and one of the most expensive.")

# ---------------- materials and parts (families guide labels)
add("mat_metals", "tech", "ladder", "Rolex metals", "Names you will hear", "families guide",
    rungs=[("Oystersteel", "Rolex steel."), ("Rolesor", "Steel combined with gold: yellow or Everose."), ("Everose gold", "Rolex's own rose gold."), ("Platinum", "Used on the top models, for example the Day-Date.")], confirm=True)
add("mat_bracelets", "tech", "ladder", "Rolex bracelets", "Oyster, Jubilee, President", "families guide",
    rungs=[("Oyster", "Submariner, GMT, Daytona."), ("Jubilee", "Datejust, Sky-Dweller, some GMT."), ("President", "Day-Date."), ("Oysterflex", "Yacht-Master rubber strap.")])
add("mat_bezel", "tech", "qa_card", "Rolex bezels", "Fluted, smooth or tachymetric?", "families guide",
    q="What are the main Rolex bezels?",
    a="Fluted or smooth on the Datejust, a rotating two-colour bezel on the GMT, a tachymetric bezel on the Daytona, and the Ring Command bezel on the Sky-Dweller.")
add("mat_size", "tech", "ladder", "Sizes", "Case sizes by family", "families guide",
    rungs=[("Datejust", "31 to 41 mm."), ("Submariner", "41 mm."), ("Daytona and GMT", "40 mm."), ("Sky-Dweller", "42 mm.")])
add("mat_dive", "tech", "myth_fact", "Waterproof", "Is every Rolex a diver?", "families guide",
    myth="Only the Submariner is waterproof.", fact="Every Oyster case is waterproof. What changes is the depth: 300 metres on the Submariner, 1,220 on the Sea-Dweller, 3,900 on the Deepsea.")
add("mat_ym", "tech", "qa_card", "Sailing", "What is a Yacht-Master?", "families guide",
    q="Which Rolex is the sailing watch?",
    a="The Yacht-Master (since 1992), with precious metals, Oysterflex straps and a bidirectional bezel. The Yacht-Master II (2007) adds a regatta countdown.")
add("mat_oyster", "tech", "myth_fact", "Colour", "Rolex only makes plain dials", "families guide",
    myth="Rolex dials are always black, white or blue.", fact="The Oyster Perpetual comes in colourful dials, such as pistachio, candy pink and blue, in sizes from 28 to 41 mm.")
add("mat_land", "tech", "qa_card", "The newest family", "What is the Land-Dweller?", "families guide",
    q="What is new about the Land-Dweller?",
    a="It is Rolex's newest family (2025), with the new Dynapulse escapement and an integrated bracelet, in 36 and 40 mm.")

# ---------------- why / how we work (his published why-buy slide)
add("why_us", "buy", "checklist", "Why buy with us", "7 reasons", "special/why-buy",
    items=[("A wide network", "Private owners and trusted suppliers."), ("Competitive prices", "So you never overpay."), ("Guidance", "Matched to your budget."), ("Verified", "Condition, date, dial, box and papers checked by experts."),
           ("Same-day sourcing", "Subject to availability."), ("Delivery anywhere in the UAE", "")])
add("hrs_find", "buy", "big_number", "Sourcing time", "1 to 48", "script-bank 06",
    big="1-48", unit="HOURS", text="Finding your watch can take from one hour up to forty-eight hours, depending on the watch. We tell you honestly which.")
add("dep_25", "buy", "big_number", "How the deposit works", "25", "script-bank 06",
    big="25", unit="% DEPOSIT", text="A twenty-five percent deposit confirms your order. The balance is paid when you have checked the watch, by bank transfer, cash or crypto.")
add("deliv", "buy", "timeline", "Delivery", "How it arrives", "script-bank 06",
    items=[("Same day", "In Dubai, with a private presentation."), ("24 to 48 hours", "Across the UAE."), ("You check the watch", "An independent check can be arranged."), ("Then you pay the balance", "")])
add("ask_card", "buy", "steps", "Before you pay", "Read your card in 3 steps", "batch2 C3",
    items=[("Check the date", "The five year guarantee starts on the date on the card."), ("Match reference and serial", "To the watch in your hand."), ("Look at the card itself", "If anything does not match, stop and ask before you pay.")])
add("dont_pay", "buy", "do_dont", "Quick rules", "Before paying", "daily 08",
    do=["See the watch first", "Ask for photos with today's date"], dont=["Pay in full first", "Trust papers alone"])

# ---------------- extra ideas from carousel data
add("fk_one", "fake", "big_number", "How many checks?", "12", "daily 06-07",
    big="12", unit="CHECKS", text="Twelve checks on dial, case, glow, numbers, papers, price and seller, ending with an independent check. None proves it alone. Use them together.")
add("ts_first", "buy", "quote_card", "Quote and compare", "Your reference point", "daily 08",
    quote="Get a boutique quote first. It is your reference point for every offer.", note="Then compare honestly.")

for x in L:
    if x["layout"] == "ladder" and "foot" not in x:
        x["foot"] = ""
assert len(L) >= 60, len(L)
ids = [x["id"] for x in L]
assert len(ids) == len(set(ids))
