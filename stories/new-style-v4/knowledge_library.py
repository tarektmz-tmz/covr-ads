"""Knowledge story library (42 different stories). Facts ONLY from the owner's confirmed notes:
 - private pages awc-knowledge-base-private, awc-course-knowledge-private (Q&A and key points, paraphrased, never the course text),
   awc-reel-queue-private, awc-reel-ideas-inbox-private (tiers)
 - reels/scripts/script-bank.md, carousels/daily/*/caption.txt, batch2_save_reels_v2.md, consult_reel_final.md
Rules: no investment promises, no invented stories, no made-up advice (the course lessons L11/L15 are NOT used).
'confirm': True = the wording still needs the owner's OK before posting (numbers of years, rules that vary, unpublished offer).
Each story has one topic; no fact is told twice."""

L = []


def add(id, layout, eyebrow, title, src, confirm=False, **kw):
    L.append(dict(id=id, layout=layout, eyebrow=eyebrow, title=title, src=src, confirm=confirm, **kw))


# ------------------------------------------------------------------ myth vs fact
add("seconds_hand", "myth_fact", "Know before you buy", "The seconds hand myth", "script-bank 02",
    myth="A smooth sweeping seconds hand proves a Rolex is real.",
    fact="The better fakes sweep too. Check the Cyclops (it magnifies the date 2.5 times), the tiny crown etched on the crystal at six o'clock, and the weight.")
add("first_come", "myth_fact", "How it really works", "The waiting list", "course L10",
    myth="The Rolex waiting list is first come, first served.",
    fact="It is not. Watches go to the clients with the strongest purchase history and loyalty, handed out by category.")
add("dealers_resellers", "myth_fact", "Straight answer", "Dealers and resellers", "course Q18",
    myth="Dealers only sell to resellers, never to people who want to wear the watch.",
    fact="Not true. Rolex is against the black market, and a salesperson cannot tell a reseller from a collector. Both come with passion for the brand.")
add("limit_production", "myth_fact", "Honest answer", "Does Rolex limit production?", "course Q19",
    myth="Rolex limits production on purpose to keep the waiting lists long.",
    fact="Nobody outside knows for sure. Demand jumped after the pandemic, and making more watches means training highly skilled watchmakers, which takes years. Rolex will not trade quality for short-term demand.")

# ------------------------------------------------------------------ checklists
add("three_checks", "checklist", "Checklist", "3 checks before you pay", "script-bank 01",
    items=[("Photos or a video of the exact watch", "With today's date, showing the reference and the serial number."),
           ("A full set that matches", "The numbers on the watch must match the card and the papers."),
           ("A recent warranty date", "A brand new watch should have a recent one.")])
add("red_flags", "checklist", "Stop and check", "5 red flags", "script-bank 07",
    items=[("A price far below the market", "Popular steel models rarely sell for much less."),
           ("Pressure to pay in full today", "A real seller lets you check first."),
           ("A used or polished watch sold as new", ""),
           ("A seller who refuses an independent check", "A genuine dealer agrees without a fuss."),
           ("A swapped watch", "They show you a genuine one but deliver another.")])
add("full_set", "checklist", "What is a full set?", "Box, card and papers", "carousel 12 + script-bank 03",
    items=[("The box", "Original box for the model."),
           ("The card", "The warranty card, with the date of the sale."),
           ("The papers", "Reference and serial must match the watch.")])
add("more_questions", "checklist", "Ask any dealer", "3 more questions", "carousel 02",
    items=[("Is an independent check possible?", "Before you pay the balance."),
           ("In what order do I pay?", "Know the payment order up front."),
           ("Are the prices clear, in AED?", "No surprise numbers later.")])
add("more_fake_checks", "checklist", "No single check proves it", "6 more checks", "carousel 07",
    items=[("The glow", ""), ("The numbers", ""), ("The papers", ""), ("The price", ""), ("The seller", ""),
           ("The independent check", "Finish with this one.")])
add("keep_everything", "checklist", "After you buy", "Keep everything", "script-bank 03",
    items=[("The card", ""), ("The papers", ""), ("The messages", "Keep the seller's messages too.")])

# ------------------------------------------------------------------ big number
add("five_years", "big_number", "The Rolex guarantee", "5", "script-bank 08",
    big="5", unit="YEARS", text="It starts on the date on the warranty card, the date of the sale. A recent date means most of it is still ahead of you.")
add("next_watch_timing", "big_number", "When to ask for your next watch", "1", "course L12",
    big="1", unit="MONTH", text="A first-time buyer waits about a month before asking about the next one. A seasoned collector, about two weeks.", confirm=True)
add("new_models_wait", "big_number", "New models", "5", "course Q23",
    big="5", unit="MONTHS", text="A brand new model can take up to about five months before it is officially on sale.", confirm=True)

