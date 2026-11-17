"""Conteúdo das duas listas enviadas em 17/11/2026. Não publicar as fotos."""

GEOMETRY = []
MATH = []


def geo(n, title, topic, prompt, steps, answer, pitfall, choices=None, note=None):
    GEOMETRY.append(dict(id=f'geo-{n:02}', number=n, title=title, topic=topic,
                        prompt=prompt, steps=steps, answer=answer, pitfall=pitfall,
                        choices=choices or [], note=note, figure=f'geo-{n:02}'))


def math(n, title, topic, prompt, steps, answer, pitfall, choices, figure=None, note=None):
    MATH.append(dict(id=f'mat-{n:02}', number=n, title=title, topic=topic,
                    prompt=prompt, steps=steps, answer=answer, pitfall=pitfall,
                    choices=choices, note=note, figure=figure))


geo(1, 'Entre quatro círculos', 'Diferença de áreas',
    r'Quatro círculos de raio unitário, cujos centros são os vértices de um quadrado, são tangentes exteriormente. Determine a área da região central sombreada, em unidades de área.',
    [r'A distância entre os centros de dois círculos tangentes é a soma dos raios: $1+1=2$. Esse é o lado do quadrado dos centros.',
     r'A área desse quadrado é $2^2=4$. Dentro dele aparecem quatro quartos de círculo de raio 1.',
     r'Os quatro quartos equivalem a um círculo inteiro: $4\cdot\frac{\pi\cdot1^2}{4}=\pi$.',
     r'Subtraia os setores: $A=4-\pi$. Alternativa D.'],
    r'$4-\pi$ (D).', r'O quadrado relevante liga os centros dos círculos; seu lado é 2, e não 4.',
    [r'$2\sqrt3-\pi$', r'$3\sqrt2-\pi$', r'$\pi/2$', r'$4-\pi$', r'$5-\pi$'])

geo(2, 'Segmento circular de 60°', 'Setores e segmentos',
    r'Um setor circular tem ângulo central de $60^\circ$ e raio de $2$ cm. Calcule a área do segmento circular destacado, limitado pela corda e pelo arco.',
    [r'O setor ocupa $60/360=1/6$ do círculo. Logo $A_s=\frac16\pi\cdot2^2=\frac{2\pi}{3}$.',
     r'Os dois raios medem 2 e formam $60^\circ$. O triângulo entre eles e a corda é equilátero de lado 2.',
     r'A área do triângulo é $A_t=\frac{2^2\sqrt3}{4}=\sqrt3$.',
     r'O segmento circular é setor menos triângulo: $A=\frac{2\pi}{3}-\sqrt3$ cm².'],
    r'$\left(\dfrac{2\pi}{3}-\sqrt3\right)\,\mathrm{cm}^2$.',
    r'Setor circular inclui o triângulo. A região entre a corda e o arco é apenas o segmento circular.')

geo(3, 'Quatro discos recortados', 'Diferença de áreas',
    r'De uma chapa quadrada de papelão recortam-se quatro discos iguais, dispostos em duas linhas e duas colunas, tangentes entre si e aos lados da chapa. Cada círculo tem diâmetro de $10$ cm. Qual é a área não aproveitada da chapa, em cm²?',
    [r'O lado da chapa contém dois diâmetros: $L=10+10=20$ cm. Sua área é $20^2=400$ cm².',
     r'O raio de cada disco é $10/2=5$ cm, e sua área é $25\pi$ cm².',
     r'Os quatro discos ocupam $4\cdot25\pi=100\pi$ cm².',
     r'A sobra é $400-100\pi$ cm². Alternativa E.'],
    r'$(400-100\pi)\,\mathrm{cm}^2$ (E).', r'Diâmetro 10 significa raio 5. A área dos quatro discos deve ser retirada da área da chapa.',
    [r'$20-5\pi$', r'$40-10\pi$', r'$100-20\pi$', r'$200-50\pi$', r'$400-100\pi$'])

