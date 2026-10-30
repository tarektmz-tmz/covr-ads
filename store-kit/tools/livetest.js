// Render a saved storefront HTML with its real assets (rewritten to cdn.shopify.com), then run checks.
const fs=require('fs'),path=require('path'),{chromium}=require('playwright');
const [,, htmlFile, outPrefix, width='1440', mode='page'] = process.argv;
const SHOP='https://cdn.shopify.com/s/files/1/1031/5989/0291';
function rewrite(u){
  const m=u.match(/^https?:\/\/ceyllora\.myshopify\.com\/cdn\/(.*)$/); if(!m) return null;
  let p=m[1];
  if(p.startsWith('shop/t/')) return SHOP+'/'+p.slice(5);
  if(p.startsWith('shop/files/')) return SHOP+'/files/'+p.slice(11);
  if(p.startsWith('fonts/')) return null;
  if(p.startsWith('shopifycloud/')) return 'https://cdn.shopify.com/'+p;
  return 'https://cdn.shopify.com/'+p;
}
(async()=>{
  const b=await chromium.launch(); const ctx=await b.newContext({viewport:{width:+width,height:+(process.env.VH||900)}});
  const failed=[];
  await ctx.route('**/*',async r=>{const u=r.request().url();
    if(u.startsWith('http://local/')) return r.fulfill({body:fs.readFileSync(htmlFile,'utf8'),contentType:'text/html'});
    const pm=u.match(/fonts\/poppins\/poppins_n(\d)/); if(pm){const fp=path.join(__dirname,`node_modules/@fontsource/poppins/files/poppins-latin-${pm[1]}00-normal.woff2`);if(fs.existsSync(fp))return r.fulfill({body:fs.readFileSync(fp),contentType:'font/woff2'});}
    const nu=rewrite(u); if(nu){try{const resp=await r.fetch({url:nu});return r.fulfill({response:resp});}catch(e){failed.push("fetch "+nu);return r.abort();}}
    if(/ceyllora\.myshopify\.com/.test(u)) return r.fulfill({status:204,body:''});
    if(/(monorail|analytics|trekkie|shop\.app|otlp|web-pixels|perf-kit)/.test(u)) return r.abort();
    return r.continue();});
  const p=await ctx.newPage(); const errs=[];
  p.on('pageerror',e=>errs.push(e.message)); 
  p.on('response',x=>{if(x.status()>=400) failed.push(x.status()+' '+x.url())});
  await p.goto('http://local/',{waitUntil:'networkidle',timeout:60000}).catch(e=>console.log('goto',e.message));
  await p.evaluate(()=>document.fonts.ready);
  // force lazy content to render
  const H=await p.evaluate(()=>document.documentElement.scrollHeight);
  for(let y=0;y<H;y+=700){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(120);}
  await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(500);
  if(mode==='pageX'){
    const total=await p.evaluate(()=>document.documentElement.scrollHeight); let k=0;
    for(let y=0;y<total;y+=900,k++){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(250);await p.screenshot({path:`${outPrefix}_${String(k).padStart(2,'0')}.png`});}
    console.log('shots',k,'height',total);
  }
  if(fs.existsSync(path.join(__dirname,'livetest_extra.js'))) await require('./livetest_extra.js')(p,outPrefix,mode);
  console.log('JS errors:',errs.slice(0,8)); console.log('failed:',[...new Set(failed)].filter(u=>!/monorail|analytics|trekkie|204/.test(u)).slice(0,15));
  await b.close();
})();
