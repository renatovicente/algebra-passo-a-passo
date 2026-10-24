// New questions calibrated against the five supplied pages of provaQ3.pdf.
// The source scan and its personal information are deliberately not distributed.
const examRaw = String.raw;
const examQuestions = [
  {
    id: 1, subject: 'Geometria', title: 'Uma circunferência, dois polígonos', points: 1,
    prompt: examRaw`Uma circunferência de centro $O$ e raio $3\sqrt3\,\mathrm{cm}$ está inscrita em um hexágono regular. Um quadrado está inscrito nessa mesma circunferência. Calcule:`,
    figure: 'hex-square',
    parts: [
      {label:'a', points:0.5, level:'Intermediário', prompt:'a medida do lado e o perímetro do hexágono.',
       answer:examRaw`$\ell_6=6\,\mathrm{cm}$ e $P_6=36\,\mathrm{cm}$.`,
       steps:[examRaw`O hexágono é circunscrito à circunferência. Portanto, seu apótema é $a_6=3\sqrt3\,\mathrm{cm}$.`,examRaw`No hexágono regular, $a_6=\ell_6\sqrt3/2$. Assim, $\ell_6=2(3\sqrt3)/\sqrt3=6\,\mathrm{cm}$.`,examRaw`O perímetro é $P_6=6\ell_6=36\,\mathrm{cm}$.`],
       rubric:'0,25 pela relação entre apótema e lado; 0,25 pelo lado e perímetro corretos.'},
      {label:'b', points:0.5, level:'Intermediário', prompt:'a medida do lado do quadrado.',
       answer:examRaw`$\ell_4=3\sqrt6\,\mathrm{cm}$.`,
       steps:[examRaw`Para o quadrado, o raio da mesma circunferência é o raio externo: $R_4=3\sqrt3\,\mathrm{cm}$.`,examRaw`A diagonal é $d=2R_4=6\sqrt3\,\mathrm{cm}$. Por Pitágoras, $2\ell_4^2=d^2=108$.`,examRaw`Logo, $\ell_4=\sqrt{54}=3\sqrt6\,\mathrm{cm}$, escolhendo a raiz positiva.`],
       rubric:'0,25 por identificar a diagonal como diâmetro; 0,25 pelo cálculo do lado.'}
    ],
    pitfall:'O raio dado é o apótema do hexágono e o raio externo do quadrado. Não use a mesma relação nos dois polígonos.',
    sources:[['poligonos.html#title-30','Polígonos · 30: lado pelo apótema'],['poligonos.html#title-17','Polígonos · 17: quadrado inscrito'],['poligonos.html#title-38','Polígonos · 38: dentro e fora do círculo']]
  },
  {
    id:2, subject:'Geometria', title:'Do quadrado ao octógono', points:0.75,
    prompt:examRaw`Um quadrado $ACDE$ está inscrito em uma circunferência de centro $O$ e raio $8\,\mathrm{cm}$. O ponto $B$ é o ponto médio do arco menor $AC$, e $M$ é o ponto médio do lado $AC$. Os pontos $O$, $M$ e $B$ estão alinhados, com $M$ entre $O$ e $B$. Ao acrescentar os pontos médios dos quatro arcos menores determinados pelos lados do quadrado, obtém-se um octógono regular.`,
    figure:'octagon',
    parts:[
      {label:'a',points:0.5,level:'Avançado',prompt:examRaw`Determine o lado $AB$ do octógono, mostrando como obtém $AM$ e $BM$.`,
       answer:examRaw`$AB=8\sqrt{2-\sqrt2}\,\mathrm{cm}$.`,
       steps:[examRaw`O lado do quadrado é $AC=8\sqrt2\,\mathrm{cm}$. Assim, $AM=AC/2=4\sqrt2\,\mathrm{cm}$.`,examRaw`No triângulo retângulo $OMA$, $OM^2=OA^2-AM^2=64-32=32$. Portanto, $OM=4\sqrt2\,\mathrm{cm}$.`,examRaw`Como $OB=8$ e $M$ está entre $O$ e $B$, $BM=8-4\sqrt2\,\mathrm{cm}$.`,examRaw`No triângulo retângulo $AMB$, $AB^2=(4\sqrt2)^2+(8-4\sqrt2)^2=128-64\sqrt2=64(2-\sqrt2)$.`,examRaw`Logo, $AB=8\sqrt{2-\sqrt2}\,\mathrm{cm}$.`],
       rubric:'0,25 pelas medidas auxiliares AM e BM; 0,25 por Pitágoras e a medida de AB.'},
      {label:'b',points:0.25,level:'Básico',prompt:'Determine o perímetro do octógono, usando o resultado do item anterior.',
       answer:examRaw`$P_8=64\sqrt{2-\sqrt2}\,\mathrm{cm}$.`,
       steps:[examRaw`Um octógono regular tem oito lados iguais. Portanto, $P_8=8AB=64\sqrt{2-\sqrt2}\,\mathrm{cm}$.`],
       rubric:'0,25 por multiplicar corretamente o lado por oito. Considere o procedimento se houver erro transportado de (a).'}
    ],
    pitfall:'AB é o lado do octógono; AC é o lado do quadrado. BM é uma diferença de comprimentos, e seu quadrado exige o termo do meio.',
    sources:[['poligonos.html#title-47','Polígonos · 47: do quadrado ao octógono'],['poligonos.html#title-17','Polígonos · 17: lado do quadrado inscrito']]
  },
  {
    id:3,subject:'Geometria',title:'Triângulo entre duas circunferências',points:0.75,
    prompt:examRaw`Um triângulo equilátero $ABC$ é circunscrito a uma circunferência de centro $O$ e raio $4\,\mathrm{cm}$. Outra circunferência, também de centro $O$, passa pelos três vértices do triângulo. O ponto $M$ é o ponto médio de $BC$. Calcule:`,
    figure:'triangle',
    parts:[
      {label:'a',points:0.25,level:'Básico',prompt:'o raio da circunferência que passa pelos vértices.',
       answer:examRaw`$R=8\,\mathrm{cm}$.`,
       steps:[examRaw`O raio interno é o apótema: $OM=a=4\,\mathrm{cm}$. No triângulo equilátero, $R=2a$.`,examRaw`Portanto, $R=8\,\mathrm{cm}$.`],
       rubric:'0,25 pela relação R = 2a e pelo resultado.'},
      {label:'b',points:0.5,level:'Intermediário',prompt:examRaw`o lado $BC$ do triângulo. Justifique usando o triângulo retângulo $OMB$.`,
       answer:examRaw`$BC=8\sqrt3\,\mathrm{cm}$.`,
       steps:[examRaw`No triângulo retângulo $OMB$, a hipotenusa é $OB=R=8$ e um cateto é $OM=4$.`,examRaw`Por Pitágoras, $MB^2=8^2-4^2=48$, então $MB=4\sqrt3\,\mathrm{cm}$.`,examRaw`Como $M$ é o ponto médio, $BC=2MB=8\sqrt3\,\mathrm{cm}$.`],
       rubric:'0,25 pela aplicação de Pitágoras; 0,25 pela simplificação e por dobrar MB.'}
    ],
    pitfall:'O segmento MB é metade do lado. O apótema é 4 cm, enquanto o raio externo é 8 cm.',
    sources:[['poligonos.html#title-20','Polígonos · 20: apótema do triângulo'],['poligonos.html#title-31','Polígonos · 31: raio, lado e apótema'],['poligonos.html#title-55','Apótema e lado · 55: apótema inteiro']]
  },
  {
    id:4,subject:'Álgebra',title:'Função e inequação exponencial',points:1.25,
    prompt:examRaw`Considere os números reais como universo. No item (a), use a função $f:\mathbb R\to\mathbb R$, definida por $f(x)=2^x-8$.`,
    parts:[
      {label:'a.i',points:0.25,level:'Básico',prompt:examRaw`Determine os valores de $x$ para os quais $f(x)=0$.`,
       answer:examRaw`$S=\{3\}$.`,
       steps:[examRaw`De $2^x-8=0$, obtemos $2^x=8=2^3$.`,examRaw`A função de base 2 é estritamente crescente; potências iguais têm expoentes iguais. Logo, $x=3$.`],
       rubric:'0,25 pela redução à mesma base e pela solução.'},
      {label:'a.ii',points:0.25,level:'Intermediário',prompt:examRaw`Determine os valores de $x$ para os quais $f(x)\leq0$, justificando pela monotonicidade.`,
       answer:examRaw`$S=(-\infty,3]$.`,
       steps:[examRaw`A desigualdade equivale a $2^x\leq8=2^3$.`,examRaw`Como a base 2 é maior que 1, a função é crescente e a ordem se mantém: $x\leq3$. O ponto 3 está incluído.`],
       rubric:'0,25 pelo intervalo correto e pela justificativa de crescimento.'},
      {label:'b',points:0.75,level:'Avançado',prompt:examRaw`Resolva $\displaystyle\frac{4^x-10\cdot2^x+16}{2^x-4}\geq0$, indicando a restrição de domínio e o estudo de sinais.`,
       answer:examRaw`$S=[1,2)\cup[3,+\infty)$.`,
       steps:[examRaw`O denominador não pode ser zero: $2^x\ne4$, portanto $x\ne2$. Faça $t=2^x>0$; assim, $4^x=t^2$.`,examRaw`Fatore: $t^2-10t+16=(t-2)(t-8)$. A inequação passa a ser $\dfrac{(t-2)(t-8)}{t-4}\geq0$, com $t>0$ e $t\ne4$.`,examRaw`Nos intervalos $(0,2)$, $(2,4)$, $(4,8)$ e $(8,+\infty)$, o quociente tem sinais, respectivamente, $-$, $+$, $-$ e $+$.`,examRaw`Os zeros do numerador, 2 e 8, são incluídos; 4 é excluído. Logo, $t\in[2,4)\cup[8,+\infty)$.`,examRaw`Como $2^x$ é crescente, $2\leq2^x<4$ equivale a $1\leq x<2$, e $2^x\geq8$ equivale a $x\geq3$. Assim, $S=[1,2)\cup[3,+\infty)$.`],
       rubric:'0,25 pelo domínio e substituição; 0,25 pela fatoração e sinais; 0,25 pelo conjunto solução em x.'}
    ],
    pitfall:'Não multiplique uma inequação pelo denominador sem conhecer seu sinal. O valor x = 2 fica excluído, mesmo com ≥ no enunciado.',
    sources:[['exponenciais-logaritmos.html#title-8','Exponenciais · 8: translação da função'],['exponenciais-logaritmos.html#title-11','Exponenciais · 11: mesma base'],['exponenciais-logaritmos.html#title-20','Exponenciais · 20: substituição por 2ˣ'],['equacoes-segundo-grau.html','Equações e inequações · estudo de sinais de quocientes']]
  },
  {
    id:5,subject:'Álgebra',title:'Sinal e mudança de base',points:1.25,
    prompt:'Resolva as inequações em ℝ. Apresente o conjunto solução e justifique cada resposta.',
    parts:[
      {label:'a',points:0.5,level:'Básico',prompt:examRaw`$3^{2x}-6\cdot3^x+9<0$.`,
       answer:examRaw`$S=\varnothing$.`,
       steps:[examRaw`Como $3^{2x}=(3^x)^2$, o lado esquerdo é o quadrado perfeito $(3^x-3)^2$.`,examRaw`O quadrado de um número real é sempre não negativo. Portanto, não pode ser estritamente menor que zero.`,examRaw`Em $x=1$, a expressão vale zero, mas a desigualdade é estrita. Logo, $S=\varnothing$.`],
       rubric:'0,25 por reconhecer o quadrado perfeito; 0,25 pela justificativa do conjunto vazio.'},
      {label:'b',points:0.75,level:'Intermediário',prompt:examRaw`$\displaystyle\left(\frac14\right)^{x-1}\geq8^{x+1}$.`,
       answer:examRaw`$S=\left(-\infty,-\frac15\right]$.`,
       steps:[examRaw`Escreva as bases como potências de 2: $1/4=2^{-2}$ e $8=2^3$.`,examRaw`Assim, $2^{-2(x-1)}\geq2^{3(x+1)}$. Como a base 2 é maior que 1, $-2x+2\geq3x+3$.`,examRaw`Reorganize: $-5x\geq1$. Ao dividir por $-5$, inverta a desigualdade: $x\leq-1/5$.`,examRaw`O extremo está incluído, pois a igualdade é permitida. Logo, $S=(-\infty,-1/5]$.`],
       rubric:'0,25 pela base comum; 0,25 pela comparação dos expoentes; 0,25 pelo intervalo com extremo incluído.'}
    ],
    pitfall:'Em (a), uma raiz da expressão não satisfaz a desigualdade estrita. Em (b), preserve os parênteses dos expoentes e inverta o sinal ao dividir por um número negativo.',
    sources:[['exponenciais-logaritmos.html#title-15','Exponenciais · 15: substituição'],['exponenciais-logaritmos.html#title-14','Exponenciais · 14: base fracionária'],['exponenciais-logaritmos.html#title-18','Exponenciais · 18: base entre zero e um'],['exponenciais-logaritmos.html#title-19','Exponenciais · 19: desigualdade com várias etapas']]
  }
];

