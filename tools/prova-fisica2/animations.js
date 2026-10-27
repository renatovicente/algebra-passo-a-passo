'use strict';
function physicsState(id,p){
 p=Math.max(0,Math.min(1,p));
 if(id===1){const t=2*p;return {t,a:2,x:t*t,v:2*t,T:16,N:34};}
 if(id===2){const t=4*p;return {t,x:15*t,y:80-5*t*t,vx:15,vy:-10*t};}
 if(id===3){const t=4*p;return {t,x:6*t,y:75-3*t*t,vy:-6*t,ay:-6};}
 if(id===4)return {fraction:p,object:80-40*p,water:20+20*p,Q:12000*p};
 const t=360*p,Q=10*t,melt=Math.max(0,(Q-400)/80);
 return {t,Q,QJ:4*Q,temp:Math.min(0,-10+Q/40),water:melt,ice:80-melt};
}
const PhysicsVisuals=(()=>{
 const f=(n,d=1)=>Number((Math.abs(n)<1e-8?0:n).toFixed(d)).toLocaleString('pt-BR',{maximumFractionDigits:d});
 const text=(x,y,s,extra='')=>`<text x="${x}" y="${y}" ${extra}>${s}</text>`;
 const line=(x1,y1,x2,y2,color='#243f35',dash='')=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="2" ${dash?'stroke-dasharray="5 5"':''}/>`;
 function arrow(x1,y1,x2,y2,color='#8b4527'){
  const dx=x2-x1,dy=y2-y1,len=Math.hypot(dx,dy);if(len<.01)return '';
  const ux=dx/len,uy=dy/len,size=Math.min(9,len*.45);
  return line(x1,y1,x2,y2,color)+`<polygon points="${x2},${y2} ${x2-size*ux+size*.45*uy},${y2-size*uy-size*.45*ux} ${x2-size*ux-size*.45*uy},${y2-size*uy+size*.45*ux}" fill="${color}"/>`;
 }
 const rect=(x,y,w,h,fill='#e9eddf')=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="4" fill="${fill}" stroke="#657168"/>`;
 const circle=(x,y,r=7,color='#8b4527')=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${color}"/>`;
 function wrap(content,label,height=320){return `<svg viewBox="0 0 680 ${height}" role="img" aria-label="${label}">${content}</svg>`;}
 function pulley(p,solution){
  const s=physicsState(1,p),ax=190+s.x*22,by=260+s.x*22;
  let c=line(25,235,480,235)+line(455,235,455,470)+rect(ax,175,80,60)+text(ax+40,216,'A · 4 kg','text-anchor="middle"')+line(ax+80,195,480,195)+`<circle cx="480" cy="215" r="20" fill="none" stroke="#243f35" stroke-width="2"/>`+line(500,215,500,by)+rect(470,by,60,50)+text(500,by+22,'B','text-anchor="middle"')+text(500,by+43,'2 kg','text-anchor="middle"')+arrow(ax,175,ax-60,130)+text(ax-95,112,'F = 10 N')+line(ax-80,175,ax,175,'#657168',true)+text(ax-43,166,'θ');
  if(solution){
   c+=arrow(ax+80,195,ax+132,195,'#347b8e')+text(ax+100,180,'T = 16 N')+arrow(ax+40,175,ax+40,120,'#347b8e')+text(ax+20,99,'N = 34 N')+arrow(ax+40,235,ax+40,305)+text(ax+52,310,'P = 40 N')+arrow(500,by,500,by-48,'#347b8e')+text(516,by-25,'T = 16 N')+arrow(500,by+50,500,by+110)+text(516,by+99,'P = 20 N')+text(30,390,'A: T − 8 = 4a')+text(30,422,'B: 20 − T = 2a')+text(30,454,'A: N + 6 − 40 = 0');
  }else c+=text(30,285,'Mesa sem atrito · fio e polia ideais');
  return wrap(c,solution?'Bloco A acelera para a direita e B para baixo com a mesma aceleração. Sobre A, tração para a direita, força oblíqua para a esquerda e cima, normal para cima e peso para baixo. Sobre B, tração para cima e peso para baixo.':'Bloco A de 4 kg na mesa ligado por fio que passa por polia fixa a B de 2 kg suspenso. Uma força de 10 N puxa A para a esquerda e para cima.',solution?490:345);
 }
 function launch(p,solution){
  const s=physicsState(2,p),sx=x=>100+x*7.2,sy=y=>270-y*2.4;
  let c=rect(30,sy(80),70,270-sy(80))+line(25,270,650,270)+text(32,185,'80 m')+text(575,298,'x (m)')+text(34,40,'y (m)')+text(79,295,'0');
  if(solution){
   const path=Array.from({length:61},(_,i)=>{const t=4*i/60;return `${i?'L':'M'}${sx(15*t)},${sy(80-5*t*t)}`;}).join(' ');
   c+=`<path d="${path}" fill="none" stroke="#9aa68d" stroke-width="2" stroke-dasharray="5 5"/>`+line(100,sy(s.y),sx(s.x),sy(s.y),'#657168',true)+circle(100,sy(s.y),5,'#347b8e')+circle(sx(s.x),sy(s.y))+arrow(sx(s.x),sy(s.y),sx(s.x)+s.vx*1.3,sy(s.y),'#347b8e')+arrow(sx(s.x),sy(s.y),sx(s.x),sy(s.y)-s.vy*1.3)+text(sx(s.x)+12,sy(s.y)-13,'vₓ')+text(sx(s.x)+12,sy(s.y)-s.vy*1.3+18,'vᵧ')+text(285,34,'Mesma queda, mesmo tempo')+text(510,295,'60');
  }else c+=circle(100,sy(80))+arrow(100,sy(80),210,sy(80),'#347b8e')+text(110,sy(80)-18,'15 m/s')+arrow(610,100,610,155)+text(532,90,'g = 10 m/s²');
  return wrap(c,solution?'Trajetória parabólica da esfera, com componentes de velocidade horizontal constante e vertical crescente em módulo. Um ponto azul em queda vertical permanece na mesma altura da esfera.':'Esfera sai horizontalmente a 15 m/s de uma passarela a 80 m do solo.',350);
 }
 function velocityGraph(p,solution=false){
  const s=physicsState(3,p),gx=t=>85+t/4*490,gy=v=>65-v/24*180;
  let c=arrow(85,65,625,65,'#657168')+arrow(85,30,85,265,'#657168')+text(25,28,'vᵧ (m/s)')+text(610,48,'t (s)')+text(65,58,'0')+text(570,50,'4')+text(28,251,'−24')+line(85,245,575,245,'#9aa68d',true)+line(575,65,575,245,'#9aa68d',true)+line(85,65,575,245,'#8b4527');
  if(solution)c+=`<polygon points="85,65 ${gx(s.t)},65 ${gx(s.t)},${gy(s.vy)}" fill="#dfb79c" opacity=".35"/>`+circle(gx(s.t),gy(s.vy))+line(gx(s.t),65,gx(s.t),gy(s.vy),'#347b8e',true)+text(130,298,`Inclinação = −6 m/s² · área = ${f(s.y-75)} m`);
  return wrap(c,'Gráfico de velocidade vertical por tempo: reta de zero a menos 24 m/s em 4 segundos. A área com sinal representa o deslocamento vertical.',330);
 }
 function planet(p){
  const s=physicsState(3,p),x=100+s.x*18,y=265-s.y*2.5;
  return wrap(line(45,265,620,265)+text(30,295,'Solo: y = 0')+text(30,38,'Posição da partícula')+line(100,77.5,100,265,'#9aa68d',true)+text(23,83,'75 m')+circle(x,y)+arrow(x,y,x,y-s.vy*1.7)+text(x+15,y-13,`y = ${f(s.y)} m`)+text(345,295,'Cima positivo · g = 6 m/s²'),320);
 }
 function equilibrium(p){
  const s=physicsState(4,p),base=245,scale=2;
  let c=text(175,30,'Objeto · C = 300 J/°C','text-anchor="middle"')+text(505,30,'Água · C = 600 J/°C','text-anchor="middle"');
  for(const [x,T,color,name] of [[175,s.object,'#b66b44','Objeto'],[505,s.water,'#347b8e','Água']])c+=rect(x-55,65,110,180,'#f7f7ef')+rect(x-53,base-T*scale,106,T*scale,color)+text(x,275,`${f(T)} °C`,'text-anchor="middle"')+text(x,300,name,'text-anchor="middle"');
  c+=line(95,base-40*scale,585,base-40*scale,'#657168',true)+text(286,base-40*scale-12,'40 °C');
  if(p<1)c+=arrow(255,200,425,200)+text(340,226,'calor','text-anchor="middle"');else c+=text(340,205,'Equilíbrio','text-anchor="middle"');
  return wrap(c,'Temperaturas do objeto e da água. O calor flui do objeto quente para a água fria. A temperatura do objeto varia duas vezes mais que a da água, porque sua capacidade térmica é metade. Ambos chegam a 40 graus Celsius.',320);
 }
 function phase(p){
  const s=physicsState(5,p),gx=q=>85+q/3600*500,gy=t=>80-t*14;
  let c=arrow(85,260,635,260,'#657168')+arrow(85,260,85,35,'#657168')+text(20,28,'T (°C)')+text(570,301,'Q (cal)')+text(55,85,'0')+text(25,225,'−10')+text(71,283,'0')+text(gx(400),283,'400','text-anchor="middle"')+text(gx(3600),283,'3600','text-anchor="middle"')+line(85,80,585,80,'#9aa68d',true)+line(gx(400),80,gx(400),260,'#9aa68d',true)+`<path d="M85 220 L${gx(400)} 80 H585" stroke="#8b4527" stroke-width="3" fill="none"/>`+circle(gx(s.Q),gy(s.temp))+text(155,180,'gelo aquece até 0 °C')+text(365,65,'fusão a 0 °C')+text(100,325,'Massas · total de 80 g');
  c+=rect(85,340,500*(s.ice/80),35,'#d8e7e7');if(s.water>0)c+=rect(85+500*s.ice/80,340,500*s.water/80,35,'#347b8e');
  c+=text(85,405,`Gelo: ${f(s.ice)} g`)+text(410,405,`Água: ${f(s.water)} g`);
  return wrap(c,'Curva de aquecimento: a temperatura sobe de menos 10 a zero grau com 400 calorias e permanece em zero durante a fusão. A barra inferior mostra as massas, até 40 gramas de gelo e 40 gramas de água.',430);
 }
 function diagram(kind){
  if(kind==='pulley')return pulley(0,false);
  if(kind==='launch')return launch(0,false);
  if(kind==='exam-graph')return velocityGraph(0,false);
  return wrap(rect(210,70,250,130,'#d8e7e7')+text(335,122,'80 g de gelo','text-anchor="middle"')+text(335,158,'−10 °C','text-anchor="middle"')+rect(235,235,200,40,'#f0d2bd')+text(335,262,'Fonte de 40 W','text-anchor="middle"')+arrow(290,230,290,205)+arrow(380,230,380,205),'Amostra de 80 gramas de gelo a menos 10 graus recebe energia de uma fonte de 40 watts.',300);
 }
 const configs={
  1:{title:'O fio liga os dois movimentos',label:'Tempo do movimento (0 a 2 s)',marks:[0,.25,.5,.75,1],note:'Para visualizar, o sistema parte do repouso e a mesa é suficientemente longa. O fio mantém seu comprimento. As setas indicam sentidos; seus comprimentos são esquemáticos.',draw:p=>pulley(p,true),read:s=>[['Tempo',`${f(s.t)} s`],['Deslocamento de cada bloco',`${f(s.x)} m`],['Rapidez de cada bloco',`${f(s.v)} m/s`],['Aceleração (módulo)',`${s.a} m/s²`],['Tração',`${s.T} N`],['Normal de A',`${s.N} N`]],caption:s=>'Somando as equações nos sentidos do fio: 20 − 8 = (4 + 2)a. A acelera para a direita; B acelera para baixo. A tração se cancela na soma das equações.'},
  2:{title:'O alcance vem depois do tempo',label:'Tempo de queda (0 a 4 s)',marks:[0,.25,.5,.75,1],note:'O ponto azul cai verticalmente do mesmo nível, a partir do repouso. A esfera e o ponto azul permanecem na mesma altura. Vetores em escala própria; reprodução em câmera lenta.',draw:p=>launch(p,true),read:s=>[['Tempo',`${f(s.t)} s`],['x',`${f(s.x)} m`],['Altura y',`${f(s.y)} m`],['vₓ',`${s.vx} m/s`],['vᵧ',`${f(s.vy)} m/s`]],caption:s=>s.t<4?'A altura é y = 80 − 5t² e a posição horizontal é x = 15t. A gravidade altera apenas a velocidade vertical.':'A esfera chega ao solo em 4 s, a 60 m da passarela. Os vetores representam a velocidade imediatamente antes do impacto; a colisão não é simulada.'},
  3:{title:'A inclinação determina a aceleração',label:'Tempo no gráfico (0 a 4 s)',marks:[0,.5,.75,1],note:'A área sombreada tem sinal negativo e representa o deslocamento vertical. A animação termina em 4 s, antes de a partícula chegar ao solo.',draw:p=>`<div class="visual-pair">${velocityGraph(p,true)}${planet(p)}</div>`,read:s=>[['Tempo',`${f(s.t)} s`],['aᵧ',`${s.ay} m/s²`],['vᵧ',`${f(s.vy)} m/s`],['Altura y',`${f(s.y)} m`],['Deslocamento Δy',`${f(s.y-75)} m`]],caption:s=>'A inclinação é −24/4 = −6 m/s². Some o deslocamento à altura inicial: y = 75 − 3t². Em 2 s, y = 63 m; em 3 s, vᵧ = −18 m/s.'},
  4:{title:'Capacidades diferentes, mesma energia trocada',label:'Fração da energia trocada (0 a 100%)',marks:[0,.5,1],note:'O controle representa energia transferida, não tempo físico. As colunas indicam temperaturas uniformes, não níveis de líquido. O modelo vale para o item (b).',draw:equilibrium,read:s=>[['Energia trocada',`${f(s.fraction*100)}%`],['Objeto',`${f(s.object)} °C`],['Água',`${f(s.water)} °C`],['Q do objeto',`${s.Q?'−':''}${f(s.Q,0)} J`],['Q da água',`+${f(s.Q,0)} J`]],caption:s=>s.fraction<1?'A água tem o dobro da capacidade térmica do objeto. Para a mesma energia, a temperatura do objeto varia pelo dobro do módulo: ΔT do objeto = −2 · ΔT da água.':'No equilíbrio, ambos estão a 40 °C. O objeto perde 12.000 J e esfria 40 °C; a água recebe 12.000 J e aquece 20 °C. A soma dos calores é zero.'},
  5:{title:'A energia decide quanto gelo derrete',label:'Tempo de aquecimento (0 a 360 s)',marks:[0,1/9,1],note:'A reprodução comprime 6 minutos de aquecimento. A barra representa proporções de massa, não volumes. Adota-se equilíbrio térmico na amostra.',draw:phase,read:s=>[['Tempo',`${f(s.t,0)} s`],['Calor',`${f(s.Q,0)} cal`],['Energia',`${f(s.QJ,0)} J`],['Temperatura',`${f(s.temp)} °C`],['Gelo',`${f(s.ice)} g`],['Água',`${f(s.water)} g`]],caption:s=>s.Q<400?'Nos primeiros 40 s, o calor eleva a temperatura do gelo: Q = 80 · 0,5 · ΔT. São necessárias 400 cal para atingir 0 °C.':s.Q<3600?'A partir de 40 s, a temperatura fica em 0 °C. A energia adicional provoca fusão: massa fundida = (Q − 400)/80.':'Após 360 s, a amostra recebeu 3600 cal: 400 aquecem o gelo e 3200 fundem 40 g. Restam 40 g de gelo e 40 g de água, a 0 °C.'}
 };
 function markup(q){const c=configs[q.id];return `<section class="physics-animation" data-animation="${q.id}" aria-label="Animação da questão ${q.id}"><p class="eyebrow">Explore a solução</p><h4>${c.title}</h4><div class="animation-stage"></div><div class="animation-readouts" aria-live="off"></div><p class="animation-caption"></p><div class="animation-controls"><button type="button" data-action="play" aria-pressed="false">Reproduzir</button><button type="button" data-action="prev">Etapa anterior</button><button type="button" data-action="next">Próxima etapa</button><button type="button" data-action="reset">Reiniciar animação</button><label class="animation-speed">Ritmo <select aria-label="Ritmo da animação ${q.id}"><option value=".5">Lento</option><option value="1" selected>Normal</option><option value="2">Rápido</option></select></label><label class="animation-slider" for="animation-range-${q.id}">${c.label}<input id="animation-range-${q.id}" type="range" min="0" max="1" step="any" value="0"></label></div><p class="small animation-note">${c.note}</p></section>`;}
 function init(){
  const players=[];
  document.querySelectorAll('[data-animation]').forEach(el=>{
   const id=Number(el.dataset.animation),c=configs[id],range=el.querySelector('input'),play=el.querySelector('[data-action="play"]');
   let p=0,running=false,frame=0,last=0;
   function render(){
    const s=physicsState(id,p);range.value=p;
    el.querySelector('.animation-stage').innerHTML=c.draw(p);
    el.querySelector('.animation-readouts').innerHTML=c.read(s).map(([label,value])=>`<div><span>${label}</span><strong>${value}</strong></div>`).join('');
    el.querySelector('.animation-caption').textContent=c.caption(s);
    range.setAttribute('aria-valuetext',c.read(s).slice(0,3).map(row=>row.join(': ')).join('; '));
    el.querySelector('[data-action="prev"]').disabled=p<=0;
    el.querySelector('[data-action="next"]').disabled=p>=1;
   }
   function pause(){running=false;cancelAnimationFrame(frame);play.textContent='Reproduzir';play.setAttribute('aria-pressed','false');}
   function seek(value){pause();p=Math.max(0,Math.min(1,value));render();}
   function tick(now){
    if(!running)return;
    p=Math.min(1,p+(now-last)/12000*Number(el.querySelector('select').value));last=now;render();
    if(p>=1){pause();return;}frame=requestAnimationFrame(tick);
   }
   play.addEventListener('click',()=>{
    if(running){pause();return;}players.forEach(player=>player.pause());
    if(p>=1)p=0;running=true;last=performance.now();play.textContent='Pausar';play.setAttribute('aria-pressed','true');render();frame=requestAnimationFrame(tick);
   });
   el.querySelector('[data-action="prev"]').addEventListener('click',()=>seek([...c.marks].reverse().find(v=>v<p-1e-6)??0));
   el.querySelector('[data-action="next"]').addEventListener('click',()=>seek(c.marks.find(v=>v>p+1e-6)??1));
   el.querySelector('[data-action="reset"]').addEventListener('click',()=>seek(0));
   range.addEventListener('input',()=>seek(Number(range.value)));
   players.push({pause,seek,get:()=>p});render();
  });
  const pauseAll=()=>players.forEach(p=>p.pause());
  document.addEventListener('visibilitychange',()=>{if(document.hidden)pauseAll();});
  let printPositions=[];
  window.addEventListener('beforeprint',()=>{printPositions=players.map(p=>p.get());players.forEach(p=>p.seek(1));});
  window.addEventListener('afterprint',()=>players.forEach((p,i)=>p.seek(printPositions[i]??0)));
  return {pauseAll};
 }
 return {diagram,markup,init};
})();
