(()=>{
'use strict';
const form=document.querySelector('#test-form'),result=document.querySelector('#result');
let corrected=false;
function correct(){
 corrected=true;let total=0,answered=0;const counts={};
 document.querySelectorAll('.test-card').forEach(card=>{
  const selected=form.querySelector(`input[name="q${card.dataset.id}"]:checked`),key=Number(card.dataset.answer),subject=card.dataset.subject;
  counts[subject]??={right:0,answered:0};
  const ok=selected&&Number(selected.value)===key;
  if(selected){answered++;counts[subject].answered++;} if(ok){total++;counts[subject].right++;}
  card.querySelector('.feedback').textContent=ok?'Correta.':selected?`Incorreta. Resposta: ${'ABCDE'[key]}. Confira a resolução no gabarito.`:`Não respondida. Resposta: ${'ABCDE'[key]}.`;
 });
 result.replaceChildren();const p=document.createElement('p');p.textContent=`Resultado: ${total}/32 acertos · ${answered}/32 respondidas · nota ${(total/32*10).toFixed(2).replace('.',',')}/10. Questões em branco contam como zero.`;result.append(p);
 for(const [name,c] of Object.entries(counts)){const line=document.createElement('p');line.textContent=`${name}: ${c.right}/8 acertos · ${c.answered}/8 respondidas.`;result.append(line);}
 result.hidden=false;
}
document.querySelector('#correct').addEventListener('click',()=>{correct();result.focus();});
form.addEventListener('change',()=>{if(corrected)correct();});
document.querySelector('#clear').addEventListener('click',()=>{if(!confirm('Limpar todas as respostas desta tentativa?'))return;form.reset();corrected=false;result.hidden=true;document.querySelectorAll('.feedback').forEach(e=>e.textContent='');});
function mode(answers){document.querySelector('#exam').hidden=answers;document.querySelector('#answers').hidden=!answers;document.querySelector('#show-exam').setAttribute('aria-pressed',String(!answers));document.querySelector('#show-answers').setAttribute('aria-pressed',String(answers));document.body.classList.toggle('print-answers',answers);}
document.querySelector('#show-exam').onclick=()=>mode(false);
document.querySelector('#show-answers').onclick=()=>mode(true);
document.querySelector('#print-exam').onclick=()=>{mode(false);window.print();};
document.querySelector('#print-answers').onclick=()=>{mode(true);window.print();};
renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:true,strict:'ignore'});
})();
