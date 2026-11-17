const fs = require('fs'), path = require('path'), vm = require('vm'), assert = require('assert');
const root = path.resolve(__dirname, '../..');
const pages = JSON.parse(fs.readFileSync(path.join(__dirname, 'content.json'), 'utf8'));
const source = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const katex = [...source.matchAll(/<script>([\s\S]*?)<\/script>/g)][0][1];
const context = {}; vm.createContext(context); vm.runInContext(katex, context);
let formulas = 0, figures = 0;
function inspect(value) {
  if (typeof value === 'string') {
    assert(!/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/.test(value), 'Control character');
    const clean = value.replace(/R\$/g, 'reais');
    assert.equal((clean.match(/\$/g) || []).length % 2, 0, 'Unbalanced math: '+value);
    for (const [, formula] of clean.matchAll(/\$([^$]+)\$/g)) {
      context.katex.renderToString(formula, {throwOnError: true, strict: false}); formulas++;
    }
  } else if (value && typeof value === 'object') Object.values(value).forEach(inspect);
}
inspect(pages);
assert.equal(pages.length, 2); assert.equal(pages[0].items.length, 17); assert.equal(pages[1].items.length, 9);
const ids = pages.flatMap(page => page.items.map(q => q.id));
assert.equal(new Set(ids).size, 26);
for (const page of pages) {
  const html = fs.readFileSync(path.join(root, page.slug+'.html'), 'utf8');
  assert.equal((html.match(/class="card"/g) || []).length, page.items.length);
  assert.equal((html.match(/class="solution-toggle"/g) || []).length, page.items.length);
  assert.equal((html.match(/class="exercise-figure"/g) || []).length, page.items.filter(q => q.figure).length);
  for (const [, script] of html.matchAll(/<script>([\s\S]*?)<\/script>/g)) new vm.Script(script);
  const htmlIds = [...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
  assert.equal(new Set(htmlIds).size, htmlIds.length, 'Duplicate IDs');
  for (const q of page.items) {
    assert(q.steps.length>=3 && q.answer && q.pitfall, q.id);
    assert(q.choices.length===0 || q.choices.length===5, q.id);
    if(q.figure) { figures++; assert(html.includes('figure-desc-'+q.id), q.id+' accessible figure'); }
  }
  const markup = html.replace(/<script>[\s\S]*?<\/script>/g, '');
  for (const [, href] of markup.matchAll(/href="([^"]+)"/g)) {
    if (/^(https?:|data:)/.test(href)) continue;
    const [file, anchor] = href.split('#');
    if (file) assert(fs.existsSync(path.join(root,file)), 'Broken link '+href);
    else if (anchor) assert(htmlIds.includes(anchor), 'Broken anchor '+href);
  }
  assert(!html.includes('src="http'), 'Unexpected external dependency');
}
assert.equal(figures,19);
for (const filename of fs.readdirSync(root).filter(f=>f.endsWith('.html'))) {
  const nav = fs.readFileSync(path.join(root,filename),'utf8').match(/<nav[^>]*aria-label="Cadernos de estudo"[^>]*>[\s\S]*?<\/nav>/);
  if (nav) for(const page of pages) assert.equal(nav[0].split('href="'+page.slug+'.html"').length-1,1,filename);
}

