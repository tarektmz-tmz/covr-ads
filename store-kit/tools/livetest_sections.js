module.exports=async(p,out,mode)=>{
  const want=(process.env.ONLY||'').split(',').filter(Boolean);
  const secs=await p.$$eval('[id^="shopify-section-"]',els=>els.map(e=>e.id));
  let k=0;
  for(const id of secs){ if(want.length && !want.some(w=>id.endsWith('__'+w))) continue;
    const l=p.locator('#'+id); await l.scrollIntoViewIfNeeded(); await p.waitForTimeout(800);
    await p.evaluate(()=>Promise.all([...document.images].filter(i=>!i.complete).map(i=>new Promise(r=>{i.onload=i.onerror=r;setTimeout(r,4000)}))));
    await l.screenshot({path:`${out}_s${String(k++).padStart(2,'0')}.png`}).catch(e=>console.log('fail',id,e.message));
    console.log(k-1,id.split('__')[1]);
  }
  const broken=await p.$$eval('img',a=>a.filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.slice(0,100)));
  console.log('broken images:',broken);
};
