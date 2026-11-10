T=[]
def w(prompt,answer,*steps): return dict(title='Aquecimento',prompt=prompt,answer=answer,steps=list(steps),kind='warmup')
def t(id,title,idea,method,formula,focus,example,visual,warmups,link):
 T.append(dict(id=id,title=title,discipline={'m':'Matemática','p':'Física','q':'Química'}[id[0]],idea=idea,method=method,formula=formula,focus=focus,example=example,visual=visual,warmups=warmups,link=link))
t('m01','Números, potências, raízes e notação científica',
 r'Uma potência conta fatores iguais; uma raiz desfaz uma potência. $2^3=8$ e $\sqrt[3]8=2$. Expoente negativo pede o inverso, não um resultado negativo. Uma dízima periódica é uma fração exata: se $u=0{,}666\ldots$, subtrair u de 10u dá $9u=6$.',
 r'Faça primeiro potências e raízes, depois produtos e divisões, e por último somas. Reescreva decimais como frações. Para somar números em notação científica, iguale as potências de 10; para multiplicar, multiplique coeficientes e some expoentes. Só arredonde ao final.',
 r'$a^{-n}=1/a^n$; $a^{p/q}=\sqrt[q]{a^p}$ (a>0); $\sqrt{x^2}=|x|$; $a^ma^n=a^{m+n}$.',
 'Reforçar inverso, raiz principal e contagem das casas decimais. O operador # foi bem resolvido: use a mesma disciplina de seguir regras.',17,'powers',[
 w(r'Calcule $(1/4)^{-3/2}$.','8.',r'$1/4=2^{-2}$; $(-2)(-3/2)=3$; $2^3=8$.'),
 w(r'Simplifique $\sqrt{72}+\sqrt{8}$ e $\sqrt[3]{24}$.',r'$8\sqrt2$ e $2\sqrt[3]3$.',r'$\sqrt{72}=6\sqrt2$ e $\sqrt8=2\sqrt2$. Para raiz cúbica, retire o fator $8=2^3$.'),
 w(r'Converta 0,0045 g para mg e escreva em notação científica. Calcule $0{,}333\ldots+1/6$.',r'4,5 mg; $4{,}5\cdot10^{-3}$ g; 1/2.',r'$1$ g = $1000$ mg. A dízima vale 1/3; $1/3+1/6=1/2$.')],'index.html')
t('m02','Produtos notáveis, fatoração e frações algébricas',
 r'Desenhar um quadrado de lado a+b revela quatro regiões: $a^2$, ab, ab e $b^2$. Por isso o termo 2ab não pode desaparecer. Fatorar faz o caminho inverso: troca uma soma por um produto para tornar visíveis os fatores comuns.',
 r'Antes de simplificar uma fração, registre onde o denominador é zero. Depois fatore. Cancelar significa dividir numerador e denominador pelo mesmo fator não nulo. Não é permitido cancelar parcelas separadas por + ou −. No cubo, os coeficientes são 1,3,3,1.',
 r'$(a+b)^2=a^2+2ab+b^2$; $a^2-b^2=(a-b)(a+b)$; $(a+b)^3=a^3+3a^2b+3ab^2+b^3$.',
 'Prioridade: diferença de quadrados, termos mistos e cancelamento por fatores. Releia também o que a pergunta pede após achar a expressão.',5,'square',[
 w(r'Calcule $101^2-100^2$ sem elevar os números ao quadrado.','201.',r'$(101-100)(101+100)=201$.'),
 w(r'Simplifique $(x^2-9)/(x^2-3x)$, indicando restrições.',r'$(x+3)/x$, com $x\ne0,3$.',r'Fatore: $(x-3)(x+3)/[x(x-3)]$. Cancele x−3; preserve as restrições originais.'),
 w(r'Se $x+1/x=4$, calcule $x^2+1/x^2$.','14.',r'Eleve a soma: $16=x^2+2+1/x^2$; subtraia 2.')],'index.html')
t('m03','Conjuntos, Venn e contagem',
 'A interseção reúne quem pertence aos dois conjuntos; a união reúne quem pertence a pelo menos um. Somar os totais dos conjuntos conta quem está na interseção duas vezes. No desenho, cada pessoa deve ocupar exatamente uma região.',
 'Comece pelo centro do diagrama. Em três conjuntos, retire a interseção tripla dos números das interseções aos pares antes de preencher essas regiões. Só depois calcule as regiões exclusivas e os que estão fora. Confira a soma de todas as regiões.',
 r'$|A\cup B|=|A|+|B|-|A\cap B|$. Para três conjuntos: somar individuais, subtrair pares, somar o triplo.',
 'Prioridade: distinguir total de um conjunto e região exclusiva. Operações de diferença já apareceram corretas, mas o diagrama e a soma final precisam de revisão.',1,'venn',[
 w('Em 50 alunos, 30 estudam inglês, 25 espanhol e 10 ambos. Quantos estudam pelo menos uma língua e quantos nenhuma?','45 e 5.','União = 30+25−10=45. Fora = 50−45=5.'),
 w('A={1,2,3,4} e B={3,4,5}. Calcule A∩B e A−B.','{3,4} e {1,2}.','A∩B mantém os comuns; A−B mantém só os elementos de A que não estão em B.'),
 w('Em três conjuntos, 12 pertencem a A∩B, e 5 pertencem aos três. Quantos pertencem a A e B, mas não a C?','7.','A interseção A∩B inclui o centro; subtraia 5 de 12.')],'index.html')
t('m04','Razões, porcentagens e proporcionalidade',
 'Uma razão compara grandezas e suas unidades. Uma eficiência de 15 km/L informa quantos quilômetros cabem em cada litro: distância dividida pela eficiência dá litros. Em divisão direta, maior peso recebe maior parte; na inversa, use os recíprocos dos pesos.',
 'Transforme porcentagens em fatores: 70% = 0,70; aumento de 20% multiplica por 1,20. Se 56% não é absorvido, a fração absorvida é 44%. Para recuperar o total a partir de uma parte, divida pelo fator. Em dinheiro, mantenha colunas distintas para custo, receita e saldo.',
 r'$\text{parte}=p\cdot\text{total}$; divisão direta em $a:b$; inversa em $1/a:1/b$.',
 'A divisão direta e os ângulos em proporção inversa tiveram acertos; aplicar o mesmo método e conferir a soma ajuda a evitar os erros de outros contextos.',2,'ratio',[
 w('Divida 180 diretamente em 2:3 e inversamente a 2 e 3.','Direta: 72 e 108. Inversa: 108 e 72.','Direta: 180/5=36 por parte. Inversa: 1/2:1/3=3:2.'),
 w('44% de uma massa são 22 g. Qual é a massa total?','50 g.','0,44M=22, então M=22/0,44=50.'),
 w('Um carro rende 12 km/L. Quanto consome em 90 km? Qual a autonomia com 40 L?','7,5 L e 480 km.','90 km ÷ 12 km/L = 7,5 L; 40 L × 12 km/L = 480 km.')],'conversao-unidades.html')
