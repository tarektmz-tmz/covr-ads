const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(const n of ["available_1_boutique_window", "available_2_ivory_plate", "available_3_emerald_velvet", "available_4_editorial", "available_5_dial_macro", "knowledge_1_collectors_note", "knowledge_2_three_checks", "knowledge_3_five_years", "knowledge_4_question_answer"]){await p.goto('file://'+path.resolve('templates/'+n+'.html'));await p.waitForTimeout(900);
await p.screenshot({path:'previews/'+n+'.png'});}
await b.close()})();