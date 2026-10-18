from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[1]
E=[]
def ex(topic,title,q,steps,check):
 E.append(dict(topic=topic,title=title,q=q,steps=steps,check=check))
def direct(topic,title,context,value,unit,target,factor,relation,check):
 result=value*factor
 def fmt(x):return f'{x:.8g}'.replace('.',',')
 calculation = f'{fmt(value)} {unit} × ({fmt(factor)} {target}/{unit}) = {fmt(result)} {target}.'
 if factor == 1/60 or factor == 1/3600:
  calculation = f'{fmt(value)} {unit} ÷ {round(1/factor)} = {fmt(result)} {target}.'
 ex(topic,title,f'{context} {fmt(value)} {unit}. Expresse essa medida em {target}.',[relation,calculation],check)
L='Comprimento';T='Tempo';M='Massa';Q='Energia';A='Aplicações'
for title,context,value,unit,target,factor in [
('Trajeto de uma caminhada','Um estudante caminha',2.4,'km','m',1000),
('Comprimento de uma mola','Uma mola esticada mede',35,'cm','m',.01),
('Pista de atletismo','Uma volta de uma pista mede',400,'m','km',.001),
('Altura de lançamento','Uma bola é solta de uma altura de',1.8,'m','cm',100),
('Extensão de uma estrada','O trecho analisado por um radar tem',.075,'km','cm',100000),
('Deslocamento de um carrinho','Em um trilho, um carrinho percorre',1250,'cm','km',.00001),
('Espessura de uma lâmina','Uma lâmina usada em laboratório tem espessura de',.08,'cm','m',.01),
('Raio de uma roda','O raio de uma roda é',.32,'m','cm',100),
('Distância de frenagem','Durante a frenagem, um automóvel percorre',.042,'km','m',1000),
('Amplitude de oscilação','A amplitude de um pêndulo é',6.5,'cm','m',.01)]:
 relation={'km':'1 km = 1000 m = 100000 cm.','m':'1 m = 100 cm = 0,001 km.','cm':'1 cm = 0,01 m = 0,00001 km.'}[unit]
 direct(L,title,context,value,unit,target,factor,relation,'Ao passar para uma unidade menor, o valor numérico aumenta; para uma unidade maior, diminui.')
for title,context,value,unit,target,factor in [
('Duração de uma viagem','Uma viagem dura',1.5,'h','min',60),
('Tempo de aquecimento','Um aquecedor fica ligado por',3,'min','s',60),
('Cronômetro da corrida','Um cronômetro registra',150,'s','min',1/60),
('Ensaio de resistência','Um motor é testado durante',5400,'s','h',1/3600),
('Intervalo de medição','Um sensor faz medições durante',.25,'h','s',3600),
('Experimento de resfriamento','O resfriamento dura',90,'min','h',1/60),
('Pulso de um equipamento','Um equipamento permanece ativo durante',.05,'min','s',60),
('Queda registrada em vídeo','Um evento filmado dura',.02,'h','s',3600)]:
 direct(T,title,context,value,unit,target,factor,'1 h = 60 min = 3600 s; 1 min = 60 s.','Horas, minutos e segundos usam fatores de 60, e não de 100.')