t('m05','Equações, sistemas e tradução do enunciado',
 'Uma variável deve ter um significado antes de entrar na conta: número de notas, valor em reais ou tempo. São coisas diferentes. Uma equação funciona como balança; operar igualmente nos dois lados preserva a igualdade.',
 'Escreva uma frase para cada equação. Em um sistema, use substituição ou eliminação para combinar as informações. No final, substitua os valores encontrados em todas as condições e confira se atendem à realidade: quantidades inteiras, tempos positivos e totais corretos. Para operadores novos, use exatamente a regra fornecida.',
 r'$x+y=N$ e $ax+by=V$: contagem de objetos e valor total são duas equações diferentes.',
 'Prioridade: definir variáveis e distinguir quantidade de valor. Resolver a equação não basta se ela não representa o problema.',47,'balance',[
 w('Há 12 ingressos de R$ 10 ou R$ 20, totalizando R$ 190. Quantos de cada?','5 de R$ 10 e 7 de R$ 20.','x+y=12; 10x+20y=190. Subtraia 10(x+y)=120: 10y=70.'),
 w('Resolva 3(x−2)=2x+5.','x=11.','3x−6=2x+5; x=11. Confira: 27=27.'),
 w('Defina a★b=2a−b. Calcule (3★1)★4 e 3★(1★4).','6 e 8.','3★1=5; 5★4=6. Já 1★4=−2; 3★(−2)=8. Parênteses mudam o resultado.')],'index.html')
t('m06','Função afim, tabelas, gráficos e lucro',
 'Em y=ax+b, b é o valor quando x=0, e a é a mudança de y por unidade de x. Um custo fixo existe mesmo sem produção; por isso dividir custo por quantidade não encontra a taxa. No tanque, a taxa negativa indica perda de água.',
 'Escolha dois pontos e calcule a variação vertical dividida pela horizontal. Substitua um ponto para achar b. Confira um terceiro ponto. Em problemas econômicos, escreva receita R, custo C e só então lucro L=R−C. No gráfico, leia os nomes e unidades dos eixos antes de fazer contas.',
 r'$a=(y_2-y_1)/(x_2-x_1)$; $b=y_1-ax_1$; $L(x)=R(x)-C(x)$.',
 'O tanque foi resolvido corretamente; transferir a ideia de taxa e valor inicial para tabelas de custo é a meta.',39,'affine',[
 w('Uma reta passa por (2,7) e (5,16). Determine sua equação.','y=3x+1.','a=(16−7)/(5−2)=3. 7=3·2+b, então b=1.'),
 w('C(x)=8x+120 e preço de venda R$ 14. Calcule lucro em 30 unidades e ponto de equilíbrio.','R$ 60; 20 unidades.','L=14x−(8x+120)=6x−120. L(30)=60; L=0 dá x=20.'),
 w('V(t)=500−25t, em litros e horas. Quando atinge 200 L? Até quando vale o modelo?','12 h; de 0 a 20 h.','500−25t=200 dá t=12. O tanque esvazia em t=20; volumes negativos não fazem sentido.')],'exponenciais-logaritmos.html')
t('m07','Quadrática, inequações e intervalos',
 'As raízes marcam onde uma expressão quadrática muda de sinal. Uma parábola voltada para cima fica negativa entre duas raízes reais distintas e positiva fora delas. Testar um número em cada intervalo confirma o desenho.',
 'Depois de achar as raízes, volte ao símbolo: < ou > exclui as fronteiras, ≤ ou ≥ pode incluí-las. Quando duas condições precisam valer ao mesmo tempo, tome a interseção. Na notação de intervalos, desenhe primeiro a reta numérica e só depois escreva os colchetes.',
 r'$\Delta=b^2-4ac$; $x=(-b\pm\sqrt\Delta)/(2a)$; “e” → interseção; “ou” → união.',
 'Prioridade: raízes não são a solução completa de uma inequação. Cuidado com soluções negativas e com a direção do intervalo.',None,'quadratic',[
 w(r'Resolva $x^2-5x+6=0$.','x=2 ou x=3.',r'$(x-2)(x-3)=0$; cada fator pode ser zero.'),
 w(r'Resolva $x^2-5x+6<0$.',r'$2<x<3$.','As raízes são 2 e 3. Com coeficiente principal positivo, a expressão é negativa entre elas.'),
 w(r'Interseccione $x\ge1/2$ e $x<3$.',r'$[1/2,3)$.','Marque os dois conjuntos na reta. O trecho comum inclui 1/2 e exclui 3.')],'equacoes-segundo-grau.html')
t('m08','Funções e inequações exponenciais',
 'Uma exponencial multiplica por um mesmo fator a cada passo. Em f(x)=k·aˣ, k=f(0) e a=f(x+1)/f(x). Para k positivo, um gráfico crescente exige a>1; uma razão invertida produz um gráfico decrescente.',
 'Em equações e inequações, reescreva as bases como potências de uma base comum. Se a base é maior que 1, preserve a ordem dos expoentes; entre 0 e 1, inverta. Para limites duplos, resolva cada condição e interseccione. Uma reta entre dois pontos tem fórmula mx+b, mesmo que os pontos venham de uma curva.',
 r'$a^{u}>a^{v}\Leftrightarrow u>v$ para a>1; $a^{u}>a^{v}\Leftrightarrow u<v$ para 0<a<1.',
 'Prioridade: razão na ordem correta, bases fracionárias e intervalo final coerente com a conta.',None,'exponential',[
 w(r'Resolva $4^{x-1}>8$.',r'$x>5/2$.',r'$2^{2x-2}>2^3$, logo $2x-2>3$.'),
 w(r'Resolva $(1/2)^{2x}\le1/8$.',r'$x\ge3/2$.',r'$1/8=(1/2)^3$. A base é menor que 1: $2x\ge3$.'),
 w('f(x)=k·aˣ passa por (1,6) e (2,18). Ache a, k e f(0).','a=3; k=2; f(0)=2.','a=18/6=3; 6=k·3, então k=2.')],'novembro-exponenciais.html')