# ------------------------------------------------------------------ Q&A card
add("walk_in_daytona", "qa_card", "Ask us anything", "Why can't I just walk in and buy a Daytona?", "script-bank 04",
    q="Why can't I just walk in and buy a Daytona?",
    a="Demand is much bigger than supply. Boutiques have waiting lists, and in our experience clients with a purchase history are offered the watches first.")
add("display_not_sale", "qa_card", "Ask us anything", "Why are the watches on display not for sale?", "course Q20",
    q="Why are the Rolex watches on display not for sale?",
    a="At one time people bought anything on display and stores were left empty, which hurt the brand image. Now the display stays, so a sold-out store still looks full and clients can see the watches and place orders.")
add("card_changed", "qa_card", "Good to know", "Did the Rolex card change?", "KB confirmed",
    q="Did the Rolex warranty card change?",
    a="Yes. The card, green seal and tag changed in mid-April 2026 (a wood-grain look, and the tag is back to green). There was an earlier change around 2020.")
add("found_elsewhere", "qa_card", "Ask us anything", "Found a Rolex somewhere else?", "script-bank 12",
    q="I found a Rolex somewhere else and I am not sure about it.",
    a="Send us the photos. We tell you honestly what we see, with no obligation. Look at the reference, serial, card and price, and ask the seller for an independent check.")
add("other_brands", "qa_card", "Ask us anything", "Do you only sell Rolex?", "script-bank 11",
    q="Do you only sell Rolex?",
    a="No. We also offer Patek Philippe and Audemars Piguet. Patek prices move, so we give the exact price for the exact reference on WhatsApp.")
add("new_or_preowned", "qa_card", "Ask us anything", "Are the watches new?", "KB confirmed",
    q="Are your watches brand new?",
    a="Mostly brand new. For discontinued models we can source pre-owned or like-new pieces, and we always say clearly which.")
add("buy_trade", "qa_card", "Ask us anything", "Do you also buy and trade?", "script-bank 10",
    q="Do you also buy and trade watches?",
    a="Yes, we also buy and trade watches. Message us the watch you have and what you are looking for.")
add("best_dealer", "qa_card", "Ask us anything", "Which dealer is best?", "course L9",
    q="Which Rolex dealer is best, big or small?",
    a="Bigger is not always better. In our observation, clients at small dealerships were often more satisfied and received watches faster. Check reputation and service.")
add("out_of_catalogue", "qa_card", "Ask us anything", "What are out-of-catalogue watches?", "course Q24",
    q="How do you get an out-of-catalogue watch?",
    a="They are not for the general public and are made in very small numbers. They go to clients with a long purchase history and a strong relationship with a dealer.")

# ------------------------------------------------------------------ compare table
add("boutique_vs_dealer", "compare_table", "Side by side", "Boutique list or dealer?", "script-bank 05",
    cols=("Boutique", "Dealer"),
    rows=[("Route", "The official one", "Sourced for you"), ("Wait", "Can be long, no promise", "Speed and choice"),
          ("Price", "Retail", "Above retail"), ("Tip", "Get this quote first", "Compare honestly")])
add("new_client_first", "compare_table", "New client", "Datejust or Daytona first?", "course L4 + L13",
    cols=("Datejust", "Daytona / GMT"),
    rows=[("For a new client", "The normal first model", "High demand, history first"),
          ("What it does", "Builds your profile", "Offered to loyal clients"),
          ("Ask in store", "Yes, ask about it", "Do not open with it")])
add("reselling", "compare_table", "Before you sell", "Selling your Rolex", "course Q22",
    cols=("Too fast", "Safer"),
    rows=[("Timing", "Within about 2 months looks like flipping", "Keep it at least a year"),
          ("Frequency", "Buying and selling often", "Buy and sell rarely"),
          ("Who to sell to", "A dealer can see the watch history", "An end user")], confirm=True)

# ------------------------------------------------------------------ steps
add("how_we_work", "steps", "How buying from us works", "5 steps, no surprises", "script-bank 06",
    items=[("You tell us the watch you want", ""), ("We find it", "From 1 hour up to 48 hours, depending on the watch"),
           ("A 25% deposit confirms the order", ""), ("We deliver to your door", "Same day in Dubai, 24 to 48 hours across the UAE"),
           ("You check it, then pay the balance", "Bank transfer, cash or crypto. Independent check on request.")])
add("build_profile", "steps", "Step by step", "Build your Rolex profile", "batch2 C5",
    items=[("Start with a Datejust", "The normal first model."),
           ("Buy for family through your profile", "A ladies' Datejust or a Day-Date 36 builds history without hurting your sports-model chance."),
           ("Stay with one salesperson", "Loyalty gets noticed."), ("Be polite and patient", "Pushing does the opposite."),
           ("Tell them your plan", "Share what you want next.")])
