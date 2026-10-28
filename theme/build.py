import json
HDR="""/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 * ------------------------------------------------------------
 */
"""
def blocks(lst):
    b={};o=[]
    for i,(t,s) in enumerate(lst):
        k=f"b{i+1}";b[k]={"type":t,"settings":s};o.append(k)
    return b,o
def sec(type_,settings,bl=None):
    d={"type":type_,"settings":settings}
    if bl is not None:
        b,o=blocks(bl);d["blocks"]=b;d["block_order"]=o
    return d
WA="https://wa.me/971561853856?text=Hi%2C%20I%27m%20interested%20in%20your%20watches."
# ---------- kept sections (copied from live theme) ----------
hero={"type":"hero-banner","blocks":{
 "heading_rqk3m7":{"type":"heading","settings":{"heading":"Luxury Watches.\n\nWithout the Wait.","html_tag":"h2","heading_size_mobile":"text-4xl","heading_size_desktop":"md:text-6xl","heading_weight":"font-normal"}},
 "paragraph_nDhYxK":{"type":"paragraph","settings":{"paragraph":"<p>Rolex • Audemars Piguet • Patek Philippe</p><p>Brand New • Full Set • Same-Day Delivery in Dubai</p><p><strong>500+ watches delivered • 400+ happy clients</strong></p>","text_size_mobile":"text-base","text_size_desktop":"md:text-2xl","text_weight":"font-light"}},
 "button_GFKEMH":{"type":"button","settings":{"button_text":"View All Watches","button_link":"shopify://collections","show_button_mobile":True,"show_button_desktop":True,"button_style":"btn--secondary","custom_bg_color":"","custom_text_color":"","custom_border_color":"","custom_hover_color":"","custom_hover_border_color":"","custom_border_width":1}},
 "button_whatsapp":{"type":"button","settings":{"button_text":"Chat on WhatsApp","button_link":WA,"show_button_mobile":True,"show_button_desktop":True,"button_style":"btn--custom","custom_bg_color":"#25D366","custom_text_color":"#ffffff","custom_border_color":"#25D366","custom_hover_color":"#1ebe5a","custom_hover_border_color":"#1ebe5a","custom_border_width":1}}},
 "block_order":["heading_rqk3m7","paragraph_nDhYxK","button_GFKEMH","button_whatsapp"],
 "settings":{"image_desktop":"shopify://shop_images/config-launcher-watches-day-date-m228235-0055_2403jva_002.jpg","image_mobile":"shopify://shop_images/hero-mobile-day-date.jpg","overlay_color":"linear-gradient(90deg, #000000f2 20%, #0000 80%)","text_color":"#ffffff","align_mobile":"text-left justify-end items-start","align_desktop":"md:text-left md:justify-center md:items-start"}}
tb,to=blocks([("item",{"text":t}) for t in ["100% Authentic","Full Set, Box & Papers","Third-Party Authenticated","Same-Day Delivery in Dubai","Manufacturer Warranty"]])
trust={"type":"trust-bar","blocks":tb,"block_order":to,"settings":{"background_color":"#000000","text_color":"#ffffff","accent_color":"#d4af37"}}
feat={"type":"featured-collection","name":"Featured Collection","settings":{"title":"Ready for Same-Day Delivery in Dubai","heading_tag":"h2","heading_size_mobile":"text-2xl","heading_size_desktop":"md:text-3xl","heading_weight":"font-normal","heading_align_mobile":"text-center","heading_align_desktop":"md:text-left","collection":"frontpage","products_shown":12,"show_product_count":False,"show_button_mobile":False,"show_button_desktop":True,"button_label":"View all","button_style":"btn--primary","custom_bg_color":"","custom_text_color":"","custom_border_color":"","custom_hover_color":"","custom_hover_border_color":"","custom_border_width":1}}
signup={"type":"whatsapp-signup","name":"WhatsApp signup","settings":{"eyebrow":"New arrivals","heading":"Be the first to see new arrivals","text":"<p>Join our WhatsApp list and get new watches, prices and availability before they go on Instagram.</p>","button_text":"Join on WhatsApp","wa_message":"Hi, please add me to your New Arrivals list.","note":"No spam. Reply STOP anytime.","background_color":"#000000","text_color":"#ffffff"}}
# ---------- new sections ----------
mission=sec("awc-mission",{
 "eyebrow":"Our mission",
 "heading":"A watch dealer built by someone who worked inside Rolex.",
 "text":"<p>Buying a luxury watch should feel exciting, not stressful. But between multi-year waiting lists, inflated prices and sellers who pass off polished or altered watches as new, it is hard to know who to trust.</p><p>I started Advance Watch Co. to change that: expert guidance, fair prices published in AED, and brand new, authenticated watches, delivered with a private presentation.</p>",
 "button_1_text":"Shop watches in stock","button_1_link":"shopify://collections/all",
 "button_2_text":"Ask on WhatsApp","button_2_link":WA,
 "button_3_text":"Read the free guides","button_3_link":"#guides",
 "video":"shopify://files/videos/Advance Watch.mov","poster":"shopify://shop_images/WhatsApp_Image_2025-10-26_at_9.01.58_PM.jpg","video_tag":"Inside Advance Watch Co."},
 [("point",{"title":"Brand new, full set","text":"Box, papers and warranty card."}),
  ("point",{"title":"Multiple stages of authentication","text":"Third-party authentication on request."}),
  ("point",{"title":"Fair prices, published in AED","text":"Never “price on request”."}),
  ("point",{"title":"One personal contact","text":"From first message to private presentation."}),
  ("stat",{"number":"2019–23","label":"Inside Rolex, Dubai Mall"}),
  ("stat",{"number":"500+","label":"Watches delivered"}),
  ("stat",{"number":"400+","label":"Happy clients"})])