t('m09','Logaritmos, domínio e aplicações',
 r'Logaritmo responde “qual expoente?”. $\log_2 8=3$ porque $2^3=8$. As propriedades vêm das potências: multiplicar resultados soma expoentes; dividir subtrai. Logaritmo de uma soma não se separa.',
 r'Antes de transformar uma equação, imponha argumento positivo, base positiva e base diferente de 1. Se a base depende de x, as três condições importam. Use uma variável auxiliar quando o mesmo logaritmo se repete. Em escalas de energia, subtrair logaritmos produz o logaritmo de uma razão, não uma diferença de energias.',
 r'$\log_a(MN)=\log_a M+\log_a N$; $\log_a(M/N)=\log_a M-\log_a N$; $\log_a M=\log_b M/\log_b a$.',
 'Preparação: as fotos trazem lista e teoria, sem uma prova resolvida que permita diagnosticar erros próprios neste tema. Reforçar domínio e os pré-requisitos de expoentes.',None,'logarithm',[
 w(r'Calcule $\log_3 81$ e $\log_{1/2}8$.','4 e −3.',r'$3^4=81$; $(1/2)^{-3}=8$.'),
 w(r'Qual o domínio de $\log_{x-1}(x-3)$?',r'$x>3$.',r'Base: x>1 e x≠2. Argumento: x>3. A interseção é x>3.'),
 w(r'Resolva $\log_2 x+\log_2(x-2)=3$.','x=4.',r'Domínio x>2. $x(x-2)=8$, então x²−2x−8=0. Raízes 4 e −2; descarte −2.')],'logaritmos-ilustrados.html')
t('m10','Ângulos, triângulos e segmentos notáveis',
 'Uma medida angular pertence a duas semirretas específicas. Ângulos opostos pelo vértice são iguais; adjacentes sobre uma reta somam 180°. Paralelas transportam ângulos correspondentes e alternos. No triângulo, a soma interna é 180°.',
 'Bissetriz divide um ângulo; mediana liga vértice ao ponto médio do lado oposto; altura é perpendicular ao lado oposto; mediatriz é perpendicular no ponto médio de um segmento e pode nem passar por um vértice. Não atribua 90° a uma linha apenas porque o desenho parece perpendicular.',
 r'$A+B+C=180°$; equilátero: 60° em cada vértice; isósceles: lados iguais ↔ ângulos opostos iguais.',
 'Há bons acertos em isósceles e equiláteros. Prioridade: identificar o ângulo solicitado e distinguir mediana, mediatriz, altura e bissetriz.',11,'triangle',[
 w('Em um triângulo retângulo, um ângulo agudo mede 35°. Quanto mede o outro? E sua metade?','55° e 27,5°.','180−90−35=55; a bissetriz o divide em duas partes de 27,5.'),
 w('Uma transversal faz 130° com uma de duas paralelas. Qual é o ângulo agudo correspondente?','50°.','130+50=180. Transporte o ângulo agudo usando o paralelismo.'),
 w('Uma reta passa pelo ponto médio de BC e é perpendicular a BC. Ela é necessariamente mediana de ABC?','Não; é a mediatriz de BC.','Para ser mediana de ABC, o segmento precisa partir de A. A definição da mediatriz não exige isso.')],'poligonos.html')
t('m11','Polígonos e circunferências',
 'Diagonais ligam vértices não vizinhos. Cada vértice vê n−3 outros; dividir por dois corrige a dupla contagem. Num polígono regular, o centro cria triângulos congruentes. A apótema é perpendicular ao lado; o raio vai até um vértice.',
 'Inscrito: vértices sobre o círculo. Circunscrito: lados tangentes ao círculo; o raio é a apótema. No quadrado inscrito, a diagonal é 2R. Em círculos tangentes externamente, a distância entre centros é soma dos raios. Em ângulos inscritos, a medida é metade do arco correspondente.',
 r'$D=n(n-3)/2$; $\alpha=(n-2)180°/n$; quadrado inscrito: $l=R\sqrt2$; hexágono circunscrito: $l=2R/\sqrt3$.',
 'Prioridade: substituir n+1 em toda a fórmula; conferir 8÷4; distinguir raio, diâmetro e apótema. A construção dos polígonos inscritos já teve acerto.',15,'circles',[
 w('Quantas diagonais tem um decágono? Qual seu ângulo interno?','35; 144°.','D=10·7/2=35; α=8·180/10=144.'),
 w(r'Um quadrado está inscrito em círculo de raio $3\sqrt2$ cm. Qual seu lado?',r'6 cm.',r'$l=R\sqrt2=3\sqrt2\sqrt2=6$.'),
 w('Quatro círculos iguais, em duas filas, são tangentes entre si e aos lados de um quadrado de lado 12. Ache R e o raio r do círculo central tangente aos quatro.',r'$R=3$; $r=3(\sqrt2-1)$.',r'$4R=12$. Entre centro do quadrado e de um círculo: $R+r=R\sqrt2$.')],'novembro-circunferencias.html')
t('m12','Semelhança, Pitágoras e trigonometria',
 'Triângulos semelhantes têm os mesmos ângulos e lados correspondentes proporcionais. Escreva as razões na mesma ordem: altura grande/altura pequena = sombra grande/sombra pequena. Pitágoras só vale em triângulo retângulo; a hipotenusa fica oposta ao ângulo de 90°.',
 'Em triângulos retângulos, escolha seno, cosseno ou tangente pelo par de lados envolvido. Em triângulos quaisquer, a lei dos senos relaciona cada lado ao seno de seu ângulo oposto. Identifique os pares antes de substituir. Um resultado deve ser compatível com a escala do desenho.',
 r'$c^2=a^2+b^2$; $\sin\theta=\mathrm{oposto}/\mathrm{hipotenusa}$; $\cos\theta=\mathrm{adjacente}/\mathrm{hipotenusa}$; $a/\sin A=b/\sin B=2R$.',
 'Prioridade: relacionar lados e ângulos corretos e manter unidades iguais. Um desenho inclinado não transforma um ângulo em reto.',9,'similar',[
 w('Uma haste de 2 m faz sombra de 3 m. Na mesma hora um poste faz sombra de 12 m. Qual a altura?','8 m.','h/12=2/3; h=8.'),
 w('Um triângulo retângulo tem catetos 6 e 8. Calcule a hipotenusa e o seno do ângulo oposto ao cateto 6.','10 e 0,6.','c=√(36+64)=10; sen=6/10.'),
 w('Num triângulo, o lado oposto a 30° mede 4. Qual é o raio da circunferência circunscrita?','4.','4/sen30°=2R; 4/(1/2)=8=2R.')],'novembro-circunferencias.html')
