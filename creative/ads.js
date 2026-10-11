// COVR ad designs. Each ad = { id, stage, format, html, css? }. Rendered at 1080x1350 by build.js.
// Facts only from data/products.json and padelcovr.com copy. No invented reviews, offers or certifications.
const SIZES = require('./media-sizes.json');
const src = n => `../../media/${n}`;

// Crop any region of a photo into a box. cx,cy = point of the photo (0..1) to centre on,
// zoom = photo width as a multiple of the box width.
function crop(n, cx, cy, zoom, w, h) {
  const [W, H] = SIZES[n];
  zoom = Math.max(zoom, 1, (h * W) / (H * w)); // always cover the box, never leave gaps
  const iw = w * zoom, ih = iw * H / W;
  const left = Math.min(0, Math.max(w - iw, w / 2 - cx * iw));
  const top = Math.min(0, Math.max(h - ih, h / 2 - cy * ih));
  return {
    img: `<img src="${src(n)}" style="position:absolute;max-width:none;width:${iw}px;height:${ih}px;left:${left}px;top:${top}px">`,
    at: (fx, fy) => [left + fx * iw, top + fy * ih], // photo point -> box px
  };
}
function frame(n, cx, cy, zoom, x, y, w, h, style = '') {
  const c = crop(n, cx, cy, zoom, w, h);
  return {
    html: `<div class="photo" style="left:${x}px;top:${y}px;width:${w}px;height:${h}px;${style}">${c.img}</div>`,
    at: (fx, fy) => { const [px, py] = c.at(fx, fy); return [x + px, y + py]; },
  };
}
function circle(n, cx, cy, zoom, d, x, y, style = '') {
  const c = crop(n, cx, cy, zoom, d, d);
  return `<div class="circle" style="left:${x}px;top:${y}px;width:${d}px;height:${d}px;${style}">${c.img}</div>`;
}
const X = `<span class="mark no"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></span>`;
const V = `<span class="mark yes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>`;
const ARROW = `<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>`;
const logo = (style = '') => `<div class="logo abs" style="${style}">COVR</div>`;

const ads = [];

/* ───────────────────────── TOFU ───────────────────────── */

// Billboard: one huge message, product, nothing else.
{
  const p = frame('IMG_0572.JPG', 0.55, 0.47, 1.55, 0, 560, 1080, 790);
  ads.push({
    id: 't1-billboard-zero-protection', stage: 'TOFU', format: 'Billboard',
    html: `
      <div class="abs" style="left:72px;top:78px">
        <div class="mega" style="font-size:132px">$300 racket.</div>
        <div class="mega tan" style="font-size:132px">Zero</div>
        <div class="mega tan" style="font-size:132px">protection?</div>
      </div>
      ${p.html}
      <div class="abs" style="left:0;right:0;bottom:0;height:150px;background:linear-gradient(transparent,rgba(0,0,0,.45))"></div>
      <div class="kicker abs" style="left:72px;bottom:62px;color:#fff">Premium protection for padel</div>
      ${logo('right:72px;bottom:56px;color:#fff;font-size:40px')}`,
  });
}

// Billboard on photo.
ads.push({
  id: 't2-billboard-protect', stage: 'TOFU', format: 'Billboard',
  html: `
    ${frame('IMG_8754.jpg', 0.5, 0.56, 1.0, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,rgba(14,12,10,.82) 0%,rgba(14,12,10,.45) 36%,transparent 58%)"></div>
    <div class="abs" style="left:72px;top:96px;color:#fff">
      <div class="mega" style="font-size:118px">Protect</div>
      <div class="mega" style="font-size:118px">what you</div>
      <div class="mega" style="font-size:118px;color:var(--tan-light)">play with.</div>
    </div>
    ${logo('right:72px;bottom:70px;color:#fff')}`,
});

