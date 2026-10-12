// "Did you know?" — 3 treatments of the same copy, clearer photos, 2x resolution.
const { frame } = require('./ads.js').helpers;
const COPY = {
  kick: 'Did you know?',
  head: 'Your racket spends more time in a bag than on court.',
  body: 'So make it a good one. COVR’s cotton and leather keep direct sun and scuffs off your racket.',
};
const text = (color, kick, sub, w = 960) => `
  <div class="serif" style="font-size:118px;line-height:1;color:${kick}"><em>${COPY.kick}</em></div>
  <div style="font-family:Montserrat;font-weight:800;font-size:64px;line-height:1.08;letter-spacing:-.02em;color:${color};margin-top:24px;max-width:${w}px">${COPY.head}</div>
  <div style="font-size:29px;line-height:1.45;color:${sub};margin-top:22px;max-width:780px">${COPY.body}</div>`;
const ads = [];
const add = a => ads.push({ outDir: 'didyouknow', scale: 2, stage: 'TOFU', ...a });

/* A — Clean split: solid panel, photo below with a straight edge. Nothing blends. */
add({
  id: 'dyk-a-clean-split', format: 'Clean split',
  css: `body{background:#2a2420}`,
  html: `
    <div class="abs" style="left:64px;right:64px;top:64px">${text('#fff', '#d9b07c', 'rgba(255,255,255,.72)')}</div>
    ${frame('latte-bench-clean.jpg', 0.5, 0.6, 1.0, 0, 480, 1080, 870).html}
    <div class="abs" style="left:0;right:0;top:480px;height:6px;background:#d9b07c"></div>
    <div class="logo abs" style="right:56px;bottom:50px;color:#fff;font-size:38px;text-shadow:0 2px 10px rgba(0,0,0,.4)">COVR</div>`,
});

/* B — Full-bleed photo, long soft fade into the text. */
add({
  id: 'dyk-b-soft-fade', format: 'Soft fade',
  html: `
    ${frame('latte-shoulder-court.jpg', 0.5, 0.6, 1.0, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(36,26,20,.94) 0%,rgba(36,26,20,.86) 30%,rgba(36,26,20,.45) 48%,rgba(36,26,20,0) 66%)"></div>
    <div class="abs" style="left:64px;right:64px;top:64px">${text('#fff', '#f0d2a8', 'rgba(255,255,255,.82)')}</div>
    <div class="logo abs" style="right:56px;bottom:50px;color:#fff;font-size:38px;text-shadow:0 2px 10px rgba(0,0,0,.4)">COVR</div>`,
});

/* C — Editorial card: cream page, photo as a framed print. */
add({
  id: 'dyk-c-framed-card', format: 'Framed card',
  css: `body{background:#f3ede3}`,
  html: `
    <div class="abs" style="left:64px;right:64px;top:60px">${text('#1d1a17', '#9b6b3e', '#5d5750')}</div>
    ${frame('latte-unboxing-hands.jpg', 0.5, 0.45, 1.0, 64, 600, 952, 680, 'border-radius:24px;box-shadow:0 30px 60px rgba(60,40,20,.22)').html}
    <div class="logo abs" style="left:0;right:0;bottom:22px;text-align:center;color:#9b6b3e;font-size:30px">COVR</div>`,
});

/* B variants — same soft-fade treatment, other photos. */
for (const [id, n, cx, cy, z] of [
  ['dyk-b2-bench', 'latte-bench-clean.jpg', 0.5, 0.62, 1.0],
  ['dyk-b3-card', 'latte-thankyou-card.jpg', 0.5, 0.4, 1.3],
  ['dyk-b4-unboxing', 'IMG_8776.jpg', 0.47, 0.42, 1.15],
]) add({
  id, format: 'Soft fade',
  html: `
    ${frame(n, cx, cy, z, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(36,26,20,.94) 0%,rgba(36,26,20,.86) 30%,rgba(36,26,20,.45) 48%,rgba(36,26,20,0) 66%)"></div>
    <div class="abs" style="left:64px;right:64px;top:64px">${text('#fff', '#f0d2a8', 'rgba(255,255,255,.82)')}</div>
    <div class="logo abs" style="right:56px;bottom:50px;color:#fff;font-size:38px;text-shadow:0 2px 10px rgba(0,0,0,.4)">COVR</div>`,
});
module.exports = ads;
