(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const cards = [...document.querySelectorAll('.card')];
  const ids = new Set(cards.map(card => card.id));
  const storageKey = 'revisao-logaritmos-fotos-v1';
  const pending = document.getElementById('pending');
  const topic = document.getElementById('topic');
  let kind = 'all';
  let done = new Set();
  try {
    const saved = JSON.parse(localStorage.getItem(storageKey) || '[]');
    if (Array.isArray(saved)) done = new Set(saved.filter(id => ids.has(id)));
  } catch { document.getElementById('storage-note').hidden = false; }

  function update() {
    let visible = 0;
    for (const card of cards) {
      card.hidden = (kind !== 'all' && card.dataset.kind !== kind)
        || (topic.value !== 'all' && card.dataset.topic !== topic.value)
        || (pending.checked && done.has(card.id));
      card.classList.toggle('done', done.has(card.id));
      card.querySelector('input[type=checkbox]').checked = done.has(card.id);
      if (!card.hidden) visible++;
    }
    document.querySelectorAll('.question-group').forEach(group => {
      group.hidden = ![...group.querySelectorAll('.card')].some(card => !card.hidden);
    });
    document.querySelectorAll('[data-kind-filter]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.kindFilter === kind));
    });
    document.getElementById('shown').textContent = `${visible} de ${cards.length} itens exibidos`;
    document.getElementById('progresslabel').textContent = `${done.size} de ${cards.length} concluídos`;
    document.getElementById('progress').value = done.size;
    document.getElementById('empty').hidden = visible !== 0;
  }
  document.querySelectorAll('[data-kind-filter]').forEach(button => {
    button.addEventListener('click', () => { kind = button.dataset.kindFilter; update(); });
  });
  pending.addEventListener('change', update);
  topic.addEventListener('change', update);
  for (const card of cards) {
    card.querySelector('input[type=checkbox]').addEventListener('change', event => {
      if (event.target.checked) done.add(card.id); else done.delete(card.id);
      try { localStorage.setItem(storageKey, JSON.stringify([...done])); }
      catch { document.getElementById('storage-note').hidden = false; }
      update();
    });
  }
  function revealTarget(id) {
    const card = document.getElementById(id);
    if (!ids.has(id) && !['originais', 'treino'].includes(id)) return;
    kind = 'all'; topic.value = 'all'; pending.checked = false; update();
    if (ids.has(id)) card.querySelector('details').open = true;
  }
  document.querySelectorAll('a[data-jump]').forEach(link => {
    link.addEventListener('click', () => { revealTarget(link.hash.slice(1)); });
  });
  window.addEventListener('hashchange', () => revealTarget(location.hash.slice(1)));

  // All solutions are opened for printing, then their previous state is restored.
  // CSS determines whether the printout includes them, independently of filters.
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
      throwOnError: true, strict: 'ignore', trust: false,
      errorCallback: () => { document.getElementById('math-error').hidden = false; }
    });
  } catch { document.getElementById('math-error').hidden = false; }
  update();
  if (location.hash) {
    revealTarget(location.hash.slice(1));
    document.getElementById(location.hash.slice(1))?.scrollIntoView();
  }
})();
