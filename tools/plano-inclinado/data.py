"""Oito questões das duas fotos de 19/11/2026, sem dados pessoais."""

QUESTIONS = []


def question(n, title, topic, prompt, parts, steps, answer, pitfall, lab, note=None, choices=None):
    QUESTIONS.append(dict(id=n, title=title, topic=topic, prompt=prompt, parts=parts,
                          steps=steps, answer=answer, pitfall=pitfall, lab=lab,
                          note=note, choices=choices or []))


def control(key, label, minimum, maximum, step, unit=''):
    return dict(key=key, label=label, min=minimum, max=maximum, step=step, unit=unit)


question(1, 'O peso se divide em duas direções', 'Forças na rampa',
    r'Um corpo de massa $2{,}0$ kg é abandonado sobre um plano perfeitamente liso, inclinado de $37^\circ$ com a horizontal. Adote $g=10\,\mathrm{m/s^2}$, $\operatorname{sen}37^\circ=0{,}60$ e $\cos37^\circ=0{,}80$. Determine a aceleração com que o corpo desce o plano e a intensidade da força normal.', [],
    [r'O peso é vertical e tem módulo $P=mg=2\cdot10=20$ N. Escolha um eixo paralelo à rampa, positivo para baixo, e outro perpendicular a ela.',
     r'Projete o peso: $P_{\parallel}=mg\operatorname{sen}\theta=20\cdot0{,}60=12$ N e $P_{\perp}=mg\cos\theta=20\cdot0{,}80=16$ N.',
     r'O corpo não acelera perpendicularmente ao plano: $N-P_{\perp}=0$. Assim $N=16$ N.',
     r'Sem atrito, a resultante ao longo da rampa é $P_{\parallel}$. Logo $ma=mg\operatorname{sen}\theta$ e $a=10\cdot0{,}60=6\,\mathrm{m/s^2}$, para baixo da rampa.'],
    r'$a=6\,\mathrm{m/s^2}$, descendo a rampa; $N=16$ N.',
    r'A normal não é igual ao peso inteiro: ela equilibra a componente perpendicular. A massa cancela no cálculo de a, mas permanece no cálculo de N.',
    dict(kind='forces', title='Mude a massa: o que realmente muda?',
         base=dict(mass=2, sine=.6, g=10), controls=[control('mass','Massa',.5,8,.5,'kg'),control('sine','Inclinação: sen θ',.1,.9,.05)],
         note='O controle de etapas monta o diagrama; não representa tempo físico. Nos dados da folha, usamos sen 37° = 0,60 e cos 37° = 0,80. Ao explorar outros senos, calculamos o cosseno pela relação trigonométrica.',
         insight='Compare duas massas no mesmo plano: a aceleração não muda, mas o peso e a normal crescem na mesma proporção.',
         stages=['Reconheça o peso vertical.','Projete o peso nos eixos da rampa.','Equilibre as forças perpendiculares.','A componente paralela determina a aceleração.']))

question(2, 'Do alto da rampa até o chão', 'Descida e tempo',
    r'(UFAL) Uma rampa AB, inclinada de $37^\circ$ em relação à horizontal, tem $12$ m de comprimento e não oferece atrito. Um corpo de massa $1{,}0$ kg é abandonado do repouso no ponto A, no alto da rampa. Adote $g=10\,\mathrm{m/s^2}$, $\cos37^\circ=0{,}80$ e $\operatorname{sen}37^\circ=0{,}60$.',
    [r'a) Determine a força resultante sobre o corpo.',r'b) Determine o tempo necessário para o percurso AB.'],
    [r'Perpendicularmente à rampa, a normal equilibra a componente do peso. Ao longo dela, $F_R=mg\operatorname{sen}\theta=1\cdot10\cdot0{,}60=6$ N, para baixo.',
     r'Pela segunda lei de Newton, $a=F_R/m=6/1=6\,\mathrm{m/s^2}$.',
     r'O corpo parte do repouso, então $s=v_0t+\frac12at^2$ reduz-se a $12=\frac12\cdot6\cdot t^2=3t^2$.',
     r'Escolha a raiz positiva: $t=\sqrt4=2$ s. A velocidade imediatamente antes de B é $v=at=12$ m/s.'],
    r'a) $F_R=6$ N, descendo a rampa; b) $t=2$ s.',
    r'Os 12 m são medidos ao longo da rampa. Não substitua esse comprimento pela altura vertical na equação do movimento paralelo ao plano.',
    dict(kind='down', title='Acompanhe a descida e o gráfico da velocidade',
         base=dict(mass=1, sine=.6, length=12, g=10), controls=[control('length','Comprimento AB',4,24,1,'m'),control('sine','Inclinação: sen θ',.2,.8,.05)],
         note='O movimento termina na chegada a B. A velocidade final é a de chegada; uma colisão ou uma transição para outro piso não é simulada. O desenho ajusta a escala quando você muda o comprimento.',
         insight='O tempo cresce com o comprimento da rampa e diminui quando a componente do peso ao longo dela aumenta.'))