geo(4, 'Triângulo equilátero e círculo tangente', 'Polígonos regulares',
    r'A área do triângulo equilátero $OAB$ é $9\sqrt3$ cm². O círculo tem centro em $O$ e é tangente ao lado $AB$. Determine a área desse círculo, em cm².',
    [r'Para o lado $\ell$ do triângulo, $\frac{\ell^2\sqrt3}{4}=9\sqrt3$. Assim $\ell^2=36$ e $\ell=6$ cm.',
     r'A distância de $O$ à reta $AB$ é a altura do triângulo: $h=\frac{\ell\sqrt3}{2}=3\sqrt3$ cm.',
     r'Como o círculo tem centro em $O$ e tangencia $AB$, seu raio é essa altura: $r=3\sqrt3$.',
     r'$A=\pi r^2=\pi(3\sqrt3)^2=27\pi$ cm². Alternativa A.'],
    r'$27\pi\,\mathrm{cm}^2$ (A).', r'O centro do círculo é o vértice O. O raio é a altura inteira do triângulo, não seu apótema.',
    [r'$27\pi$', r'$32\pi$', r'$36\pi$', r'$42\pi$', r'$48\pi$'])

geo(5, 'Comparando uma coroa circular', 'Coroas e discos',
    r'(PUC) Dados dois discos concêntricos de raios $1$ e $1/2$, a área da coroa circular compreendida entre eles corresponde a qual das alternativas?',
    [r'O disco maior tem área $A_M=\pi\cdot1^2=\pi$. O menor tem área $A_m=\pi(1/2)^2=\pi/4$.',
     r'A coroa tem área $A_c=A_M-A_m=3\pi/4$.',
     r'Comparando com o disco maior, $A_c/A_M=3/4=75\%$. Alternativa B.',
     r'Comparando com o menor, a coroa vale três vezes sua área, pois $(3\pi/4)/(\pi/4)=3$.'],
    r'$75\%$ da área do disco maior (B).', r'A área depende do quadrado do raio. Um raio pela metade produz área igual a um quarto.',
    ['50% da área do disco menor.', '75% da área do disco maior.', 'Igual à área do disco menor.', 'O dobro da área do disco menor.', 'A metade da área do disco menor.'])

geo(6, 'O menor quadrado inscrito', 'Área e função quadrática',
    r'(PUCCAMP) Um quadrado de lado $8$ cm contém outro quadrado com um vértice em cada lado. Esses vértices dividem cada lado externo em segmentos de medidas $x$ e $8-x$, como na figura. Subtraindo os quatro triângulos dos cantos, determine o valor mínimo da área $A(x)$ do quadrado interno.',
    [r'O quadrado externo tem área $8^2=64$ cm². Cada triângulo dos cantos tem catetos $x$ e $8-x$.',
     r'A soma das áreas dos quatro triângulos é $4\cdot\frac{x(8-x)}2=2x(8-x)$.',
     r'$A(x)=64-2x(8-x)=2x^2-16x+64$.',
     r'Complete o quadrado: $A(x)=2(x-4)^2+32$. O termo quadrático é não negativo.',
     r'O mínimo ocorre em $x=4$, permitido pela geometria, e vale $32$ cm². Alternativa D.'],
    r'$32\,\mathrm{cm}^2$, em $x=4$ cm (D).', r'Não minimize separadamente os quatro triângulos: minimizar a área interna equivale a maximizar a área retirada.',
    [r'$16\,\mathrm{cm}^2$', r'$24\,\mathrm{cm}^2$', r'$28\,\mathrm{cm}^2$', r'$32\,\mathrm{cm}^2$', r'$48\,\mathrm{cm}^2$'])

geo(7, 'Coroa de raios 6 e 9', 'Coroas e discos',
    r'Dados dois círculos concêntricos de raios $6$ cm e $9$ cm, calcule a área da coroa circular pintada de cinza, em cm².',
    [r'O raio externo é $R=9$ cm e o interno é $r=6$ cm.',
     r'A área da coroa é a diferença dos discos: $A=\pi R^2-\pi r^2$.',
     r'$A=\pi(9^2-6^2)=\pi(81-36)=45\pi$ cm². Alternativa E.'],
    r'$45\pi\,\mathrm{cm}^2$ (E).', r'$R^2-r^2$ não é igual a $(R-r)^2$. A largura 3 da coroa não é um raio de disco.',
    [r'$225\pi$', r'$117\pi$', r'$81\pi$', r'$54\pi$', r'$45\pi$'])

