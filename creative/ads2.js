// Round 2: 10 scroll-stopping formats borrowed from proven viral static ads.
const { crop, frame, circle, ARROW, logo, src } = require('./ads.js').helpers;

const RED = '#d4342b';
const ads = [];

/* 1. Text behind subject — giant word sits between the court and the player. */
{
  const args = [0.45, 0.5, 1.03, 0, 0, 1080, 1350];
  const bg = frame('latte-walking-court.jpg', ...args);
  const fg = frame('latte-walking-court_cutout.png', ...args);
  ads.push({
    id: 'n01-text-behind-player', stage: 'TOFU', format: 'Text behind subject',
    html: `
      ${bg.html}
      <div class="abs serif" style="left:0;right:0;top:-20px;text-align:center;font-size:440px;line-height:1;color:#f7f2e9;letter-spacing:.01em">COVR</div>
      ${fg.html}
      <div class="abs" style="left:0;right:0;bottom:0;height:260px;background:linear-gradient(transparent,rgba(10,10,8,.55))"></div>
      <div class="abs" style="left:64px;right:64px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end;color:#fff">
        <div><div class="serif" style="font-size:64px;line-height:1">Off court. <em>On brand.</em></div>
        <div class="kicker" style="font-size:17px;margin-top:14px">Latte · Handmade padel racket cover</div></div>
        <div style="font-family:Montserrat;font-weight:800;font-size:44px">$249</div>
      </div>`,
  });
}

/* 2. Red-marker annotations on the photo. */
{
  const p = frame('latte-unboxing-hands.jpg', 0.5, 0.5, 1.0, 0, 0, 1080, 1350);
  const notes = [
    // [text, label x, y, rotate, arrow from (label side) -> photo point]
    ['genuine leather +<br>gold rivets', 340, 285, -4, [330, 240], [0.17, 0.215]],
    ['D-ring for the<br>ball pouch', 40, 560, -3, [170, 505], [0.24, 0.325]],
    ['zip pocket:<br>phone, keys, cards', 40, 1010, 3, [300, 930], [0.384, 0.63]],
    ['embroidered<br>crest', 790, 1060, -5, [840, 985], [0.74, 0.62]],
  ];
  const arrows = notes.map(([, , , , [x1, y1], [fx, fy]]) => {
    const [x2, y2] = p.at(fx, fy);
    const mx = (x1 + x2) / 2 + (y2 - y1) * 0.18, my = (y1 + y2) / 2 - (x2 - x1) * 0.18;
    const a = Math.atan2(y2 - my, x2 - mx), L = 26;
    const h1 = [x2 - L * Math.cos(a - .5), y2 - L * Math.sin(a - .5)], h2 = [x2 - L * Math.cos(a + .5), y2 - L * Math.sin(a + .5)];
    return `<path d="M${x1} ${y1} Q${mx} ${my} ${x2} ${y2}" fill="none" stroke="${RED}" stroke-width="6" stroke-linecap="round"/>
            <path d="M${h1} L${x2} ${y2} L${h2}" fill="none" stroke="${RED}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>`;
  }).join('');
  ads.push({
    id: 'n02-red-marker-details', stage: 'MOFU', format: 'Annotated photo',
    css: `.hand{font-family:Caveat;font-weight:700;color:${RED};line-height:.95;position:absolute;text-shadow:0 0 12px rgba(255,255,255,.9),0 0 3px #fff}`,
    html: `
      ${p.html}
      <svg class="fill" width="1080" height="1350" style="position:absolute">${arrows}
        <ellipse cx="${p.at(0.74, 0.585)[0]}" cy="${p.at(0.74, 0.585)[1]}" rx="205" ry="235" fill="none" stroke="${RED}" stroke-width="6" transform="rotate(-8 ${p.at(0.74, 0.585)[0]} ${p.at(0.74, 0.585)[1]})"/></svg>
      ${notes.map(([t, x, y, r]) => `<div class="hand" style="left:${x}px;top:${y - 60}px;font-size:58px;transform:rotate(${r}deg)">${t}</div>`).join('')}
      <div class="abs" style="left:56px;top:56px;background:#fffdf7;padding:18px 30px;border-radius:6px;transform:rotate(-2deg);box-shadow:0 8px 24px rgba(0,0,0,.18)">
        <div class="hand" style="position:static;font-size:66px;color:var(--ink);text-shadow:none">ok, but look at the details</div></div>
      <div class="abs" style="right:56px;bottom:60px;background:var(--ink);color:#fff;border-radius:999px;padding:16px 30px;font-weight:600;font-size:24px">Latte · $249</div>`,
  });
}

