const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),questions=JSON.parse(fs.readFileSync(path.join(__dirname,'content.json'),'utf8'));
const html=fs.readFileSync(path.join(root,'plano-inclinado.html'),'utf8');
const ctx={};vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname,'physics.js'),'utf8')+'\n'+fs.readFileSync(path.join(__dirname,'visuals.js'),'utf8')+'\nthis.P=InclinePhysics;this.V=InclineVisuals;',ctx);
const near=(a,b,n='')=>assert(Math.abs(a-b)<1e-8,`${n}: ${a} != ${b}`);
const initial=questions.map(q=>ctx.P.state(q,q.lab.base,1));
near(initial[0].a,6);near(initial[0].normal,16);near(initial[1].parallel,6);near(initial[1].duration,2);near(initial[1].s,12);near(initial[1].v,12);
near(initial[2].a,-3);near(initial[2].duration,4);near(initial[2].s,24);near(initial[2].v,0);near(initial[3].a,4);near(initial[4].duration,2);
near(initial[5].distance,10);near(initial[6].a,3);near(initial[6].tension,6);near(initial[7].a,2);near(initial[7].p.ratio,4);
let cases=0;
for(const q of questions){
  // Sweep all corners and defaults; include the equilibrium points explicitly.
  let params=[{...q.lab.base}];
  for(const c of q.lab.controls)params=params.flatMap(p=>[c.min,q.lab.base[c.key],c.max].map(v=>({...p,[c.key]:v})));
  if(q.id===4)params.push({...q.lab.base,force:14});
  if(q.id===8)params.push({...q.lab.base,ratio:2});
  for(const p of params)for(const t of [0,.25,.5,.75,1]){
    const z=ctx.P.state(q,p,t);cases++;
    for(const [key,v]of Object.entries(z))if(typeof v==='number')assert(Number.isFinite(v),`${q.id} ${key}`);
    if(z.kind==='down'){near(z.s,z.a*z.t**2/2);near(z.v**2,2*z.g*z.s*z.sine);if(t===1)near(z.s,p.length);}
    if(z.kind==='up'){near(z.kinetic+z.potential,p.v0**2/2,'energy');near(z.a,-p.g*z.sine);if(t===1){near(z.v,0);assert(z.a<0);}}
    if(z.kind==='tablePulley'){near(z.tension,p.massA*z.a);near(p.massB*p.g*p.sine-z.tension,p.massB*z.a);}
    if(z.kind==='hangingPulley'){near(z.massLarge*p.g*z.sine-z.tension,z.massLarge*z.a);near(z.tension-p.massSmall*p.g,p.massSmall*z.a);}
    if(z.kind.includes('Pulley'))near(ctx.P.rope(z).length,ctx.P.rope(ctx.P.state(q,p,0)).length,'inextensible rope');
    for(const output of [ctx.V.motion(z),ctx.V.forces(z,true,true),ctx.V.graph(z)])assert(!/NaN|Infinity|undefined/.test(output),`SVG ${q.id}`);
  }
}
near(ctx.P.state(questions[7],{...questions[7].lab.base,ratio:2},1).a,0);
assert(ctx.P.state(questions[7],{...questions[7].lab.base,ratio:1},1).a<0);
near(ctx.P.state(questions[7],{...questions[7].lab.base,massSmall:3},1).a,2);
near(ctx.P.state(questions[4],{...questions[4].lab.base,length:6,height:9.5},0).p.height,5.5);
for(const [,script]of html.matchAll(/<script>([\s\S]*?)<\/script>/g))new vm.Script(script);
const katex=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)][0][1];vm.runInContext(katex,ctx);
let formulas=0;
function scan(v){if(typeof v==='string'){assert.equal((v.match(/\$/g)||[]).length%2,0);for(const [,m]of v.matchAll(/\$([^$]+)\$/g)){ctx.katex.renderToString(m,{throwOnError:true,strict:false});formulas++;}}else if(v&&typeof v==='object')Object.values(v).forEach(scan);}
scan(questions);
assert.equal(questions.length,8);assert.equal((html.match(/class="card"/g)||[]).length,8);assert.equal((html.match(/class="lab"/g)||[]).length,8);
const markup=html.replace(/<script[^>]*>[\s\S]*?<\/script>/g,'');
const ids=[...markup.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);assert.equal(new Set(ids).size,ids.length);
for(const [,href]of markup.matchAll(/href="([^"]+)"/g)){if(/^(https?:|data:)/.test(href))continue;const[file,anchor]=href.split('#');if(file)assert(fs.existsSync(path.join(root,file)),href);else if(anchor)assert(ids.includes(anchor),href);}
for(const file of fs.readdirSync(root).filter(f=>f.endsWith('.html'))){const text=fs.readFileSync(path.join(root,file),'utf8');const nav=text.match(/<nav[^>]*aria-label="Cadernos de estudo"[^>]*>[\s\S]*?<\/nav>/);if(nav)assert.equal(nav[0].split('href="plano-inclinado.html"').length-1,1,file);}
assert(!/src="https?:/.test(html));assert(!/Lara|Buarque|Barbarato/.test(markup));
console.log(`8 questões; ${formulas} fórmulas; ${cases} estados físicos conferidos. Newton, energia, fio, limites, SVGs, scripts e navegação válidos.`);