geo(8, 'Hexágono e dois setores', 'Polígonos regulares',
    r'(UNIRIO) A figura representa um hexágono regular $ABCDEF$. Dois setores circulares, com centros nos vértices opostos $B$ e $E$, têm raio de $4$ cm e passam pelos vértices adjacentes a seus centros. Calcule: a) o apótema do hexágono; b) a área da região sombreada, que resta no hexágono após retirar os dois setores.',
    [r'Cada raio indicado coincide com um lado do hexágono. Logo $\ell=4$ cm.',
     r'a) Ao dividir o hexágono em seis triângulos equiláteros, o apótema é a altura de um deles: $a=\frac{\ell\sqrt3}{2}=2\sqrt3$ cm.',
     r'b) A área do hexágono é $A_h=6\cdot\frac{\ell^2\sqrt3}{4}=24\sqrt3$ cm².',
     r'O ângulo interno de um hexágono regular é $120^\circ$. Cada setor retirado tem área $\frac{120}{360}\pi\cdot4^2=\frac{16\pi}{3}$.',
     r'Os dois setores só se tocam no centro, sem sobreposição de área. Assim $A=24\sqrt3-\frac{32\pi}{3}=\frac{72\sqrt3-32\pi}{3}$ cm².'],
    r'a) $2\sqrt3$ cm; b) $\dfrac{72\sqrt3-32\pi}{3}\,\mathrm{cm}^2$.',
    r'Os setores têm centros nos vértices B e E: seus ângulos são 120°, não os 60° dos triângulos com vértice no centro do hexágono.')

geo(9, 'Duas circunferências de um triângulo', 'Polígonos regulares',
    r'Calcule a área da coroa circular limitada pelas circunferências inscrita e circunscrita a um triângulo equilátero de lado $6$ cm.',
    [r'A altura do triângulo é $h=6\sqrt3/2=3\sqrt3$ cm.',
     r'No triângulo equilátero, o centro comum divide a altura na razão 2:1. Logo $R=2h/3=2\sqrt3$ e $r=h/3=\sqrt3$.',
     r'A coroa tem área $A=\pi(R^2-r^2)=\pi(12-3)=9\pi$ cm². Alternativa C.'],
    r'$9\pi\,\mathrm{cm}^2$ (C).', r'Os raios das duas circunferências não são o lado nem a altura do triângulo.',
    [r'$3\pi\,\mathrm{cm}^2$', r'$6\pi\,\mathrm{cm}^2$', r'$9\pi\,\mathrm{cm}^2$', r'$12\pi\,\mathrm{cm}^2$', r'$15\pi\,\mathrm{cm}^2$'])

geo(10, 'Área a partir do apótema', 'Polígonos regulares',
    r'O raio da circunferência inscrita em um hexágono regular mede $2\sqrt3$ cm. Calcule a área do hexágono.',
    [r'O raio da circunferência inscrita é o apótema: $a=2\sqrt3$ cm.',
     r'Para o hexágono regular, $a=\ell\sqrt3/2$. Então $\ell=2a/\sqrt3=4$ cm.',
     r'O perímetro é $P=6\ell=24$ cm. A área é $A=Pa/2=24\cdot2\sqrt3/2=24\sqrt3$ cm².'],
    r'$24\sqrt3\,\mathrm{cm}^2$.', r'O raio inscrito é o apótema. É o raio circunscrito que coincide com o lado do hexágono.')

geo(11, 'Quatro triângulos, quatro intervalos', 'Setores e segmentos',
    r'A figura mostra um círculo de área $36$ cm² sobre o qual estão desenhados quatro triângulos equiláteros, com um vértice comum no centro do círculo. Determine a área sombreada: a parte do círculo que fica fora dos quatro triângulos, como indicado.',
    [r'Cada triângulo equilátero tem ângulo de $60^\circ$ no centro do círculo.',
     r'Na disposição da figura, os triângulos cobrem quatro setores sem sobreposição, totalizando $4\cdot60^\circ=240^\circ$.',
     r'Os setores sombreados restantes somam $360^\circ-240^\circ=120^\circ$, isto é, um terço do círculo.',
     r'Como a área total do círculo já é $36$ cm², $A=\frac{120}{360}\cdot36=12$ cm².'],
    r'$12\,\mathrm{cm}^2$.', r'O dado é a área do círculo: 36 cm², sem π. Não é necessário calcular o raio nem as áreas inteiras dos triângulos.')