// Meme (posted as COVR's own account, no fake engagement numbers).
ads.push({
  id: 't3-meme-naked-in-the-boot', stage: 'TOFU', format: 'Meme',
  css: `.tw{position:absolute;left:60px;right:60px;top:70px;background:#fff;border-radius:34px;padding:52px 56px;box-shadow:0 20px 60px rgba(0,0,0,.08)}`,
  html: `
    <div class="tw">
      <div style="display:flex;align-items:center;gap:22px">
        <div style="width:92px;height:92px;border-radius:50%;background:var(--ink);color:var(--paper);display:flex;align-items:center;justify-content:center;font-family:'Instrument Serif';font-size:52px">C</div>
        <div><div style="font-weight:600;font-size:32px">COVR</div><div style="color:var(--stone);font-size:27px">@padelcovr</div></div>
      </div>
      <div style="font-size:44px;line-height:1.34;margin:38px 0 34px;font-weight:400">
        Padel players:<br>
        <b style="font-weight:600">· buys a $400 racket</b><br>
        <b style="font-weight:600">· throws it naked in the car boot</b><br>
        · wonders why it looks tired by March
      </div>
      <div style="position:relative;height:640px;border-radius:24px;overflow:hidden">
        ${crop('IMG_9618.JPG', 0.55, 0.42, 1.45, 844, 640).img}
        <div style="position:absolute;left:28px;bottom:26px;background:rgba(255,255,255,.92);border-radius:999px;padding:12px 26px;font-weight:600;font-size:25px">Be the other kind of padel player.</div>
      </div>
    </div>`,
});

// News mock-up: clearly COVR's own editorial, labelled as such.
ads.push({
  id: 't4-news-forgetting-this', stage: 'TOFU', format: 'News mock-up',
  css: `body{background:var(--paper)}`,
  html: `
    <div class="abs" style="left:72px;right:72px;top:62px;border-bottom:2px solid var(--ink);padding-bottom:22px;display:flex;justify-content:space-between;align-items:flex-end">
      <div class="serif" style="font-size:58px;letter-spacing:.02em">The COVR Journal</div>
      <div class="kicker" style="font-size:16px;color:var(--stone)">COVR editorial</div>
    </div>
    <div class="kicker abs tan" style="left:72px;top:182px;font-size:19px">Padel · Gear</div>
    <div class="serif abs" style="left:72px;right:72px;top:224px;font-size:82px;line-height:1.02">
      Padel players are spending hundreds on rackets <em class="tan">— and forgetting this.</em>
    </div>
    ${frame('IMG_8776.jpg', 0.48, 0.5, 1.0, 72, 520, 936, 640).html}
    <div class="abs" style="left:72px;right:72px;top:1190px;display:flex;justify-content:space-between;align-items:center">
      <div style="font-size:23px;color:var(--stone);max-width:640px;line-height:1.4">Natural canvas, leather trim and a waterproof lining. Shipped in a box and dust bag.</div>
      <div style="font-weight:600;font-size:24px;display:flex;align-items:center;gap:10px">Read more ${ARROW}</div>
    </div>`,
});

// Did you know? (Safe, true observation. No unverified science.)
ads.push({
  id: 't5-did-you-know-bag', stage: 'TOFU', format: 'Did you know?',
  css: `body{background:var(--char);color:var(--paper)}`,
  html: `
    <div class="serif abs" style="left:72px;top:70px;font-size:128px;color:var(--tan-light)"><em>Did you know?</em></div>
    <div class="abs" style="left:72px;right:72px;top:250px;font-family:Montserrat;font-weight:800;font-size:68px;line-height:1.05;letter-spacing:-.02em">
      Your racket spends more time in a bag than on court.
    </div>
    <div class="abs body" style="left:72px;right:300px;top:500px;color:rgba(250,247,242,.72)">So make it a good one. COVR's cotton and leather keep direct sun and scuffs off your racket.</div>
    ${frame('IMG_0582.JPG', 0.6, 0.53, 2.05, 0, 690, 1080, 660).html}
    <div class="abs" style="left:0;right:0;top:690px;height:120px;background:linear-gradient(var(--char),transparent)"></div>
    ${logo('right:72px;bottom:62px;color:var(--ink)')}`,
});

/* ───────────────────────── MOFU ───────────────────────── */