t('m13','Áreas, decomposição e escala',
 'Área mede cobertura; altura é a distância perpendicular à base. Deslizar o topo de um paralelogramo conserva base e altura, portanto conserva sua área. Uma diagonal divide um paralelogramo em dois triângulos de mesma área.',
 'Em figuras compostas, some regiões sem sobreposição ou subtraia recortes. Para triângulos com dois lados e ângulo compreendido, use metade do produto dos lados pelo seno. Ao ampliar comprimentos por k, áreas crescem por k² e volumes por k³. Não confunda cm com cm².',
 r'$A_\triangle=bh/2=ab\sin C/2$; $A_{\text{trapézio}}=(B+b)h/2$; $A_{\rm regular}=P\cdot\mathrm{apótema}/2$.',
 'Preparação a partir da lista de áreas. Reforçar altura perpendicular e conferir se todos os dados geométricos são compatíveis.',None,'area',[
 w('Triângulo de base 12 cm e altura 5 cm: qual a área? E de um paralelogramo com os mesmos dados?','30 cm² e 60 cm².','Triângulo: 12·5/2; paralelogramo:12·5.'),
 w('Trapézio com bases 8 e 14 e altura 6: calcule a área.','66 unidades².','(8+14)·6/2=66.'),
 w('Uma figura de área 18 cm² é ampliada com lados triplicados. Qual a nova área?','162 cm².','Fator de área 3²=9. 18·9=162.')],'novembro-areas.html')
t('p01','Unidades, vetores e componentes',
 'Uma grandeza física precisa de número e unidade. Para passar de km/h a m/s, divida por 3,6. Vetores têm módulo, direção e sentido; duas setas podem ser iguais em posições diferentes. Somar vetores é somar seus deslocamentos em cada eixo.',
 'Escolha eixos e sinais, converta as unidades e faça as componentes. Some ou subtraia componentes antes de calcular o módulo. Os módulos só podem ser somados diretamente em condições especiais, como vetores no mesmo sentido e direção.',
 r'$v_x=v\cos\theta$; $v_y=v\sin\theta$; $|\vec v|=\sqrt{v_x^2+v_y^2}$; 1 h = 3600 s; 1 m = 100 cm.',
 'Componentes e igualdade de vetores já tiveram acertos. Prioridade: combinação de vetores e conversões de comprimento, tempo e massa.',38,'vector',[
 w('Converta 72 km/h, 30 min e 0,025 g para m/s, h e mg.','20 m/s; 0,5 h; 25 mg.','Divida 72 por 3,6; divida 30 por 60; multiplique 0,025 por 1000.'),
 w('A=(3,−2), B=(−1,4). Ache A+2B.','(1,6).','2B=(−2,8); some eixo por eixo.'),
 w('Um vetor tem componentes −6 N e 8 N. Qual o módulo?','10 N.','√[(−6)²+8²]=√100=10.')],'conversao-unidades.html')
t('p02','Movimento uniforme e leitura de gráficos',
 'Posição é uma coordenada; deslocamento é posição final menos inicial; distância soma o comprimento de cada trecho. Uma viagem com retorno pode ter deslocamento zero e distância positiva. A inclinação do gráfico s×t é velocidade; a área com sinal do gráfico v×t é deslocamento.',
 'Divida o movimento nos trechos indicados. Para cada um, anote duração, velocidade e deslocamento. Some deslocamentos para obter a velocidade média; some módulos dos deslocamentos para a distância. Em encontros, iguale posições no mesmo instante, não velocidades.',
 r'$s=s_0+vt$; $\Delta s=v\Delta t$; $v_m=\Delta s/\Delta t$; rapidez média = distância/tempo.',
 'Prioridade: área = base × altura, sinais das posições e conservação da variável t. Não use a altura de um gráfico de velocidade como distância.',48,'velocity',[
 w('Um móvel vai de −3 m a 5 m e volta a 1 m. Ache deslocamento total e distância.','4 m e 12 m.','Δs=1−(−3)=4. Distância=8+4=12.'),
 w('v=4 m/s por 3 s e v=−2 m/s por 2 s. Ache deslocamento e velocidade média.','8 m e 1,6 m/s.','Áreas:12 e −4. Deslocamento8; tempo5; média8/5.'),
 w('sA=2t e sB=12−t (SI). Quando e onde se encontram?','4 s; 8 m.','2t=12−t; 3t=12. Substitua t=4 nas duas funções.')],'cinematica.html')
t('p03','MRUV, reação e sinais',
 'A aceleração diz quanto a velocidade muda a cada segundo. Aceleração negativa pode aumentar a rapidez se o móvel já se move no sentido negativo. Durante o tempo de reação de um motorista, o carro continua avançando antes da frenagem.',
 'Separe reação e frenagem. No primeiro trecho, use velocidade constante; no segundo, MRUV. Escreva todos os dados, inclusive v₀, antes de escolher a fórmula. Em s=s₀+v₀t+at²/2, apenas t está ao quadrado. A intensidade da velocidade é |v|.',
 r'$v=v_0+at$; $s=s_0+v_0t+at^2/2$; $v^2=v_0^2+2a\Delta s$.',
 'Prioridade: não trocar posição inicial por velocidade inicial; descontar a distância da reação; classificar pelo par de sinais de v e a.',51,'mruv',[
 w('v₀=12 m/s, a=−3 m/s². Ache v em 5 s e classifique.','−3 m/s; retrógrado e acelerado.','v=12−15=−3. v e a negativos: rapidez crescente.'),
 w('Um carro a 20 m/s leva 0,8 s para reagir. Quantos metros percorre antes de frear?','16 m.','Ainda não há frenagem: d=20·0,8.'),
 w('Após reagir, freia de 20 m/s até parar em 40 m. Qual a aceleração?','−5 m/s².','0=20²+2a·40; a=−400/80.')],'cinematica.html')
t('p04','Lançamento horizontal e queda',
 'No lançamento horizontal sem resistência do ar, o movimento horizontal é uniforme e o vertical é uma queda livre. Os dois acontecem ao mesmo tempo. A velocidade vertical começa em zero, mas a horizontal não.',
 'Obtenha o tempo pela altura. Use esse mesmo tempo na horizontal. Para o módulo da velocidade, combine as componentes por Pitágoras e extraia a raiz. Se o evento ocorre certo tempo antes de atingir o solo, subtraia esse intervalo do tempo total de queda.',
 r'$h=gt^2/2$; $x=v_0t$; $v_y=gt$; $v=\sqrt{v_0^2+(gt)^2}$.',
 'O problema do fosso foi bem resolvido. No lançamento do avião, faltou concluir o módulo da velocidade após montar Pitágoras.',None,'projectile',[
 w('Um corpo cai 20 m a partir do repouso vertical. Use g=10 m/s². Qual o tempo?','2 s.','20=5t²; t²=4; escolha a raiz positiva.'),
 w('É lançado horizontalmente a 15 m/s e cai por 2 s. Qual alcance e velocidade vertical?','30 m e 20 m/s para baixo.','x=15·2=30; vy=10·2=20.'),
 w('No caso anterior, qual o módulo da velocidade ao final?','25 m/s.','v=√(15²+20²)=√625=25.')],'novembro-lancamento.html')