revs=[("WhatsApp_Image_2025-10-27_at_11.04.11.jpg","“Thanks again for the watch and the amazing buying experience. Would definitely get all our watches from you.”","Verified client · Rolex Datejust"),
 ("WhatsApp_Image_2025-10-28_at_8.57.20_PM.jpg","“I enjoyed working with you. I can only recommend. We will continue.”","Verified client · Datejust, blue dial"),
 ("WhatsApp_Image_2025-10-28_at_8.57.11_PM_1.jpg","“Got it fitted. Crazy watch man, thanks!”","Verified client · Datejust, mint green"),
 ("WhatsApp_Image_2025-10-27_at_11.04.04_1.jpg","“Thank you Tarek for this bad ass Rolex!”","Verified client"),
 ("WhatsApp_Image_2025-10-27_at_11.04.06.jpg","“Yes finished! Fits well.”","Verified client · AP Royal Oak"),
 ("WhatsApp_Image_2025-10-28_at_8.57.19_PM.jpg","“Wow, looks amazing!!”","Verified client · Datejust, Everose Rolesor"),
 ("WhatsApp_Image_2025-10-28_at_8.57.20_PM_1.jpg","“Thank you really much.”","Verified client · Rolex Day-Date"),
 ("WhatsApp_Image_2025-10-27_at_11.04.05.jpg","“Another watch added to the collection.”","@lukebatchelor__ · Day-Date 40"),
 ("WhatsApp_Image_2025-10-28_at_8.57.11_PM.jpg","“You know what time it is.”","@mrbrandowner · Private handover")]
rb=[("review",{"image":"shopify://shop_images/"+f,"quote":q,"author":a}) for f,q,a in revs]
rb.append(("review",{"video":"shopify://files/videos/IMG_6535_hero_desktop_horizontal.mp4","quote":"Client handover, caught on camera.","author":"Client handover"}))
reviews=sec("awc-reviews",{"eyebrow":"Client messages","heading":"What our clients say","text":"Real messages from real handovers. Tap a message to read it."},rb)
why=sec("awc-why",{"eyebrow":"Contact us","heading":"Contact Us to Buy Luxury Watches in Dubai",
 "text":"<p>Choose Advance Watch Co: where exceptional service meets an exclusive selection of the world’s most sought-after watches. Tell us the model, dial and budget you have in mind and we confirm availability, usually within a few hours.</p>",
 "us_label":"Advance Watch Co.","them_label":"Some sellers"},
 [("row",{"topic":"Condition","us":"Brand new, unworn, full set","them":"Polished, used watches sold as new"}),
  ("row",{"topic":"Originality","us":"Original dial, date and parts","them":"Dial or date changed, parts swapped"}),
  ("row",{"topic":"Authentication","us":"Multiple stages, third-party on request","them":"None, just “trust me”"}),
  ("row",{"topic":"Price","us":"Fair, published in AED","them":"Overpriced, or “price on request”"}),
  ("row",{"topic":"Service","us":"One dedicated contact, private presentation","them":"Anonymous chat, rushed handover"}),
  ("row",{"topic":"Payment","us":"25% deposit, balance on delivery","them":"Pay in full before you see anything"})])
