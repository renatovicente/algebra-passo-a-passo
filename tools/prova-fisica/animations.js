'use strict';
// Pure physical states shared by the drawing, readouts and step controls.
function physicsState(id, p) {
  p=Math.min(1,Math.max(0,p));
  if(id===1){const t=2*p;return {t,a:4,x:2*t*t,v:4*t,T:12,N:5};}
  if(id===2){const t=3*p;return {t,x:24*t,y:45-5*t*t,vx:24,vy:-10*t};}
  if(id===3){const t=6*p;return {t,x:8*t,y:98-2*t*t,vy:-4*t,ay:-4};}
  if(id===4)return {fraction:p,object:20+25*p,water:70-25*p,Q:15000*p};
  const t=600*p,Q=5*t,melt=Math.max(0,(Q-1000)/80);
  return {t,Q,QJ:4*Q,temp:Math.min(0,-20+Q/50),water:melt,ice:100-melt};
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
 function blocks(p,solution){
  const s=physicsState(1,p),b=70+s.x*22,a=b+160;
  let c=line(25,230,655,230)+rect(b,174,75,56)+rect(a,174,75,56)+line(b+75,202,a,202)+text(b+37,208,'B · 3 kg','text-anchor="middle"')+text(a+37,208,'A · 2 kg','text-anchor="middle"')+arrow(a+75,174,a+(solution?135:175),solution?129:99)+text(a+100,solution?108:83,'F = 25 N')+line(a+75,174,a+185,174,'#657168',true)+text(a+109,167,'θ')+text(30,265,'Mesa sem atrito · fio ideal');
  if(solution)c+=arrow(b+75,195,b+111,195,'#347b8e')+text(b+85,181,'T')+arrow(a,217,a-36,217,'#347b8e')+text(a-27,243,'T')+arrow(a+35,174,a+35,159)+text(a-5,132,'N = 5 N')+arrow(a+35,216,a+35,276)+text(a+46,282,'P = 20 N')+text(30,310,'A: N + 15 − 20 = 0. A força oblíqua alivia a normal.');
  return wrap(c,solution?'Dois blocos aceleram juntos para a direita. A tração aponta para a direita em B e para a esquerda em A. A normal de A é 5 N.':'B à esquerda e A à direita ligados por fio horizontal; uma força de 25 N puxa A para cima e para a direita.',solution?340:290);
 }
 function launch(p,solution){
  const s=physicsState(2,p),sx=x=>100+x*6,sy=y=>270-y*4.2;
  let c=rect(30,sy(45),70,270-sy(45))+line(25,270,650,270)+text(32,185,'45 m')+text(550,298,'x (m)')+text(34,40,'y (m)')+text(79,295,'0');
  if(solution){
   const path=Array.from({length:61},(_,i)=>{const t=3*i/60;return `${i?'L':'M'}${sx(24*t)},${sy(45-5*t*t)}`;}).join(' ');
   c+=`<path d="${path}" fill="none" stroke="#9aa68d" stroke-width="2" stroke-dasharray="5 5"/>`+line(100,sy(s.y),sx(s.x),sy(s.y),'#657168',true)+circle(100,sy(s.y),5,'#347b8e')+circle(sx(s.x),sy(s.y))+arrow(sx(s.x),sy(s.y),sx(s.x)+s.vx*1.7,sy(s.y),'#347b8e')+arrow(sx(s.x),sy(s.y),sx(s.x),sy(s.y)-s.vy*1.7)+text(sx(s.x)+13,sy(s.y)-12,'vₓ')+text(sx(s.x)+10,sy(s.y)-s.vy*1.7+18,'vᵧ')+text(285,34,'Mesma queda, mesmo tempo')+text(495,295,'72');
  }else c+=circle(100,sy(45))+arrow(100,sy(45),210,sy(45),'#347b8e')+text(110,sy(45)-18,'24 m/s')+arrow(610,100,610,155)+text(532,90,'g = 10 m/s²');
  return wrap(c,solution?'Trajetória parabólica com componentes horizontal e vertical da velocidade. Um ponto azul cai verticalmente da plataforma e permanece na mesma altura da esfera.':'Esfera sai horizontalmente a 24 m/s de uma plataforma de 45 m.',350);
 }
 function velocityGraph(p,end=6,magnitude=24,solution=false){
  const t=end*p,v=-magnitude*p,gx=t=>85+t/end*490,gy=v=>65-v/magnitude*180;
  let c=arrow(85,65,625,65,'#657168')+arrow(85,30,85,265,'#657168')+text(25,28,'vᵧ (m/s)')+text(610,48,'t (s)')+text(65,58,'0')+text(570,50,String(end))+text(28,gy(-magnitude)+6,String(-magnitude))+line(85,gy(-magnitude),575,gy(-magnitude),'#9aa68d',true)+line(575,65,575,gy(-magnitude),'#9aa68d',true)+line(85,65,575,245,'#8b4527');
  if(solution)c+=`<polygon points="85,65 ${gx(t)},65 ${gx(t)},${gy(v)}" fill="#dfb79c" opacity=".35"/>`+circle(gx(t),gy(v))+line(gx(t),65,gx(t),gy(v),'#347b8e',true)+text(130,298,`Inclinação: Δvᵧ/Δt = −${f(magnitude/end)} m/s² · área = ${f(-magnitude*p*t/2)} m`);
  return wrap(c,`Gráfico de velocidade vertical por tempo: reta de zero a menos ${magnitude} m/s em ${end} segundos. A área com sinal representa o deslocamento vertical.`,330);
 }
 function planet(p){
  const s=physicsState(3,p),x=100+s.x*8,y=265-s.y*2;
  return wrap(line(45,265,620,265)+text(30,295,'Solo: y = 0')+text(30,38,'Posição da partícula')+line(100,69,100,265,'#9aa68d',true)+text(23,75,'98 m')+circle(x,y)+arrow(x,y,x,y-s.vy*2)+text(x+15,y-13,`y = ${f(s.y)} m`)+text(345,295,'Cima positivo · g = 4 m/s²'),320);
 }
 function equilibrium(p){
  const s=physicsState(4,p),base=245,scale=2.2;
  let c=text(175,30,'Objeto · C = 600 J/°C','text-anchor="middle"')+text(505,30,'Água · C = 600 J/°C','text-anchor="middle"');
  for(const [x,T,color,name] of [[175,s.object,'#347b8e','Objeto'],[505,s.water,'#b66b44','Água']]){
   c+=rect(x-55,65,110,180,'#f7f7ef')+rect(x-53,base-T*scale,106,T*scale,color)+text(x,275,`${f(T)} °C`,'text-anchor="middle"')+text(x,300,name,'text-anchor="middle"');
  }
  c+=line(95,base-45*scale,585,base-45*scale,'#657168',true)+text(286,base-45*scale-12,'45 °C');
  if(p<1)c+=arrow(425,200,255,200)+text(340,226,'calor','text-anchor="middle"');
  else c+=text(340,205,'Equilíbrio','text-anchor="middle"');
  return wrap(c,'Duas colunas representam as temperaturas do objeto e da água. O calor flui da água mais quente para o objeto, até ambos chegarem a 45 graus Celsius.',320);
 }
 function phase(p){
  const s=physicsState(5,p),gx=q=>85+q/3000*500,gy=t=>80-t*7;
  let c=arrow(85,260,635,260,'#657168')+arrow(85,260,85,35,'#657168')+text(20,28,'T (°C)')+text(570,294,'Q (cal)')+text(55,85,'0')+text(25,225,'−20')+text(71,283,'0')+text(gx(1000),283,'1000','text-anchor="middle"')+text(gx(3000),283,'3000','text-anchor="middle"')+line(85,80,585,80,'#9aa68d',true)+line(gx(1000),80,gx(1000),260,'#9aa68d',true)+`<path d="M85 220 L${gx(1000)} 80 H585" stroke="#8b4527" stroke-width="3" fill="none"/>`+circle(gx(s.Q),gy(s.temp))+text(115,180,'gelo aquece')+text(380,65,'fusão a 0 °C')+text(100,325,'Massas · total de 100 g');
  c+=rect(85,340,500*(s.ice/100),35,'#d8e7e7');
  if(s.water>0)c+=rect(85+500*s.ice/100,340,500*s.water/100,35,'#347b8e');
  c+=text(85,405,`Gelo: ${f(s.ice)} g`)+text(410,405,`Água: ${f(s.water)} g`);
  return wrap(c,'Curva de aquecimento: a temperatura sobe de menos 20 a zero grau com 1000 calorias e permanece em zero durante a fusão. A barra inferior representa as massas de gelo e água.',430);
 }
 function diagram(kind){
  if(kind==='blocks')return blocks(0,false);
  if(kind==='launch')return launch(0,false);
  if(kind==='exam-graph')return velocityGraph(1,6,24);
  if(kind==='warm-graph')return velocityGraph(1,3,12);
  if(kind==='components')return wrap(arrow(180,230,420,50)+arrow(180,230,420,230,'#347b8e')+arrow(420,230,420,50,'#347b8e')+text(270,120,'F = 25 N')+text(275,260,'Fₓ')+text(437,143,'Fᵧ')+text(230,217,'θ'),'Decomposição de uma força para a direita e para cima em componentes horizontal e vertical.',290);
  if(kind==='pulley')return wrap(line(60,150,420,150)+line(420,150,420,300)+rect(130,90,110,60)+line(240,110,435,110)+`<circle cx="435" cy="130" r="20" stroke="#243f35" fill="none" stroke-width="2"/>`+line(455,130,455,220)+rect(425,220,65,65)+text(144,125,'A · 3 kg')+text(432,250,'B')+text(432,274,'2 kg')+text(65,190,'Mesa sem atrito'),'Bloco A numa mesa ligado por fio que passa por uma polia fixa ao bloco B suspenso.',330);
  return wrap(rect(210,70,250,130,'#d8e7e7')+text(335,122,'100 g de gelo','text-anchor="middle"')+text(335,158,'−20 °C','text-anchor="middle"')+rect(235,235,200,40,'#f0d2bd')+text(335,262,'Fonte de 20 W','text-anchor="middle"')+arrow(290,230,290,205)+arrow(380,230,380,205),'Amostra de 100 gramas de gelo a menos 20 graus recebe energia de uma fonte de 20 watts.',300);
 }
 const configs={
  1:{title:'Dois blocos, uma aceleração',label:'Tempo do movimento (0 a 2 s)',marks:[0,.25,.5,.75,1],note:'Para visualizar, os blocos partem do repouso. O desenho usa escalas próprias para posições e vetores. As forças são constantes. Em B, peso e normal se equilibram e foram omitidos do desenho.',draw:p=>blocks(p,true),read:s=>[['Tempo',`${f(s.t)} s`],['Deslocamento',`${f(s.x)} m`],['Velocidade',`${f(s.v)} m/s`],['Aceleração',`${f(s.a)} m/s² →`],['Tração',`${s.T} N`],['Normal de A',`${s.N} N`]],caption:s=>`A tração acelera B para a direita e puxa A para a esquerda. No conjunto, as forças internas se cancelam: 20 = (2 + 3) · 4. Em A, 20 − 12 = 2 · 4.`},
  2:{title:'Horizontal uniforme, vertical acelerada',label:'Tempo de queda (0 a 3 s)',marks:[0,1/3,2/3,1],note:'O ponto azul cai verticalmente do mesmo nível, a partir do repouso. Ele permanece na mesma altura da esfera. Vetores em escala própria; reprodução em câmera lenta.',draw:p=>launch(p,true),read:s=>[['Tempo',`${f(s.t)} s`],['x',`${f(s.x)} m`],['Altura y',`${f(s.y)} m`],['vₓ',`${s.vx} m/s`],['vᵧ',`${f(s.vy)} m/s`]],caption:s=>s.t<3?'A gravidade altera apenas a componente vertical. A altura obedece a y = 45 − 5t² e a posição horizontal a x = 24t.':'A esfera chega ao solo em 3 s, a 72 m da plataforma. Os vetores representam a velocidade imediatamente antes do impacto; a colisão não é simulada.'},
  3:{title:'O gráfico revela a gravidade',label:'Tempo no gráfico (0 a 6 s)',marks:[0,.5,2/3,1],note:'A região sombreada representa o deslocamento vertical com sinal. A animação termina em 6 s, ainda antes de chegar ao solo.',draw:p=>`<div class="visual-pair">${velocityGraph(p,6,24,true)}${planet(p)}</div>`,read:s=>[['Tempo',`${f(s.t)} s`],['aᵧ',`${s.ay} m/s²`],['vᵧ',`${f(s.vy)} m/s`],['Altura y',`${f(s.y)} m`],['Deslocamento Δy',`${f(s.y-98)} m`]],caption:s=>`O solo é y = 0. A altura inicial de 98 m deve ser somada ao deslocamento: y = 98 − 2t². A inclinação da reta é −4 m/s² em todos os instantes.`},
  4:{title:'O calor perdido é igual ao recebido',label:'Fração da energia trocada (0 a 100%)',marks:[0,.5,1],note:'O controle representa a fração de energia trocada, não o tempo físico. As colunas representam temperaturas uniformes dos corpos, não níveis de líquido.',draw:equilibrium,read:s=>[['Energia trocada',`${f(s.fraction*100)}%`],['Objeto',`${f(s.object)} °C`],['Água',`${f(s.water)} °C`],['Q do objeto',`+${f(s.Q,0)} J`],['Q da água',`${s.Q?'−':''}${f(s.Q,0)} J`]],caption:s=>s.fraction<1?'As capacidades térmicas são iguais: 600 J/°C. A cada joule transferido, as duas temperaturas variam pelo mesmo módulo, em sentidos opostos.':'Ambos chegam a 45 °C: ΔT do objeto = +25 °C; ΔT da água = −25 °C. A soma dos calores é zero. Não há mais transferência líquida de calor.'},
  5:{title:'Primeiro aquece. Depois derrete.',label:'Tempo de aquecimento (0 a 600 s)',marks:[0,1/3,1],note:'A reprodução comprime 10 minutos de aquecimento. A barra de fases mostra proporções de massa, não volumes. Adota-se equilíbrio térmico na amostra.',draw:phase,read:s=>[['Tempo',`${f(s.t,0)} s`],['Calor',`${f(s.Q,0)} cal`],['Energia',`${f(s.QJ,0)} J`],['Temperatura',`${f(s.temp)} °C`],['Gelo',`${f(s.ice)} g`],['Água',`${f(s.water)} g`]],caption:s=>s.Q<1000?'Até 200 s, toda a energia aumenta a temperatura do gelo: Q = 100 · 0,5 · ΔT. Ainda não há água líquida.':s.Q<3000?'A partir de 200 s, a temperatura permanece em 0 °C. O calor adicional muda a fase: massa fundida = (Q − 1000)/80.':'Após 600 s, foram recebidas 3000 cal: 1000 aquecem o gelo e 2000 fundem 25 g. Restam 75 g de gelo com 25 g de água, a 0 °C.'}
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
