(() => {
  'use strict';
  const byId = id => document.getElementById(id);
  const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const points = n => n.toFixed(2).replace('.', ',');
  const polygon = (n, cx, cy, radius, angle = -90) => Array.from({length:n}, (_,i) => {
    const a=(angle+i*360/n)*Math.PI/180;
    return `${cx+radius*Math.cos(a)},${cy+radius*Math.sin(a)}`;
  }).join(' ');
  const sourceLinks = q => q.sources.map(([href,label])=>`<a href="${escape(href)}">${escape(label)}</a>`).join('');
  function diagram(kind) {
    let content, label, viewBox;
    if (kind === 'triangle-square') {
      label='À esquerda, triângulo equilátero circunscrito à circunferência de raio r. À direita, quadrado inscrito na mesma circunferência, representada separadamente.';
      viewBox='0 0 600 280';
      content=`<polygon class="shape" points="${polygon(3,150,130,110,-90)}"/><circle class="circle" cx="150" cy="130" r="55"/><path class="aux" d="M150 130 V185"/><path d="M150 177 H158 V185" stroke="#8b4527" fill="none"/><text x="135" y="130">O</text><text x="160" y="161">r</text><text x="150" y="258" text-anchor="middle">Triângulo circunscrito</text><circle class="circle" cx="450" cy="130" r="55"/><polygon class="shape" points="${polygon(4,450,130,55,-45)}"/><path class="aux" d="M450 130 L488.891 91.109"/><text x="435" y="143">O</text><text x="470" y="119">r</text><text x="450" y="258" text-anchor="middle">Quadrado inscrito</text>`;
    } else if (kind === 'dodecagon') {
      label='Hexágono ACDEFG inscrito. A e C são vértices consecutivos, B é o ponto médio do arco menor AC e M é o ponto médio de AC. O, M e B estão alinhados, nessa ordem. O raio OA mede 8 cm.';
      viewBox='0 0 350 300';
      content=`<circle class="circle" cx="160" cy="145" r="110"/><polygon points="${polygon(12,160,145,110,0)}" fill="none" stroke="#9da991" stroke-dasharray="4 4"/><polygon class="shape" points="${polygon(6,160,145,110,-30)}"/><path class="aux" d="M160 145 L255.263 90 M160 145 H270"/><path d="M255.263 90 L270 145 L255.263 200" stroke="#8b4527" stroke-width="2.5" fill="none"/><path d="M248.263 145 V138 H255.263" stroke="#8b4527" fill="none"/><circle cx="160" cy="145" r="2.5" fill="#243f35"/><text x="145" y="163">O</text><text x="262" y="82">A</text><text x="279" y="150">B</text><text x="262" y="218">C</text><text x="154" y="277">D</text><text x="45" y="211">E</text><text x="45" y="86">F</text><text x="154" y="26">G</text><text x="236" y="168">M</text><text x="185" y="107">8 cm</text>`;
    } else {
      label='Hexágono regular ABCDEF entre uma circunferência externa de raio 10 cm e uma circunferência interna tangente aos lados. O é o centro comum, M é o ponto médio de AB, e OM é perpendicular a AB.';
      viewBox='0 0 350 290';
      content=`<circle class="circle" cx="175" cy="140" r="110"/><polygon class="shape" points="${polygon(6,175,140,110,-30)}"/><circle class="circle" cx="175" cy="140" r="95.26279"/><path class="aux" d="M175 140 L270.263 85 M175 140 H270.263"/><path d="M262.263 140 V132 H270.263" stroke="#8b4527" fill="none"/><circle cx="175" cy="140" r="2.5" fill="#243f35"/><text x="160" y="157">O</text><text x="277" y="78">A</text><text x="277" y="210">B</text><text x="170" y="273">C</text><text x="61" y="209">D</text><text x="61" y="82">E</text><text x="169" y="22">F</text><text x="246" y="163">M</text><text x="203" y="96">10 cm</text><text x="221" y="158">a</text>`;
    }
    return `<figure class="diagram"><svg viewBox="${viewBox}" role="img" aria-label="${escape(label)}">${content}</svg><figcaption>Figura esquemática · fora de escala · medidas em centímetros.</figcaption></figure>`;
  }
  const heading = q => `<div class="card-heading"><div><p class="eyebrow">Questão ${String(q.id).padStart(2,'0')} · ${q.subject}</p><h3>${q.title}</h3></div><span class="points">${points(q.points)} ponto${q.points===1?'':'s'}</span></div>`;
  byId('exam-questions').innerHTML = examQuestions.map(q => `<article class="question-card" id="questao-${q.id}" aria-label="Questão ${q.id}">${heading(q)}<p class="question-prompt math-content">${escape(q.prompt)}</p>${q.figure?diagram(q.figure):''}<ol class="question-parts">${q.parts.map(p=>`<li><span class="part-label">${p.label})</span><div class="math-content">${escape(p.prompt)}<span class="part-points">${points(p.points)} ponto</span></div></li>`).join('')}</ol><div class="timer" id="timer-${q.id}"><div><div class="timer-caption">Tempo da questão ${q.id}</div><div class="time-value" id="time-${q.id}" role="timer" aria-live="off" aria-label="Tempo restante da questão ${q.id}">15:00</div></div><span class="timer-state" id="timer-state-${q.id}" role="status">Aguardando início</span><button type="button" class="start-timer" data-start="${q.id}" aria-label="Iniciar cronômetro da questão ${q.id}">Iniciar</button><button type="button" data-reset="${q.id}" aria-label="Reiniciar cronômetro da questão ${q.id}" title="Voltar a 15 minutos e aguardar novo início" disabled>Reiniciar</button></div><div class="answer-space">Resolução · apresente seu raciocínio.</div></article>`).join('');
  byId('answer-key').innerHTML=examQuestions.map(q=>`<div class="key-card"><h3>Questão ${q.id}</h3>${q.parts.map(p=>`<p class="math-content"><strong>${p.label})</strong> ${escape(p.answer)}</p>`).join('')}</div>`).join('');
  byId('answer-solutions').innerHTML=examQuestions.map(q=>`<article class="solution-card" id="solucao-${q.id}">${heading(q)}${q.parts.map(p=>`<section class="solution-part"><h4>Item ${p.label} · ${points(p.points)} ponto</h4><p class="answer-result math-content">${escape(p.answer)}</p><ol>${p.steps.map(s=>`<li class="math-content">${escape(s)}</li>`).join('')}</ol><p class="rubric"><strong>Critério sugerido:</strong> ${escape(p.rubric)}</p></section>`).join('')}<p class="pitfall"><strong>De olho no erro comum.</strong> ${escape(q.pitfall)}</p><div class="sources"><strong>Para revisar nos cadernos:</strong><br>${sourceLinks(q)}</div></article>`).join('');
  byId('calibration-rows').innerHTML=examCalibration.map(row=>`<tr>${row.map(value=>`<td>${escape(value)}</td>`).join('')}</tr>`).join('');
  renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:true,strict:'ignore'});

  function setMode(mode) {
    const answers=mode==='answers';
    byId('exam').hidden=answers;
    byId('answers').hidden=!answers;
    byId('show-exam').setAttribute('aria-pressed',String(!answers));
    byId('show-answers').setAttribute('aria-pressed',String(answers));
    document.body.classList.toggle('print-answers',answers);
  }
  byId('show-exam').addEventListener('click',()=>setMode('exam'));
  byId('show-answers').addEventListener('click',()=>setMode('answers'));
  byId('print-exam').addEventListener('click',()=>{setMode('exam');window.print();});
  byId('print-answers').addEventListener('click',()=>{setMode('answers');window.print();});

  // Absolute deadlines prevent background-tab throttling from extending the limit.
  const duration=15*60*1000;
  const storageKey='reforcco-prova2-poligonos-exponenciais-timers-v1';
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