t('p05','Movimento circular e transmissões',
 'Período é o tempo de uma volta; frequência é o número de voltas por segundo. Dois pontos de um disco rígido completam cada volta juntos, mas o ponto mais distante do centro percorre um caminho maior e tem maior velocidade linear.',
 'Distinga ligação por eixo de ligação por correia sem deslizamento. No mesmo eixo, a velocidade angular é igual; numa correia, as velocidades tangenciais nas bordas são iguais. A aceleração centrípeta aponta para o centro e muda a direção da velocidade.',
 r'$f=1/T$; $\omega=2\pi f$; $v=\omega R$; $a_c=v^2/R$.',
 'Revisão complementar do conteúdo já trabalhado no site; não atribuir erro pessoal a um tema sem resolução correspondente nas novas fotos.',None,'circular',[
 w('Uma roda gira a 120 rpm. Ache frequência e período.','2 Hz; 0,5 s.','120 voltas/min ÷60=2 voltas/s. T=1/2.'),
 w('Em um disco, R₂=3R₁. Compare ω e v nos dois pontos.','ω₂=ω₁; v₂=3v₁.','A volta leva o mesmo tempo; v é proporcional ao raio.'),
 w('Polias de raios 2 e 6 cm são ligadas por correia sem deslizar. A menor gira a 9 Hz. Quanto gira a maior?','3 Hz.','2π·9·2=2π·f·6; f=3.')],'movimento-circular.html')
t('p06','Forças, aceleração e tração',
 'Força resultante é a soma vetorial das interações sobre um corpo. Peso e normal não são um par ação–reação, pois atuam no mesmo corpo. Em uma corda ideal e polia ideal, a tração tem o mesmo módulo, mas é uma força diferente do peso.',
 'Desenhe um diagrama de forças para cada corpo. Escolha um sentido positivo compatível com o fio. Para achar a aceleração, pode-se somar as equações do sistema e cancelar trações internas; depois volte a um corpo para achar T. Sem atrito e sem aceleração vertical, a normal equilibra as forças verticais.',
 r'$\sum F=ma$; $P=mg$; mesa + massa pendente: $a=m_2g/(m_1+m_2)$ sob as hipóteses ideais.',
 'Revisão complementar das provas de física já presentes no site: separar forças, componentes e sentido positivo.',None,'forces',[
 w('Um corpo de 4 kg recebe 18 N à direita e 6 N à esquerda. Qual a aceleração?','3 m/s² à direita.','Resultante12 N; a=12/4.'),
 w('Blocos de 3 kg na mesa lisa e 2 kg pendurado são ligados por fio e polia ideais. Use g=10. Ache a.','4 m/s².','Força externa que move o conjunto=20 N; massa total5 kg.'),
 w('No sistema anterior, determine a tração.','12 N.','No bloco da mesa, T=3·4=12 N. No pendurado,20−12=2·4.')],'prova-fisica.html')
t('p07','Propagação da luz, sombra e penumbra',
 'Em um meio homogêneo, o modelo de raios usa trajetórias retilíneas. Uma fonte pontual produz uma borda de sombra definida. Uma fonte extensa pode ser parcialmente escondida: aparece a penumbra; na umbra, nenhuma parte da fonte é visível.',
 'Desenhe raios dos extremos da fonte tangenciando os extremos do obstáculo. Eles determinam limites distintos na tela. Use triângulos semelhantes, escrevendo todas as distâncias na mesma unidade. A espessura de um anel é a diferença dos raios, metade da diferença dos diâmetros.',
 r'$H/h=D/d$ para fonte pontual e planos paralelos; $E=R_{\rm externo}-R_{\rm interno}$.',
 'Prioridade: distinguir a sombra total da região parcialmente iluminada e não confundir raio com diâmetro.',44,'penumbra',[
 w('Uma fonte pontual fica a 2 m de um disco de 10 cm de diâmetro. A tela está a 6 m da fonte. Qual o diâmetro da sombra?','30 cm.','Ampliação=6/2=3. Diâmetro=3·10.'),
 w('Uma penumbra em anel tem diâmetro externo de 60 cm e interno de 40 cm. Qual sua espessura?','10 cm.','Raios30 e20; diferença10. A diferença dos diâmetros deve ser dividida por2.'),
 w('Uma pessoa de 1,5 m faz sombra de 2 m; uma árvore faz sombra de 8 m. Qual a altura da árvore?','6 m.','h/8=1,5/2; h=6.')],'termologia.html')
t('p08','Reflexão e espelhos planos',
 'A normal é a reta perpendicular ao espelho no ponto de incidência. Os ângulos de incidência e reflexão são medidos em relação a ela. A imagem virtual aparece atrás do espelho, à mesma distância que o objeto está à frente.',
 'Para traçar um raio, reflita o ponto do objeto para trás do espelho e ligue a imagem ao observador. O encontro dessa linha com o espelho dá o ponto de reflexão. Em espelho vertical, as alturas se preservam. Para campo visual, use os raios das bordas e semelhança.',
 r'$i=r$; ângulo com a superfície $=90°-i$; distância objeto–imagem $=2d$.',
 'Há acertos sólidos em altura de imagem e ângulos. Reforçar caminho total da luz e ampliação do campo visual.',23,'mirror',[
 w('Um raio faz 25° com a normal. Qual o ângulo refletido com a normal e com o espelho?','25° e 65°.','i=r; a superfície faz90° com a normal.'),
 w('Um objeto está a 1,8 m do espelho. Qual a distância até sua imagem?','3,6 m.','São1,8 m à frente mais1,8 m atrás.'),
 w('A luz percorre 12 m em 4×10⁻⁸ s. Qual sua rapidez?','3×10⁸ m/s.','12/(4×10⁻⁸)=3×10⁸. Use caminho percorrido, não deslocamento se houver retorno.')],'termologia.html')