geo(12, 'Círculo inscrito no hexágono', 'Polígonos regulares',
    r'(UFSE) As circunferências $C_1$ e $C_2$ estão, respectivamente, inscrita e circunscrita a um hexágono regular. Se o raio de $C_2$ é $3$ cm, determine a área do círculo limitado por $C_1$, em cm².',
    [r'No hexágono regular, o lado coincide com o raio circunscrito: $\ell=3$ cm.',
     r'O raio inscrito é o apótema: $r=\ell\sqrt3/2=3\sqrt3/2$ cm.',
     r'$A_{C_1}=\pi r^2=\pi\left(\frac{3\sqrt3}{2}\right)^2=\frac{27\pi}{4}$ cm². Alternativa A.'],
    r'$\dfrac{27\pi}{4}\,\mathrm{cm}^2$ (A).', r'Não use o raio 3 diretamente na área do círculo interno: ele pertence ao círculo externo.',
    [r'$\dfrac{27\pi}{4}$', r'$6\pi$', r'$\dfrac{21\pi}{4}$', r'$\dfrac{9\pi}{4}$', r'$\dfrac{5\pi}{4}$'])

geo(13, 'Um círculo dentro do trapézio', 'Diferença de áreas',
    r'(Fatec-SP) Os catetos do triângulo retângulo $ABC$, com ângulo reto em $B$, medem $8$ cm. $N$ e $M$ são os pontos médios de $AC$ e $AB$, respectivamente. A circunferência tangencia os segmentos $MB$, $BC$ e $NM$. Usando $\pi=3{,}1$, calcule a área hachurada: o trapézio $BMNC$ menos o disco.',
    [r'Como M e N são pontos médios, $MN$ é paralelo a $BC$ e mede metade dele: $MN=4$ cm. Também $BM=4$ cm.',
     r'O trapézio tem bases 8 e 4, e altura 4: $A_t=\frac{(8+4)\cdot4}{2}=24$ cm².',
     r'O círculo tangencia as bases paralelas BC e MN, separadas por 4 cm. Portanto seu diâmetro é 4 e seu raio é 2 cm.',
     r'Com a aproximação pedida, $A_c=3{,}1\cdot2^2=12{,}4$ cm².',
     r'A região hachurada mede $24-12{,}4=11{,}6$ cm². Alternativa A.'],
    r'$11{,}6\,\mathrm{cm}^2$ (A), usando $\pi=3{,}1$.',
    r'A região externa ao disco é um trapézio, não o triângulo ABC inteiro. O círculo não precisa tangenciar a hipotenusa AC.',
    [r'$11{,}6$', r'$11{,}8$', r'$12{,}4$', r'$24{,}2$', r'$37{,}6$'])

geo(14, 'Triângulo e semicírculo', 'Composição de áreas',
    r'A figura é formada por um triângulo retângulo de hipotenusa $5$ cm e um cateto de $3$ cm, unido a um semicírculo cujo diâmetro coincide com o outro cateto. Calcule a área total.',
    [r'Pelo teorema de Pitágoras, o cateto desconhecido satisfaz $d^2+3^2=5^2$. Portanto $d=4$ cm.',
     r'A área do triângulo é $A_t=4\cdot3/2=6$ cm².',
     r'O semicírculo tem diâmetro 4 e raio 2. Sua área é $A_s=\pi\cdot2^2/2=2\pi$ cm².',
     r'As duas regiões só compartilham a borda. Logo $A=6+2\pi$ cm².'],
    r'$(6+2\pi)\,\mathrm{cm}^2$.', r'O cateto de 4 cm é o diâmetro do semicírculo, não seu raio. Aqui as áreas são somadas.')

