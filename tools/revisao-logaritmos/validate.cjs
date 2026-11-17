const fs = require('fs'), path = require('path'), vm = require('vm'), assert = require('assert');
const root = path.resolve(__dirname, '../..');
const items = JSON.parse(fs.readFileSync(path.join(__dirname, 'content.json'), 'utf8'));
const html = fs.readFileSync(path.join(root, 'logaritmos-prova-treino.html'), 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
scripts.forEach(script => new vm.Script(script));
const ctx = {}; vm.createContext(ctx); vm.runInContext(scripts[0], ctx);
let formulas = 0;
for (const q of items) {
  assert(q.steps.length >= 3 && q.pitfall && q.answer, q.id);
  for (const text of [q.prompt, ...q.steps, q.answer, q.pitfall]) {
    assert(!/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/.test(text), q.id);
    assert.equal((text.match(/\$/g) || []).length % 2, 0, `Unpaired math delimiter: ${q.id}`);
    for (const [, formula] of text.matchAll(/\$([^$]+)\$/g)) {
      ctx.katex.renderToString(formula, {throwOnError: true, strict: false}); formulas++;
    }
  }
}
assert.equal(items.filter(q => q.kind === 'original').length, 7);
assert.equal(items.filter(q => q.kind === 'treino').length, 20);
assert.equal(new Set(items.map(q => q.id)).size, 27);
assert.equal(new Set(items.filter(q => q.kind === 'treino').map(q => q.reference)).size, 7);
for (const q of items.filter(q => q.reference)) assert(items.some(o => o.kind === 'original' && o.id === q.reference));
assert.equal((html.match(/class="card"/g) || []).length, 27);
assert.equal((html.match(/class="solution-toggle"/g) || []).length, 27);
const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]);
assert.equal(new Set(ids).size, ids.length, 'Duplicate HTML ids');
const body = html.replace(/<script>[\s\S]*?<\/script>/g, '');
for (const [, href] of body.matchAll(/href="([^"]+)"/g)) {
  if (/^(https?:|data:)/.test(href)) continue;
  const [file, anchor] = href.split('#');
  if (file) assert(fs.existsSync(path.join(root, file)), `Broken link: ${href}`);
  else if (anchor) assert(ids.includes(anchor), `Broken anchor: ${href}`);
}
for (const file of fs.readdirSync(root).filter(file => file.endsWith('.html'))) {
  const page = fs.readFileSync(path.join(root, file), 'utf8');
  const nav = page.match(/<nav[^>]*aria-label="Cadernos de estudo"[^>]*>[\s\S]*?<\/nav>/);
  if (nav) assert.equal((nav[0].match(/href="logaritmos-prova-treino.html"/g) || []).length, 1, file);
}

// Independent numerical checks use original expressions, including the stated
// approximate logarithms. They cover all 27 answers, not the handwritten work.
const near = (actual, expected, label) => assert(Math.abs(actual - expected) < 1e-10, `${label}: ${actual} != ${expected}`);
const approx = n => {
  let value = 0;
  for (const [prime, logarithm] of [[2, .3], [3, .5], [5, .7]]) {
    while (n % prime === 0) { n /= prime; value += logarithm; }
  }
  assert.equal(n, 1, 'Unsupported approximate factor');
  return value;
};
const log = (base, n) => Math.log(n) / Math.log(base);
const ph = (power, decimal) => -(power * .3 + decimal);
near(ph(5, -4), 2.5, 'foto-1');
near(log(10, ((10 ** 1.42) ** 2 * 10) / (10 ** -.16)), 4, 'foto-2a');
near(log(7 ** (1 / 3), 7) + Math.log10(.001), 0, 'foto-2b');
near(log(.5, 75), -log(2, 3) - 2 * log(2, 5), 'foto-2c');
near([2, 3, 4, 5, 6, 7].reduce((p, b) => p * log(b, b + 2), 1), 6, 'foto-3');
near((approx(72) / 3 * approx(4) * approx(27)) / (approx(360) * approx(16)), 19 / 104, 'foto-4a');
near(log(2, 2 ** (6 / 7)) + log(4, 2 ** (6 / 7)) - log(8, 2 ** (6 / 7)), 1, 'foto-4b');
near(ph(3, -4), 3.1, 'treino-01'); near(ph(4, -4), 2.8, 'treino-02'); near(ph(6, -6), 4.2, 'treino-03');
near(log(10, ((10 ** .8) ** 3 * 10) / ((10 ** -.2) ** 2)), 3.8, 'treino-04');
near(log(10, Math.sqrt(10 ** 1.2) / (10 * 10 ** .4)), -.8, 'treino-05');
near(log(10, ((10 ** -.3) ** 2 * 10 ** 3) / (10 ** .6)), 1.8, 'treino-06');
near(log(5 ** .25, 25) + Math.log10(.0001), 4, 'treino-07');
near(log(2 ** (1 / 3), 4) + Math.log10(.01), 4, 'treino-08');
near(log(.5, 45), -2 * log(2, 3) - log(2, 5), 'treino-09');
near(log(.25, 150), -(1 + log(2, 3) + 2 * log(2, 5)) / 2, 'treino-10');
near(log(1 / 3, 20 / 9), 2 - 2 * log(3, 2) - log(3, 5), 'treino-11');
near(log(2, 3) * log(3, 5) * log(5, 16), 4, 'treino-12');
near(log(3, 4) * log(4, 5) * log(5, 6) * log(6, 81), 4, 'treino-13');
near(log(2, 4) * log(3, 5) * log(4, 8) * log(5, 27), 9, 'treino-14');
near(approx(18) / 2 * approx(8) / (approx(45) * approx(4)), 39 / 68, 'treino-15');
near(approx(500) / 3 * approx(9) / (approx(50) * approx(8)), 10 / 17, 'treino-16');
near(approx(80) / 2 * approx(25) / (approx(200) * approx(4)), 133 / 138, 'treino-17');
near(log(3, 3 ** (12 / 7)) + log(9, 3 ** (12 / 7)) - log(27, 3 ** (12 / 7)), 2, 'treino-18');
near(2 * log(2, 64) - log(4, 64) + log(8, 64), 11, 'treino-19');
near(log(2, 2 ** (-6 / 7)) + log(4, 2 ** (-6 / 7)) - log(8, 2 ** (-6 / 7)), -1, 'treino-20');
const gcd = (a, b) => b ? gcd(b, a % b) : a;
for (const [a, b] of [[19, 104], [39, 68], [10, 17], [133, 138]]) assert.equal(gcd(a, b), 1);
console.log(`27 itens; ${formulas} fórmulas válidas; 27 resultados conferidos; frações irredutíveis, links, navegação e scripts válidos.`);
