// Renders a transparent 90-day money-back badge PNG.
const fs = require('fs'), path = require('path'), { chromium } = require('playwright');
const f = w => 'file://' + path.join(__dirname, `node_modules/@fontsource/poppins/files/poppins-latin-${w}-normal.woff2`);
const html = `<!doctype html><html><head><style>
@font-face{font-family:P;font-weight:700;src:url(${f(700)})}@font-face{font-family:P;font-weight:800;src:url(${f(800)})}
html,body{margin:0;background:transparent}
.b{width:600px;height:600px;border-radius:50%;background:#b8673a;display:flex;align-items:center;justify-content:center;font-family:P}
.i{width:540px;height:540px;border-radius:50%;border:6px dashed rgba(255,255,255,.75);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;box-sizing:border-box}
</style></head><body><div class="b"><div class="i">
<div style="font-size:46px;font-weight:700;letter-spacing:6px">MONEY BACK</div>
<div style="font-size:200px;font-weight:800;line-height:.95">90</div>
<div style="font-size:64px;font-weight:800;letter-spacing:10px;line-height:1">DAY</div>
<div style="font-size:46px;font-weight:700;letter-spacing:6px;margin-top:10px">GUARANTEE</div>
</div></div></body></html>`;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:600,height:600}});const t=path.join(__dirname,'_badge.html');fs.writeFileSync(t,html);await p.goto('file://'+t);await p.evaluate(()=>document.fonts.ready);await p.locator('.b').screenshot({path:path.join(__dirname,'..','final','ceylora-90-day-badge.png'),omitBackground:true});await b.close();console.log('ok')})();
