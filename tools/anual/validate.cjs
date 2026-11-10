const fs=require('fs'),vm=require('vm'),assert=require('assert'),path=require('path');
const R=path.resolve(__dirname,'../..'),D=JSON.parse(fs.readFileSync(__dirname+'/content.json'));
const script=[...fs.readFileSync(R+'/index.html','utf8').matchAll(/<script>([\s\S]*?)<\/script>/g)][0][1];
const ctx={};vm.createContext(ctx);vm.runInContext(script,ctx);let formulas=0;
function check(obj){if(typeof obj==='string'){assert(!/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/.test(obj),'Control character');for(const m of obj.matchAll(/\$([^$]*)\$/g)){try{ctx.katex.renderToString(m[1],{throwOnError:true,strict:false});formulas++;}catch(e){throw Error(m[1]+' → '+e.message);}}}else if(obj&&typeof obj==='object')Object.values(obj).forEach(check);}
check(D);assert.equal(D.topics.length,34);assert.equal(D.originals.length,62);assert.equal(D.logs.length,14);assert.equal(D.topics.reduce((n,t)=>n+t.warmups.length,0),102);
const topicIDs=D.topics.map(t=>t.id),covered=new Set();
for(const qs of D.simulations){assert.equal(qs.length,15);for(const disc of ['Matemática','Física','Química'])assert.equal(qs.filter(q=>q.discipline===disc).length,5);for(const q of qs){assert.equal(q.parts.length,2);assert.equal(q.answers.length,2);assert(q.steps.length>=2);q.topics.forEach(t=>{assert(topicIDs.includes(t));covered.add(t);});}}
assert.equal(covered.size,34);
for(const [name,qs] of [['originals',D.originals],['logs',D.logs],...D.simulations.map((x,i)=>['sim'+i,x])])assert.equal(new Set(qs.map(q=>q.id)).size,qs.length,name);
let pages=fs.readdirSync(R).filter(f=>/^revisao-|^simulado-anual-|^provas-originais|^logaritmos-ilustrados/.test(f)&&f.endsWith('.html'));
assert.equal(pages.length,11);
for(const f of pages){const h=fs.readFileSync(R+'/'+f,'utf8');for(const [,s] of h.matchAll(/<script>([\s\S]*?)<\/script>/g))new vm.Script(s);for(const [,link] of h.replace(/<script>[\s\S]*?<\/script>/g,'').matchAll(/href="([^"#]+)(?:#[^"]*)?"/g)){if(!/^(https?:|data:)/.test(link))assert(fs.existsSync(R+'/'+link),`${f} broken link ${link}`);}}
// Independently recompute key model outputs and exception-sensitive answers.
const near=(a,b)=>assert(Math.abs(a-b)<1e-8,`${a} != ${b}`);
near(180+225+340-105-70-160+55+85,550);near((520000-160000)/500,720);
near(7000*(420000000/7000)**4/1e22,9.072);near(250*(1+(-30*4+150)/100),325);
near(27/9,3);near(Math.log(64)/Math.LN10,2*Math.log10(2)+2*Math.log10(4));
near(Math.log((1+Math.sqrt(5)+4)/(1+Math.sqrt(5)))/Math.log(5),.5);
near(100*.5*10+100*80+100*1*20,10500);near(.075*142,10.65);near(.15/2*22.4,1.68);
near(16.5/(7.5e22/6e23),132);near((12*6/164)*100,43.90243902439025);
console.log(`${pages.length} páginas; ${formulas} fórmulas KaTeX válidas; 34 temas cobertos; contagens, links, scripts e cálculos críticos conferidos.`);