const examCalibration = [
 ['1a','Lei dos cossenos e cálculo de lado','Relação entre apótema, lado e perímetro','Intermediário','0,50'],
 ['1b','Lei dos senos e ângulos relacionados','Raio comum e lado do quadrado inscrito','Intermediário','0,50'],
 ['2a','Lado de um quadrado dentro de um octógono','Lado do octógono por construção e Pitágoras','Avançado','0,50'],
 ['2b','Diagonal a partir do lado já calculado','Perímetro a partir do lado já calculado','Básico','0,25'],
 ['3a','Pitágoras em um triângulo retângulo','Relação direta entre raios do triângulo equilátero','Básico','0,25'],
 ['3b','Uso da lei dos senos com a medida anterior','Pitágoras e recuperação do lado completo','Intermediário','0,50'],
 ['4a.i','Zeros de uma função quadrática','Zero de uma função exponencial transladada','Básico','0,25'],
 ['4a.ii','Sinal da função quadrática','Sinal e monotonicidade da função exponencial','Intermediário','0,25'],
 ['4b','Inequação racional: domínio e sinais','Inequação exponencial racional: substituição, domínio e sinais','Avançado','0,75'],
 ['5a','Quadrado perfeito estritamente negativo','Quadrado perfeito em 3ˣ estritamente negativo','Básico','0,50'],
 ['5b','Quociente com denominador sempre positivo','Potências de bases diferentes e inequação linear','Intermediário','0,75']
];