F="shopify://shop_images/"
M=lambda n,p,i,u:("model",{"title":n,"price":p,"link":u,"image":F+i})
models=[M("Submariner","from AED 51,500","m126610ln-0001.webp","/pages/rolex-submariner-dubai"),
 M("Daytona","from AED 103,000","m126500ln-0001.webp","/pages/rolex-daytona-dubai"),
 M("GMT-Master II","from AED 67,000","m126710blro-0002.webp","/pages/rolex-gmt-master-ii-dubai"),
 M("Datejust 41","from AED 48,000","m126334-0028.webp","/pages/rolex-datejust-41-dubai"),
 M("Day-Date 40","from AED 210,000","m228238-0042_32d5b89f-b4e4-4a76-ab9b-b390ffdb3120.webp","/pages/rolex-day-date-40-dubai"),
 M("Sky-Dweller","from AED 80,000","m336934-0005.webp","/pages/rolex-sky-dweller-dubai"),
 M("Yacht-Master","from AED 93,500","m226627-0001.webp","/pages/rolex-yacht-master-dubai"),
 M("Land-Dweller","from AED 73,500","m127234-0001_1.webp","/pages/rolex-land-dweller-dubai"),
 M("Air-King","from AED 36,000","m126900-0001.webp","/pages/rolex-air-king-dubai")]
articles=sec("awc-learn",{"eyebrow":"Articles & research","heading":"Learn before you buy","text":"Straight answers from a former Rolex insider: prices, fakes, waiting lists and which model fits you.","dark":False,"blog":"guides","show_articles":True,"article_count":6,"models_title":"Tap a model to read its guide","models_link":"/pages/buy-rolex-dubai","models_link_text":"Prices for every model"},
 [(t,s) for t,s in models])
G=lambda n,p,u:("model",{"title":n,"price":p,"link":u,"image":F+"m126610ln-0001.webp"})
guides=sec("awc-learn",{"eyebrow":"Free guides","heading":"We give the value first","text":"Read, compare, then decide. Every guide is free and written to help you avoid scams and overpaying.","dark":True,"blog":"guides","show_articles":False,"models_title":"","models_link":"/blogs/guides","models_link_text":"All guides"},
 [("model",{"title":"Buy Rolex in Dubai","price":"Every model, price & checklist","link":"/pages/buy-rolex-dubai","image":F+"m126610ln-0001.webp"}),
  ("model",{"title":"Spot a fake Rolex","price":"12 checks before you pay","link":"/blogs/guides/how-to-spot-a-fake-rolex-dubai","image":F+"m126710blro-0002.webp"}),
  ("model",{"title":"Buy safely in Dubai","price":"10 steps, start to finish","link":"/blogs/guides/how-to-buy-a-rolex-safely-in-dubai","image":F+"m126500ln-0001.webp"}),
  ("model",{"title":"Rolex FAQ","price":"Your questions, answered","link":"/pages/rolex-faq-dubai","image":F+"m126334-0028.webp"})])
founder_text="<p>I’m a former Senior Sales Representative at Rolex with over four years in the luxury watch industry. I’ve personally assisted more than 10,000 clients, and learned what makes someone love a watch, and what makes a bad deal.</p><p>After seeing long waiting lists, high prices and delays in traditional retail, I founded Advance Watch Co. to give you a trusted, transparent and seamless way to own your dream watch.</p>"
offers=["A trusted, transparent process, so you buy with full confidence","Fair market pricing, no overpaying or guessing","Fast and secure delivery, no months of waiting","A personal luxury experience, you learn every detail of your watch","The peace of mind that every watch is brand new and authentic"]
steps=[("step",{"year":"2019","text":"Joined Rolex, Dubai Mall"}),("step",{"year":"2023","text":"Founded Advance Watch Co."}),("step",{"year":"Today","text":"500+ watches delivered"})]
founder=lambda gal: sec("awc-founder",{"image":F+"IMG-6227.jpg","badge_number":"10,000+","badge_label":"Clients served at Rolex","eyebrow":"Meet the founder","heading":"Hi, I’m Tarek.","text":founder_text,"button_text":"Our full story","button_link":"/pages/about-us","show_gallery":gal,
  **({"gal_1":F+"DSC1017-edited-scaled-2.jpg","gal_cap_1":"Every watch is inspected","gal_2":F+"WhatsApp_Image_2025-10-26_at_9.01.58_PM.jpg","gal_cap_2":"Unboxing at handover","gal_3":F+"6627af95f0be36627af4e88215_rolex-3jpg.webp","gal_cap_3":"A private presentation"} if gal else {})},
  steps+[("offer",{"text":o}) for o in offers])