question(3, 'Sobe, diminui a rapidez e para', 'Subida e parada',
    r'Uma partícula é lançada para cima sobre um plano inclinado sem atrito, com velocidade inicial $v_0=12$ m/s e $\operatorname{sen}\theta=0{,}3$. O ponto A é o lançamento e B é o ponto em que ela para pela primeira vez.',
    [r'a) Determine o módulo da aceleração durante a subida.',r'b) Determine o tempo entre o lançamento e a parada.',r'c) Determine a distância AB.'],
    [r'Adote o eixo positivo para cima da rampa. A componente do peso aponta para baixo, portanto $a=-g\operatorname{sen}\theta=-10\cdot0{,}3=-3\,\mathrm{m/s^2}$. Seu módulo é $3\,\mathrm{m/s^2}$.',
     r'Na primeira parada, $v=0$. Use $v=v_0+at$: $0=12-3t$, então $t=4$ s.',
     r'O deslocamento é $s=v_0t+\frac12at^2=12\cdot4-\frac32\cdot4^2=48-24=24$ m.',
     r'Conferência por Torricelli: $0=12^2+2(-3)s$, logo $s=144/6=24$ m.',
     r'Na parada instantânea, a velocidade é zero, mas a aceleração continua apontando para baixo. Se o movimento continuar, a partícula volta a descer.'],
    r'a) $|a|=3\,\mathrm{m/s^2}$; b) $t=4$ s; c) $AB=24$ m.',
    r'Subir não significa ter aceleração para cima. Durante essa subida, velocidade e aceleração têm sentidos opostos.',
    dict(kind='up', title='Veja a velocidade chegar a zero sem a aceleração desaparecer',
         base=dict(v0=12, sine=.3, g=10), controls=[control('v0','Velocidade inicial',4,20,1,'m/s'),control('sine','Inclinação: sen θ',.1,.8,.05)],
         note='A simulação vai de A até a primeira parada em B. A massa não foi informada e não é necessária: o diagrama usa os símbolos P = mg e N, sem inventar valores de força.',
         insight='Dobre a velocidade inicial: o tempo de subida dobra, mas a distância até parar fica quatro vezes maior.'),
    note=r'A questão 3 não informa g. Adotamos $g=10\,\mathrm{m/s^2}$, como nas demais questões numéricas da lista; essa hipótese reproduz o gabarito impresso.')

question(4, 'Uma força puxa o bloco para cima', 'Forças na rampa',
    r'Uma partícula de massa $2$ kg sobe um plano inclinado, puxada por uma força $F=22$ N paralela ao plano e dirigida para cima. Determine a intensidade da aceleração. Dados: $\operatorname{sen}\theta=0{,}7$ e $g=10\,\mathrm{m/s^2}$.', [],
    [r'Escolha o eixo positivo para cima da rampa. A força F é positiva nesse eixo; a componente paralela do peso é negativa.',
     r'Calcule a componente que se opõe à subida: $P_{\parallel}=mg\operatorname{sen}\theta=2\cdot10\cdot0{,}7=14$ N.',
     r'A resultante paralela é $F_R=22-14=8$ N, para cima da rampa.',
     r'Pela segunda lei de Newton, $a=F_R/m=8/2=4\,\mathrm{m/s^2}$. A aceleração tem o mesmo sentido da subida.'],
    r'$a=4\,\mathrm{m/s^2}$, para cima da rampa.',
    r'F não é a resultante: antes de dividir pela massa, subtraia a componente do peso ao longo do plano.',
    dict(kind='forces', title='Compare a força aplicada com a componente do peso',
         base=dict(mass=2, force=22, sine=.7, g=10), controls=[control('force','Força aplicada F',0,40,1,'N'),control('mass','Massa',1,5,.5,'kg')],
         note='A lista não fornece velocidade inicial nem duração. Por isso, a visualização monta o diagrama de forças, sem inventar uma trajetória. O eixo positivo aponta para cima da rampa.',
         insight='Com m = 2 kg, experimente F = 14 N: a aceleração zera. Abaixo disso, a aceleração aponta para baixo, mesmo que o bloco ainda esteja subindo.',
         stages=['Escolha o sentido positivo para cima.','Encontre a componente do peso na rampa.','Compare a força aplicada e a componente do peso.','Divida a resultante pela massa.']),
    note=r'A folha não informa uma força de atrito nem um coeficiente. Adotamos o plano sem atrito, em continuidade com os outros exercícios e com o gabarito de $4\,\mathrm{m/s^2}$.')