geo(15, 'Um disco retirado de outro', 'Coroas e discos',
    r'O diâmetro da circunferência menor é igual ao raio da circunferência maior. Calcule a área assinalada — o disco maior menos o menor — sabendo que o diâmetro da circunferência maior é $24$ cm. Os círculos são tangentes internamente, como na figura.',
    [r'O raio maior é $R=24/2=12$ cm.',
     r'O diâmetro menor vale 12 cm; por isso, seu raio é $r=12/2=6$ cm.',
     r'A área restante é $A=\pi(R^2-r^2)=\pi(144-36)=108\pi$ cm².',
     r'Os centros são distintos, mas o disco menor está totalmente contido no maior. Isso permite subtrair suas áreas.'],
    r'$108\pi\,\mathrm{cm}^2$.', r'A igualdade dada relaciona o diâmetro menor ao raio maior. Os dois raios não são iguais.')

geo(16, 'A área preta do logotipo', 'Setores e segmentos',
    r'(VUNESP) Uma empresa tem o logotipo da figura, formado por um quadrado e sua circunferência inscrita, de raio $3$ cm. As retas desenhadas são as diagonais e os segmentos que unem os pontos médios de lados opostos. Determine a área total pintada de preto, em cm².',
    [r'O lado do quadrado é o diâmetro do círculo: 6 cm. Assim $A_q=36$ e $A_c=9\pi$.',
     r'Nos quatro cantos, cada diagonal divide a região externa ao círculo em duas partes iguais. Está pintada metade de cada canto, totalizando $(36-9\pi)/2$.',
     r'Dentro do círculo estão pintados dois setores de $45^\circ$ cada. Juntos, ocupam $90^\circ$, ou um quarto do círculo: $9\pi/4$.',
     r'Some as partes sem sobreposição: $A=\frac{36-9\pi}{2}+\frac{9\pi}{4}=18-\frac{9\pi}{4}$ cm². Alternativa B.'],
    r'$\left(18-\dfrac{9\pi}{4}\right)\,\mathrm{cm}^2$ (B).',
    r'Separe as partes pretas dentro e fora do círculo. A figura não pinta metade do círculo.',
    [r'$9-\dfrac{9\pi}{4}$', r'$18-\dfrac{9\pi}{4}$', r'$18-\dfrac{9\pi}{2}$', r'$36-\dfrac{9\pi}{4}$', r'$36-\dfrac{9\pi}{2}$'])

geo(17, 'Semicírculo cortado pela diagonal', 'Composição de áreas',
    r'Na figura há um quadrado de lado $4$, uma de suas diagonais e uma semicircunferência de raio $2$, cujo diâmetro é o lado inferior do quadrado. Determine a área hachurada: a região dentro do semicírculo e abaixo da diagonal.',
    [r'Considere o vértice inferior esquerdo como $(0,0)$. A diagonal é $y=x$; o círculo tem centro $(2,0)$ e equação $(x-2)^2+y^2=4$.',
     r'Nas interseções, $(x-2)^2+x^2=4$, isto é, $2x(x-2)=0$. Além de $(0,0)$, o encontro é $(2,2)$, o topo do semicírculo.',
     r'À esquerda desse encontro, a região sombreada é um triângulo retângulo de catetos 2 e 2: área $2\cdot2/2=2$.',
     r'À direita, a região é um quarto de círculo de raio 2: área $\pi\cdot2^2/4=\pi$.',
     r'Somando, $A=2+\pi$ unidades de área. Alternativa B.'],
    r'$\pi+2$ (B).', r'Não some o semicírculo inteiro ao triângulo: a metade esquerda do semicírculo foi recortada pela diagonal.',
    [r'$\dfrac{\pi}{2}+2$', r'$\pi+2$', r'$\pi+3$', r'$\pi+4$', r'$2\pi+1$'])


math(1, 'A cota final da excursão', 'Equações e problemas',
     'Um grupo de 40 estudantes organizou uma excursão, com orçamento inicialmente dividido em cotas iguais. A despesa final ficou R$ 520,00 acima do orçamento e mais 8 estudantes entraram no grupo. A divisão final foi feita igualmente entre os 48 participantes. Cada estudante do grupo inicial pagou R$ 5,00 além da cota inicial. Qual foi a cota final por participante?',
     [r'Seja $c$ a cota inicial, em reais. O orçamento inicial era $40c$.',
      r'A cota final é $c+5$ e há 48 participantes. Portanto $48(c+5)=40c+520$.',
      r'Desenvolva: $48c+240=40c+520$. Logo $8c=280$ e $c=35$.',
      r'A pergunta pede a cota final: $c+5=40$ reais. Alternativa D.',
      r'Conferência: o orçamento era $40\cdot35=1400$ reais e a despesa foi $48\cdot40=1920$ reais, diferença de 520 reais.'],
     'R$ 40,00 (D).', 'O valor 35 é a cota inicial. Some os 5 reais para responder à pergunta.',
     ['R$ 25,00', 'R$ 30,00', 'R$ 35,00', 'R$ 40,00', 'R$ 45,00'])

