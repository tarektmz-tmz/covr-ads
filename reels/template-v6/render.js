const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const [A,B,page,out,fps]=[+process.argv[2],+process.argv[3],process.argv[4],process.argv[5],+(process.argv[6]||25)];
 fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 p.on('pageerror',e=>console.log('pageerror',e.message));
 await p.goto('file://'+path.resolve(page));await p.evaluate(()=>window.setup());await p.waitForTimeout(500);
 for(let i=A;i<B;i++){await p.evaluate(t=>window.setTime(t),i/fps);await p.screenshot({path:`${out}/f_${String(i+1).padStart(5,'0')}.jpg`,type:'jpeg',quality:100})}
 await b.close();console.log('done',A,B)})();
