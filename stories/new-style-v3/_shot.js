const {chromium}=require('playwright');const path=require('path');
(async()=>{const names=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of names){await p.goto('file://'+path.resolve('templates/'+n+'.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
await p.screenshot({path:'previews/'+n+'.png',type:'png'});}await b.close()})();