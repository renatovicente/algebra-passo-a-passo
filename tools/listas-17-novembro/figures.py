"""Deterministic SVG reconstructions; no external images or personal material."""
from math import sin, cos, pi, sqrt
from html import escape

INK = '#243f35'
SHADE = '#b9cda0'
PAPER = '#fffef9'


def point(cx, cy, r, angle):
    t = angle*pi/180
    return (cx+r*cos(t), cy+r*sin(t))


def xy(p):
    return f'{p[0]:.3f},{p[1]:.3f}'


def poly(points, fill='none', extra=''):
    return f'<polygon points="{" ".join(xy(p) for p in points)}" fill="{fill}" stroke="{INK}" stroke-width="1.7" {extra}/>'


def circle(x, y, r, fill='none', extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="1.7" {extra}/>'


def line(x1, y1, x2, y2, dashed=False):
    dash = 'stroke-dasharray="5 5"' if dashed else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="1.5" {dash}/>'


def text(x, y, value, size=18, anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{INK}">{escape(value)}</text>'


def path(d, fill='none', stroke=INK, extra=''):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="1.7" {extra}/>'


def sector(cx, cy, r, start, end, fill=SHADE):
    a, b = point(cx, cy, r, start), point(cx, cy, r, end)
    return path(f'M {cx},{cy} L {xy(a)} A {r},{r} 0 {int(end-start>180)} 1 {xy(b)} Z', fill)


def label_point(p, label, dx=0, dy=-10):
    return circle(*p, 2.3, INK) + text(p[0]+dx, p[1]+dy, label)


def right_angle(x, y, sx=1, sy=-1):
    return path(f'M {x+sx*11},{y} L {x+sx*11},{y+sy*11} L {x},{y+sy*11}')


def render(key):
    b = ''
    caption = 'Figura redesenhada a partir da lista. Medidas indicadas no enunciado.'
    description = ''
    if key == 'geo-01':
        b += poly([(185,100),(295,100),(295,210),(185,210)], SHADE)
        for x,y in [(185,100),(295,100),(185,210),(295,210)]:
            b += circle(x,y,55,PAPER) + circle(x,y,2.5,INK)
        b += poly([(185,100),(295,100),(295,210),(185,210)], extra='stroke-dasharray="5 4"')
        b += line(185,100,240,100) + text(212,89,'1')
        description = 'Quatro círculos tangentes de raio 1. Seus centros formam um quadrado. A região central entre os quatro arcos está sombreada.'
    elif key == 'geo-02':
        o=(160,245); a=point(*o,180,-90); c=point(*o,180,-30)
        b += sector(*o,180,-90,-30,PAPER)
        b += path(f'M {xy(a)} A 180,180 0 0 1 {xy(c)} L {xy(a)} Z',SHADE)
        b += poly([o,a,c]) + path(f'M {xy(point(*o,45,-90))} A 45,45 0 0 1 {xy(point(*o,45,-30))}')
        b += text(192,190,'60°') + text(143,157,'2 cm') + text(246,222,'2 cm') + label_point(o,'O',-10,20)
        description = 'Setor de raio 2 cm e ângulo de 60 graus. A região entre sua corda e seu arco está sombreada.'
    elif key == 'geo-03':
        b += poly([(130,50),(350,50),(350,270),(130,270)],PAPER)
        for x,y in [(185,105),(295,105),(185,215),(295,215)]: b += circle(x,y,55,SHADE)
        b += line(130,105,240,105,True) + text(185,95,'10 cm')
        caption = 'Os quatro discos cinza são recortados. A pergunta pede a sobra branca entre eles e a chapa.'
        description = 'Quatro discos de diâmetro 10 cm, em duas linhas e duas colunas, tangentes entre si e a uma chapa quadrada.'
    elif key == 'geo-04':
        b += circle(240,145,108,SHADE)
        b += poly([(240,145),(177.646,253),(302.354,253)])
        b += line(240,145,240,253,True)+right_angle(240,253)
        for p,n,dx,dy in [((240,145),'O',0,-12),((177.646,253),'A',-10,20),((302.354,253),'B',10,20)]:b+=label_point(p,n,dx,dy)
        b += text(253,207,'r',anchor='start')
        description = 'Triângulo equilátero OAB. O círculo tem centro no vértice O e tangencia o lado AB; seu raio perpendicular a AB coincide com a altura do triângulo.'
    elif key in ['geo-05','geo-07']:
        r=55 if key=='geo-05' else 110*2/3
        b+=circle(240,155,110,SHADE)+circle(240,155,r,PAPER)
        b+=line(240,155,350,155,True)+line(240,155,240,155-r,True)
        b+=circle(240,155,2.5,INK)+text(304,146,'1' if key=='geo-05' else '9 cm')+text(223,145-r/2,'1/2' if key=='geo-05' else '6 cm',anchor='end')
        description = ('Círculos concêntricos com raios 1 e 1/2.' if key=='geo-05' else 'Círculos concêntricos com raios 9 cm e 6 cm.')+' A coroa entre as circunferências está sombreada.'
    elif key=='geo-06':
        b+=poly([(130,50),(350,50),(350,270),(130,270)],PAPER)
        b+=poly([(130,105),(295,50),(350,215),(185,270)],SHADE)
        b+=text(322,39,'x')+text(116,82,'x')+text(106,190,'8 − x')+text(158,291,'x')+text(370,246,'x')
        b+=text(240,316,'Lado externo: 8 cm',14)
        description='Quadrado externo de lado 8 cm e quadrado interno girado. Cada lado externo é dividido em x e 8 menos x pelos vértices do quadrado interno.'
    elif key=='geo-08':
        o=(240,160); radius=140
        vertices=[point(*o,radius,a) for a in [-120,-60,0,60,120,180]]
        b+=poly(vertices,SHADE)
        b+=sector(100,160,140,-60,60,PAPER)+sector(380,160,140,120,240,PAPER)
        b+=poly(vertices)
        for p,name in zip(vertices,['F','A','B','C','D','E']):
            dx=14 if name=='B' else -14 if name=='E' else 0
            dy=-10 if name in ['F','A'] else 20 if name in ['C','D'] else 5
            b+=text(p[0]+dx,p[1]+dy,name)
        b+=line(100,160,240,160,True)+line(240,160,380,160,True)+text(165,149,'4 cm')+text(316,149,'4 cm')
        description='Hexágono regular ABCDEF. Dois setores brancos de raio 4 cm, centrados nos vértices opostos B e E, deixam duas regiões sombreadas entre os arcos e os lados FA e DC.'
    elif key=='geo-09':
        vertices=[point(240,155,110,a) for a in [210,330,90]]
        b+=circle(240,155,110,SHADE)+circle(240,155,55,PAPER)+poly(vertices)
        b+=line(240,155,240,265,True)+line(240,155,240,100,True)+text(255,214,'R')+text(225,132,'r')+text(240,86,'6 cm')
        description='Triângulo equilátero de lado 6 cm, inscrito na circunferência maior e circunscrito à menor. As duas circunferências têm o mesmo centro.'
    elif key=='geo-10':
        vertices=[point(240,155,120,a) for a in range(0,360,60)]
        r=120*sqrt(3)/2
        b+=poly(vertices,SHADE)+circle(240,155,r)+poly(vertices)
        b+=line(240,155,240,155-r,True)+right_angle(240,155-r,1,1)+text(257,113,'a = 2√3 cm',14,anchor='start')
        caption='O raio inscrito é o apótema. A área pedida é a de todo o hexágono, incluindo a região do círculo.'
        description='Hexágono regular e circunferência inscrita. O raio perpendicular a um lado é o apótema de medida 2 raiz de 3 cm.'
    elif key=='geo-11':
        b+=circle(240,155,68,SHADE)
        for a in [-90,0,90,180]: b+=poly([(240,155),point(240,155,125,a-30),point(240,155,125,a+30)],PAPER)
        b+=circle(240,155,68)+circle(240,155,2.5,INK)
        b+=path(f'M {xy(point(240,155,35,-120))} A 35,35 0 0 1 {xy(point(240,155,35,-60))}')+text(240,111,'60°',13)
        caption='A área do círculo é 36 cm². As partes sombreadas são os quatro intervalos entre os triângulos.'
        description='Quatro triângulos equiláteros com vértice comum no centro de um círculo. Seus quatro ângulos centrais são de 60 graus; os espaços entre eles ficam sombreados dentro do círculo.'
    elif key=='geo-12':
        vertices=[point(240,155,112,a) for a in range(0,360,60)]
        b+=circle(240,155,112)+poly(vertices)+circle(240,155,112*sqrt(3)/2,SHADE)
        b+=line(240,155,352,155,True)+line(240,155,240,155-112*sqrt(3)/2,True)
        b+=text(298,145,'3 cm')+text(225,107,'r')+text(284,215,'C₁')+text(369,161,'C₂')
        description='Hexágono entre as circunferências C1, inscrita, e C2, circunscrita. O raio externo é 3 cm e o círculo interno é a área solicitada.'
    elif key=='geo-13':
        b+=poly([(140,255),(140,155),(240,155),(340,255)],SHADE)
        b+=poly([(140,55),(140,255),(340,255)])+circle(190,205,50,PAPER)
        b+=line(140,155,240,155)+right_angle(140,255)
        for p,n,dx,dy in [((140,55),'A',0,-12),((140,255),'B',-12,18),((340,255),'C',12,18),((140,155),'M',-15,5),((240,155),'N',12,-7)]: b+=text(p[0]+dx,p[1]+dy,n)
        b+=line(102,55,102,255)+line(97,55,107,55)+line(97,255,107,255)+text(91,145,'8 cm',14,anchor='end')+text(240,288,'8 cm')
        description='Triângulo retângulo ABC com AB e BC medindo 8 cm. M está no ponto médio de AB, N no de AC. O trapézio BMNC está sombreado, exceto o círculo tangente a MB, BC e MN.'
    elif key=='geo-14':
        b+=poly([(100,190),(300,190),(300,40)],SHADE)
        b+=path('M 100,190 A 100,100 0 0 0 300,190 Z',SHADE)
        b+=line(100,190,300,190,True)+right_angle(300,190,-1,-1)
        b+=text(181,102,'5 cm')+text(322,123,'3 cm')+text(200,178,'d')
        description='Triângulo retângulo de hipotenusa 5 cm e cateto vertical 3 cm. O outro cateto é diâmetro de um semicírculo situado abaixo do triângulo.'
    elif key=='geo-15':
        b+=circle(260,155,112,SHADE)+circle(204,155,56,PAPER)
        b+=line(260,43,260,267,True)+text(279,234,'24 cm')+line(148,155,260,155,True)+text(204,145,'d')+line(260,155,372,155,True)+text(321,145,'R')
        caption='O diâmetro menor d é igual ao raio maior R. A região sombreada exclui o disco menor.'
        description='Dois círculos tangentes internamente, com centros distintos. O diâmetro maior é 24 cm; o diâmetro menor coincide com um raio do maior.'
    elif key=='geo-16':
        b+=poly([(130,45),(350,45),(350,265),(130,265)],PAPER)
        for pts in [[(130,45),(240,45),(240,155)],[(350,45),(350,155),(240,155)],[(350,265),(240,265),(240,155)],[(130,265),(130,155),(240,155)]]:b+=poly(pts,INK)
        b+=circle(240,155,110,PAPER)
        b+=sector(240,155,110,-90,-45,INK)+sector(240,155,110,90,135,INK)
        for ends in [(130,45,350,265),(130,265,350,45),(130,155,350,155),(240,45,240,265)]:b+=line(*ends)
        b+=circle(240,155,110)+text(297,179,'3 cm')
        description='Logotipo: círculo inscrito em quadrado, dividido por diagonais e eixos. Dentro do círculo, dois setores opostos de 45 graus estão pretos; fora dele, metade de cada um dos quatro cantos está preta.'
    elif key=='geo-17':
        b+=poly([(120,35),(360,35),(360,275),(120,275)],PAPER)
        b+=path('M 120,275 L 240,155 A 120,120 0 0 1 360,275 Z',SHADE)
        b+=path('M 120,275 A 120,120 0 0 1 360,275')+line(120,275,360,35)
        b+=line(240,275,360,275)+text(101,158,'4')+text(296,299,'raio 2')
        description='Quadrado de lado 4 com diagonal do canto inferior esquerdo ao superior direito. Um semicírculo de raio 2 tem diâmetro no lado inferior. A região sombreada fica dentro do semicírculo e abaixo da diagonal.'
    elif key=='mat-05':
        def p(x,y):return (64+(x+4)*36,227-y*10)
        b+=line(*p(-4.5,0),*p(5.55,0))+line(*p(0,-7.5),*p(0,16.5))
        for n in range(-4,6):
            x,y=p(n,0); b+=line(x,y-4,x,y+4)+text(x,y+19,str(n),12)
        samples=[-4.2+i*9.4/160 for i in range(161)]
        d='M '+' L '.join(xy(p(x,(x+2)*(x-3))) for x in samples)
        b+=path(d,extra='class="curve-f"')+path('M '+xy(p(-4.4,-4.4))+' L '+xy(p(5.5,5.5)),stroke='#a04f2c',extra='stroke-dasharray="7 4"')
        b+=text(432,222,'x')+text(220,57,'y')+text(347,29,'f: parábola',13)+text(347,49,'g: reta tracejada',13)
        description='Gráfico da parábola f de raízes -2 e 3, e da reta g que passa pela origem e tem inclinação positiva. O eixo x mostra o intervalo de -4 a 5.'
        caption='Curvas redesenhadas a partir das funções do enunciado. As escalas horizontal e vertical são diferentes.'
    elif key=='mat-08':
        from math import log2
        def p(x,y):return (145+x*65,220-y*60)
        b+=poly([p(0,0),p(1,0),p(1,1),p(0,1)],SHADE)
        b+=line(*p(-1.1,0),*p(4,0))+line(*p(0,-1.25),*p(0,2.7))
        xs=[-.7+i*4.5/140 for i in range(141)]
        b+=path('M '+' L '.join(xy(p(x,log2(x+1))) for x in xs))
        b+=circle(*p(1,1),3,INK)+text(252,146,'(a/2, 1)',14)+text(210,239,'a/2',13)+text(132,165,'1',13)+text(134,239,'0',13)+text(416,225,'x')+text(133,55,'y')
        description='Curva logarítmica crescente passando pela origem e pelo ponto de coordenadas a/2 e 1. Um retângulo sombreado tem esses dois pontos como vértices opostos.'
    else:
        raise ValueError(f'Figura desconhecida: {key}')
    viewbox = '35 10 400 310' if key.startswith('geo-') else '0 0 480 330'
    return (f'<figure class="exercise-figure"><svg viewBox="{viewbox}" role="img" aria-labelledby="figure-title-{key} figure-desc-{key}" xmlns="http://www.w3.org/2000/svg">'
            f'<title id="figure-title-{key}">Figura da questão {int(key[-2:])}</title><desc id="figure-desc-{key}">{escape(description)}</desc>{b}</svg><figcaption>{escape(caption)}</figcaption></figure>')
