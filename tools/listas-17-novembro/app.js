(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const cards = [...document.querySelectorAll('.card')];
  const ids = new Set(cards.map(card => card.id));
  const storageKey = document.body.dataset.progressKey;
  const pending = document.getElementById('pending');
  const topic = document.getElementById('topic');
  let done = new Set();
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || '[]');
    if (Array.isArray(saved)) done = new Set(saved.filter(id => ids.has(id)));
  } catch { document.getElementById('storage-note').hidden = false; }

  function update() {
    let visible = 0;
    for (const card of cards) {
      card.hidden = (topic.value !== 'all' && card.dataset.topic !== topic.value)
        || (pending.checked && done.has(card.id));
      card.classList.toggle('done', done.has(card.id));
      card.querySelector('input[type=checkbox]').checked = done.has(card.id);
      if (!card.hidden) visible++;
    }
    document.getElementById('shown').textContent = `${visible} de ${cards.length} exercícios exibidos`;
    document.getElementById('progresslabel').textContent = `${done.size} de ${cards.length} concluídos`;
    document.getElementById('progress').value = done.size;
    document.getElementById('empty').hidden = visible !== 0;
  }
  function clearFilters() { topic.value = 'all'; pending.checked = false; update(); }
  pending.addEventListener('change', update);
  topic.addEventListener('change', update);
  document.getElementById('clear-filters').addEventListener('click', clearFilters);
  for (const card of cards) {
    card.querySelector('input[type=checkbox]').addEventListener('change', event => {
      if (event.target.checked) done.add(card.id); else done.delete(card.id);
      try { localStorage.setItem(storageKey, JSON.stringify([...done])); }
      catch { document.getElementById('storage-note').hidden = false; }
      update();
    });
  }
  function revealTarget(id, openSolution = false) {
    if (!ids.has(id) && id !== 'questoes') return;
    clearFilters();
    if (openSolution && ids.has(id)) document.getElementById(id).querySelector('.solution-toggle').open = true;
  }
  document.querySelectorAll('a[data-jump]').forEach(link => {
    link.addEventListener('click', () => revealTarget(link.hash.slice(1), link.hasAttribute('data-solution')));
  });
  window.addEventListener('hashchange', () => revealTarget(location.hash.slice(1)));

  let printState = null;
  function preparePrint() {
    if (printState) return;
    const solutions = [...document.querySelectorAll('.solution-toggle')];
    printState = solutions.map(details => [details, details.open]);
    solutions.forEach(details => { details.open = true; });
  }
  function finishPrint() {
    if (printState) printState.forEach(([details, open]) => { details.open = open; });
    printState = null;
    document.body.classList.remove('printanswers');
  }
  window.addEventListener('beforeprint', preparePrint);
  window.addEventListener('afterprint', finishPrint);
  document.querySelectorAll('[data-print]').forEach(button => {
    button.addEventListener('click', () => {
      document.body.classList.toggle('printanswers', button.dataset.print === 'answers');
      preparePrint();
      try { window.print(); } finally { finishPrint(); }
    });
  });

  try {
    renderMathInElement(document.querySelector('main'), {
      delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}],
      ignoredClasses: ['currency'], throwOnError: true, strict: 'ignore', trust: false,
      errorCallback: () => { document.getElementById('math-error').hidden = false; }
    });
  } catch { document.getElementById('math-error').hidden = false; }
  update();
  if (location.hash) {
    revealTarget(location.hash.slice(1));
    document.getElementById(location.hash.slice(1))?.scrollIntoView();
  }
})();