// Comparison (website copy, COVR vs other covers).
{
  const rows = [
    ['IMG_0583.JPG', 0.51, 0.68, 4.2, 'Built with protection in mind.', 'Cotton and leather keep direct sun and scuffs off your racket.'],
    ['IMG_0572.JPG', 0.73, 0.38, 5.0, 'Made for everyday carrying.', 'Zip pocket, adjustable strap and carry handle.'],
    ['IMG_0617.JPG', 0.31, 0.505, 5.5, 'Premium materials that last.', 'Cotton, leather and metal hardware, built for long-term use.'],
    ['IMG_9618.JPG', 0.79, 0.33, 4.6, 'Open-back handle design.', 'Lets your grip breathe after play.'],
  ];
  const others = ['Thin nylon, little insulation', 'Little between racket and kit', 'Polyester that loses its shape', 'Often no pocket, strap or handle'];
  ads.push({
    id: 'm1-compare-covr-vs-others', stage: 'MOFU', format: 'Comparison',
    css: `body{background:var(--paper)}`,
    html: `
      <div class="abs" style="left:64px;top:70px">
        <div class="mega" style="font-size:78px">Your padel</div>
        <div class="mega" style="font-size:78px">racket</div>
        <div class="mega tan" style="font-size:78px">deserves</div>
        <div class="mega tan" style="font-size:78px">better.</div>
      </div>
      ${frame('IMG_0617.JPG', 0.5, 0.5, 1.5, 660, 0, 420, 470).html}
      <div class="abs" style="left:0;top:470px;width:380px;bottom:0;background:#d8d1c6;padding:54px 40px 0 48px">
        <div class="h3" style="font-size:31px;font-weight:800;text-transform:uppercase">Other racket covers</div>
        <div class="kicker" style="font-size:15px;margin:12px 0 44px;color:#57524b">Basic protection.</div>
        ${others.map(t => `<div style="display:flex;gap:20px;align-items:center;margin-bottom:46px;font-size:25px;line-height:1.3;color:#3d3934">${X}<span>${t}</span></div>`).join('')}
      </div>
      <div class="abs" style="left:380px;top:470px;right:0;bottom:0;padding:50px 50px 0 48px">
        <div class="logo" style="font-size:44px">COVR</div>
        <div class="kicker" style="font-size:15px;margin:14px 0 34px">Premium protection.</div>
        ${rows.map(([n, cx, cy, z, h, t]) => `
          <div style="display:flex;gap:28px;align-items:center;margin-bottom:26px">
            <div style="position:relative;width:150px;height:150px;flex:none">${circle(n, cx, cy, z, 150, 0, 0)}</div>
            <div><div class="h3" style="font-size:27px">${h}</div><div style="font-size:22px;line-height:1.36;color:#4a4540;margin-top:6px">${t}</div></div>
          </div>`).join('')}
      </div>`,
  });
}