ex(T,'Uma hora e vinte minutos','Um experimento dura 1 h e 20 min. Qual é sua duração total em segundos?',['1 h = 3600 s e 20 min = 20 × 60 = 1200 s.','Some os tempos na mesma unidade: Δt = 3600 + 1200 = 4800 s.'],'1 h e 20 min correspondem a 1 + 20/60 h, e não a 1,20 h.')
ex(T,'Duas leituras do cronômetro','O cronômetro marca 2 min e 45 s. Expresse o intervalo em segundos e em minutos decimais.',['Em segundos: Δt = 2 × 60 + 45 = 165 s.','Em minutos: Δt = 165/60 = 2,75 min.'],'2 min e 45 s não são 2,45 min: divida os 45 s por 60.')
for title,context,value,unit,target,factor in [
('Carrinho de laboratório','A massa de um carrinho é',750,'g','kg',.001),
('Bloco para calorimetria','Um bloco metálico tem massa de',.25,'kg','g',1000),
('Pequena esfera','Uma esfera tem massa de',12,'g','kg',.001),
('Carga de uma balança','A balança indica uma massa de',2.5,'kg','g',1000),
('Amostra de pó','Uma amostra tem massa de',.8,'g','kg',.001),
('Massa de um pacote','Um pacote tem massa de',1250,'g','kg',.001),
('Objeto leve','A massa de um objeto é',.045,'kg','g',1000),
('Peça de metal','Uma peça tem massa de',3500,'g','kg',.001)]:
 direct(M,title,context,value,unit,target,factor,'1 kg = 1000 g; 1 g = 0,001 kg.','Massa pode ser medida em kg ou g; peso é uma força e sua unidade SI é o newton.')
ex(M,'Duas massas no carrinho','Um carrinho de 0,8 kg recebe uma carga de 350 g. Qual é a massa total em kg?',['Converta a carga: 350 g = 350/1000 = 0,35 kg.','Some: m = 0,8 + 0,35 = 1,15 kg.'],'Converta antes de somar: 0,8 e 350 estão originalmente em unidades diferentes.')
ex(M,'Separando uma amostra','De uma amostra de 1,2 kg retiram-se 275 g. Qual massa resta, em gramas?',['Converta: 1,2 kg = 1200 g.','Subtraia: m = 1200 − 275 = 925 g.'],'As duas parcelas precisam estar em gramas para fazer a subtração.')
for title,context,value,unit,target,factor in [
('Calor recebido','Uma amostra recebe',100,'cal','J',4.2),
('Energia de um aquecedor','Um aquecedor fornece',840,'J','cal',1/4.2),
('Pequena troca de calor','Uma peça absorve',25,'cal','J',4.2),
('Energia dissipada','Uma força de atrito dissipa',2100,'J','cal',1/4.2),
('Calor de uma reação','Uma reação libera',1500,'cal','J',4.2),
('Energia em um pulso','Um pulso transfere',63,'J','cal',1/4.2)]:
 # Use a division expression rather than an approximate reciprocal in the displayed solution.
 result=value*factor
 ex(Q,title,f'{context} {value:g} {unit}. Converta para {target}, adotando 1 cal = 4,2 J.'.replace(f'{value:g}',f'{value:g}'.replace('.',',')),['Use a equivalência dada: 1 cal = 4,2 J.',f'{value:g} '+unit+(' × 4,2' if unit=='cal' else ' ÷ 4,2')+f' = {result:g} {target}.'],'De cal para J, multiplique por 4,2; de J para cal, divida por 4,2.')