math(2, 'Raízes sem usar a fórmula de Bhaskara', 'Função quadrática',
     r'Se $m$ e $n$ são as raízes da equação $2x^2+6x-8=0$, determine o valor de $(m+5)(n+5)$.',
     [r'Pelas relações entre coeficientes e raízes, $m+n=-6/2=-3$ e $mn=-8/2=-4$.',
      r'Expanda a expressão: $(m+5)(n+5)=mn+5(m+n)+25$.',
      r'Substitua: $-4+5(-3)+25=6$. Alternativa A.',
      r'Conferência opcional: as raízes são 1 e −4; assim $(1+5)(-4+5)=6\cdot1=6$.'],
     r'$6$ (A).', r'Preserve os sinais: a soma é $-b/a$ e o produto é $c/a$.',
     [r'$6$', r'$10$', r'$15$', r'$20$', r'$24$'])

math(3, 'Esferas e nível da água', 'Função afim',
     r'Um experimento relaciona o número $x$ de esferas colocadas em um recipiente ao nível $y$ da água, em centímetros. O nível varia linearmente. Para 4 esferas, mediram-se 5,4 cm; para 8 esferas, 5,8 cm; para 12 esferas, 6,2 cm. Qual expressão representa essa relação?',
     [r'Escreva $y=ax+b$. A taxa de variação é $a=(5{,}8-5{,}4)/(8-4)=0{,}4/4=0{,}1$ cm por esfera.',
      r'Use o ponto $(4;5{,}4)$: $5{,}4=0{,}1\cdot4+b$, logo $b=5$.',
      r'A função é $y=0{,}1x+5$. Alternativa A.',
      r'Confira o terceiro dado: $0{,}1\cdot12+5=6{,}2$ cm.'],
     r'$y=0{,}1x+5$ (A).', r'A subida de 0,4 cm corresponde a quatro esferas. Divida por 4 para obter o coeficiente de x.',
     [r'$y=0{,}1x+5$', r'$y=0{,}4x+5$', r'$y=0{,}1x+5{,}4$', r'$y=x+1{,}4$', r'$y=5x+0{,}1$'])

math(4, 'Uma parábola entre dois instantes', 'Função quadrática',
     r'Um objeto é lançado do solo e descreve trajetória parabólica. Ele retorna ao solo 6 segundos após o lançamento e atinge altura máxima de 45 metros. Qual é a função da altura $h$, em metros, em função do tempo $t$, em segundos, para $0\le t\le6$?',
     [r'Os zeros são $t=0$ e $t=6$, então a altura pode ser escrita como $h(t)=k\,t(t-6)$.',
      r'O vértice fica no ponto médio das raízes: $t_v=(0+6)/2=3$ s.',
      r'Como $h(3)=45$, temos $k\cdot3\cdot(-3)=45$. Logo $k=-5$.',
      r'$h(t)=-5t(t-6)=-5t^2+30t$. Alternativa D.',
      r'A concavidade é para baixo, $h(0)=h(6)=0$ e $h(3)=45$, como pedido.'],
     r'$h(t)=-5t^2+30t$, para $0\le t\le6$ (D).', r'O máximo ocorre em 3 segundos. Não substitua o instante de retorno, 6 segundos, no lugar do instante do vértice.',
     [r'$h(t)=-5t^2+15t$', r'$h(t)=-10t^2+60t$', r'$h(t)=5t^2-30t$', r'$h(t)=-5t^2+30t$', r'$h(t)=-t^2+6t$'])