// Anatomy / feature callouts.
{
  const p = frame('IMG_0572.JPG', 0.56, 0.47, 1.95, 300, 250, 480, 1040, 'border-radius:300px 300px 24px 24px');
  const callouts = [
    // [photo point, circle x,y, label, text, circle crop]
    [[0.80, 0.355], 860, 300, 'Open-back leather collar', 'Lets your grip breathe after play.', ['IMG_0572.JPG', 0.80, 0.355, 5.2]],
    [[0.46, 0.43], 40, 420, 'Front zip pocket', 'Phone, keys and cards.', ['IMG_0572.JPG', 0.45, 0.43, 5.5]],
    [[0.72, 0.405], 860, 760, 'D-ring', 'Clip on a COVR ball pouch.', ['IMG_0572.JPG', 0.72, 0.40, 6.5]],
    [[0.42, 0.70], 40, 880, 'Adjustable strap', 'Carry it by hand or on your back.', ['IMG_0572.JPG', 0.40, 0.72, 5.5]],
  ];
  const lines = callouts.map(([[fx, fy], cx, cy]) => {
    const [px, py] = p.at(fx, fy);
    const sx = cx < 540 ? cx + 182 : cx;  // line leaves the circle edge facing the photo
    return `<line x1="${sx}" y1="${cy + 91}" x2="${px}" y2="${py}" stroke="#161412" stroke-width="2"/><circle cx="${px}" cy="${py}" r="9" fill="#fff" stroke="#161412" stroke-width="3"/>`;
  }).join('');
  ads.push({
    id: 'm2-anatomy-every-detail', stage: 'MOFU', format: 'Feature callouts',
    html: `
      <div class="serif abs" style="left:0;right:0;top:56px;text-align:center;font-size:104px;line-height:.95">Every detail <em class="tan">has a job.</em></div>
      ${p.html}
      <svg class="fill" width="1080" height="1350" style="position:absolute">${lines}</svg>
      ${callouts.map(([, , , l, t, [n, x, y, z]], i) => {
        const [cx, cy] = [callouts[i][1], callouts[i][2]];
        const right = cx > 540;
        return `${circle(n, x, y, z, 182, cx, cy)}
          <div class="abs" style="${right ? `left:${cx - 50}px;width:230px` : `left:${cx}px;width:250px`};top:${cy + 196}px;${right ? 'text-align:left' : ''}">
            <div class="h3" style="font-size:24px">${l}</div><div style="font-size:20px;line-height:1.35;color:#4a4540;margin-top:4px">${t}</div></div>`;
      }).join('')}
      <div class="abs" style="left:0;right:0;bottom:22px;text-align:center" class="kicker"><span class="kicker" style="font-size:17px">Waterproof, wipe-clean lining · $199</span></div>`,
  });
}

// Text-heavy static.
{
  const pts = [
    ['Cotton canvas & genuine leather', 'With metal hardware. Built for long-term use.'],
    ['Waterproof, wipe-clean lining', 'Damp cloth, done.'],
    ['Front zip pocket', 'Phone, keys and cards stay with your racket.'],
    ['Adjustable strap & carry handle', 'Shoulder, back or hand.'],
    ['Arrives boxed, in a dust bag', 'Ready to keep, or ready to give.'],
  ];
  ads.push({
    id: 'm3-what-youre-paying-for', stage: 'MOFU', format: 'Text-heavy static',
    css: `body{background:var(--paper)}`,
    html: `
      ${frame('IMG_8754.jpg', 0.5, 0.5, 1.0, 0, 0, 1080, 470).html}
      <div class="serif abs" style="left:72px;top:500px;font-size:84px;line-height:1">What you're <em class="tan">actually paying for.</em></div>
      <div class="abs" style="left:72px;right:72px;top:690px">
        ${pts.map(([h, t], i) => `
          <div style="display:flex;gap:30px;align-items:baseline;padding:20px 0;border-top:1.5px solid var(--rule)">
            <div style="font-family:Montserrat;font-weight:800;font-size:28px;color:var(--tan);width:46px">0${i + 1}</div>
            <div style="flex:1;display:flex;justify-content:space-between;gap:24px;align-items:baseline">
              <div class="h3" style="font-size:29px">${h}</div><div style="font-size:21px;color:var(--stone);text-align:right;max-width:330px">${t}</div></div>
          </div>`).join('')}
      </div>`,
  });
}