ex(Q,'Aproximação pedida no enunciado','Para estimar a energia transferida, adote 1 cal = 4 J. Quantos joules correspondem a 300 cal?',['Use o fator específico do problema: 1 cal = 4 J.','Q = 300 × 4 = 1200 J.'],'Neste exercício use 4 J/cal; o fator 4,2 J/cal dos outros problemas não se aplica aqui.')
ex(Q,'Somando energias','Uma amostra recebe 420 J e depois mais 50 cal. Qual é a energia total em J? Adote 1 cal = 4,2 J.',['Converta a segunda parcela: 50 cal = 50 × 4,2 = 210 J.','Q = 420 + 210 = 630 J.'],'Não some 420 e 50 sem converter as unidades de energia.')
ex(Q,'Energia que falta','Um processo precisa de 1000 cal e já recebeu 1680 J. Quantas calorias faltam? Adote 1 cal = 4,2 J.',['Energia já recebida: 1680/4,2 = 400 cal.','Energia que falta: 1000 − 400 = 600 cal.'],'Primeiro converta para a unidade pedida, depois subtraia.')
ex(Q,'Caloria e quilocaloria','Um alimento informa 2 kcal de energia. Expresse o valor em cal e em J. Adote 1 kcal = 1000 cal e 1 cal = 4,2 J.',['2 kcal = 2 × 1000 = 2000 cal.','E = 2000 × 4,2 = 8400 J.'],'kcal e cal são diferentes: o prefixo quilo multiplica a unidade por 1000.')
ex(A,'Velocidade na estrada','Um carro viaja a 72 km/h. Expresse a velocidade em m/s.',['Converta numerador e denominador: 72 km/h = (72 × 1000 m)/(3600 s).','v = 72000/3600 = 20 m/s.'],'De km/h para m/s, divida por 3,6: a conversão envolve distância e tempo.')
ex(A,'Velocidade de um corredor','Um corredor atinge 5 m/s. Qual é essa velocidade em km/h?',['v = 5 × (1 km/1000 m) × (3600 s/1 h).','v = 5 × 3,6 = 18 km/h.'],'De m/s para km/h, multiplique por 3,6.')
ex(A,'Distância em uma viagem','Um ônibus mantém 54 km/h por 2 min. Qual distância percorre em metros?',['v = 54/3,6 = 15 m/s; Δt = 2 × 60 = 120 s.','s = vΔt = 15 × 120 = 1800 m.'],'Use segundos com m/s, para que as unidades de tempo se cancelem.')
ex(A,'Carrinho no trilho','Um carrinho percorre 250 cm em 5 s. Determine sua velocidade média em m/s.',['Δs = 250/100 = 2,5 m.','v_m = Δs/Δt = 2,5/5 = 0,5 m/s.'],'O comprimento em centímetros precisa virar metros antes de obter m/s.')
ex(A,'Energia cinética de uma bola','Uma bola de 200 g move-se a 36 km/h. Calcule sua energia cinética em J usando E_c = mv²/2.',['m = 200/1000 = 0,2 kg; v = 36/3,6 = 10 m/s.','E_c = 0,2 × 10²/2 = 10 J.'],'Converta a velocidade antes de elevá-la ao quadrado; use massa em kg para obter J.')
ex(A,'Trabalho ao erguer uma carga','Uma carga de 500 g é elevada em 120 cm, com velocidade constante. Adote g = 10 m/s². Qual é o trabalho da força que a ergue, em J? Use W = mgh.',['m = 0,5 kg; h = 1,2 m.','W = 0,5 × 10 × 1,2 = 6 J.'],'O símbolo g em mgh representa a aceleração da gravidade; g depois de 500 é a unidade grama.')
ex(A,'Aquecimento de água','Uma amostra de água de 0,2 kg recebe 8400 J. Adote c = 1 cal/(g·°C) e 1 cal = 4,2 J. Qual é a elevação de temperatura? Use Q = mcΔT.',['Use as unidades de c: m = 0,2 × 1000 = 200 g; Q = 8400/4,2 = 2000 cal.','ΔT = Q/(mc) = 2000/(200 × 1) = 10 °C.'],'Com c em cal/(g·°C), use energia em cal e massa em g.')
ex(A,'Potência de um aquecedor','Um aquecedor fornece 600 cal em 2 min. Qual é sua potência média em W? Adote 1 cal = 4,2 J e 1 W = 1 J/s.',['Q = 600 × 4,2 = 2520 J; Δt = 2 × 60 = 120 s.','P = Q/Δt = 2520/120 = 21 W.'],'J dividido por s fornece W; cal dividido por min não fornece diretamente watts.')
ex(A,'Tempo de uma caminhada','Uma pessoa percorre 1,8 km a 1,5 m/s. Determine o tempo em segundos e em minutos.',['s = 1,8 × 1000 = 1800 m.','Δt = s/v = 1800/1,5 = 1200 s.','Em minutos: 1200/60 = 20 min.'],'A unidade final de tempo depende das unidades usadas em distância e velocidade.')
ex(A,'Bateria e autonomia','Uma bateria fornece 7560 J a um dispositivo que consome 30 cal por minuto. Quanto tempo a bateria dura, em minutos e em segundos? Adote 1 cal = 4,2 J e consumo constante.',['Energia disponível: E = 7560/4,2 = 1800 cal.','Δt = 1800/(30 cal/min) = 60 min.','Em segundos: 60 × 60 = 3600 s.'],'A divisão de cal por cal/min resulta em minutos; converta para segundos apenas ao final.')
assert len(E)==50
# Each diagram preserves the numerical values and units of its own problem.
D=[
('2,4 km','× 1000','2400 m'),('35 cm','÷ 100','0,35 m'),('400 m','÷ 1000','0,4 km'),('1,8 m','× 100','180 cm'),('0,075 km','× 100000','7500 cm'),('1250 cm','÷ 100000','0,0125 km'),('0,08 cm','÷ 100','0,0008 m'),('0,32 m','× 100','32 cm'),('0,042 km','× 1000','42 m'),('6,5 cm','÷ 100','0,065 m'),
('1,5 h','× 60','90 min'),('3 min','× 60','180 s'),('150 s','÷ 60','2,5 min'),('5400 s','÷ 3600','1,5 h'),('0,25 h','× 3600','900 s'),('90 min','÷ 60','1,5 h'),('0,05 min','× 60','3 s'),('0,02 h','× 3600','72 s'),('1 h + 20 min','3600 s + 1200 s','4800 s'),('2 min + 45 s','165 s ÷ 60','2,75 min'),
('750 g','÷ 1000','0,75 kg'),('0,25 kg','× 1000','250 g'),('12 g','÷ 1000','0,012 kg'),('2,5 kg','× 1000','2500 g'),('0,8 g','÷ 1000','0,0008 kg'),('1250 g','÷ 1000','1,25 kg'),('0,045 kg','× 1000','45 g'),('3500 g','÷ 1000','3,5 kg'),('0,8 kg + 350 g','0,8 kg + 0,35 kg','1,15 kg'),('1,2 kg − 275 g','1200 g − 275 g','925 g'),
('100 cal','× 4,2 J/cal','420 J'),('840 J','÷ 4,2 J/cal','200 cal'),('25 cal','× 4,2 J/cal','105 J'),('2100 J','÷ 4,2 J/cal','500 cal'),('1500 cal','× 4,2 J/cal','6300 J'),('63 J','÷ 4,2 J/cal','15 cal'),('300 cal','× 4 J/cal','1200 J'),('420 J + 50 cal','420 J + 210 J','630 J'),('1000 cal − 1680 J','1000 cal − 400 cal','600 cal'),('2 kcal','2000 cal × 4,2 J/cal','8400 J'),
('72 km/h','72 × 1000 ÷ 3600','20 m/s'),('5 m/s','5 × 3600 ÷ 1000','18 km/h'),('54 km/h por 2 min','15 m/s × 120 s','1800 m'),('250 cm em 5 s','2,5 m ÷ 5 s','0,5 m/s'),('200 g a 36 km/h','½ × 0,2 kg × (10 m/s)²','10 J'),('500 g elevados 120 cm','0,5 kg × 10 m/s² × 1,2 m','6 J'),('0,2 kg recebem 8400 J','2000 cal ÷ (200 g × 1 cal/(g·°C))','ΔT = 10 °C'),('600 cal em 2 min','2520 J ÷ 120 s','21 W'),('1,8 km a 1,5 m/s','1800 m ÷ 1,5 m/s','1200 s = 20 min'),('7560 J; 30 cal/min','1800 cal ÷ 30 cal/min','60 min = 3600 s')]
assert len(D)==len(E)==50
for e,(start,operation,result) in zip(E,D):
 e['illustration']=dict(start=start,operation=operation,result=result)