/* 3. iPhone Notes checklist. */
ads.push({
  id: 'n03-notes-app-checklist', stage: 'TOFU', format: 'Notes app',
  css: `body{background:#fff;font-family:Inter}
        .row{display:flex;gap:26px;align-items:flex-start;font-size:40px;line-height:1.25;margin-bottom:26px}
        .ck{width:44px;height:44px;border-radius:50%;flex:none;margin-top:2px;display:flex;align-items:center;justify-content:center}
        .ck.on{background:#f4b400}.ck.off{border:3px solid #c7c7cc}
        .done{color:#a1a1a6;text-decoration:line-through}`,
  html: `
    <div class="abs" style="left:40px;right:40px;top:44px;display:flex;justify-content:space-between;color:#e0a400;font-size:38px;font-weight:500">
      <span>‹ Notes</span><span style="letter-spacing:.1em">⋯</span></div>
    <div class="abs" style="left:0;right:0;top:130px;text-align:center;color:#a1a1a6;font-size:24px">11 October 2026 at 09:14</div>
    <div class="abs" style="left:64px;right:64px;top:200px">
      <div style="font-weight:700;font-size:64px;margin-bottom:40px">padel bag checklist</div>
      ${['racket', '3 new balls', 'grip tape', 'water + towel'].map(t => `<div class="row"><span class="ck on"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span><span class="done">${t}</span></div>`).join('')}
      <div class="row"><span class="ck off"></span><span><b style="font-weight:600">something that actually protects the racket I spent $300 on</b></span></div>
      <div style="position:relative;height:470px;border-radius:22px;overflow:hidden;margin:18px 0 26px">${crop('latte-thankyou-card.jpg', 0.5, 0.52, 1.0, 952, 470).img}</div>
      <div style="font-size:38px">found it → <span style="color:#e0a400;text-decoration:underline">padelcovr.com</span></div>
    </div>`,
});

/* 4. Group chat. */
{
  const L = (name, t) => `<div style="margin:0 0 18px 0"><div style="font-size:21px;color:#8e8e93;margin:0 0 6px 26px">${name}</div><div class="b l">${t}</div></div>`;
  const R = t => `<div style="display:flex;justify-content:flex-end;margin-bottom:18px"><div class="b r">${t}</div></div>`;
  ads.push({
    id: 'n04-group-chat', stage: 'TOFU', format: 'Group chat',
    css: `body{background:#fff}
          .b{display:inline-block;max-width:690px;padding:20px 30px;border-radius:40px;font-size:35px;line-height:1.28}
          .l{background:#e9e9eb;color:#000;border-bottom-left-radius:12px}
          .r{background:#0b84ff;color:#fff;border-bottom-right-radius:12px}`,
    html: `
      <div class="abs" style="left:0;right:0;top:0;height:210px;background:#f6f6f6;border-bottom:1px solid #ddd;text-align:center;padding-top:40px">
        <div style="width:84px;height:84px;border-radius:50%;background:#2f4a3a;margin:0 auto;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:30px">PT</div>
        <div style="font-size:26px;margin-top:10px;font-weight:500">Padel Tuesday ›</div></div>
      <div class="abs" style="left:40px;right:40px;top:250px">
        ${L('Nadia', 'who’s bringing balls tonight')}
        ${R('me')}
        ${L('Omar', 'also can we talk about Sara’s racket bag')}
        <div style="margin:0 0 18px 0"><div style="width:520px;height:390px;border-radius:30px;overflow:hidden;position:relative">${crop('latte-walking-court.jpg', 0.48, 0.52, 1.6, 520, 390).img}</div></div>
        ${L('Jade', 'ok that’s actually nice')}
        ${R('it’s COVR. canvas + leather, zip pocket for your phone')}
        ${L('Nadia', 'link pls')}
        ${R('padelcovr.com')}
      </div>`,
  });
}