math(5, 'Sinais de um produto', 'Inequações',
     r'Os gráficos representam $f(x)=(x+2)(x-3)$ e $g(x)=x$. No intervalo $[-4,5]$, determine o conjunto solução de $f(x)\cdot g(x)<0$.',
     [r'O produto é $x(x+2)(x-3)$. Seus zeros são $-2$, $0$ e $3$.',
      r'Em $x<-2$, os três fatores são negativos e o produto é negativo. Em $-2<x<0$, há dois fatores negativos e o produto é positivo.',
      r'Em $0<x<3$, só $x-3$ é negativo, então o produto é negativo. Em $x>3$, todos os fatores são positivos.',
      r'A desigualdade é estrita: exclua os zeros $-2$, 0 e 3. A solução real é $(-\infty,-2)\cup(0,3)$.',
      r'Interseccione com o intervalo solicitado $[-4,5]$: $[-4,-2)\cup(0,3)$. O extremo $-4$ entra, pois o produto ali é negativo. Alternativa B.'],
     r'$[-4,-2)\cup(0,3)$ (B).', r'Ser menor que zero exige fatores de sinais opostos. Não basta olhar onde a parábola é negativa; é preciso considerar também o sinal de x.',
     [r'$(-2,0)\cup(3,5]$', r'$[-4,-2)\cup(0,3)$', r'$[-4,0)$', r'$(-2,3)$', r'$[-4,-2]\cup[0,3]$'], 'mat-05')

math(6, 'O limite de uma cultura', 'Exponenciais',
     r'Uma cultura inicia com 1 500 bactérias e dobra a cada hora. Seu crescimento é descrito por $N(t)=1500\cdot2^t$, com $t\ge0$ em horas. Um tratamento deve ser aplicado enquanto a população for, no máximo, 384 000 bactérias. Qual é o tempo máximo após o início da cultura para aplicar o tratamento?',
     [r'Precisamos de $1500\cdot2^t\le384000$. Dividindo por 1500, $2^t\le256$.',
      r'Como $256=2^8$ e a base 2 é maior que 1, a função é crescente: $t\le8$.',
      r'Juntando com $t\ge0$, temos $0\le t\le8$. O tempo máximo é 8 horas. Alternativa C.'],
     '8 horas (C).', r'“No máximo” inclui a igualdade. No instante 8 h, a população é exatamente 384 000.',
     ['6 horas', '7 horas', '8 horas', '9 horas', '10 horas'])

math(7, 'Igualdade entre potências', 'Exponenciais',
     r'Considere $f(x)=2^{x^2-9}$ e $g(x)=4^{x^2-3x}$. Se $f(x)=g(x)$, qual é o valor de $2^x$?',
     [r'Escreva a segunda função na base 2: $g(x)=(2^2)^{x^2-3x}=2^{2x^2-6x}$.',
      r'A função exponencial de base 2 é injetiva. Assim $x^2-9=2x^2-6x$.',
      r'Reorganize: $x^2-6x+9=0$, ou $(x-3)^2=0$. A única solução é $x=3$.',
      r'A pergunta pede $2^x$, portanto $2^3=8$. Alternativa D.',
      r'Conferência: $f(3)=2^0=1$ e $g(3)=4^0=1$.'],
     r'$2^x=8$ (D).', r'Converter a base 4 em base 2 multiplica todo o expoente por 2. O valor pedido não é x.',
     [r'$2$', r'$4$', r'$6$', r'$8$', r'$16$'],
     note=r'A folha repete o fragmento “g(x) = 4” logo após $4^{x^2-3x}$. Ele foi tratado como duplicação de impressão. A resolução usa as duas definições completas acima; interpretar o fragmento como uma condição adicional tornaria o enunciado incompatível, pois na solução $g(3)=1$.')