(root/'tools/units-exercises.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
source=(root/'cinematica.html').read_text();styles=re.findall(r'<style>(.*?)</style>',source,re.S);scripts=re.findall(r'<script>(.*?)</script>',source,re.S)
nav=re.search(r'<nav class="page-tabs"[^>]*>.*?</nav>',source,re.S).group();nav=re.sub(r' aria-current="page"','',nav)
link='<a href="conversao-unidades.html">Conversão de unidades · 50 exercícios</a>'
if 'href="conversao-unidades.html"' not in nav:nav=nav.replace('</nav>',link+'</nav>')
nav=nav.replace('href="conversao-unidades.html"','href="conversao-unidades.html" aria-current="page"')
lesson='''<section class="lesson" id="theory"><div class="eyebrow">01 / Preparar as unidades</div><h2>A mesma medida, outra unidade.</h2><p>Converter uma unidade muda o número usado para escrever uma medida. A distância, o tempo, a massa ou a energia continuam os mesmos. Escolha a unidade que combina com a fórmula antes de fazer as contas.</p><div class="concepts"><article><h3>Comprimento</h3><p>1 km = 1000 m<br>1 m = 100 cm<br>1 km = 100000 cm</p></article><article><h3>Tempo</h3><p>1 h = 60 min<br>1 min = 60 s<br>1 h = 3600 s</p></article><article><h3>Massa</h3><p>1 kg = 1000 g<br>1 g = 0,001 kg</p></article><article><h3>Energia</h3><p>Neste caderno, adote 1 cal = 4,2 J, salvo quando o enunciado pedir outra aproximação. 1 kcal = 1000 cal.</p></article></div><h3>Multiplique por uma equivalência</h3><p>Para converter 250 cm em metros: 250 cm × (1 m / 100 cm) = 2,5 m. O fator vale 1 e as unidades cm se cancelam. Para converter 72 km/h em m/s: 72 × 1000/3600 = 20 m/s.</p><div class="check"><strong>Confira antes de calcular</strong><p>Em fórmulas que fornecem energia em J, use kg, m e s. Em calorimetria, siga as unidades do calor específico: se c está em cal/(g·°C), use cal e g. Horas e minutos usam fatores de 60. 1,5 h são 1 h e 30 min.</p></div></section>'''
js='''
const exercises=DATA;
const $=id=>document.getElementById(id);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function illustration(e,id){
 const v=e.illustration;
 const common='fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"';
 const icons={
 'Comprimento':`<g ${common}><rect x="15" y="25" width="170" height="35" rx="3"/><path d="M32 25v18m17-18v10m17-10v18m17-18v10m17-10v18m17-18v10m17-10v18m17-18v10m17-10v18"/></g>`,
 'Tempo':`<g ${common}><circle cx="100" cy="42" r="30"/><path d="M100 17v5m25 20h-5m-20 25v-5M75 42h5m20-23v23l16 10"/><path d="M35 28h23M25 42h30M35 56h23"/></g>`,
 'Massa':`<g ${common}><path d="M100 17v51M70 68h60M45 29h110M55 29L35 52h40L55 29m90 0-20 23h40l-20-23"/><path d="M35 52q20 20 40 0m50 0q20 20 40 0"/></g>`,
 'Energia':`<g ${common}><rect x="25" y="21" width="140" height="44" rx="6"/><path d="M165 34h10v18h-10M100 27 84 45h19l-6 15 20-22H98z"/></g>`,
 'Aplicações':`<g ${common}><path d="M20 59h160M43 53V25h45v28m5-5h61l-17-25h-30z"/><circle cx="109" cy="53" r="7"/><circle cx="145" cy="53" r="7"/><path d="M27 19h23m108 6h22m-15 10h15"/></g>`};
 const captions={
 'Comprimento':'A distância é a mesma. Uma unidade menor exige um número maior; uma unidade maior exige um número menor.',
 'Tempo':'O intervalo é o mesmo: 1 h = 60 min = 3600 s. Converta cada parcela antes de somar.',
 'Massa':'A massa de cada objeto não muda ao trocar kg por g. Para somar ou subtrair, iguale primeiro as unidades.',
 'Energia':'J e cal medem energia. O fator de conversão usado aqui é o informado neste enunciado.',
 'Aplicações':'Primeiro ajuste as unidades; depois aplique a relação física. As unidades da operação determinam a unidade do resultado.'};
 return `<figure class="unit-illustration" aria-labelledby="unit-caption-${id}"><div class="unit-visual"><svg viewBox="0 0 200 84" aria-hidden="true" focusable="false">${icons[e.topic]}</svg><strong>${esc(e.topic)} · acompanhe a conversão</strong></div><div class="unit-flow"><div class="unit-node"><span>Dados do problema</span><b>${esc(v.start)}</b></div><span class="unit-arrow" aria-hidden="true">→</span><div class="unit-node unit-operation"><span>${e.topic==='Aplicações'?'Unidades ajustadas e cálculo':'Conversão na mesma grandeza'}</span><b>${esc(v.operation)}</b></div><span class="unit-arrow" aria-hidden="true">→</span><div class="unit-node unit-result"><span>Resultado</span><b>${esc(v.result)}</b></div></div><figcaption id="unit-caption-${id}">${esc(captions[e.topic])} Esquema fora de escala.</figcaption></figure>`;
}
const key='algebra-conversao-unidades-v1';let done=new Set();
try{const saved=JSON.parse(localStorage.getItem(key)||'[]');if(Array.isArray(saved))done=new Set(saved.filter(n=>Number.isInteger(n)&&n>=1&&n<=exercises.length))}catch{$('storage').hidden=false}
exercises.forEach((e,i)=>{const id=i+1,card=document.createElement('article');card.className='card';card.dataset.id=id;card.dataset.topic=e.topic;
card.innerHTML=`<div class="cardhead"><span class="num">${String(id).padStart(2,'0')}</span><h3 id="title-${id}">${esc(e.title)}</h3><span class="badge">${esc(e.topic)}</span></div><p class="question">${esc(e.q)}</p><div class="actions"><button class="reveal" aria-expanded="false" aria-controls="solution-${id}">Ver solução passo a passo</button><label><input type="checkbox" ${done.has(id)?'checked':''} aria-label="Concluí o exercício ${id}"> Consegui refazer</label></div><div class="solution" id="solution-${id}" role="region" aria-labelledby="title-${id}" hidden>${illustration(e,id)}<ol>${e.steps.map(s=>'<li>'+esc(s)+'</li>').join('')}</ol><div class="check"><strong>Confira o raciocínio</strong><p>${esc(e.check)}</p></div></div>`;
card.querySelector('button').onclick=ev=>{const solution=$('solution-'+id);solution.hidden=!solution.hidden;ev.currentTarget.setAttribute('aria-expanded',String(!solution.hidden));ev.currentTarget.textContent=solution.hidden?'Ver solução passo a passo':'Ocultar solução'};
card.querySelector('input').onchange=ev=>{ev.target.checked?done.add(id):done.delete(id);try{localStorage.setItem(key,JSON.stringify([...done]))}catch{$('storage').hidden=false}update()};$('exercises').append(card)});
[...new Set(exercises.map(e=>e.topic))].forEach(t=>{const option=document.createElement('option');option.value=t;option.textContent=t;$('topic').append(option)});
function update(){let count=0;document.querySelectorAll('.card').forEach(c=>{c.hidden=($('topic').value!=='all'&&c.dataset.topic!==$('topic').value)||($('pending').checked&&done.has(+c.dataset.id));c.classList.toggle('done',done.has(+c.dataset.id));if(!c.hidden)count++});$('shown').textContent=count+' de '+exercises.length+' exercícios exibidos';$('progress').textContent=done.size+' de '+exercises.length+' refeitos';$('empty').hidden=count>0}
$('topic').onchange=update;$('pending').onchange=update;update();
$('printquestions').onclick=()=>{document.body.classList.remove('printanswers');window.print()};$('printanswers').onclick=()=>{document.body.classList.add('printanswers');window.print()};window.addEventListener('afterprint',()=>document.body.classList.remove('printanswers'));
'''.replace('DATA',json.dumps(E,ensure_ascii=False))
diagram_css='.unit-illustration{margin:18px 0 24px;padding:20px;border:1px solid #cbd7c3;border-radius:12px;background:#f6f8f2;break-inside:avoid}.unit-visual{display:flex;align-items:center;gap:16px;color:#243f35;margin-bottom:16px}.unit-visual svg{width:110px;height:47px;flex:none}.unit-flow{display:flex;align-items:center;gap:10px}.unit-node{flex:1;min-width:0;padding:16px 12px;background:white;border:1px solid #d9ded4;border-radius:8px;text-align:center;overflow-wrap:anywhere}.unit-node span{display:block;font-size:12px;margin-bottom:8px;color:#536458}.unit-node b{font-size:18px;line-height:1.5;font-variant-numeric:tabular-nums}.unit-operation{background:#edf2e5}.unit-result{background:#dfecdc;border-color:#91ad7e}.unit-arrow{font-size:24px;color:#536458}.unit-illustration figcaption{font-size:14px;line-height:1.6;margin-top:14px;color:#536458}@media(max-width:650px){.unit-flow{flex-direction:column;gap:6px}.unit-node{width:100%;box-sizing:border-box}.unit-arrow{transform:rotate(90deg);line-height:1}.unit-visual{gap:10px}.unit-visual svg{width:80px}.unit-illustration{padding:14px}}@media print{.unit-illustration{background:white;padding:10px}.unit-node{padding:8px}.unit-node b{font-size:14px}.unit-visual svg{width:70px;height:30px}}'
head=''.join('<style>'+s+'</style>' for s in styles)+''.join('<script>'+s+'</script>' for s in scripts[:2])+'<style>'+diagram_css+'</style>'
html='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="50 problemas de física sobre conversão de km, cm, m, h, min, s, kg, g, J e cal, com soluções passo a passo."><title>Conversão de unidades · 50 exercícios</title>'''+head+'''</head><body><header><div class="masthead"><strong>Reforço · Física</strong><span>1º ano · Ensino médio</span></div>'''+nav+'''<div class="hero"><div class="eyebrow">Conversões em problemas de física</div><h1>Conversão de unidades,<br>passo a passo.</h1><p class="intro">Comprimento, tempo, massa e energia: pratique com km, cm, m, h, min, s, kg, g, J e cal.</p><div class="jump"><a href="#theory">Revisar as conversões</a><a href="#practice">Resolver os 50 exercícios</a></div></div></header><main>'''+lesson+'''<section id="practice" class="practice"><div class="eyebrow">02 / Praticar e conferir</div><h2>50 problemas para acertar as unidades.</h2><p>São 10 exercícios de comprimento, 10 de tempo, 10 de massa, 10 de energia e 10 aplicações que combinam conversões e fórmulas de física. Tente no papel antes de abrir a solução.</p><div class="toolbar"><label for="topic">Assunto</label><select id="topic"><option value="all">Todos os assuntos</option></select><label><input type="checkbox" id="pending"> Só pendentes</label></div><div class="counter"><span id="shown" aria-live="polite"></span><span id="progress" aria-live="polite"></span></div><p id="storage" class="small" hidden>Não foi possível salvar o progresso neste navegador. As marcações funcionam nesta sessão.</p><div id="exercises"></div><p id="empty" hidden>Nenhum exercício pendente neste filtro.</p><div class="printtools"><button class="utility" id="printquestions">Imprimir exercícios</button><button class="utility" id="printanswers">Imprimir com soluções</button></div></section><noscript>Ative o JavaScript para carregar os 50 exercícios e suas soluções.</noscript></main><footer>Problemas autorais para o 1º ano do ensino médio. Nas conversões de energia, use o fator informado no enunciado. Progresso salvo apenas neste navegador. Este caderno funciona sem internet quando salvo como HTML.</footer><script>'''+js+'''</script></body></html>'''
(root/'conversao-unidades.html').write_text(html)
for p in root.glob('*.html'):
 if p.name=='conversao-unidades.html':continue
 def add(m):
  n=m.group();return n if 'href="conversao-unidades.html"' in n else n.replace('</nav>',link+'</nav>')
 p.write_text(re.sub(r'<nav class="page-tabs"[^>]*>.*?</nav>',add,p.read_text(),flags=re.S))
print('Conversão de unidades: 50 exercícios; navegação integrada.')