add("relationship", "steps", "Be a client they remember", "Build the relationship", "course L6-L8",
    items=[("Show long-term interest", ""), ("Learn the brand's history", ""), ("Share your wishlist", ""),
           ("Ask for their advice", ""), ("Small gestures help", "A small gift keeps you top of mind.")])

# ------------------------------------------------------------------ timeline
add("new_release_path", "timeline", "A new Rolex reaches the store", "From Switzerland to the wishlist", "course Q23",
    items=[("Watches and Wonders", "Unveiled in Switzerland. Only a few selected people try it."),
           ("Display pieces", "Sent without a movement to selected stores, mostly the bigger dealers."),
           ("The wishlist opens", "Clients with the longest purchase history come first."),
           ("On sale", "Ask for one piece only.")], confirm=True)
add("demand_story", "timeline", "Why it changed", "From walk-in to waiting list", "course L2",
    items=[("Before 2019", "You could walk in and buy a Rolex."), ("The pandemic", "People bought to sell, and resellers pushed prices up."),
           ("The bubble", "Prices kept growing, then it burst and prices dropped."), ("Today", "Focus is back on the steel sports models.")])
add("followup_first", "timeline", "Your first Datejust order", "The follow-up schedule", "course L14",
    items=[("1 month", "First follow-up."), ("2 weeks later", "Follow up again."), ("2 to 3 months", "The watch arrives.")], confirm=True)
add("followup_sports", "timeline", "High-demand sports models", "How often to follow up", "course L14",
    items=[("After 3 months", "First follow-up."), ("Every 3 to 4 months", "Then keep it polite and steady."),
           ("Be patient", "These can take years.")], confirm=True)

# ------------------------------------------------------------------ quote card
add("papers_not_proof", "quote_card", "Papers", "Papers help", "script-bank 03",
    quote="Papers help, but they are never the proof on their own.", note="Boxes and cards can be faked, and real papers can be swapped onto another watch.")
add("lose_deal", "quote_card", "Think about it", "Lose a deal", "script-bank 12 + carousel 09",
    quote="Better to lose a deal than to lose your money.", note="If you see a red flag, stop and check.")
add("unrealistic_promises", "quote_card", "Be wary", "Big promises", "course Q21",
    quote="A dealer who promises a sports model on an unrealistic timeline is probably not being honest.", note="Supply and demand cannot be talked away.", confirm=True)
add("first_date", "quote_card", "In the boutique", "The first-date rule", "course L4",
    quote="Asking for a Submariner or a Daytona on your first visit is like proposing on a first date.", note="Ask about the normal models first.")
add("lifetime", "quote_card", "A thought", "A watch for a lifetime", "course L3 (no value promise)",
    quote="A Rolex is a watch you can wear for a lifetime and pass on.", note="Buy the one you love to wear.")
add("no_single_check", "quote_card", "Authenticity", "Use the checks together", "carousel 06",
    quote="No single check proves a watch is real. Use them together.", note="Then finish with an independent check.")
add("ask_expert", "quote_card", "Before a big purchase", "Ask an expert first", "consult reel",
    quote="The right watch can hold its value. The wrong one can lose twenty-five to fifty percent.", note="Ask an expert before you buy, not after.", confirm=True)

# ------------------------------------------------------------------ ladder
add("wait_tiers", "ladder", "How hard is it to get?", "Waiting time by tier", "KB tiers (approximate)",
    rungs=[("Impossible", "About 5 years. Daytona steel, GMT-Master Pepsi."), ("Hard", "About 2 to 3 years."),
           ("Medium", "About 1 year."), ("Easy", "A few months, often available.")], confirm=True)
# ------------------------------------------------------------------ do and don't
add("boutique_phrases", "do_dont", "In the boutique", "What to say and not say", "course L4",
    do=["Ask what is available in men's models", "Ask about the normal models"],
    dont=["“Is there one at the back?”", "“Has anyone cancelled?”"])
add("dress_code", "do_dont", "Make a good impression", "How you show up", "course L5-L6",
    do=["Dress respectfully", "Be polite and patient"], dont=["Push or rush the salesperson", "Go from salesperson to salesperson"])
add("haggle", "do_dont", "Before you pay", "Chasing the cheapest deal", "consult reel",
    do=["Pay a little more for peace of mind", "Get a trusted third-party authentication"],
    dont=["Haggle over a couple of hundred dollars", "Risk a polished, changed-date or changed-dial watch, or a fake box"])
assert len(L) >= 40, len(L)
ids = [x["id"] for x in L]
assert len(ids) == len(set(ids))