math(8, 'A base escondida no gráfico', 'Logaritmos',
     r'O gráfico de $y=\log_a(x+b)$, com $a>1$, passa pela origem e pelo ponto $(a/2,1)$. O retângulo destacado tem lados paralelos aos eixos, com vértices opostos em $(0,0)$ e $(a/2,1)$. Qual é sua área, em unidades de área?',
     [r'Passar pela origem significa $0=\log_a b$. Pela definição, $b=a^0=1$.',
      r'No ponto $(a/2,1)$, $1=\log_a(a/2+1)$. Logo $a/2+1=a$.',
      r'Daí $1=a/2$ e $a=2$, satisfazendo $a>1$.',
      r'O retângulo tem base $a/2=1$ e altura 1. Sua área é $1\cdot1=1$. Alternativa B.',
      r'A função encontrada é $y=\log_2(x+1)$, definida para $x>-1$, e passa pelos dois pontos dados.'],
     r'$1$ unidade de área (B).', r'Use os dois pontos para encontrar b e a. A coordenada horizontal do vértice é a/2, não a.',
     [r'$1/2$', r'$1$', r'$3/2$', r'$2$', r'$4$'], 'mat-08')

math(9, 'Trinta pontos a menos', 'Logaritmos',
     r'A pontuação de uma pessoa em um teste de memória, $t$ meses após a avaliação inicial, é modelada por $P(t)=90-15\log(t+1)$, para $t\ge0$. Depois de quantos meses a pontuação terá diminuído 30 pontos em relação ao valor inicial? Considere o logaritmo decimal.',
     [r'Na avaliação inicial, $P(0)=90-15\log1=90$.',
      r'Uma diminuição de 30 pontos significa pontuação final $90-30=60$. Então $90-15\log(t+1)=60$.',
      r'Isole o logaritmo: $15\log(t+1)=30$, logo $\log(t+1)=2$.',
      r'Pela definição na base 10, $t+1=10^2=100$. Portanto $t=99$ meses, no domínio $t\ge0$. Alternativa E.'],
     '99 meses (E).', r'Diminuir 30 pontos não significa terminar com 30 pontos. O valor final é 60.',
     ['9 meses', '19 meses', '30 meses', '90 meses', '99 meses'])

PAGES = [
    dict(slug='areas-figuras-planas-lista-11', label='Áreas planas · Lista 11', title='Áreas de figuras planas',
         subtitle='Lista 11 · 17 exercícios', intro='Círculos, setores e polígonos. Leia a figura, escolha as áreas que entram na conta e acompanhe cada etapa da resolução.',
         description='17 exercícios da Lista 11 de 2026, com figuras redesenhadas, soluções passo a passo e gabarito conferido.',
         guide='Primeiro, identifique a região.',
         guidance='Separe os dados em raios, diâmetros, lados e alturas. Decida quais áreas devem ser somadas e quais devem ser retiradas. Mantenha π e as raízes exatos, exceto quando o enunciado pedir uma aproximação.',
         formulas=[('Círculo e coroa', r'$A=\pi r^2$; $A_c=\pi(R^2-r^2)$'),
                   ('Setor circular', r'$A_s=\dfrac{\theta}{360^\circ}\pi r^2$'),
                   ('Triângulo equilátero', r'$A_t=\dfrac{\ell^2\sqrt3}{4}$; $h=\dfrac{\ell\sqrt3}{2}$'),
                   ('Polígono regular', r'$A=\dfrac{P\cdot a}{2}$, com perímetro $P$ e apótema $a$.')],
         items=GEOMETRY),
    dict(slug='matematica-revisao-17-novembro', label='Matemática · Revisão de 17/11', title='Revisão de matemática',
         subtitle='9 exercícios · Álgebra e funções', intro='Do orçamento da excursão aos logaritmos. Organize os dados, resolva e confira o que a pergunta pede ao final.',
         description='9 exercícios de revisão de matemática, com equações, funções, inequações, exponenciais e logaritmos resolvidos em LaTeX.',
         guide='Uma linha de raciocínio por vez.',
         guidance='Tente resolver no papel antes de abrir a solução. Nomeie a incógnita, observe o domínio e confira a resposta no enunciado. Nas inequações, decida com cuidado quais extremos entram no conjunto solução.',
         formulas=[('Raízes de uma quadrática', r'$m+n=-\dfrac ba$; $mn=\dfrac ca$'),
                   ('Função afim', r'$y=ax+b$; $a=\dfrac{\Delta y}{\Delta x}$'),
                   ('Potências', r'$(a^m)^n=a^{mn}$; use uma base comum.'),
                   ('Logaritmos', r'$\log_a u=v\iff a^v=u$, com $u>0$, $a>0$, $a\ne1$.')],
         items=MATH)
]