question(5, 'O ângulo está nas medidas da rampa', 'Descida e tempo',
    r'(UECE) Um plano inclinado tem $10$ m de comprimento e $5$ m de altura. Uma caixa, com velocidade inicial nula, escorrega sem atrito. Se $g=10\,\mathrm{m/s^2}$, qual é o tempo para percorrer todo o comprimento do plano?', [],
    [r'Use a geometria: $\operatorname{sen}\theta=h/L=5/10=0{,}5$.',
     r'A aceleração na descida é $a=g\operatorname{sen}\theta=10\cdot0{,}5=5\,\mathrm{m/s^2}$.',
     r'Como o corpo parte do repouso, $L=\frac12at^2$. Então $10=\frac12\cdot5\cdot t^2$.',
     r'Logo $t^2=4$ e $t=2$ s. Alternativa D.'],
    r'$t=2$ s (D).',
    r'Na geometria, 5 m é a altura; na equação do movimento ao longo do plano, a distância percorrida é 10 m.',
    dict(kind='down', title='Altere a altura e o comprimento separadamente',
         base=dict(length=10, height=5, g=10), controls=[control('length','Comprimento da rampa',6,20,1,'m'),control('height','Altura vertical',1,9.5,.5,'m')],
         note='Mantemos 0 < altura < comprimento. Se uma mudança de comprimento exigir reduzir a altura, o controle a ajusta para continuar representando uma rampa possível. A massa não é necessária para calcular o tempo.',
         insight='Para uma mesma altura, uma rampa mais longa tem menor aceleração e demora mais; a velocidade de chegada continua dependendo apenas da altura.'),
    choices=['5 s','3 s','4 s','2 s'])

question(6, 'Da horizontal à primeira parada', 'Subida e parada',
    r'(UFGO) Um bloco desliza sobre um plano horizontal sem atrito, com velocidade constante de módulo $v_0$. Em seguida, sobe uma rampa de inclinação $\theta$, também sem atrito, até parar no ponto C. Calcule a distância BC ao longo da rampa, em função de $v_0$, $g$ e $\theta$.', [],
    [r'No trecho horizontal AB, não há resultante horizontal, portanto a velocidade permanece $v_0$. A entrada na rampa é tratada como uma transição ideal, sem perda de energia.',
     r'Na rampa, escolha o sentido positivo para cima: $a=-g\operatorname{sen}\theta$.',
     r'No ponto C, $v=0$. A equação $v^2=v_0^2+2a\,BC$ fica $0=v_0^2-2g\operatorname{sen}\theta\cdot BC$.',
     r'Isole a distância: $BC=\dfrac{v_0^2}{2g\operatorname{sen}\theta}$.',
     r'Pela energia, $\frac12mv_0^2=mg\,h$ e $h=BC\operatorname{sen}\theta$, o que produz a mesma fórmula. Ela vale para $g>0$ e $0<\theta<90^\circ$.'],
    r'$BC=\dfrac{v_0^2}{2g\operatorname{sen}\theta}$.',
    r'O fator $2g\operatorname{sen}\theta$ inteiro fica no denominador. BC é o comprimento na rampa, não a altura alcançada.',
    dict(kind='up', title='Explore a fórmula sem perder seu significado',
         base=dict(v0=10, sine=.5, g=10), controls=[control('v0','Velocidade em B',4,20,1,'m/s'),control('sine','Inclinação: sen θ',.1,.9,.05),control('g','Gravidade',4,12,1,'m/s²')],
         note='A resposta da lista é algébrica. Para a visualização, escolhemos inicialmente v₀ = 10 m/s, g = 10 m/s² e sen θ = 0,5. A animação começa em B; AB é mostrado apenas como referência. A transição ideal não simula uma colisão na quina.',
         insight='Observe a energia por unidade de massa: a energia cinética diminui enquanto a potencial aumenta. A soma permanece constante.', example=True))