t('p09','Calorimetria e mudanças de fase',
 'Calor é energia transferida por diferença de temperatura. Num trecho inclinado de uma curva de aquecimento, a temperatura muda; num patamar de mudança de fase de substância pura sob pressão constante, a energia muda o estado físico sem mudar a temperatura.',
 'Separe aquecimento, mudança de fase e novo aquecimento. Cada trecho usa sua própria quantidade de calor. Num gráfico de calor acumulado, subtraia os valores das extremidades do trecho. Em mistura isolada, calor recebido e cedido se equilibram; confira se há energia suficiente para completar a mudança de fase.',
 r'$Q=mc\Delta T$; $Q=mL$; $\sum Q=0$ em sistema termicamente isolado.',
 'A fusão do gelo com aquecimento foi correta. No patamar de vaporização, o erro foi usar o calor acumulado final em vez da diferença.',None,'heat',[
 w('200 g de água passam de20 a35°C. c=1 cal/(g·°C). Calcule Q.','3 000 cal.','ΔT=15°C. Q=200·1·15.'),
 w('Um patamar vai de12 000 a32 000 cal para200 g. Qual o calor latente?','100 cal/g.','Q do trecho=20 000; L=20 000/200.'),
 w('100 g de água a80°C se misturam com100 g a20°C, sem perdas. Qual a temperatura final?','50°C.','Mesmas massas e calores específicos:100(T−80)+100(T−20)=0; T=50.')],'novembro-calorimetria.html')
t('p10','Dilatação linear, superficial e volumétrica',
 'Ao aquecer, a distância média entre partículas de muitos materiais aumenta. Uma barra muda de comprimento; uma chapa muda em duas dimensões; um bloco, em três. Um furo numa chapa também se dilata, como se estivesse preenchido pelo mesmo material.',
 'Use a temperatura final menos a inicial; resfriamento dá ΔT negativo. Diferencie variação ΔL de comprimento final L₀+ΔL. As relações β≈2α e γ≈3α são aproximações para sólidos isotrópicos e pequenas dilatações. Desenhos ampliam a deformação para torná-la visível.',
 r'$\Delta L=L_0\alpha\Delta T$; $\Delta A\approx A_0(2\alpha)\Delta T$; $\Delta V\approx V_0(3\alpha)\Delta T$.',
 'Preparação a partir das anotações: ainda não há prova resolvida deste tópico nas fotos novas. Aquecer com porcentagens e unidades.',None,'dilation',[
 w('Uma barra de2 m tem α=10⁻⁵ °C⁻¹ e aquece50°C. Calcule ΔL em mm.','1 mm.','ΔL=2·10⁻⁵·50=0,001 m=1 mm.'),
 w('No caso anterior, qual o comprimento final?','2,001 m.','Some a variação ao comprimento inicial, na mesma unidade.'),
 w('Um sólido isotrópico tem α=2×10⁻⁵ °C⁻¹. Estime β e γ.','4×10⁻⁵ e6×10⁻⁵ °C⁻¹.','β≈2α; γ≈3α.')],'novembro-dilatacao.html')
t('p11','Leis de Kepler e sistema solar',
 'Primeira lei: o planeta descreve uma elipse com o Sol em um foco. A distância muda ao longo da órbita; o semieixo maior a é a média entre distâncias de periélio e afélio. Segunda lei: o segmento Sol–planeta varre áreas iguais em tempos iguais, por isso o planeta anda mais rápido perto do Sol.',
 'Terceira lei: para corpos orbitando o mesmo centro, T²/a³ é aproximadamente constante. Em anos e unidades astronômicas para o sistema solar, essa constante é aproximadamente1. O gráfico de T versus a é curvo; o de T² versus a³ é uma reta pela origem. a é semieixo maior, não a distância instantânea.',
 r'$a=(r_p+r_a)/2$; $A_1/A_2=\Delta t_1/\Delta t_2$; $(T_2/T_1)^2=(a_2/a_1)^3$.',
 'Preparação a partir das anotações e da aula interativa já criada. A constante só pode ser comparada para o mesmo corpo central.',None,'kepler',[
 w('Uma órbita tem periélio0,6 UA e afélio1,4 UA. Qual a?','1 UA.','a=(0,6+1,4)/2=1; não use apenas uma das distâncias.'),
 w('Em torno do Sol, a=4 UA. Estime o período em anos.','8 anos.','T²=4³=64; T=8.'),
 w('O raio vetor varre10 unidades² em2 dias. Quanto varre em5 dias na mesma órbita?','25 unidades².','Velocidade areolar=10/2=5 unidades²/dia; área=5·5.')],'novembro-kepler.html')
t('q01','Matéria, mudanças de estado e fórmulas',
 'Substância simples contém um único elemento, mesmo que suas partículas tenham vários átomos: O₂ e Cl₂ são exemplos. Substância composta tem mais de um elemento. Mistura reúne substâncias diferentes. Em uma mudança física, a identidade química permanece; numa reação, formam-se novas substâncias.',
 'Fusão, vaporização e sublimação absorvem calor; os processos inversos o liberam. Conte elementos pelos símbolos diferentes e átomos pelos índices, incluindo o1 implícito. Parênteses multiplicam todos os átomos dentro deles: Ca(OH)₂ tem1 Ca,2 O e2 H.',
 r'$N_{\rm átomos/partícula}=\text{soma dos índices}$; quantidade de elementos = número de símbolos distintos.',
 'Prioridade: condensação não é vaporização. A identificação de Cl₂ como simples e a contagem de56 átomos foram corretas.',7,'states',[
 w('Classifique a passagem vapor→líquido e sólido→líquido quanto ao nome e troca de calor.','Condensação exotérmica; fusão endotérmica.','A primeira libera calor; a segunda precisa receber energia.'),
 w('Quantos elementos e átomos há em Ca(OH)₂?','3 elementos;5 átomos por unidade de fórmula.','Ca:1, O:2,H:2; total5.'),
 w('O₂, H₂O e uma mistura dos dois: identifique simples, composta e mistura.','O₂ simples; H₂O composta; o conjunto é mistura.','Número de elementos distingue simples de composta; número de substâncias distingue substância de mistura.')],'prova-quimica.html')
t('q02','Estrutura atômica, íons e transformações nucleares',
 'Z conta prótons e identifica o elemento; A conta prótons mais nêutrons. Num átomo neutro, elétrons e prótons têm a mesma quantidade. Um cátion perdeu elétrons e um ânion ganhou; ionização comum não muda o núcleo.',
 'Isótopos têm mesmo Z; isóbaros, mesmo A; isótonos, mesmo número de nêutrons; isoeletrônicos, mesmo número de elétrons. Em emissão alfa, o núcleo perde2 prótons e2 nêutrons. A partícula deve aparecer na equação para conservar carga e número de massa. Dalton tratava átomos como indivisíveis; Rutherford introduz o núcleo, e Bohr níveis de energia eletrônicos.',
 r'$N=A-Z$; $e^-=Z-q$ para carga algébrica q; $\alpha={}^4_2He$.',
 'Prioridade: não usar número de prótons quando se pede igualdade de elétrons ou de nêutrons. Separar modelo nuclear de camadas eletrônicas.',31,'atom',[
 w(r'Em ${}^{23}_{11}Na^+$, conte p,n,e.','11 prótons,12 nêutrons,10 elétrons.','p=11; n=23−11; e=11−1.'),
 w(r'${}^{40}_{18}X$ e ${}^{A}_{20}Y$ são isótonos. Ache A.','42.','X tem22 nêutrons; A−20=22.'),
 w(r'Complete ${}^{238}_{92}U\to X+{}^4_2He$.',r'$X={} ^{234}_{90}Th$.','Conserve massa:238−4=234; carga nuclear:92−2=90.')],'prova-quimica.html')