// FAQ: Will it fit?
ads.push({
  id: 'm4-faq-will-it-fit', stage: 'MOFU', format: 'FAQ',
  css: `body{background:var(--paper)}`,
  html: `
    <div class="kicker abs tan" style="left:72px;top:76px">Your questions, answered</div>
    <div class="serif abs" style="left:72px;top:118px;font-size:120px;line-height:.95">Will COVR fit<br><em>my racket?</em></div>
    <div class="abs" style="left:72px;top:400px;font-family:Montserrat;font-weight:800;font-size:46px;letter-spacing:-.01em">Yes. It fits most standard padel rackets.</div>
    <svg class="abs" style="left:40px;top:500px" width="560" height="800" viewBox="0 0 560 800">
      <rect x="236" y="40" width="88" height="170" rx="22" fill="#e9e1d4" stroke="#161412" stroke-width="3"/>
      <path d="M280 170 C 450 170 500 300 500 450 C 500 640 400 740 280 740 C 160 740 60 640 60 450 C 60 300 110 170 280 170 Z" fill="#e9e1d4" stroke="#161412" stroke-width="3"/>
      <path d="M150 300 L 430 590" stroke="#9b6b3e" stroke-width="5" stroke-dasharray="14 10" fill="none"/>
      <line x1="530" y1="40" x2="530" y2="740" stroke="#161412" stroke-width="2"/><line x1="515" y1="40" x2="545" y2="40" stroke="#161412" stroke-width="2"/><line x1="515" y1="740" x2="545" y2="740" stroke="#161412" stroke-width="2"/>
      <line x1="60" y1="782" x2="500" y2="782" stroke="#161412" stroke-width="2"/><line x1="60" y1="767" x2="60" y2="797" stroke="#161412" stroke-width="2"/><line x1="500" y1="767" x2="500" y2="797" stroke="#161412" stroke-width="2"/>
    </svg>
    <div class="abs" style="left:582px;top:830px;font-family:Montserrat;font-weight:800;font-size:44px">39 cm<div style="font-family:Inter;font-weight:400;font-size:21px;color:var(--stone)">height</div></div>
    <div class="abs" style="left:270px;top:1196px;font-family:Montserrat;font-weight:800;font-size:44px;background:var(--paper);padding:0 14px">29 cm</div>
    <div class="abs" style="left:620px;top:930px;font-size:22px;color:var(--tan);font-weight:600;display:flex;gap:12px;align-items:center"><span style="width:44px;border-top:5px dashed var(--tan)"></span>36 cm curved zip</div>
    ${circle('IMG_0583.JPG', 0.5, 0.62, 2.2, 360, 660, 470)}
    <div class="abs" style="left:620px;top:990px;right:60px;font-size:24px;line-height:1.5;color:#4a4540">
      Waterproof lining<br>Front zip pocket<br>Adjustable strap<br>D-ring for a ball pouch</div>
    <div class="abs" style="left:620px;top:1210px;font-weight:600;font-size:24px;display:flex;gap:10px;align-items:center">padelcovr.com ${ARROW}</div>`,
});

// Studio shoot: desire, not education.
ads.push({
  id: 'm5-studio-never-looked-like-this', stage: 'MOFU', format: 'Studio shoot',
  html: `
    ${frame('IMG_0617.JPG', 0.48, 0.52, 1.25, 0, 0, 1080, 1350).html}
    <div class="fill" style="background:linear-gradient(180deg,transparent 55%,rgba(20,16,12,.7) 100%)"></div>
    ${logo('left:72px;top:72px')}
    <div class="serif abs" style="left:72px;bottom:150px;font-size:116px;line-height:.95;color:#fff">Protection never<br><em>looked like this.</em></div>
    <div class="kicker abs" style="left:76px;bottom:80px;color:rgba(255,255,255,.85);font-size:18px">Vanilla Cream · Handmade padel racket cover</div>`,
});

/* ───────────────────────── BOFU ───────────────────────── */

// Product / colour picker.
{
  const tiles = [
    ['Coffee', 'IMG_0561.JPG', 0.42, 0.56, 1.75],
    ['Vanilla Cream', 'IMG_0617.JPG', 0.42, 0.58, 1.7],
    ['Ash', 'IMG_8754.jpg', 0.76, 0.43, 2.0],
    ['Sky Denim', 'IMG_8776.jpg', 0.78, 0.45, 2.1],
  ];
  ads.push({
    id: 'b1-pick-your-covr', stage: 'BOFU', format: 'Product image',
    html: `
      <div class="serif abs" style="left:72px;top:58px;font-size:118px;line-height:1">Pick your <em class="tan">COVR.</em></div>
      <div class="abs" style="left:76px;top:200px;font-size:27px;color:#4a4540">Ten colours. One standard. Handmade, $199.</div>
      ${tiles.map(([name, n, cx, cy, z], i) => {
        const x = 60 + (i % 2) * 490, y = 280 + Math.floor(i / 2) * 470;
        return `${frame(n, cx, cy, z, x, y, 470, 450, 'border-radius:22px').html}
          <div class="abs" style="left:${x + 20}px;top:${y + 384}px;background:var(--paper);border-radius:999px;padding:10px 22px;font-weight:600;font-size:22px">${name}</div>`;
      }).join('')}
      <div class="abs" style="left:0;right:0;bottom:56px;display:flex;justify-content:center"><span class="btn">Shop all colours ${ARROW}</span></div>`,
  });
}