faqs=[("What condition are the watches you sell?","<p>Most of our watches are unworn. For discontinued models, we can also source pre-owned and like-new watches.</p>"),
("Does the watch come with a box and papers?","<p>Yes. Our watches come as a full set, with box and papers.</p>"),
("Is there a manufacturer’s warranty?","<p>Yes, if the watch is less than 5 years old. Watches are sold with the remaining manufacturer guarantee, counted from the original purchase date. Rolex offers a 5-year worldwide guarantee.</p>"),
("How long does delivery take?","<p>Same-day delivery in Dubai, or 24–48 hours across the UAE, depending on the watch’s availability.</p>"),
("Why can’t I buy a luxury watch at the retail store?","<p>Retail shops have had little or no availability for years, with waiting lists of 2–8 years for some watches. The secondary market is where you can find almost any watch, at a premium price.</p>"),
("Do you only sell Rolex?","<p>No. Besides Rolex we offer Audemars Piguet, Patek Philippe, Richard Mille and other prestigious brands.</p>"),
("What do you mean by watch sourcing?","<p>We find the watch you want, even if it’s not in our collection. We search far and wide for the exact timepiece you’re looking for.</p>"),
("Do you buy or trade watches?","<p>Yes. Reach out and one of our team will assist you with the process.</p>"),
("What do I need to know before buying?","<p>Research the models, buy from a reputable dealer, check the condition, compare prices, ask for certification and warranty, and choose a seller with real after-sales support.</p>"),
("What payment methods do you accept?","<p>Bank transfer, cash, crypto and credit cards (applicable fees). A 25% deposit confirms your order, with the balance paid on delivery.</p>")]
faq=sec("awc-faq",{"eyebrow":"Good to know","heading":"Frequently asked questions","more_link":"/pages/rolex-faq-dubai","more_text":"All questions answered"},[("qa",{"q":q,"a":a}) for q,a in faqs])
def tpl(order):
    secs={};ord_=[]
    for k,v in order:
        secs[k]=v;ord_.append(k)
    return HDR+json.dumps({"sections":secs,"order":ord_},indent=2,ensure_ascii=False)
open('templates/index.json','w').write(tpl([("hero-banner",hero),("trust_bar",trust),("featured_collection",feat),("awc_mission",mission),("awc_reviews",reviews),("awc_why",why),("awc_articles",articles),("awc_guides",guides),("awc_founder",founder(False)),("awc_faq",faq),("whatsapp_signup",signup)]))
ah=sec("awc-about-hero",{"eyebrow":"About us","heading":"Luxury watches, bought with complete confidence.",
 "text":"<p>At Advance Watch Co., buying a watch is more than a transaction. It’s an experience. Choosing a timepiece should feel exciting, effortless and unforgettable, so we guide you every step of the way, with the confidence and clarity we would expect if we were the ones buying.</p>"},
 [("stat",{"number":"2019–23","label":"Inside Rolex, Dubai Mall"}),("stat",{"number":"500+","label":"Watches delivered"}),("stat",{"number":"400+","label":"Happy clients"}),("stat",{"number":"100%","label":"Brand new & authentic"})])
vals=sec("awc-values",{"eyebrow":"How we work","heading":"Our commitment to you"},
 [("value",{"title":"Expert guidance","text":"Advice shaped by years inside the brand, including an honest view of what is, and isn’t, worth the price."}),
  ("value",{"title":"Fair, open pricing","text":"Every price is published in AED. No games, no overpaying, no guessing."}),
  ("value",{"title":"Verified authenticity","text":"Brand new, full set, multiple stages of authentication. Verify it anywhere you choose."}),
  ("value",{"title":"Personal service","text":"One dedicated contact, from your first message to the private presentation of your watch."})])
open('templates/page.about.json','w').write(tpl([("awc_about_hero",ah),("awc_founder",founder(True)),("awc_values",vals),("awc_why",why),("awc_reviews",reviews),("whatsapp_signup",signup)]))
print("ok")
