module.exports=async(p,out,mode)=>{
  if(mode==='product'){await require('./livetest_product.js')(p,out);return;}
  if(mode==='scroll'){ for(const [k,y] of [[0,0],[1,800],[2,1500]]){await p.mouse.move(700,400);await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(600);await p.screenshot({path:`${out}_v${k}.png`});} return;}
  await require('./livetest_sections.js')(p,out,mode);
};