// Price comparison.
ads.push({
  id: 'b2-price-does-it-add-up', stage: 'BOFU', format: 'Price comparison',
  css: `.card{position:absolute;top:500px;width:450px;height:640px;border-radius:28px;padding:40px 36px}
        .li{display:flex;gap:18px;align-items:center;font-size:27px;line-height:1.3;margin-bottom:34px}
        .li .mark{width:46px;height:46px}.li .mark svg{width:18px;height:18px}`,
  html: `
    <div class="abs" style="left:72px;top:70px">
      <div class="mega" style="font-size:112px">$300 racket.</div>
      <div class="mega tan" style="font-size:112px">$20 cover?</div>
    </div>
    <div class="serif abs" style="left:76px;top:320px;font-size:64px"><em>Does that add up?</em></div>
    <div class="card" style="left:60px;background:#d8d1c6">
      <div class="kicker" style="font-size:16px;color:#57524b">A basic cover</div>
      <div style="font-family:Montserrat;font-weight:900;font-size:76px;margin:6px 0 30px">~$20</div>
      ${['Thin nylon', 'Little padding', 'Loses its shape', 'Often no pocket'].map(t => `<div class="li">${X}${t}</div>`).join('')}
    </div>
    <div class="card" style="left:570px;background:var(--ink);color:var(--paper)">
      <div class="logo" style="font-size:30px">COVR</div>
      <div style="font-family:Montserrat;font-weight:900;font-size:76px;margin:12px 0 30px;color:var(--tan-light)">$199</div>
      ${['Cotton canvas & leather', 'Waterproof lining', 'Front zip pocket', 'Strap, handle & D-ring'].map(t => `<div class="li">${V}${t}</div>`).join('')}
    </div>
    ${circle('IMG_0583.JPG', 0.5, 0.63, 2.6, 190, 830, 410)}
    <div class="abs" style="left:0;right:0;bottom:52px;text-align:center;font-size:26px;font-weight:500">Protect what you play with. <b>padelcovr.com</b></div>`,
});

// Abandoned-checkout reminder.
ads.push({
  id: 'b3-checkout-still-thinking', stage: 'BOFU', format: 'Checkout reminder',
  html: `
    ${frame('IMG_8776.jpg', 0.45, 0.52, 1.0, 0, 0, 1080, 860).html}
    <div class="serif abs" style="left:72px;top:900px;font-size:112px;line-height:.95">Still thinking<br><em class="tan">about it?</em></div>
    <div class="abs" style="left:76px;top:1150px;font-size:28px;color:#4a4540">Your COVR is waiting.</div>
    <div class="abs" style="right:72px;top:1135px"><span class="btn">Finish your order ${ARROW}</span></div>`,
});

// Gift angle (box + dust bag are real).
ads.push({
  id: 'b4-gift-ready-to-give', stage: 'BOFU', format: 'Product image',
  css: `body{background:var(--char);color:var(--paper)}`,
  html: `
    ${frame('IMG_8754.jpg', 0.5, 0.55, 1.0, 0, 330, 1080, 1020).html}
    <div class="abs" style="left:0;right:0;top:330px;height:160px;background:linear-gradient(var(--char),transparent)"></div>
    <div class="serif abs" style="left:72px;top:64px;font-size:112px;line-height:.95">For the player<br><em style="color:var(--tan-light)">who has everything.</em></div>
    <div class="abs" style="left:72px;bottom:64px;right:72px;display:flex;justify-content:space-between;align-items:center">
      <div class="kicker" style="font-size:18px">Boxed · Dust bag · $199</div>${logo('position:static;color:#fff')}</div>`,
});

ads.helpers = { crop, frame, circle, X, V, ARROW, logo, src };
module.exports = ads;