question(7, 'Dois blocos, uma mesma aceleração', 'Fios e polias',
    r'(UEL-PR) Os blocos A e B, de massas $m_A=2$ kg e $m_B=3$ kg, estão ligados por um fio que passa por uma polia: A está sobre uma superfície horizontal e B sobre uma rampa de $30^\circ$. Despreze os atritos e considere o fio e a polia ideais. Adote $g=10\,\mathrm{m/s^2}$, $\operatorname{sen}30^\circ=0{,}5$ e $\cos30^\circ=0{,}87$. Determine a intensidade da tração no fio.', [],
    [r'O bloco B desce a rampa e puxa A na direção da polia. O fio ideal e inextensível impõe o mesmo módulo de aceleração aos dois blocos.',
     r'Em A, a força horizontal resultante é a tração: $T=m_Aa=2a$.',
     r'Em B, tomando a descida como positiva, $m_Bg\operatorname{sen}30^\circ-T=m_Ba$, ou $15-T=3a$.',
     r'Some as equações para eliminar a força interna T: $15=(2+3)a$. Logo $a=3\,\mathrm{m/s^2}$.',
     r'Volte ao bloco A: $T=2\cdot3=6$ N. A componente do peso em B, 15 N, não é igual à tração.',
     r'O cosseno não é necessário para T. Ele serviria para a normal em B: $N_B=m_Bg\cos30^\circ=30\cdot0{,}87=26{,}1$ N.'],
    r'$T=6$ N. O módulo da aceleração do sistema é $3\,\mathrm{m/s^2}$.',
    r'O fio transmite a mesma tração e vincula os deslocamentos. Não use T = mBg sen θ: B também está acelerando.',
    dict(kind='tablePulley', title='O que A anda, B percorre na rampa',
         base=dict(massA=2, massB=3, sine=.5, cosine=.87, g=10), controls=[control('massA','Massa de A',.5,6,.5,'kg'),control('massB','Massa de B',.5,6,.5,'kg')],
         note='Para animar, escolhemos partida do repouso e mostramos 1 s de movimento, sem colisões. Esses dados ilustrativos não alteram a e T. Os deslocamentos dos blocos têm o mesmo módulo e o comprimento do fio permanece constante.',
         insight='Aumente a massa de A mantendo B: a aceleração diminui, mas a tração aumenta. Compare as duas equações de Newton.'))

question(8, 'Uma massa desce; a outra sobe', 'Fios e polias',
    r'(UFPE) Um bloco de massa M desce um plano de $30^\circ$ com aceleração de módulo $2{,}0\,\mathrm{m/s^2}$, puxando por um fio o bloco suspenso de massa m. Não há atrito. Com $g=10\,\mathrm{m/s^2}$, determine a razão $M/m$.', [],
    [r'Escolha os sentidos positivos acompanhando o movimento: para M, descendo a rampa; para m, verticalmente para cima. Os módulos das acelerações são iguais a $a=2$.',
     r'Para o bloco na rampa: $Mg\operatorname{sen}30^\circ-T=Ma$. Portanto $5M-T=2M$, ou $T=3M$.',
     r'Para o bloco suspenso: $T-mg=ma$. Portanto $T-10m=2m$, ou $T=12m$.',
     r'A tração é a mesma nos dois trechos do fio: $3M=12m$. Logo $M/m=4$.',
     r'De forma geral, $M(g\operatorname{sen}\theta-a)=m(g+a)$ e $\dfrac{M}{m}=\dfrac{g+a}{g\operatorname{sen}\theta-a}$. Com $a=2$ e $\theta=30^\circ$, o denominador é $5-2=3>0$.'],
    r'$M/m=4$.',
    r'O bloco suspenso sobe. Por isso sua equação é T − mg = ma. Trocar esse sinal muda a razão entre as massas.',
    dict(kind='hangingPulley', title='Explore a razão que faz o sistema acelerar',
         base=dict(ratio=4, massSmall=1, sine=.5, g=10), controls=[control('ratio','Razão M/m',1,8,.25),control('massSmall','Massa suspensa m (ilustrativa)',.5,3,.5,'kg')],
         note='Para dar escala às forças, começamos com m = 1 kg e M = 4 kg; a lista só exige a razão. A animação mostra 1 s a partir do repouso. Ao mudar a razão, a aceleração deixa de ser necessariamente 2 m/s² e pode inverter de sentido.',
         insight='Experimente M/m = 2: os blocos ficam em equilíbrio. Com razão menor que 2, M sobe. Mudar as duas massas na mesma proporção não muda a aceleração.'),
    note='Usamos fio inextensível e de massa desprezível e polia ideal, que são as hipóteses do modelo de duas massas adotado na lista.')
