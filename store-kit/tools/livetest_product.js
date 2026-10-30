module.exports=async(p,out)=>{
  const st=async()=>p.evaluate(()=>{
    const ids=[...document.querySelectorAll('form[action*="/cart/add"] input[name="id"]')].map(i=>i.value);
    const price=(document.querySelector('product-price, .price, [ref="priceContainer"]')||{}).innerText;
    const act=[...document.querySelectorAll('.ceylora-bundle')].map(b=>b.classList.contains('is-active'));
    return {ids:[...new Set(ids)],price:price&&price.replace(/\s+/g,' ').trim().slice(0,60),act,url:location.search};});
  console.log('initial',JSON.stringify(await st()));
  const cards=p.locator('.ceylora-bundle');console.log('bundle cards',await cards.count());
  for(let i=0;i<await cards.count();i++){await cards.nth(i).click();await p.waitForTimeout(1500);console.log('click',i+1,JSON.stringify(await st()));}
  // tabs
  const tabs=p.locator('details.ceylora-tab');const n=await tabs.count();
  console.log('tabs',n, 'open at start:',await p.$$eval('details.ceylora-tab',d=>d.filter(x=>x.open).length));
  if(n){await tabs.nth(1).locator('summary').scrollIntoViewIfNeeded();
    const before=await tabs.nth(1).evaluate(e=>getComputedStyle(e).transform);
    await tabs.nth(1).locator('summary').hover();await p.waitForTimeout(400);
    const after=await tabs.nth(1).evaluate(e=>getComputedStyle(e).transform);
    await tabs.nth(1).locator('summary').click();await p.waitForTimeout(400);
    console.log('hover transform',before,'->',after,'| opened after click:',await tabs.nth(1).evaluate(e=>e.open));
    await p.locator('.ceylora-tabs').screenshot({path:out+'_tabs.png'});}
  const stars=await p.evaluate(()=>{const t=document.querySelector('main').innerText;return (t.match(/.{25}\*.{10}/g)||[]).slice(0,10)});
  console.log('asterisks in page text:',stars);
  const imgs=await p.$$eval('main img',a=>a.filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.slice(0,90)));
  console.log('broken images:',imgs);
};
