const fs=require('fs'),path=require('path'),{chromium}=require('playwright');
const ic=n=>fs.readFileSync(path.join(__dirname,'node_modules/lucide-static/icons',n+'.svg'),'utf8').replace(/<!--[\s\S]*?-->/g,'').replace(/width="24"/,'width="120"').replace(/height="24"/,'height="120"').replace(/stroke="currentColor"/,'stroke="#ffffff"').replace(/stroke-width="2"/,'stroke-width="1.8"');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:240,height:240}});
for(const [n,f] of [['activity','ceylora-icon-insulin'],['droplet','ceylora-icon-blood-sugar'],['heart-pulse','ceylora-icon-blood-pressure'],['zap','ceylora-icon-energy']]){
 await p.setContent(`<html><body style="margin:0;background:transparent"><div id=c style="width:240px;height:240px;border-radius:50%;background:linear-gradient(135deg,#c27440,#8a3d17);display:flex;align-items:center;justify-content:center">${ic(n)}</div></body></html>`);
 await p.locator('#c').screenshot({path:path.join(__dirname,'..','final',f+'.png'),omitBackground:true});}
await b.close();console.log('ok')})();
