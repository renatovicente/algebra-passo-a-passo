(() => {
 'use strict';
 const byId=id=>document.getElementById(id);
 const escape=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 const points=n=>n.toFixed(2).replace('.',',');
 const diagram=kind=>`<figure class="diagram">${PhysicsVisuals.diagram(kind)}<figcaption>Figura esquemática · fora de escala.</figcaption></figure>`;
 const sourceLinks=q=>q.sources.map(([href,label])=>`<a href="${escape(href)}">${escape(label)}</a>`).join('');
 const heading=q=>`<div class="card-heading"><div><p class="eyebrow">Questão ${String(q.id).padStart(2,'0')} · ${q.subject}</p><h3>${q.title}</h3></div><span class="points">${points(q.points)} ponto</span></div>`;
 byId('exam-questions').innerHTML=examQuestions.map(q=>`<article class="question-card" id="questao-${q.id}" aria-label="Questão ${q.id}">${heading(q)}<p class="question-prompt math-content">${escape(q.prompt)}</p>${q.figure?diagram(q.figure):''}<ol class="question-parts">${q.parts.map(p=>`<li><span class="part-label">${p.label})</span><div class="math-content">${escape(p.prompt)}<span class="part-points">${points(p.points)} ponto</span></div></li>`).join('')}</ol><div class="timer" id="timer-${q.id}"><div><div class="timer-caption">Tempo da questão ${q.id}</div><div class="time-value" id="time-${q.id}" role="timer" aria-live="off" aria-label="Tempo restante da questão ${q.id}">15:00</div></div><span class="timer-state" id="timer-state-${q.id}" role="status">Aguardando início</span><button type="button" class="start-timer" data-start="${q.id}" aria-label="Iniciar cronômetro da questão ${q.id}">Iniciar</button><button type="button" data-reset="${q.id}" aria-label="Reiniciar cronômetro da questão ${q.id}" title="Voltar a 15 minutos e aguardar novo início" disabled>Reiniciar</button></div><div class="answer-space">Resolução · apresente seu raciocínio.</div></article>`).join('');
 byId('answer-solutions').innerHTML=examQuestions.map(q=>`<article class="solution-card" id="solucao-${q.id}">${heading(q)}${q.parts.map(p=>`<section class="solution-part"><h4>Item ${p.label} · ${points(p.points)} ponto</h4><p class="answer-result math-content">${escape(p.answer)}</p><ol>${p.steps.map(s=>`<li class="math-content">${escape(s)}</li>`).join('')}</ol><p class="rubric"><strong>Critério sugerido:</strong> ${escape(p.rubric)}</p></section>`).join('')}${PhysicsVisuals.markup(q)}<p class="pitfall"><strong>De olho no erro comum.</strong> ${escape(q.pitfall)}</p><div class="sources"><strong>Para revisar:</strong><br>${sourceLinks(q)}</div></article>`).join('');
 byId('calibration-rows').innerHTML=examCalibration.map(row=>`<tr>${row.map(value=>`<td>${escape(value)}</td>`).join('')}</tr>`).join('');
 renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:true,strict:'ignore'});
 const animations=PhysicsVisuals.init();
 const modes=['exam','answers','review'];
 function setMode(mode){
  if(!modes.includes(mode))return;
  animations.pauseAll();
  modes.forEach(m=>{byId(m).hidden=m!==mode;});
  document.querySelectorAll('.mode-switch [data-mode]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mode===mode)));
  document.body.dataset.mode=mode;
 }
 document.querySelectorAll('[data-mode]').forEach(b=>b.addEventListener('click',()=>{
  setMode(b.dataset.mode);
  if(b.classList.contains('next-stage'))byId('exam-heading').scrollIntoView();
 }));
 document.querySelectorAll('[data-print]').forEach(b=>b.addEventListener('click',()=>{setMode(b.dataset.print);window.print();}));
 function revealHash(){
  const hash=location.hash;
  const mode=hash.startsWith('#questao-')?'exam':hash.startsWith('#solucao-')?'answers':hash==='#calibracao'?'review':null;
  const target=byId(hash.slice(1));
  if(mode&&target){setMode(mode);requestAnimationFrame(()=>target.scrollIntoView());}
 }
 document.addEventListener('click',event=>{
  const link=event.target.closest('a[href^="#"]');if(!link)return;
  const id=link.getAttribute('href').slice(1),target=byId(id);if(!target)return;
  const section=target.closest('main > section');if(!section)return;
  setMode(section.id);
  if(location.hash===`#${id}`){event.preventDefault();target.scrollIntoView();}
 });
 window.addEventListener('hashchange',revealHash);
 setMode('exam');revealHash();
  // Absolute deadlines prevent background-tab throttling from extending the limit.
  const duration=15*60*1000;
  const storageKey='reforcco-prova-fisica2-timers-v1';
  let deadlines={};
  function readTimers(){
    try{
      const saved=JSON.parse(localStorage.getItem(storageKey)||'{}');
      if(!saved || typeof saved!=='object' || Array.isArray(saved))return {};
      return Object.fromEntries(examQuestions.filter(q=>Number.isFinite(saved[q.id])&&saved[q.id]>0).map(q=>[q.id,saved[q.id]]));
    }catch{byId('timer-storage-note').hidden=false;return {};}
  }
  deadlines=readTimers();
  function saveTimers(){
    try{localStorage.setItem(storageKey,JSON.stringify(deadlines));}
    catch{byId('timer-storage-note').hidden=false;}
  }
  function updateTimers(){
    const now=Date.now();
    for(const q of examQuestions){
      const started=Boolean(deadlines[q.id]);
      const seconds=started?Math.max(0,Math.ceil((deadlines[q.id]-now)/1000)):duration/1000;
      const expired=started&&seconds===0;
      const label=`${String(Math.floor(seconds/60)).padStart(2,'0')}:${String(seconds%60).padStart(2,'0')}`;
      if(byId(`time-${q.id}`).textContent!==label)byId(`time-${q.id}`).textContent=label;
      const state=expired?'Tempo esgotado':started?'Em andamento · limite de 15 min':'Aguardando início';
      const status=byId(`timer-state-${q.id}`);
      if(status.textContent!==state)status.textContent=state;
      const timer=byId(`timer-${q.id}`);
      timer.classList.toggle('expired',expired);
      timer.classList.toggle('warning',started&&seconds<=60&&!expired);
      const start=timer.querySelector('[data-start]');
      start.disabled=started;
      start.textContent=expired?'Encerrado':started?'Iniciado':'Iniciar';
      timer.querySelector('[data-reset]').disabled=!started;
    }
  }
  document.querySelectorAll('[data-start]').forEach(button=>button.addEventListener('click',()=>{
    if(deadlines[button.dataset.start])return;
    deadlines[button.dataset.start]=Date.now()+duration;
    saveTimers();updateTimers();
  }));
  document.querySelectorAll('[data-reset]').forEach(button=>button.addEventListener('click',()=>{
    delete deadlines[button.dataset.reset];saveTimers();updateTimers();
    byId(`timer-${button.dataset.reset}`).querySelector('[data-start]').focus();
  }));
  document.addEventListener('visibilitychange',updateTimers);
  window.addEventListener('pageshow',updateTimers);
  window.addEventListener('storage',event=>{if(event.key===storageKey||event.key===null){deadlines=readTimers();updateTimers();}});
  updateTimers();setInterval(updateTimers,250);
})();
