// Renders every ad in ads.js + ads2.js to ads/creative/<id>.png with a real browser.
// Usage:  npm install playwright && npx playwright install chromium   (first time only)
//         node creative/build.js            -> all ads
//         node creative/build.js m1-compare -> one ad
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const PAGES = path.join(__dirname, 'pages');
const OUT = path.join(ROOT, 'ads', 'creative');
const ads = [...require('./ads.js'), ...require('./ads2.js'), ...require('./ads5.js')];
// Campaign ads (ads3.js) render in both Meta sizes, plus any headline variations.
for (const c of [...require('./ads3.js'), ...require('./ads4.js')]) {
  for (const [label, h] of [['4x5', 1350], ['9x16', 1920]]) {
    ads.push({ ...c, id: `${c.id}_${label}`, size: [1080, h], html: c.render(h) });
  }
  (c.hooks || []).forEach((hl, i) => ads.push({ ...c, id: `${c.id}_hook${i + 2}_4x5`, size: [1080, 1350], html: c.render(1350, hl) }));
}

(async () => {
  fs.mkdirSync(PAGES, { recursive: true });
  fs.mkdirSync(OUT, { recursive: true });
  const only = process.argv[2];
  const browser = await chromium.launch();
  for (const ad of ads.filter(a => !only || a.id.startsWith(only))) {
    const [w, h] = ad.size || [1080, 1350];
    const html = `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../base.css">
<style>html,body{width:${w}px;height:${h}px} ${ad.css || ''}</style></head>
<body>${ad.html}</body></html>`;
    const file = path.join(PAGES, `${ad.id}.html`);
    fs.writeFileSync(file, html);
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    await page.goto('file://' + file);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    const dir = path.join(ROOT, 'ads', ad.outDir || 'creative');
    fs.mkdirSync(dir, { recursive: true });
    await page.screenshot({ path: path.join(dir, `${ad.id}.png`) });
    await page.close();
    console.log('saved', `ads/${ad.outDir || 'creative'}/${ad.id}.png`, `(${ad.stage} · ${ad.format})`);
  }
  await browser.close();
})();