// Recompute every numerical result independently from the problem data.
const near=(a,b,label)=>assert(Math.abs(a-b)<1e-8, `${label}: ${a} != ${b}`);
const PI=Math.PI, SQ3=Math.sqrt(3);
const polygonArea = points => Math.abs(points.reduce((s,[x,y],i)=>{const [u,v]=points[(i+1)%points.length];return s+x*v-y*u;},0))/2;
near((1+1)**2-4*(PI/4),4-PI,'geo-01');
near(PI*2**2/6-(2*2*Math.sin(PI/3)/2),2*PI/3-SQ3,'geo-02');
near((2*10)**2-4*PI*(10/2)**2,400-100*PI,'geo-03');
const side=Math.sqrt(4*9*SQ3/SQ3); near(PI*(side*SQ3/2)**2,27*PI,'geo-04');
near((PI-PI*.5**2)/PI,.75,'geo-05');
for(const x of [0,1,2,4,6,8]) {
  const area=polygonArea([[0,x],[8-x,0],[8,8-x],[x,8]]);
  assert(area>=32); near(area,2*(x-4)**2+32,'geo-06');
}
near(PI*(9**2-6**2),45*PI,'geo-07');
near(Math.sqrt(4**2-2**2),2*SQ3,'geo-08a');
near(6*(4**2*SQ3/4)-2*(120/360)*PI*4**2,(72*SQ3-32*PI)/3,'geo-08b');
const h=Math.sqrt(6**2-3**2); near(PI*((2*h/3)**2-(h/3)**2),9*PI,'geo-09');
const apothem=2*SQ3; near(6*(2*apothem/SQ3)*apothem/2,24*SQ3,'geo-10');
near((360-4*60)/360*36,12,'geo-11');
near(PI*(3**2-(3/2)**2),27*PI/4,'geo-12');
near(8*8/2-(8/2)*(8/2)/2-3.1*(4/2)**2,11.6,'geo-13');
const d=Math.sqrt(5**2-3**2); near(d*3/2+PI*(d/2)**2/2,6+2*PI,'geo-14');
near(PI*((24/2)**2-(24/4)**2),108*PI,'geo-15');
near((6*6-PI*3*3)/2+(2*45/360)*PI*3*3,18-9*PI/4,'geo-16');
// Integrate the region under min(diagonal, semicircle), independently of the decomposition.
let numerical=0, n=100000, dx=4/n;
for(let i=0;i<n;i++){const x=(i+.5)*dx;numerical+=Math.min(x,Math.sqrt(Math.max(0,4-(x-2)**2)))*dx;}
assert(Math.abs(numerical-(PI+2))<1e-6,'geo-17 integration');

const initial=(520-48*5)/(48-40); near(initial+5,40,'mat-01'); near(48*(initial+5)-40*initial,520,'mat-01 budget');
near((1+5)*(-4+5),6,'mat-02'); for(const rootValue of [1,-4])near(2*rootValue**2+6*rootValue-8,0,'mat-02 roots');
for(const [x,y] of [[4,5.4],[8,5.8],[12,6.2]])near(.1*x+5,y,'mat-03');
near(-5*0**2+30*0,0,'mat-04 launch');near(-5*6**2+30*6,0,'mat-04 return');near(-5*3**2+30*3,45,'mat-04 max');
for(let i=0;i<=900;i++){const x=-4+i/100;assert.equal((x+2)*(x-3)*x<0,(x>=-4&&x< -2)||(x>0&&x<3),'mat-05 '+x);}
near(1500*2**8,384000,'mat-06');assert(1500*2**9>384000);
near(2**(3**2-9),4**(3**2-3*3),'mat-07');near(2**3,8,'mat-07 answer');
near(Math.log2(0+1),0,'mat-08 origin');near(Math.log2(2/2+1),1,'mat-08 point');near((2/2)*1,1,'mat-08 area');
near((90-15*Math.log10(1))-(90-15*Math.log10(99+1)),30,'mat-09');
const expectedLetters={ 'geo-01':'D','geo-03':'E','geo-04':'A','geo-05':'B','geo-06':'D','geo-07':'E','geo-09':'C','geo-12':'A','geo-13':'A','geo-16':'B','geo-17':'B', 'mat-01':'D','mat-02':'A','mat-03':'A','mat-04':'D','mat-05':'B','mat-06':'C','mat-07':'D','mat-08':'B','mat-09':'E' };
for(const q of pages.flatMap(p=>p.items))if(q.choices.length)assert(q.answer.includes('('+expectedLetters[q.id]+')'),q.id+' option');
assert(pages[1].items[6].note.includes('duplicação'),'Source typo must be documented');
console.log(`2 páginas; 26 exercícios; 19 figuras acessíveis; ${formulas} fórmulas válidas. Cálculos, alternativas, navegação, scripts e links conferidos.`);