/* 5. Search bar with autocomplete. Generic UI, no search-engine branding. */
ads.push({
  id: 'n05-search-autocomplete', stage: 'MOFU', format: 'Search result',
  css: `body{background:var(--paper)}
        .sug{display:flex;gap:26px;align-items:center;padding:16px 36px;font-size:32px;color:#3c3c3c}
        .sug svg{flex:none}`,
  html: `
    <div class="abs" style="left:60px;right:60px;top:80px;background:#fff;border-radius:44px;box-shadow:0 10px 40px rgba(0,0,0,.12);padding:30px 0 22px">
      <div style="display:flex;align-items:center;gap:24px;padding:0 36px 24px;border-bottom:1px solid #eee;font-size:36px">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2.4"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>
        <span>padel racket cover that doesn’t look cheap<span style="border-left:3px solid #1a73e8;margin-left:3px"></span></span></div>
      ${['padel racket cover leather', 'padel racket cover with pocket', 'padel racket cover gift', 'padel racket cover <b>that doesn’t look cheap</b>'].map(t => `<div class="sug"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2.4"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><span>${t}</span></div>`).join('')}
    </div>
    <div class="abs" style="left:60px;right:60px;top:560px;background:#fff;border-radius:30px;padding:40px;display:flex;gap:34px;box-shadow:0 10px 40px rgba(0,0,0,.08)">
      <div style="flex:1">
        <div style="font-size:23px;color:#4d5156">padelcovr.com › padel-racket-covers</div>
        <div style="font-size:40px;color:#1a0dab;margin:10px 0 14px;line-height:1.15">COVR — Handmade padel racket covers</div>
        <div style="font-size:25px;line-height:1.45;color:#4d5156">Cotton canvas, genuine leather and metal hardware. Waterproof lining, front zip pocket, adjustable strap. Ten colours. $249.</div>
      </div>
      <div style="width:250px;height:300px;border-radius:18px;overflow:hidden;position:relative;flex:none">${crop('latte-unboxing-hands.jpg', 0.55, 0.45, 1.6, 250, 300).img}</div>
    </div>
    <div class="abs" style="left:64px;bottom:150px"><div class="mega" style="font-size:150px">Search</div><div class="mega tan" style="font-size:150px">over.</div></div>
    ${logo('right:64px;bottom:170px')}`,
});

/* 6. Receipt: everything included. */
{
  const items = ['Cotton canvas body', 'Genuine leather trim', 'Metal hardware', 'Waterproof lining', 'Front zip pocket', 'Adjustable strap', 'Carry handle', 'D-ring for ball pouch', 'Box + dust bag'];
  ads.push({
    id: 'n06-receipt-everything-included', stage: 'MOFU', format: 'Receipt',
    css: `.rc{position:absolute;left:170px;width:740px;top:70px;background:#fbfaf6;padding:56px 56px 90px;font-family:'Courier Prime';color:#1d1b18;transform:rotate(-2.5deg);box-shadow:0 30px 60px rgba(0,0,0,.35);
              -webkit-mask:linear-gradient(#000 0 0) top/100% calc(100% - 22px) no-repeat, conic-gradient(from 135deg at top,#0000,#000 1deg 89deg,#0000 90deg) bottom/36px 22px repeat-x}
          .it{display:flex;font-size:29px;line-height:1.75}.it span:nth-child(2){flex:1;border-bottom:3px dotted #bbb;margin:0 12px 14px}
          .dash{border-top:3px dashed #999;margin:22px 0}`,
    html: `
      ${frame('crest-duo-closeup.jpg', 0.5, 0.5, 1.03, 0, 0, 1080, 1350).html}
      <div class="fill" style="background:rgba(20,16,12,.35)"></div>
      <div class="rc">
        <div class="logo" style="text-align:center;font-size:54px;font-family:'Instrument Serif'">COVR</div>
        <div style="text-align:center;font-size:24px;margin-top:10px">padelcovr.com</div>
        <div class="dash"></div>
        <div style="font-size:27px;font-weight:700;margin-bottom:8px">1 × PADEL RACKET COVER</div>
        ${items.map(t => `<div class="it"><span>${t}</span><span></span><span>INCL</span></div>`).join('')}
        <div class="dash"></div>
        <div style="display:flex;justify-content:space-between;font-weight:700;font-size:52px">TOTAL<span>$249.00</span></div>
        <div class="dash"></div>
        <div style="text-align:center;font-size:30px;margin-top:6px">Cheap covers cost twice.</div>
        <div style="height:80px;margin:30px 40px 0;background:repeating-linear-gradient(90deg,#1d1b18 0 4px,transparent 4px 7px,#1d1b18 7px 9px,transparent 9px 15px,#1d1b18 15px 20px,transparent 20px 23px)"></div>
      </div>`,
  });
}

/* 7. Post-it note on the product. */
ads.push({
  id: 'n07-post-it-dear-racket', stage: 'TOFU', format: 'Post-it',
  html: `
    ${frame('crest-duo-closeup.jpg', 0.5, 0.5, 1.03, 0, 0, 1080, 1350).html}
    <div class="abs" style="left:470px;top:90px;width:540px;height:520px;background:#fde98a;transform:rotate(4deg);box-shadow:0 22px 40px rgba(0,0,0,.28);padding:70px 50px;font-family:Caveat;font-weight:700;font-size:70px;line-height:1.05;color:#26231f">
      <div class="abs" style="left:170px;top:-26px;width:200px;height:56px;background:rgba(255,255,255,.55);transform:rotate(-5deg)"></div>
      Dear racket,<br>sorry about<br>the car boot.<br>You’ll like it here.<div style="text-align:right;margin-top:10px">— me</div></div>
    <div class="abs" style="left:0;right:0;bottom:0;height:300px;background:linear-gradient(transparent,rgba(20,14,10,.6))"></div>
    <div class="abs" style="left:64px;bottom:62px;color:#fff">${logo('position:static;color:#fff')}<div class="kicker" style="font-size:17px;margin-top:14px">Handmade padel racket covers · $249</div></div>`,
});

/* 8. Magazine cover. */
ads.push({
  id: 'n08-magazine-cover', stage: 'TOFU', format: 'Magazine cover',
  html: `
    ${frame('mocha-strap-studio.jpg', 0.5, 0.52, 1.03, 0, 0, 1080, 1350).html}
    <div class="abs serif" style="left:0;right:0;top:-12px;text-align:center;font-size:300px;line-height:1;letter-spacing:.06em;color:var(--ink)">COVR</div>
    <div class="abs kicker" style="left:0;right:0;top:300px;text-align:center;font-size:18px">The Padel Issue · No. 01</div>
    <div class="abs" style="right:52px;top:400px;width:160px;height:160px;border-radius:50%;background:var(--tan);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(8deg)">
      <div style="font-size:18px;letter-spacing:.2em">ONLY</div><div style="font-family:Montserrat;font-weight:900;font-size:50px">$249</div></div>
    <div class="abs" style="left:0;right:0;bottom:0;height:420px;background:linear-gradient(transparent,rgba(20,14,10,.7))"></div>
    <div class="abs" style="left:56px;bottom:60px;color:#fff;width:640px">
      <div class="kicker" style="font-size:17px;color:var(--tan-light)">Cover story</div>
      <div style="font-family:Montserrat;font-weight:900;font-size:58px;line-height:1;text-transform:uppercase;margin-top:10px">The accessory padel forgot.</div>
      <div class="serif" style="font-size:34px;margin-top:14px"><em>Ten colours, one standard. Inside: the open-back handle.</em></div></div>
    <div class="abs" style="right:56px;bottom:60px;width:150px;height:90px;background:#fff;padding:10px">
      <div style="height:52px;background:repeating-linear-gradient(90deg,#111 0 3px,#fff 3px 5px,#111 5px 6px,#fff 6px 10px)"></div>
      <div style="font-family:'Courier Prime';font-size:13px;text-align:center;margin-top:4px">padelcovr.com</div></div>`,
});

/* 9. Boarding pass: from the car boot to COVR. */
ads.push({
  id: 'n09-boarding-pass', stage: 'TOFU', format: 'Boarding pass',
  css: `body{background:#2f4a3a}
        .bp{position:absolute;left:60px;right:60px;top:330px;height:760px;background:var(--paper);border-radius:34px;overflow:hidden;display:flex}
        .lbl{font-size:18px;letter-spacing:.2em;color:var(--stone);text-transform:uppercase;font-weight:500}
        .val{font-family:Montserrat;font-weight:800;font-size:34px;margin-top:6px;text-transform:uppercase}`,
  html: `
    <div class="serif abs" style="left:64px;top:70px;color:#f3ede3;font-size:116px;line-height:1">Upgrade <em style="color:var(--tan-light)">your racket.</em></div>
    <div class="bp">
      <div style="flex:1;min-width:0;padding:52px 44px;position:relative">
        <div style="display:flex;justify-content:space-between;align-items:center"><div class="kicker" style="font-size:20px">Boarding pass</div><div class="logo" style="font-size:34px">COVR</div></div>
        <div style="display:flex;align-items:center;gap:30px;margin:46px 0 40px">
          <div><div class="lbl">From</div><div class="mega" style="font-size:84px;color:#9a948b">BOOT</div><div style="font-size:22px;color:var(--stone)">Car boot</div></div>
          <svg width="64" height="40" viewBox="0 0 80 40" style="flex:none"><path d="M0 20h70M56 6l16 14-16 14" fill="none" stroke="#9b6b3e" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <div><div class="lbl">To</div><div class="mega tan" style="font-size:84px">COVR</div><div style="font-size:22px;color:var(--stone)">Cotton & leather</div></div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;row-gap:34px;column-gap:30px">
          <div><div class="lbl">Passenger</div><div class="val">Your racket</div></div>
          <div><div class="lbl">Class</div><div class="val">First</div></div>
          <div><div class="lbl">Seat</div><div class="val">Waterproof lining</div></div>
          <div><div class="lbl">Gate</div><div class="val">Court 3</div></div>
        </div>
      </div>
      <div style="width:250px;flex:none;border-left:4px dashed #cfc6b8;padding:46px 28px;display:flex;flex-direction:column;align-items:center;gap:30px">
        <div style="position:relative;width:190px;height:190px">${circle('latte-unboxing-hands.jpg', 0.74, 0.5, 3.0, 190, 0, 0, 'border-color:#e6dccd')}</div>
        <div style="text-align:center"><div class="lbl">Fare</div><div class="val" style="font-size:48px">$249</div></div>
        <div style="width:150px;height:200px;background:repeating-linear-gradient(0deg,#161412 0 4px,transparent 4px 7px,#161412 7px 9px,transparent 9px 14px)"></div>
      </div>
    </div>
    <div class="abs" style="left:64px;right:64px;bottom:80px;display:flex;justify-content:space-between;color:#f3ede3;font-size:27px">
      <span>Boarding before your next match.</span><b>padelcovr.com</b></div>`,
});

/* 10. This or that. */
ads.push({
  id: 'n10-this-or-that', stage: 'TOFU', format: 'This or that',
  html: `
    <div class="abs" style="left:0;right:0;top:0;height:230px;background:var(--cream);text-align:center;padding-top:46px">
      <div class="serif" style="font-size:96px;line-height:1">Which one <em class="tan">are you?</em></div>
      <div style="font-size:26px;color:#4a4540;margin-top:14px">Tell us in the comments.</div></div>
    ${frame('latte-unboxing-hands.jpg', 0.6, 0.5, 1.5, 0, 230, 540, 1120).html}
    ${frame('mocha-zip-bench.jpg', 0.48, 0.55, 1.75, 540, 230, 540, 1120).html}
    <div class="abs" style="left:0;right:0;bottom:0;height:300px;background:linear-gradient(transparent,rgba(15,12,10,.65))"></div>
    <div class="abs mega" style="left:40px;bottom:70px;font-size:96px;color:#fff">Latte</div>
    <div class="abs mega" style="right:40px;bottom:70px;font-size:96px;color:#fff">Mocha</div>
    <div class="abs" style="left:470px;top:720px;width:140px;height:140px;border-radius:50%;background:var(--paper);display:flex;align-items:center;justify-content:center;font-family:'Instrument Serif';font-style:italic;font-size:66px;box-shadow:0 10px 30px rgba(0,0,0,.25)">or</div>`,
});

module.exports = ads;
