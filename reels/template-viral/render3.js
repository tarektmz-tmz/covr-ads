const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{fs.mkdirSync('out',{recursive:true});
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 p.on('pageerror',e=>console.log('pageerror',e.message));p.on('console',m=>{if(m.type()=='error')console.log('err',m.text())});
 await p.goto('file://'+path.resolve('page.html'));await p.evaluate(()=>window.setup());await p.waitForTimeout(500);
 const N=parseInt(process.argv[2]||'683'),T0=parseInt(process.argv[3]||'0');
 for(let i=T0;i<N;i++){await p.evaluate(t=>window.setTime(t),i/30);await p.screenshot({path:`out/f_${String(i+1).padStart(4,'0')}.jpg`,type:'jpeg',quality:93});if(i%60==0)console.log('f',i)}
 await b.close();console.log('done')})();
