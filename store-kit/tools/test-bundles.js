// Renders the bundle block with mock Shopify data and checks the click behaviour in Chromium.
const fs = require('fs'), path = require('path'), { Liquid } = require('liquidjs'), { chromium } = require('playwright');
const src = fs.readFileSync(path.join(__dirname, '../themesrc/ceylora-bundles.liquid'), 'utf8');
const liquidPart = src.split('{% stylesheet %}')[0];
const css = src.split('{% stylesheet %}')[1].split('{% endstylesheet %}')[0];
const engine = new Liquid();
engine.registerFilter('money', c => 'Dhs. ' + (c / 100).toFixed(2));
engine.registerFilter('image_url', (img) => img);
engine.registerFilter('image_tag', (url, ...args) => `<img src="${url}" class="ceylora-bundle__img">`);
const variants = [
  { id: 1, title: 'Buy 1 Bag', price: 10999, compare_at_price: 21999, available: true },
  { id: 2, title: 'Buy 2, Get 1 Free (3 Bags)', price: 21999, compare_at_price: 65999, available: true },
  { id: 3, title: 'Buy 3, Get 2 Free (5 Bags)', price: 32999, compare_at_price: 109999, available: true },
];
const sp = path.join(__dirname, '..', 'final');
const block = { shopify_attributes: '', settings: { heading: 'Choose your bundle',
  image_1: 'file://' + sp + '/ceylora-bundle-1.jpg', label_1: 'Buy 1 Bag', bags_1: 1, badge_1: '',
  image_2: 'file://' + path.join(__dirname, '../bg/raw_family.jpg'), label_2: 'Buy 2, Get 1 Free', bags_2: 3, badge_2: 'Recommended',
  image_3: 'file://' + sp + '/ceylora-bundle-1.jpg', label_3: 'Buy 3, Get 2 Free', bags_3: 5, badge_3: 'Best Value' } };
(async () => {
  const html = await engine.parseAndRender(liquidPart, { closest: { product: { variants, selected_or_first_available_variant: variants[0] } }, block });
  const picker = `<variant-picker><form>${variants.map(v => `<input type="radio" name="b" data-variant-id="${v.id}" ${v.id === 1 ? 'checked' : ''}>`).join('')}</form></variant-picker>
  <form action="/cart/add"><input name="id" value="1"></form>`;
  const page = `<!doctype html><html><head><style>body{font-family:sans-serif;width:520px;padding:20px;background:#fbf7f2}${css}</style></head>
    <body><div class="product-details">${html}${picker}</div></body></html>`;
  fs.writeFileSync(path.join(__dirname, '_bundles.html'), page);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 560, height: 420 } });
  await p.goto('file://' + path.join(__dirname, '_bundles.html'));
  const hidden = await p.evaluate(() => document.querySelector('variant-picker').getBoundingClientRect().width <= 1);
  await p.click('.ceylora-bundle[data-variant-id="2"]');
  const r1 = await p.evaluate(() => [...document.querySelectorAll('variant-picker input')].map(i => i.checked));
  await p.click('.ceylora-bundle[data-variant-id="3"]');
  const r2 = await p.evaluate(() => [...document.querySelectorAll('variant-picker input')].map(i => i.checked));
  const active = await p.evaluate(() => [...document.querySelectorAll('.ceylora-bundle')].map(c => c.classList.contains('is-active')));
  await p.screenshot({ path: path.join(__dirname, '..', 'bundles-test.png') });
  console.log('picker hidden:', hidden, '| after card 2:', r1, '| after card 3:', r2, '| active:', active);
  await b.close();
})();
