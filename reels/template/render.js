const {chromium}=require('playwright');
const path=require('path');
(async()=>{
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve('page.html'));
  await p.evaluate(()=>window.setup()); 
  await p.waitForTimeout(500);
  const from=parseInt(process.argv[2]||'0'), to=parseInt(process.argv[3]||'914');
  for(let i=from;i<to;i++){
    const t=i/30;
    await p.evaluate(t=>window.setTime(t),t);
    await p.screenshot({path:`out/f_${String(i+1).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});
    if(i%50==0)console.log('frame',i);
  }
  await b.close();
})();