t('q03','Configuração eletrônica e íons de metais',
 'Subníveis s,p,d,f comportam2,6,10,14 elétrons. A sequência usual de preenchimento organiza energias, mas não é a mesma coisa que número da camada. A camada de valência tem o maior n ocupado. Somar expoentes deve devolver o total de elétrons.',
 'A notação por gás nobre substitui somente a parte interna já preenchida. Há exceções, como Mo=[Kr]4d⁵5s¹. Ao formar cátions de metais de transição, retire primeiro elétrons da camada de maior n, mesmo que outro subnível tenha sido preenchido depois. Para uma porcentagem, use no denominador todos os elétrons do íon.',
 r'Preenchimento usual: $1s,2s,2p,3s,3p,4s,3d,4p,5s,4d,5p,6s,4f,5d,6p$.',
 'Prioridade: preservar a exceção em todos os itens, usar o gás nobre correto e distinguir “último subnível” de “camada externa”.',46,'orbitals',[
 w('Z=20, átomo neutro: configuração abreviada e camada de valência?','[Ar]4s²; camada4 com2 elétrons.','Ar representa18; faltam2 no4s.'),
 w('Fe=[Ar]3d⁶4s². Qual a configuração de Fe²⁺?','[Ar]3d⁶.','Retire os dois elétrons do4s, de maior n.'),
 w('Um íon tem20 elétrons, dos quais6 estão em subníveis s. Qual a porcentagem?','30%.','6/20·100=30. Não divida pelo número de subníveis.')],'prova-quimica.html')
t('q04','Tabela periódica e propriedades',
 'Períodos são linhas e indicam a maior camada ocupada no átomo fundamental. Grupos são colunas de elementos com padrões de valência semelhantes. Nos representativos, grupo16 corresponde a ns²np⁴: seis elétrons externos.',
 'Em geral, o raio atômico aumenta ao descer um grupo e ao ir para a esquerda num período. Eletronegatividade tende a aumentar para cima e para a direita, com F como referência máxima usual. São tendências, não fórmulas universais. Decore famílias com âncoras:1 alcalinos,2 alcalino-terrosos,15 nitrogênio,16 calcogênios,17 halogênios,18 gases nobres.',
 'Z identifica o elemento; período localiza a camada; grupo organiza padrões de valência.',
 'No selênio, símbolo, Z e período estavam corretos; reforçar nome do grupo e leitura da coluna. Na charada, faltou reconhecer os símbolos.',52,'periodic',[
 w('Uma configuração termina em3s²3p⁵. Qual o período e a família?','Período3; halogênios, grupo17.','Maior n=3; sete elétrons de valência.'),
 w('Ordene O,C,Ca por raio atômico crescente.','O<C<Ca.','C e O no mesmo período: raio diminui para a direita. Ca tem mais camadas.'),
 w('Dê símbolos de cálcio, enxofre e arsênio.','Ca, S, As.','Maiúscula inicial e minúscula quando houver segunda letra; C é carbono, não cálcio.')],'prova-quimica.html')
t('q05','Ligações, cargas e estruturas de Lewis',
 'Ligação covalente envolve pares compartilhados. Uma linha representa dois elétrons, e pares livres também precisam ser contados. Em compostos iônicos, a fórmula expressa proporção entre cátions e ânions que torna a carga total zero.',
 'Some elétrons de valência, desenhe a conectividade e distribua os restantes em pares livres. H procura dueto; C,N,O,F frequentemente completam octeto. Para íons, ajuste a contagem pela carga. Diferença de eletronegatividade é uma pista para caráter iônico, não uma fronteira física exata. Não desenhe uma ligação covalente entre cada par de íons de um cristal.',
 r'$\sum (\text{quantidade de íons}\times\text{carga})=0$ em composto neutro; ligação simples=2 e⁻, dupla=4 e⁻.',
 'A ureia foi bem representada. Prioridade nas fórmulas iônicas: valência, neutralidade e octetos dos ânions.',13,'lewis',[
 w('Combine Al³⁺ e O²⁻ na menor proporção neutra.','Al₂O₃.','2·(+3)+3·(−2)=0.'),
 w('Na molécula NH₃, quantas ligações e quantos pares livres há no N?','3 ligações simples e1 par livre.','5+3=8 elétrons de valência;6 nas três ligações e2 no par livre.'),
 w('Quantos elétrons de valência há em CO₂? Como se ligam os átomos?','16; O=C=O, dois pares livres em cada O.','4+2·6=16;8 em ligações e8 em pares livres.')],'prova-quimica.html')
t('q06','Mol, massa, partículas e gases',
 'Mol é uma unidade de contagem: como uma dúzia reúne12 itens, um mol reúne aproximadamente6,02×10²³ entidades. É preciso dizer quais entidades: átomos, moléculas, íons ou unidades de fórmula. Uma molécula de vitamina C contém20 átomos, portanto20 mol de átomos por mol de moléculas.',
 'Use uma cadeia de conversões com unidades: massa→mol→moléculas→átomos. A massa molar tem unidade g/mol; massa molecular tem u. Em recipiente, subtraia a tara. Para gás ideal, use Kelvin e unidades compatíveis com R. Nas CNTP de0°C e1atm, o volume molar aproximado é22,4 L/mol.',
 r'$n=m/M=N/N_A$; $PV=nRT$; $N_{\rm átomos}=N_{\rm moléculas}\cdot\text{átomos/molécula}$.',
 'Prioridade: átomos versus moléculas, mg versus g, massa líquida do gás e soma de períodos de administração nos problemas escolares.',43,'mole',[
 w('Quantos mol há em9 g de H₂O? Use M=18 g/mol.','0,5 mol.','n=m/M=9/18.'),
 w('Quantos mol de átomos há em0,5 mol de H₂O?','1,5 mol de átomos.','Cada molécula tem3 átomos;0,5·3=1,5.'),
 w('Um recipiente vazio tem30 g e cheio de O₂ tem33,2 g. Qual o volume nas CNTP de22,4 L/mol? M=32.','2,24 L.','Gás:3,2 g; n=3,2/32=0,1 mol; V=0,1·22,4.')],'prova-quimica.html')
