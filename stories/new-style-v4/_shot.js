const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const jobs=JSON.parse(process.argv[2]);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});const rep=[];
for(const j of jobs){await p.goto('file://'+path.resolve(j.html));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(250);
 const chk=await p.evaluate(()=>{const out=[];document.querySelectorAll('#s *').forEach(e=>{if(e.children.length===0&&e.textContent.trim()&&!e.closest('.legal')){const rg=document.createRange();rg.selectNodeContents(e);const r=rg.getBoundingClientRect();out.push([Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom),e.textContent.trim().slice(0,30)])}});
  const imgs=[...document.querySelectorAll('#s img')].map(i=>{const r=i.getBoundingClientRect();return [Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]});return {out,imgs}});
 const bad=chk.out.filter(r=>r[3]>1585||r[2]>1030||r[0]<50||r[1]<248).map(r=>r.join(','));const badi=chk.imgs.filter(r=>r[0]<40||r[2]>1040||r[1]<248||r[3]>1585).map(r=>r.join(','));
 if(bad.length||badi.length)rep.push(j.out+' OUT OF SAFE ZONE: '+bad.slice(0,3).join(' | ')+' IMG '+badi.join(' | '));
 await p.screenshot(j.out.endsWith('.jpg')?{path:j.out,type:'jpeg',quality:90}:{path:j.out,type:'png'});}
await b.close();console.log(JSON.stringify(rep))})();