// Renders every ad in ads.js to ads/creative/<id>.png with a real browser.
// Usage:  npm install playwright && npx playwright install chromium   (first time only)
//         node creative/build.js            -> all ads
//         node creative/build.js m1-compare -> one ad
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const PAGES = path.join(__dirname, 'pages');
const OUT = path.join(ROOT, 'ads', 'creative');
const ads = require('./ads.js');

(async () => {
  fs.mkdirSync(PAGES, { recursive: true });
  fs.mkdirSync(OUT, { recursive: true });
  const only = process.argv[2];
  const browser = await chromium.launch();
  for (const ad of ads.filter(a => !only || a.id === only)) {
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
    await page.screenshot({ path: path.join(OUT, `${ad.id}.png`) });
    await page.close();
    console.log('saved', `ads/creative/${ad.id}.png`, `(${ad.stage} · ${ad.format})`);
  }
  await browser.close();
})();