t('q07','Composição percentual e fórmulas',
 'Porcentagem em massa compara a massa de um elemento com a massa total. A fórmula mínima expressa a razão inteira mais simples de átomos; a molecular é um múltiplo inteiro dela. Percentuais não são diretamente índices atômicos, porque átomos diferentes têm massas diferentes.',
 'Imagine100 g de amostra, divida cada massa percentual pela massa atômica, e divida os mols pelo menor valor. Se aparecer0,5 ou1,5, multiplique todos por2; não arredonde indiscriminadamente. Encontre a massa molar real por dados da amostra, divida pela massa da fórmula mínima e multiplique todos os índices pelo fator.',
 r'$\%C=(\text{massa de C em 1 mol}/M)\cdot100$; fator molecular $=M/M_{\rm mínima}$.',
 'Prioridade: a amostra de16,5 g e o frasco de500 g não são intercambiáveis. Leia também o subconjunto de compostos que a pergunta permite comparar.',45,'composition',[
 w('Qual a porcentagem em massa de carbono em CO₂? C=12,O=16.','27,27% aproximadamente.','M=44;12/44·100≈27,27.'),
 w('Uma substância tem40%C,6,67%H e53,33%O. Ache a fórmula mínima. C=12,H=1,O=16.','CH₂O.','Mols em100g:3,333;6,67;3,333. Dividindo pelo menor:1:2:1.'),
 w('A fórmula mínima é CH₂O e M=180 g/mol. Ache a molecular.','C₆H₁₂O₆.','Mínima tem30 g/mol;180/30=6; multiplique os três índices por6.')],'prova-quimica.html')
t('q08','Balanceamento, estequiometria e excesso',
 'Uma reação conserva átomos. Os coeficientes indicam proporções de partículas e de mols, não necessariamente de massas. A receita2H₂+O₂→2H₂O precisa do dobro de mols de H₂ em relação a O₂.',
 'Balanceie, converta massas em mols e compare mols disponíveis divididos pelos coeficientes. O menor quociente determina o reagente limitante. Calcule produtos a partir dele e desconte do excesso o que foi consumido. Em tabelas de massas, o mesmo fator deve multiplicar todas as quantidades de uma reação completa.',
 r'Avanço máximo proporcional a $\min(n_i/\nu_i)$; massa inicial = produtos + sobra, em sistema fechado.',
 'Prioridade: fator3 foi trocado por2 na tabela do precipitado. A conservação de massa fornece uma conferência independente.',50,'stoich',[
 w(r'Balanceie $H_2+O_2\to H_2O$.',r'$2H_2+O_2\to2H_2O$.','Conte4 H e2 O em cada lado. Mude coeficientes, não os índices das substâncias.'),
 w('Há3 mol de H₂ e2 mol de O₂. Usando a reação anterior, qual é o limitante e quantos mol de água se formam?','H₂;3 mol de H₂O.','Compare3/2=1,5 e2/1=2. H₂ limita; relaçãoH₂:H₂O=1:1.'),
 w('No caso anterior, quantos mol de O₂ sobram?','0,5 mol.','Consumo de O₂=3/2=1,5; sobra2−1,5=0,5.')],'prova-quimica.html')
t('q09','Ácidos, bases, sais e tipos de reação',
 'No modelo de Arrhenius, ácidos aumentam H₃O⁺ em água e bases aumentam OH⁻. Uma neutralização combina essas espécies e forma água; os demais íons formam o sal. A quantidade necessária depende de quantos H⁺ e OH⁻ cada fórmula fornece.',
 'Síntese reúne reagentes em um produto; decomposição faz o inverso. Simples troca envolve substância simples e composta; dupla troca permuta íons entre compostos. Escrever uma permuta não garante que a reação ocorra: precipitado, gás ou formação de água podem favorecê-la. Use o contexto e a reatividade informados.',
 r'$H_3O^++OH^-\to2H_2O$; $H_2SO_4+2NaOH\to Na_2SO_4+2H_2O$.',
 'Conteúdo das listas e do simulado de química já publicado; revisão complementar. Conectar balanceamento às cargas dos íons.',None,'neutralization',[
 w('Qual sal resulta de HCl com NaOH? Balanceie.','NaCl; HCl+NaOH→NaCl+H₂O.','H⁺ e OH⁻ formam água; Na⁺ e Cl⁻ formam sal.'),
 w('Quantos mol de NaOH neutralizam0,2 mol de H₂SO₄ completamente?','0,4 mol.','Relação1:2;0,2·2=0,4.'),
 w('Classifique CaCO₃→CaO+CO₂ e Zn+2HCl→ZnCl₂+H₂.','Decomposição e simples troca.','Na primeira há um reagente; na segunda o metal desloca o hidrogênio.')],'prova-quimica.html')
t('q10','Hidrocarbonetos, nomenclatura e combustão',
 'Hidrocarbonetos têm apenas C e H. Carbono faz quatro ligações no modelo usual. Em cadeias abertas, alcano só tem ligações simples; alceno tem uma dupla; alcino tem uma tripla. Uma ramificação também contém carbonos e entra na fórmula molecular.',
 'Escolha a cadeia principal apropriada que contém a insaturação, numere para dar menor posição à insaturação e depois às ramificações conforme as regras usuais. Em combustão completa, forme CO₂ e H₂O; balanceie C, depois H, por último O. Petróleo é uma mistura de origem fóssil, não uma substância de fórmula única.',
 r'Alcano acíclico $C_nH_{2n+2}$; alceno acíclico com uma dupla $C_nH_{2n}$; alcino acíclico com uma tripla $C_nH_{2n-2}$.',
 'Revisão complementar do material já estudado. Não deduza a classe só pela fórmula: CₙH₂ₙ também pode ser cicloalcano.',None,'carbon',[
 w('Qual a fórmula de um alcano aberto com5 carbonos?','C₅H₁₂.','H=2·5+2=12.'),
 w('Nomeie CH₃–CH(CH₃)–CH₂–CH₃ e dê sua fórmula.','2-metilbutano;C₅H₁₂.','Cadeia principal4C, metil no2; são5 carbonos totais.'),
 w('Balanceie a combustão completa de C₃H₈.','C₃H₈+5O₂→3CO₂+4H₂O.','3C dão3CO₂;8H dão4H₂O; produtos têm10O, exigindo5O₂.')],'prova-quimica.html')
