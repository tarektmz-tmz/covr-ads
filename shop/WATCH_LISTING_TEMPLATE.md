# Watch listing template (owner order Nov 22: fill EVERY field, same as the other watches)
Reference product copied from: Rolex Oyster Perpetual 41 134300 Blue Dial (gid .../Product/7308265553991). Done example: .../Product/9191440678983 (Celebration Dial, AED 75,000).

## Steps (in this order)
1. productCreate: title "Rolex <Model> <Ref> – <Metal>, <Dial> Dial[, Bracelet]", vendor Rolex, productType "Luxury Watches", handle from title, status ACTIVE, collectionsToJoin (Rolex Watches 280723718215 + model collections), descriptionHtml (3 paragraphs: heading <p><strong>Rolex <Model> with <Dial> Dial</strong></p>, case/bracelet paragraph, dial paragraph, movement/waterproof paragraph; same wording pattern as the other watches; add 'Brand new condition.').
2. productUpdate category = gid://shopify/TaxonomyCategory/aa-6-11 (Apparel & Accessories > Jewelry > Watches). MUST come before the shopify.* metafields.
3. productVariantsBulkUpdate: price, sku = reference, inventoryPolicy DENY, tracked false.
4. metafieldsSet (16 fields): custom.model, reference, dial_color, watch_size, case_material, bezel_material, bracelet_material, movement, water_resistant ('Waterproof to 100 metres / 330 feet' for OP/Datejust/etc: use the model's real value), gender, condition ('Unworn'), comes_with ('Original Box & Certificates'); shopify.age-group, target-gender, watch-display, watch-features (list.metaobject_reference: copy the same metaobject ids from a finished sibling watch of the same type: age 155141931079, gender 155142062151, display 155141963847, features 155141898311/155142094919/155143045191 for the OP 41 line; check siblings for other models).
5. Image: 1920x1920 transparent square, watch trimmed and centred, about 97 percent of the height (top margin about 39 px), webp; host at a public URL (repo reels/publish/shop/) and add with productUpdate(media:[...]); then fileDelete any wrong earlier image.
6. publishablePublish to the 3 publications: Online Store 117694201927, Point of Sale 117694234695, Google & YouTube 213112913991.
7. Verify: product status, 16 metafields, one 1920x1920 image, onlineStoreUrl, collections.
Facts only from the owner or Rolex's own page; never invent specs.

## Standing task: set a price from a screenshot
Tarek sends a screenshot (or reference) and says the price. Do it without asking again:
1. Find the product in Shopify by reference / model / dial in the screenshot.
2. Set the variant price (AED) to the number he gave.
3. Set custom.hide_price = false so the price shows instead of "Request price on WhatsApp".
4. Check the product is ACTIVE and published, then reply in one line: done, with the link.
If the screenshot matches more than one listing (same reference, different dial), ask which one.
