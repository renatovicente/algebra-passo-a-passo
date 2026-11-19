(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const data=JSON.parse(document.getElementById('exercise-data').textContent);
  const F=InclineVisuals.fmt, model=InclinePhysics;
  const labs=[], cards=[...document.querySelectorAll('.card')];
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  function math(el){
    try{renderMathInElement(el,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:true,strict:'ignore',trust:false,errorCallback:()=>{document.getElementById('math-error').hidden=false;}});}
    catch{document.getElementById('math-error').hidden=false;}
  }
  for(const q of data){
    const card=document.getElementById('q'+q.id), el=card.querySelector('.lab');
    const get=s=>el.querySelector(s), all=s=>[...el.querySelectorAll(s)];
    let params={...q.lab.base}, progress=0, playing=false, last=0, frame=0;
    const forceOnly=q.lab.kind==='forces', scrub=get('.scrub'), play=get('[data-action=play]');
    const snapshot=()=>model.state(q,params,progress);
    function stop(message){playing=false;cancelAnimationFrame(frame);play.textContent='Reproduzir';play.setAttribute('aria-pressed','false');if(message)get('.player-status').textContent=message;}
    function metrics(z){
      let values=[];
      if(forceOnly){values=[['Peso',F(z.weight)+' N'],['Normal',F(z.normal)+' N'],['Peso paralelo',F(z.parallel)+' N'],['Aceleração',F(z.a)+' m/s²']];}
      else{values=[['Tempo',F(z.t)+' s'],['Deslocamento',F(z.s)+' m'],['Velocidade',F(z.v)+' m/s'],['Aceleração',F(z.a)+' m/s²']];if(z.tension!=null)values.push(['Tração',F(z.tension)+' N']);}
      get('.readouts').innerHTML=values.map(([name,v])=>`<div><dt>${name}</dt><dd>${v}</dd></div>`).join('');
    }
    function render(){
      const z=snapshot();
      scrub.value=progress*100;
      get('.scrub-value').textContent=forceOnly?`Etapa ${z.stage+1} de 4`:`${F(z.t)} de ${F(z.duration)} s`;
      scrub.setAttribute('aria-valuetext',get('.scrub-value').textContent);
      if(!forceOnly){get('.motion').innerHTML=InclineVisuals.motion(z);get('.velocity-graph').innerHTML=InclineVisuals.graph(z);}
      get('.force-diagram').innerHTML=InclineVisuals.forces(z,get('.components').checked,forceOnly);
      metrics(z);
      get('.stage-caption').textContent=forceOnly?q.lab.stages[z.stage]:z.kind==='up'&&progress===1?'Primeira parada: v = 0, mas a aceleração continua para baixo.':z.kind==='down'&&progress===1?'Chegada ao fim da rampa. A velocidade mostrada é a de chegada.':z.kind==='hangingPulley'?(z.a===0?'Equilíbrio: partindo do repouso, os dois blocos permanecem parados.':z.a>0?'M desce a rampa e m sobe. Os deslocamentos têm o mesmo módulo.':'M sobe a rampa e m desce. Os valores negativos indicam inversão dos sentidos positivos escolhidos.'):'Use o controle de tempo para comparar posição, velocidade e aceleração.';
      if(z.kind==='up'){
        get('.energy-k').style.width=100*z.kinetic/z.energy+'%';get('.energy-u').style.width=100*z.potential/z.energy+'%';
        get('.energy-values').textContent=`K/m = ${F(z.kinetic)} J/kg · U/m = ${F(z.potential)} J/kg · soma = ${F(z.energy)} J/kg`;
      }
      el.dataset.progress=progress; el.dataset.acceleration=z.a; el.dataset.displacement=z.s;
    }
    const latex=x=>F(x,3).replace(',','{,}');
    function equations(){
      const z=snapshot(),n=latex;let eq=[];
      if(q.id===1)eq=[`a=g\\operatorname{sen}\\theta=${n(z.a)}\\,\\mathrm{m/s^2}`,`N=mg\\cos\\theta=${n(z.normal)}\\,\\mathrm N`];
      if(q.id===2||q.id===5)eq=[`a=g\\operatorname{sen}\\theta=${n(z.a)}\\,\\mathrm{m/s^2}`,`t_f=\\sqrt{\\frac{2L}{a}}=${n(z.duration)}\\,\\mathrm s`];
      if(q.id===3||q.id===6)eq=[`t_f=\\frac{v_0}{g\\operatorname{sen}\\theta}=${n(z.duration)}\\,\\mathrm s`,`s_f=\\frac{v_0^2}{2g\\operatorname{sen}\\theta}=${n(z.distance)}\\,\\mathrm m`];
      if(q.id===4)eq=[`F_R=F-mg\\operatorname{sen}\\theta=${n(z.resultant)}\\,\\mathrm N`,`a=\\frac{F_R}{m}=${n(z.a)}\\,\\mathrm{m/s^2}`];
      if(q.id===7)eq=[`a=\\frac{m_Bg\\operatorname{sen}\\theta}{m_A+m_B}=${n(z.a)}\\,\\mathrm{m/s^2}`,`T=m_Aa=${n(z.tension)}\\,\\mathrm N`];
      if(q.id===8)eq=[`a=\\frac{g(r\\operatorname{sen}\\theta-1)}{r+1}=${n(z.a)}\\,\\mathrm{m/s^2}`,`r=M/m=${n(params.ratio)},\\quad T=m(g+a)=${n(z.tension)}\\,\\mathrm N`];
      get('.live-equations').innerHTML=eq.map(v=>`<div>$$${v}$$</div>`).join('');math(get('.live-equations'));
      const changed=Object.keys(q.lab.base).some(key=>params[key]!==q.lab.base[key]);
      get('.model-label').textContent=changed?'Exploração · valores alterados':q.lab.example?'Exemplo numérico · resposta original é simbólica':'Dados da lista'+(q.id>=7?' · partida ilustrativa do repouso':'');
      get('.model-label').classList.toggle('modified',changed);
    }
    function syncControls(){
      if(q.id===5){params=model.state(q,params,0).p;get('[data-param=height]').max=Math.min(9.5,params.length-.5);}
      for(const input of all('[data-param]')){
        input.value=params[input.dataset.param];document.getElementById(input.id+'-value').textContent=F(params[input.dataset.param])+ (input.dataset.unit?' '+input.dataset.unit:'');
      }
    }
    for(const input of all('[data-param]'))input.addEventListener('input',()=>{stop('Parâmetros alterados; visualização reiniciada.');params[input.dataset.param]=+input.value;progress=0;syncControls();equations();render();});
    get('.components').addEventListener('change',render);
    scrub.addEventListener('input',()=>{stop('Visualização pausada no ponto escolhido.');progress=+scrub.value/100;render();});
    function tick(now){
      if(!playing)return;
      if(last)progress=Math.min(1,progress+(now-last)/8000);last=now;
      render();if(progress>=1){stop('Fim da visualização. Use Voltar ao início ou Reproduzir para recomeçar.');return;}
      frame=requestAnimationFrame(tick);
    }
    function advance(dir){stop('Avanço por pontos de referência.');const checkpoints=forceOnly?[0,.34,.67,1]:[0,.25,.5,.75,1];progress=dir>0?(checkpoints.find(x=>x>progress+.001)??1):([...checkpoints].reverse().find(x=>x<progress-.001)??0);render();}
    for(const button of all('[data-action]'))button.addEventListener('click',()=>{
      const action=button.dataset.action;
      if(action==='play'){
        if(playing){stop('Pausado.');return;}
        if(reduced.matches){if(progress>=1)progress=0;else advance(1);render();get('.player-status').textContent='Movimento reduzido: avanço por pontos de referência.';return;}
        labs.forEach(l=>l.stop());if(progress>=1)progress=0;
        playing=true;last=0;play.textContent='Pausar';play.setAttribute('aria-pressed','true');get('.player-status').textContent='Reproduzindo em ritmo didático (8 s na tela).';frame=requestAnimationFrame(tick);
      }else if(action==='next')advance(1);
      else if(action==='prev')advance(-1);
      else if(action==='start'){stop('De volta ao início.');progress=0;render();}
      else if(action==='restore'){stop('Valores iniciais restaurados.');params={...q.lab.base};progress=0;syncControls();equations();render();}
    });
    card.querySelector('.solution-toggle').addEventListener('toggle',event=>{if(!event.target.open)stop();});
    const lab={stop,card,save:()=>({params:{...params},progress,components:get('.components').checked}),load:s=>{stop();params={...s.params};progress=s.progress;get('.components').checked=s.components;syncControls();equations();render();},original:()=>({params:{...q.lab.base},progress:1,components:true})};
    labs.push(lab);syncControls();equations();render();
  }
  document.addEventListener('visibilitychange',()=>{if(document.hidden)labs.forEach(l=>l.stop());});
  reduced.addEventListener('change',()=>labs.forEach(l=>l.stop()));
  const storageKey='plano-inclinado-v1', ids=new Set(cards.map(c=>c.id));let done=new Set();
  try{const saved=JSON.parse(localStorage.getItem(storageKey)||'[]');if(Array.isArray(saved))done=new Set(saved.filter(id=>ids.has(id)));}catch{document.getElementById('storage-note').hidden=false;}
  const topic=document.getElementById('topic'),pending=document.getElementById('pending');
  function update(){let count=0;for(const card of cards){card.hidden=(topic.value!=='all'&&card.dataset.topic!==topic.value)||(pending.checked&&done.has(card.id));card.classList.toggle('done',done.has(card.id));card.querySelector('.done-check').checked=done.has(card.id);if(!card.hidden)count++;else labs.find(l=>l.card===card).stop();}document.getElementById('shown').textContent=`${count} de 8 exercícios exibidos`;document.getElementById('progresslabel').textContent=`${done.size} de 8 concluídos`;document.getElementById('progress').value=done.size;document.getElementById('empty').hidden=count!==0;}
  function clear(){topic.value='all';pending.checked=false;update();}
  topic.addEventListener('change',update);pending.addEventListener('change',update);document.getElementById('clear-filters').addEventListener('click',clear);
  for(const card of cards)card.querySelector('.done-check').addEventListener('change',e=>{if(e.target.checked)done.add(card.id);else done.delete(card.id);try{localStorage.setItem(storageKey,JSON.stringify([...done]));}catch{document.getElementById('storage-note').hidden=false;}update();});
  function jump(id,open=false){if(!ids.has(id)&&id!=='questoes')return;clear();if(open&&ids.has(id))document.getElementById(id).querySelector('.solution-toggle').open=true;}
  document.querySelectorAll('[data-jump]').forEach(a=>a.addEventListener('click',()=>jump(a.hash.slice(1),a.hasAttribute('data-solution'))));
  window.addEventListener('hashchange',()=>jump(location.hash.slice(1)));
  let printState=null;
  function beforePrint(){if(printState)return;printState=labs.map(l=>({lab:l,state:l.save(),open:l.card.querySelector('.solution-toggle').open}));for(const l of labs){l.load(l.original());l.card.querySelector('.solution-toggle').open=true;}}
  function afterPrint(){if(!printState)return;for(const s of printState){s.lab.load(s.state);s.lab.card.querySelector('.solution-toggle').open=s.open;}printState=null;document.body.classList.remove('printanswers');}
  window.addEventListener('beforeprint',beforePrint);window.addEventListener('afterprint',afterPrint);
  document.querySelectorAll('[data-print]').forEach(b=>b.addEventListener('click',()=>{document.body.classList.toggle('printanswers',b.dataset.print==='answers');beforePrint();try{window.print();}finally{afterPrint();}}));
  math(document.querySelector('main'));update();if(location.hash){jump(location.hash.slice(1));document.getElementById(location.hash.slice(1))?.scrollIntoView();}
})();
