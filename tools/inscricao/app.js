const exercises=/* DATA */;
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=n=>Number(n.toFixed(3)).toLocaleString('pt-BR');
const root3=Math.sqrt(3), root2=Math.sqrt(2);
function geometryValues(e,k=1){
 const b=e.base*k;
 switch(e.id){
 case 1:return {radius:b,result:root3*b,summary:`Raio = ${fmt(b)} cm; AO = ${fmt(2*b)} cm; AE ≈ ${fmt(root3*b)} cm.`};
 case 2:return {radius:b/root3,result:b/root3,summary:`Lado = ${fmt(b)} cm; altura ≈ ${fmt(b*root3/2)} cm; R ≈ ${fmt(b/root3)} cm.`};
 case 3:return {radius:b,result:b*root3/2,summary:`R = ${fmt(b)} cm; lado = ${fmt(b)} cm; apótema ≈ ${fmt(b*root3/2)} cm.`};
 case 4:return {radius:b,result:2*b*root3,summary:`Lado do quadrado ≈ ${fmt(b*root2)} m; R = ${fmt(b)} m; lado do triângulo ≈ ${fmt(2*b*root3)} m.`};
 case 5:return {radius:b,result:2,summary:`R = ${fmt(b)}; h₁ = ${fmt(1.5*b)}; h₂ = ${fmt(3*b)}. A razão h₂/h₁ permanece 2.`};
 case 6:return {radius:b/3,result:2/9,summary:`h = ${fmt(b)}; R₁ = ${fmt(b/3)}; R₂ = ${fmt(b/9)}. (R₁ − R₂)/h = 2/9 em qualquer escala.`};
 case 7:return {radius:b,result:8*k,summary:`Raio = ${fmt(b)}; altura de r = ${fmt(18*k)}; altura de m = ${fmt(10*k)}; x = ${fmt(8*k)}.`};
 case 8:return {radius:b,result:root2/2,summary:`R = ${fmt(b)}; lado interno ≈ ${fmt(root2*b)}; lado externo = ${fmt(2*b)}. Razão = √2/2.`};
 case 9:return {radius:b,result:b*root3/2,summary:`Lado maior = ${fmt(b)} cm; diagonal menor ≈ ${fmt(b*root3)} cm; lado menor ≈ ${fmt(b*root3/2)} cm.`};
 case 10:return {radius:b,result:2*b,summary:`Lado do triângulo ≈ ${fmt(root3*b)} cm; R = ${fmt(b)} cm; lado do quadrado = ${fmt(2*b)} cm.`};
 case 11:return {radius:b,result:8*b,summary:`Lado do triângulo ≈ ${fmt(2*root3*b)}; r = ${fmt(b)}; lado do quadrado = ${fmt(2*b)}; perímetro = ${fmt(8*b)}.`};
 case 12:return {radius:b,result:4*root3*b,summary:`Apótema = ${fmt(b)} cm; lado ≈ ${fmt(2*b/root3)} cm; perímetro ≈ ${fmt(4*root3*b)} cm.`};
 case 13:return {radius:b,result:6.4*b,summary:`R = ${fmt(b)} cm; lado = ${fmt(1.6*b)} cm; perímetro = ${fmt(6.4*b)} cm.`};
 case 14:return {radius:b,result:[2*root3*b,3*b,Math.sqrt(21)*b],summary:`R = ${fmt(b)} km; d₃,₈ ≈ ${fmt(2*root3*b)} km; d₃,₅ = ${fmt(3*b)} km; d₅,₈ ≈ ${fmt(Math.sqrt(21)*b)} km.`};
 }
}
function geometryDrawing(e,stage=0,k=1,prompt=false){
 const green='#42644f',orange='#a04f2c',purple='#78658e',grey='#adb8ab';
 const unit=e.id===14?57:83,cx=e.id===14?265:300,cy=235;
 const X=x=>cx+unit*x,Y=y=>cy-unit*y;
 const txt=(x,y,t,color=green)=>`<text x="${X(x)}" y="${Y(y)}" fill="${color}" font-size="16" text-anchor="middle" paint-order="stroke" stroke="#fffef9" stroke-width="4" stroke-linejoin="round">${esc(t)}</text>`;
 const line=(a,b,color=orange,dash=false,width=2.5)=>`<line x1="${X(a[0])}" y1="${Y(a[1])}" x2="${X(b[0])}" y2="${Y(b[1])}" stroke="${color}" stroke-width="${width}"${dash?' stroke-dasharray="6 5"':''}/>`;
 const poly=(ps,color=green,fill='none')=>`<polygon points="${ps.map(p=>`${X(p[0])},${Y(p[1])}`).join(' ')}" stroke="${color}" stroke-width="2.5" fill="${fill}"/>`;
 const circle=(r=1,x=0,y=0,dash=false)=>`<circle cx="${X(x)}" cy="${Y(y)}" r="${r*unit}" fill="none" stroke="${grey}" stroke-width="2"${dash?' stroke-dasharray="5 5"':''}/>`;
 const dot=(p,label,dx=0,dy=.15)=>`<circle cx="${X(p[0])}" cy="${Y(p[1])}" r="3.5" fill="${green}"/>`+txt(p[0]+dx,p[1]+dy,label);
 const regular=(n,r=1,angle=Math.PI/2)=>Array.from({length:n},(_,i)=>[r*Math.cos(angle+2*Math.PI*i/n),r*Math.sin(angle+2*Math.PI*i/n)]);
 const outer=[[0,2],[-root3,-1],[root3,-1]],inner=regular(3),square=[[-1,1],[1,1],[1,-1],[-1,-1]],diamond=regular(4),hex=regular(6,1,Math.PI/3);
 const v=geometryValues(e,k),r=v.radius,b=e.base*k;
 const right=(x,y)=>poly([[x,y],[x+.12,y],[x+.12,y+.12],[x,y+.12]],orange);
 let s='';
 if(e.id===14){
  const centers=[[0,0],[1.5,root3/2],[0,root3],[-1.5,root3/2],[-1.5,-root3/2],[0,-root3],[1.5,-root3/2],[3,0]];
  centers.forEach((c,i)=>{s+=poly(regular(6,1,0).map(p=>[p[0]+c[0],p[1]+c[1]]),grey);if(stage>=1&&[2,4,7].includes(i))s+=circle(1,...c,true);s+=dot(c,String(i+1),0,-.23);});
  if(stage>=1)s+=line(centers[0],centers[1],purple)+txt(.7,.7,'√3 R',purple);
  if(stage>=2){s+=line(centers[2],centers[7],orange)+line(centers[2],centers[4],green)+line(centers[4],centers[7],purple);s+=line(centers[4],[3,-root3/2],purple,true)+line([3,-root3/2],centers[7],purple,true);}
  if(stage>=3)s+=txt(2.1,1.5,'d₃,₈ = 2√3 R',orange)+txt(-2.5,-.2,'d₃,₅ = 3R')+txt(1,-1.7,'d₅,₈ = √21 R',purple);
 }else if(e.id===6){
  s+=poly(outer)+circle()+circle(1/3,0,4/3)+dot([0,2],'A',0,.22)+txt(-.65,0,'C₁')+txt(-.5,1.35,'C₂');
  s+=line([2,-1],[2,2],grey)+txt(2.2,.5,'h');
  if(stage>=1)s+=line([0,2],[0,0],orange,true)+line([0,0],[0,-1],green)+txt(.35,-.55,'R₁');
  if(stage>=2)s+=line([0,4/3],[0,1],purple)+dot([0,0],'O₁',.35)+dot([0,4/3],'O₂',.35)+txt(.4,1.07,'R₂',purple);
  if(stage>=3)s+=txt(0,-1.55,'R₁ = h/3; R₂ = h/9');
 }else if(e.id===7){
  s+=circle()+line([0,-2],[-root3,1],green)+line([0,-2],[root3,1],green);
  for(const [y,l] of [[1,'r'],[-1/3,'m'],[-2,'s']])s+=line([-2.3,y],[2.3,y],grey)+txt(2.5,y,l);
  s+=line([-2,-2],[-2,-1/3],orange)+txt(-2.3,-1.2,fmt(10*k))+line([-2,-1/3],[-2,1],purple)+txt(-2.3,.25,'x',purple);
  s+=txt(-.65,-1.9,'60°')+txt(.65,-1.9,'60°')+line([0,0],[.866,-.5],orange)+txt(.7,-.1,fmt(b));
  if(stage>=1)s+=line([0,-2],[0,1],orange,true)+dot([0,0],'O',-.2);
  if(stage>=2)s+=poly([[0,-2],[0,0],[.866,-.5]],orange,'#d5e5ad55')+txt(-.38,-1,'2R');
  if(stage>=3)s+=txt(1.7,-1.35,`x = ${fmt(8*k)}`,purple);
 }else if(e.id===13){
  s+=circle()+poly([[-.8,1],[.8,1],[.8,-.6],[-.8,-.6]])+dot([0,0],'O',-.2)+dot([0,1],'T',0,.2);
  s+=txt(1.12,.4,'l')+txt(0,-.95,'l');
  if(stage>=1)s+=line([0,0],[0,1],green)+txt(.22,.55,`R=${fmt(r)}`)+line([0,0],[.8,-.6],orange);
  if(stage>=2)s+=poly([[0,0],[0,-.6],[.8,-.6]],orange,'#d5e5ad55')+right(0,-.6)+txt(.4,-.85,'l/2')+txt(-.45,-.35,'|l−R|');
  if(stage>=3)s+=txt(0,-1.5,`l = ${fmt(1.6*r)}; P = ${fmt(6.4*r)}`);
 }else if(e.id===9){
  const mids=hex.map((p,i)=>{const q=hex[(i+1)%6];return [(p[0]+q[0])/2,(p[1]+q[1])/2];});
  s+=poly(hex)+poly(mids,purple);
  const labels=['B','A','F','E','D','C'];hex.forEach((p,i)=>s+=txt(p[0]*1.2,p[1]*1.2,labels[i]));
  ['M','S','R','Q','P','N'].forEach((l,i)=>s+=txt(mids[i][0]*.86,mids[i][1]*.86,l,purple));
  if(stage>=1)s+=poly([hex[0],hex[1],hex[2]],green,'#d5e5ad55')+line(hex[0],hex[2],orange,true);
  if(stage>=2)s+=line(mids[0],mids[1],purple,false,5)+txt(-.6,1.55,`L = ${fmt(b)}`);
  if(stage>=3)s+=txt(0,-1.65,`L menor = L√3/2 ≈ ${fmt(v.result)}`,purple);
 }else if([3,12].includes(e.id)){
  const rr=e.id===3?1:2/root3,ps=regular(6,rr,Math.PI/3),p=ps[0],q=ps[1],mid=[0,(p[1]+q[1])/2];
  s+=circle()+poly(ps);
  if(stage>=1)s+=line([0,0],p,green)+line([0,0],mid,orange)+dot([0,0],'O',-.2)+txt(.45,.2,e.id===3?'R':'L')+txt(-.3,.5,'a',orange);
  if(stage>=2)s+=poly([[0,0],mid,p],orange,'#d5e5ad55')+right(0,mid[1]-.12)+txt(.3,mid[1]+.24,'L/2');
  if(stage>=3)s+=txt(0,-1.7,e.id===3?`a ≈ ${fmt(v.result)} cm`:`P ≈ ${fmt(v.result)} cm`);
 }else{
  s+=circle();
  if([1,4,5,11].includes(e.id))s+=poly(outer);
  if([2,5,10].includes(e.id))s+=poly(e.id===5?regular(3,1,-Math.PI/2):inner,purple);
  if([4,8].includes(e.id))s+=poly(diamond,purple);
  if([8,10,11].includes(e.id))s+=poly(square,orange);
  if(e.id===1){s+=dot([0,2],'A',0,.25)+dot([-root3,-1],'B',-.15,-.2)+dot([root3,-1],'C',.15,-.2)+dot([.866,.5],'E',.2,.1)+dot([0,-1],'D',0,-.23);if(stage>=1)s+=line([0,2],[0,-1],grey,true)+dot([0,0],'O',-.2)+line([0,0],[.866,.5],orange)+txt(.5,.12,`r=${fmt(r)}`);if(stage>=2)s+=poly([[0,2],[0,0],[.866,.5]],orange,'#d5e5ad55');if(stage>=3)s+=line([0,2],[.866,.5],purple,false,5)+txt(1.15,1.5,`AE≈${fmt(v.result)}`,purple);}
  else if(e.id===2){if(stage>=1)s+=line([0,1],[0,-.5],orange,true)+dot([0,0],'O',.2);if(stage>=2)s+=poly([[0,1],[0,-.5],[.866,-.5]],orange,'#d5e5ad55')+right(0,-.5)+txt(.45,-.78,`L/2=${fmt(b/2)}`);if(stage>=3)s+=line([0,0],[0,1],purple,false,5)+txt(-.7,.55,`R≈${fmt(v.result)}`,purple);}
  else if(e.id===5){s+=txt(-1.4,-1.3,'T₂')+txt(-.7,-.7,'T₁',purple);if(stage>=1)s+=line([.2,.5],[.2,-1],purple,true)+txt(.6,.25,'h₁',purple);if(stage>=2)s+=line([-2,-1],[-2,2],orange)+txt(-2.3,.6,'h₂',orange);if(stage>=3)s+=txt(0,-1.7,'h₂/h₁ = 2');}
  else{if(stage>=1)s+=dot([0,0],'O',-.2)+line([0,0],[1,0],green)+txt(.5,.2,`R=${fmt(r)}`);if(stage>=2){if([4,8].includes(e.id))s+=line([-1,0],[1,0],purple,true)+txt(0,-.3,'diagonal = 2R',purple);else s+=line([-1,-1.2],[1,-1.2],orange)+txt(0,-1.5,'lado do quadrado = 2R',orange);}if(stage>=3)s+=txt(0,2.35,e.id===8?'Razão = √2/2':`Resultado ≈ ${fmt(v.result)} ${e.unit}`);}
 }
 const caption=prompt?'Figura reconstruída a partir da lista.':`Etapa ${stage+1}: ${['figuras e dados','raios e alturas','relações geométricas','resultado'][stage]}. ${v.summary}`;
 return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${e.id===14?'70 20 480 410':e.id===7?'70 20 460 420':'100 20 400 400'}" role="img" aria-label="${esc(caption)}"><title>${esc(e.title)}</title>${s}</svg>`;
}
const key='inscricao-lista9-2026-progress';let done=new Set();try{const a=JSON.parse(localStorage.getItem(key)||'[]');if(Array.isArray(a))done=new Set(a.filter(n=>Number.isInteger(n)&&n>=1&&n<=14));}catch{}
function math(el){renderMathInElement(el,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:true,strict:'ignore',trust:false});}
const container=document.getElementById('exercises');
for(const e of exercises){
 const c=document.createElement('article');c.className='geo-card';c.dataset.id=e.id;
 c.innerHTML=`<header class="card-heading"><span class="number">${String(e.id).padStart(2,'0')}</span><h2>${esc(e.title)}</h2></header><p>${esc(e.q)}</p><div class="prompt-figure">${geometryDrawing(e,0,1,true)}</div>${e.choices.length?`<ol type="a" class="choices">${e.choices.map(x=>`<li>${esc(x)}</li>`).join('')}</ol>`:''}<div class="actions"><button class="reveal" aria-expanded="false" aria-controls="solution-${e.id}">Ver solução ${e.id}</button><label><input class="complete" type="checkbox" ${done.has(e.id)?'checked':''}> Concluído</label></div><section id="solution-${e.id}" class="solution" aria-label="Solução da questão ${e.id}" hidden><h3>Solução passo a passo</h3><ol class="full-steps">${e.steps.map(x=>`<li>${esc(x)}</li>`).join('')}</ol><div class="interactive"><h3>Construa o raciocínio</h3><div class="live-drawing"></div><div class="current-step" aria-live="polite"></div><div class="play-controls"><button data-action="play">Reproduzir etapas</button><button data-action="prev">← Anterior</button><button data-action="next">Próxima →</button><button data-action="reset">Reiniciar</button></div><label class="step-label">Etapa <output class="step-value"></output><input class="stage" type="range" min="0" max="3" value="0" step="1" aria-label="Etapa da solução ${e.id}"></label><label>Escala das medidas <output class="scale-value"></output><input class="scale" type="range" min="50" max="150" value="100" step="5" aria-label="Escala das medidas da questão ${e.id}"></label><button class="restore">Restaurar valores do enunciado</button><p class="scale-note">A escala varia todas as medidas de comprimento na mesma proporção. As etapas escritas usam os valores originais; as razões permanecem iguais.</p><p class="values"></p><p class="player-status" aria-live="polite"></p></div><p class="answer"><strong>Resposta:</strong> ${esc(e.answer)}</p></section>`;
 container.append(c);
}
math(container);
const players=[];
for(const c of container.children){const e=exercises[Number(c.dataset.id)-1],sol=c.querySelector('.solution'),reveal=c.querySelector('.reveal'),stageSlider=c.querySelector('.stage'),scaleSlider=c.querySelector('.scale'),play=c.querySelector('[data-action="play"]'),prev=c.querySelector('[data-action="prev"]'),next=c.querySelector('[data-action="next"]');let stage=0,scale=1,timer=null;
 const stop=()=>{clearInterval(timer);timer=null;play.textContent='Reproduzir etapas';};
 const render=()=>{c.querySelector('.live-drawing').innerHTML=geometryDrawing(e,stage,scale);const note=c.querySelector('.current-step');note.textContent=e.steps[stage];math(note);stageSlider.value=stage;c.querySelector('.step-value').textContent=`${stage+1} de 4`;c.querySelector('.scale-value').textContent=`${fmt(scale)}×`;c.querySelector('.values').textContent=geometryValues(e,scale).summary;prev.disabled=stage===0;next.disabled=stage===3;};
 reveal.addEventListener('click',()=>{sol.hidden=!sol.hidden;reveal.setAttribute('aria-expanded',String(!sol.hidden));reveal.textContent=sol.hidden?`Ver solução ${e.id}`:`Ocultar solução ${e.id}`;if(sol.hidden)stop();});
 prev.addEventListener('click',()=>{stop();stage=Math.max(0,stage-1);render();});next.addEventListener('click',()=>{stop();stage=Math.min(3,stage+1);render();});
 stageSlider.addEventListener('input',()=>{stop();stage=Number(stageSlider.value);render();});scaleSlider.addEventListener('input',()=>{stop();scale=Number(scaleSlider.value)/100;render();});
 c.querySelector('[data-action="reset"]').addEventListener('click',()=>{stop();stage=0;render();});c.querySelector('.restore').addEventListener('click',()=>{stop();scale=1;scaleSlider.value=100;render();});
 play.addEventListener('click',()=>{if(timer){stop();c.querySelector('.player-status').textContent='Reprodução pausada.';return;}players.forEach(p=>p.stop());if(stage===3)stage=0;render();play.textContent='Pausar';c.querySelector('.player-status').textContent='Reproduzindo uma etapa a cada 3 segundos.';timer=setInterval(()=>{if(document.hidden||sol.hidden||c.hidden){stop();return;}stage++;render();if(stage===3){stop();c.querySelector('.player-status').textContent='Solução concluída. Explore a escala ou volte às etapas anteriores.';}},3000);});
 c.querySelector('.complete').addEventListener('change',ev=>{ev.target.checked?done.add(e.id):done.delete(e.id);try{localStorage.setItem(key,JSON.stringify([...done]));}catch{document.getElementById('storage').hidden=false;}update();});players.push({stop,c});render();
}
function update(){let shown=0;const pending=document.getElementById('pending').checked;for(const c of container.children){c.hidden=pending&&done.has(Number(c.dataset.id));if(!c.hidden)shown++;}document.getElementById('progress').textContent=`${done.size} de 14 concluídos · ${shown} exibidos`;document.getElementById('empty').hidden=shown!==0;players.forEach(p=>{if(p.c.hidden)p.stop();});}
document.getElementById('pending').addEventListener('change',update);document.addEventListener('visibilitychange',()=>{if(document.hidden)players.forEach(p=>p.stop());});window.addEventListener('beforeprint',()=>players.forEach(p=>p.stop()));document.getElementById('print').addEventListener('click',()=>window.print());update();
