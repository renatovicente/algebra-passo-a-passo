"""Enunciados transcritos das quatro fotos e vinte problemas inéditos.

Cada item mantém um resultado explícito, passos e um alerta didático.
Não incluir imagens, nomes, notas ou identificações das folhas.
"""

ITEMS = []


def add(id, label, title, topic, prompt, steps, answer, pitfall, reference=None):
    ITEMS.append(dict(id=id, label=label, title=title, topic=topic,
                      kind='original' if id.startswith('foto') else 'treino',
                      prompt=prompt, steps=steps, answer=answer,
                      pitfall=pitfall, reference=reference))


add('foto-1', 'Questão 1', 'pH e concentração', 'pH',
    r'O pH de uma solução é calculado por $\mathrm{pH}=-\log[\mathrm{H_3O^+}]$, usando o valor numérico da concentração em mol/L. Uma substância tem concentração de íons de hidrogênio de $0{,}0032$ mol/L. Qual é seu pH? Use $\log 2\approx0{,}3$.',
    [r'Sem base indicada, $\log$ tem base 10. Escreva a concentração como produto: $0{,}0032=32\cdot10^{-4}=2^5\cdot10^{-4}$.',
     r'Use as propriedades: $\log(2^5\cdot10^{-4})=5\log2+\log10^{-4}=5\log2-4$.',
     r'Substitua a aproximação dada: $\log(0{,}0032)\approx5\cdot0{,}3-4=-2{,}5$.',
     r'Aplique o sinal negativo da fórmula: $\mathrm{pH}\approx-(-2{,}5)=2{,}5$. O pH é adimensional.',
     r'Confira a ordem de grandeza: $10^{-3}<0{,}0032<10^{-2}$, então o pH deve estar entre 2 e 3.'],
    r'$\mathrm{pH}\approx2{,}5$.',
    r'O sinal de menos está fora do logaritmo. Não transforme $-\log c$ em $\log(-c)$ nem confunda o logaritmo com o seu argumento.')

add('foto-2a', 'Questão 2a', 'Produto, potência e quociente', 'Propriedades',
    r'Sejam $a,b,c$ reais positivos, com $b\ne1$. Se $\log_ba=1{,}42$ e $\log_bc=-0{,}16$, determine $\log_b\left(\dfrac{a^2b}{c}\right)$.',
    [r'Separe produto e quociente: $\log_b(a^2b/c)=\log_b(a^2)+\log_bb-\log_bc$.',
     r'O expoente vira um fator e o logaritmo da própria base vale 1: $2\log_ba+1-\log_bc$.',
     r'Substitua os valores com parênteses: $2\cdot1{,}42+1-(-0{,}16)$.',
     r'Calcule: $2{,}84+1+0{,}16=4$.'],
    r'$4$.',
    r'$\log_b(a^2)=2\log_ba$, e não $(\log_ba)^2$. O fator $b$ dentro do argumento contribui com $\log_bb=1$.')

add('foto-2b', 'Questão 2b', 'Uma raiz na base', 'Raízes e decimais',
    r'Sabendo que $A=\log_{\sqrt[3]{7}}7+\log0{,}001$, determine o valor de $A$.',
    [r'Escreva a base como potência: $\sqrt[3]{7}=7^{1/3}$.',
     r'Pela definição, $\log_{7^{1/3}}7=y$ equivale a $(7^{1/3})^y=7^1$. Logo $y/3=1$ e $y=3$.',
     r'Como $0{,}001=10^{-3}$, temos $\log0{,}001=-3$.',
     r'Some os dois termos: $A=3+(-3)=0$.'],
    r'$A=0$.',
    r'A raiz está na base do primeiro logaritmo. O índice 3 produz o valor 3, não $1/3$.')

add('foto-2c', 'Questão 2c', 'Base menor que um', 'Mudança de base',
    r'Se $\log_23=a$ e $\log_25=b$, determine, em função de $a$ e $b$, o valor de $\log_{0{,}5}75$.',
    [r'Fatore o argumento: $75=3\cdot5^2$.',
     r'Mude para a base 2: $\log_{0{,}5}75=\dfrac{\log_275}{\log_20{,}5}$.',
     r'No numerador, $\log_275=\log_23+2\log_25=a+2b$.',
     r'No denominador, $0{,}5=2^{-1}$, portanto $\log_20{,}5=-1$.',
     r'Divida: $(a+2b)/(-1)=-a-2b$. O sinal negativo faz sentido: uma base entre 0 e 1 precisa de expoente negativo para gerar 75.'],
    r'$-a-2b$.',
    r'Na mudança de base, o logaritmo da base vai no denominador. Dividir por $-1$ troca o sinal de toda a expressão.')

add('foto-3', 'Questão 3', 'Produto dos seis expoentes', 'Produtos de logaritmos',
    r'Sejam $x_1,x_2,x_3,x_4,x_5,x_6$ reais tais que $2^{x_1}=4$, $3^{x_2}=5$, $4^{x_3}=6$, $5^{x_4}=7$, $6^{x_5}=8$ e $7^{x_6}=9$. Calcule $x_1x_2x_3x_4x_5x_6$.',
    [r'Traduza cada igualdade pela definição: $x_1=\log_24$, $x_2=\log_35$, $x_3=\log_46$, $x_4=\log_57$, $x_5=\log_68$ e $x_6=\log_79$.',
     r'Use uma base comum, por exemplo 10: $P=\dfrac{\log4}{\log2}\cdot\dfrac{\log5}{\log3}\cdot\dfrac{\log6}{\log4}\cdot\dfrac{\log7}{\log5}\cdot\dfrac{\log8}{\log6}\cdot\dfrac{\log9}{\log7}$.',
     r'Cancele os fatores iguais e não nulos $\log4$, $\log5$, $\log6$ e $\log7$. Sobram $P=\dfrac{\log8\cdot\log9}{\log2\cdot\log3}$.',
     r'Use $8=2^3$ e $9=3^2$: $P=\dfrac{3\log2\cdot2\log3}{\log2\cdot\log3}=3\cdot2=6$.'],
    r'$6$.',
    r'Não há motivo para os expoentes formarem uma progressão geométrica. Aqui, a simplificação ocorre entre fatores de frações após a mudança de base.')

add('foto-4a', 'Questão 4a', 'Uma fração com logaritmos', 'Aproximações e frações',
    r'Considere $\log2\approx0{,}3$, $\log3\approx0{,}5$ e $\log5\approx0{,}7$. Calcule $E=\dfrac{\log(\sqrt[3]{72})\cdot(\log4)\cdot(\log27)}{(\log360)\cdot(\log16)}$, deixando o resultado obtido com essas aproximações como fração irredutível.',
    [r'Fatore $72=2^3\cdot3^2$. Então $\log(\sqrt[3]{72})=\frac13(3\log2+2\log3)\approx\frac13(0{,}9+1)=\frac{19}{30}$.',
     r'Calcule os outros fatores do numerador: $\log4=2\log2\approx\frac35$ e $\log27=3\log3\approx\frac32$.',
     r'Como $360=2^3\cdot3^2\cdot5$, temos $\log360\approx0{,}9+1+0{,}7=\frac{13}{5}$. Além disso, $\log16=4\log2\approx\frac65$.',
     r'Mantenha os produtos de logaritmos: $E\approx\dfrac{\frac{19}{30}\cdot\frac35\cdot\frac32}{\frac{13}{5}\cdot\frac65}=\dfrac{57/100}{78/25}$.',
     r'Divida multiplicando pelo inverso: $\frac{57}{100}\cdot\frac{25}{78}=\frac{57}{312}=\frac{19}{104}$. Como $104=2^3\cdot13$, não há fator comum com 19.',
     r'A fração é exata para os números aproximados fornecidos. Ela não é o valor exato da expressão com logaritmos reais.'],
    r'$\dfrac{19}{104}$, usando as aproximações do enunciado.',
    r'$\log u\cdot\log v$ é um produto de números. Não é $\log(uv)$: esta última expressão corresponde à soma $\log u+\log v$.')

add('foto-4b', 'Questão 4b', 'Três bases, uma incógnita', 'Equações',
    r'Seja $x>0$ tal que $\log_2x+\log_4x-\log_8x=1$. Determine $x$, escrevendo o resultado na forma de uma potência.',
    [r'As bases são potências de 2. Use $\log_4x=\frac12\log_2x$ e $\log_8x=\frac13\log_2x$.',
     r'Faça $t=\log_2x$. A equação vira $t+\frac12t-\frac13t=1$.',
     r'Some os coeficientes com denominador 6: $\left(\frac66+\frac36-\frac26\right)t=\frac76t=1$.',
     r'Logo $t=\frac67$. Volte à definição: $\log_2x=\frac67$ implica $x=2^{6/7}$.',
     r'Verifique: $\frac67+\frac37-\frac27=1$. A potência encontrada é positiva e respeita o domínio.'],
    r'$x=2^{6/7}$.',
    r'O resultado $6/7$ é o valor de $\log_2x$. Para encontrar $x$, ainda é preciso aplicar a definição do logaritmo.')

# Treino 01–03: aplicação do logaritmo decimal.
add('treino-01', 'Treino 01', 'Uma concentração menor', 'pH',
    r'Uma solução tem $[\mathrm{H_3O^+}]=0{,}0008$ mol/L. Use $\mathrm{pH}=-\log[\mathrm{H_3O^+}]$ e $\log2\approx0{,}3$ para calcular o pH.',
    [r'$0{,}0008=8\cdot10^{-4}=2^3\cdot10^{-4}$.',
     r'$\log(0{,}0008)=3\log2-4\approx0{,}9-4=-3{,}1$.',
     r'$\mathrm{pH}\approx-(-3{,}1)=3{,}1$.'],
    r'$\mathrm{pH}\approx3{,}1$.', r'A potência de 10 precisa reproduzir a posição da vírgula: $8\cdot10^{-4}=0{,}0008$.', 'foto-1')
add('treino-02', 'Treino 02', 'Concentração e potência de dois', 'pH',
    r'Calcule o pH de uma solução com $[\mathrm{H_3O^+}]=0{,}0016$ mol/L. Use $\mathrm{pH}=-\log[\mathrm{H_3O^+}]$ e $\log2\approx0{,}3$.',
    [r'$0{,}0016=16\cdot10^{-4}=2^4\cdot10^{-4}$.',
     r'$\log(0{,}0016)=4\log2-4\approx1{,}2-4=-2{,}8$.',
     r'$\mathrm{pH}\approx2{,}8$.'],
    r'$\mathrm{pH}\approx2{,}8$.', r'O expoente 4 multiplica $\log2$; ele não eleva $0{,}3$ à quarta potência.', 'foto-1')
add('treino-03', 'Treino 03', 'Mais casas decimais', 'pH',
    r'Uma solução tem concentração de íons de hidrogênio de $0{,}000064$ mol/L. Use $\mathrm{pH}=-\log[\mathrm{H_3O^+}]$ e $\log2\approx0{,}3$. Qual é o pH?',
    [r'$0{,}000064=64\cdot10^{-6}=2^6\cdot10^{-6}$.',
     r'$\log(0{,}000064)=6\log2-6\approx1{,}8-6=-4{,}2$.',
     r'$\mathrm{pH}\approx4{,}2$. Como a concentração está entre $10^{-5}$ e $10^{-4}$, o pH entre 4 e 5 é coerente.'],
    r'$\mathrm{pH}\approx4{,}2$.', r'Conte as casas decimais ao montar a potência de 10 e aplique o sinal negativo só no final.', 'foto-1')

add('treino-04', 'Treino 04', 'Cubo no numerador', 'Propriedades',
    r'Para $a,b,c>0$ e $b\ne1$, sabe-se que $\log_ba=0{,}8$ e $\log_bc=-0{,}2$. Calcule $\log_b(a^3b/c^2)$.',
    [r'$\log_b(a^3b/c^2)=3\log_ba+\log_bb-2\log_bc$.',
     r'$3\cdot0{,}8+1-2\cdot(-0{,}2)=2{,}4+1+0{,}4$.',
     r'O resultado é $3{,}8$.'], r'$3{,}8$.', r'Os expoentes multiplicam os logaritmos. Subtrair um número negativo gera uma soma.', 'foto-2a')
add('treino-05', 'Treino 05', 'Uma raiz no argumento', 'Propriedades',
    r'Para $a,b,c>0$ e $b\ne1$, sejam $\log_ba=1{,}2$ e $\log_bc=0{,}4$. Calcule $\log_b(\sqrt a/(bc))$.',
    [r'$\log_b(\sqrt a/(bc))=\frac12\log_ba-\log_bb-\log_bc$.',
     r'$\frac12\cdot1{,}2-1-0{,}4=0{,}6-1-0{,}4$.',
     r'O resultado é $-0{,}8$.'], r'$-0{,}8$.', r'O denominador inteiro é subtraído: tanto o fator $b$ quanto o fator $c$.', 'foto-2a')
add('treino-06', 'Treino 06', 'Duas potências e um quociente', 'Propriedades',
    r'Para $a,b,c>0$ e $b\ne1$, sejam $\log_ba=-0{,}3$ e $\log_bc=0{,}6$. Determine $\log_b(a^2b^3/c)$.',
    [r'$\log_b(a^2b^3/c)=2\log_ba+3\log_bb-\log_bc$.',
     r'$2\cdot(-0{,}3)+3-0{,}6=-0{,}6+3-0{,}6$.',
     r'O resultado é $1{,}8$.'], r'$1{,}8$.', r'$\log_b(b^3)=3$ para toda base permitida, não apenas para a base 10.', 'foto-2a')

add('treino-07', 'Treino 07', 'Raiz quarta e decimal', 'Raízes e decimais',
    r'Calcule $A=\log_{\sqrt[4]{5}}25+\log0{,}0001$.',
    [r'$\sqrt[4]{5}=5^{1/4}$ e $25=5^2$. Se $(5^{1/4})^y=5^2$, então $y/4=2$ e $y=8$.',
     r'$\log0{,}0001=\log10^{-4}=-4$.',
     r'$A=8-4=4$.'], r'$A=4$.', r'Considere o expoente do argumento e o da base: $\log_{5^{1/4}}5^2=2/(1/4)$.', 'foto-2b')
add('treino-08', 'Treino 08', 'Raiz cúbica e quadrado', 'Raízes e decimais',
    r'Determine $B=\log_{\sqrt[3]{2}}4+\log0{,}01$.',
    [r'$\log_{2^{1/3}}2^2=2/(1/3)=6$.',
     r'$\log0{,}01=\log10^{-2}=-2$.',
     r'$B=6-2=4$.'], r'$B=4$.', r'Um número decimal entre 0 e 1 tem logaritmo decimal negativo.', 'foto-2b')

add('treino-09', 'Treino 09', 'Quarenta e cinco na base um meio', 'Mudança de base',
    r'Sabendo que $\log_23=a$ e $\log_25=b$, escreva $\log_{1/2}45$ em função de $a$ e $b$.',
    [r'$45=3^2\cdot5$, logo $\log_245=2a+b$.',
     r'$\log_2(1/2)=-1$. Pela mudança de base, $\log_{1/2}45=(2a+b)/(-1)$.',
     r'O resultado é $-2a-b$.'], r'$-2a-b$.', r'O fator 2 pertence ao logaritmo de 3, pois $45=3^2\cdot5$.', 'foto-2c')
add('treino-10', 'Treino 10', 'Uma base igual a um quarto', 'Mudança de base',
    r'Sejam $\log_23=a$ e $\log_25=b$. Escreva $\log_{1/4}150$ em função de $a$ e $b$.',
    [r'$150=2\cdot3\cdot5^2$, então $\log_2150=1+a+2b$.',
     r'$1/4=2^{-2}$, logo $\log_2(1/4)=-2$.',
     r'$\log_{1/4}150=\dfrac{1+a+2b}{-2}=-\dfrac{1+a+2b}{2}$.'],
    r'$-\dfrac{1+a+2b}{2}$.', r'A base $1/4$ produz o denominador $-2$, não $-1$.', 'foto-2c')
add('treino-11', 'Treino 11', 'Quociente no argumento', 'Mudança de base',
    r'Sejam $\log_32=a$ e $\log_35=b$. Determine $\log_{1/3}(20/9)$ em função de $a$ e $b$.',
    [r'$20/9=2^2\cdot5/3^2$, logo $\log_3(20/9)=2a+b-2$.',
     r'$\log_3(1/3)=-1$. Divida o numerador inteiro por $-1$.',
     r'$\log_{1/3}(20/9)=-(2a+b-2)=2-2a-b$.'],
    r'$2-2a-b$.', r'Troque também o sinal do termo $-2$ ao dividir a expressão por $-1$.', 'foto-2c')

add('treino-12', 'Treino 12', 'Uma cadeia de três expoentes', 'Produtos de logaritmos',
    r'Sejam $2^u=3$, $3^v=5$ e $5^w=16$. Calcule $uvw$.',
    [r'$u=\log_23$, $v=\log_35$ e $w=\log_516$.',
     r'$uvw=\dfrac{\log3}{\log2}\cdot\dfrac{\log5}{\log3}\cdot\dfrac{\log16}{\log5}=\dfrac{\log16}{\log2}$.',
     r'Como $16=2^4$, o produto vale $4$.'], r'$4$.', r'Cancele fatores idênticos entre numeradores e denominadores, não argumentos isolados.', 'foto-3')
add('treino-13', 'Treino 13', 'Quatro elos na cadeia', 'Produtos de logaritmos',
    r'Sejam $3^u=4$, $4^v=5$, $5^w=6$ e $6^z=81$. Calcule $uvwz$.',
    [r'Escreva o produto como $\log_34\cdot\log_45\cdot\log_56\cdot\log_681$.',
     r'Na base 10, os fatores intermediários $\log4$, $\log5$ e $\log6$ se cancelam. Sobra $\log81/\log3=\log_381$.',
     r'Como $81=3^4$, temos $uvwz=4$.'], r'$4$.', r'O produto final depende dos extremos da cadeia; não é necessário aproximar cada expoente.', 'foto-3')
add('treino-14', 'Treino 14', 'Duas cadeias intercaladas', 'Produtos de logaritmos',
    r'Sejam $2^{x_1}=4$, $3^{x_2}=5$, $4^{x_3}=8$ e $5^{x_4}=27$. Determine $x_1x_2x_3x_4$.',
    [r'$P=\dfrac{\log4}{\log2}\cdot\dfrac{\log5}{\log3}\cdot\dfrac{\log8}{\log4}\cdot\dfrac{\log27}{\log5}$.',
     r'Cancele $\log4$ e $\log5$. Então $P=\dfrac{\log8}{\log2}\cdot\dfrac{\log27}{\log3}$.',
     r'$P=\log_28\cdot\log_327=3\cdot3=9$.'], r'$9$.', r'As duas cadeias deixam dois quocientes. Não transforme tudo em um único logaritmo sem justificativa.', 'foto-3')

APPROX = r'Use $\log2\approx0{,}3$, $\log3\approx0{,}5$ e $\log5\approx0{,}7$. Escreva o resultado obtido com esses valores como fração irredutível. '
add('treino-15', 'Treino 15', 'Raiz quadrada no numerador', 'Aproximações e frações',
    APPROX + r'Calcule $E=\dfrac{\log(\sqrt{18})\cdot\log8}{\log45\cdot\log4}$.',
    [r'$18=2\cdot3^2$, então $\log\sqrt{18}=\frac12(\log2+2\log3)\approx\frac{13}{20}$.',
     r'$\log8\approx\frac9{10}$, $\log45=2\log3+\log5\approx\frac{17}{10}$ e $\log4\approx\frac35$.',
     r'$E\approx\dfrac{(13/20)(9/10)}{(17/10)(3/5)}=\dfrac{117/200}{51/50}=\dfrac{117}{204}=\dfrac{39}{68}$.'],
    r'$\dfrac{39}{68}$, com as aproximações dadas.', r'A raiz quadrada introduz um fator $1/2$ no logaritmo de 18.', 'foto-4a')
add('treino-16', 'Treino 16', 'Um cancelamento depois das contas', 'Aproximações e frações',
    APPROX + r'Calcule $F=\dfrac{\log(\sqrt[3]{500})\cdot\log9}{\log50\cdot\log8}$.',
    [r'$500=2^2\cdot5^3$, então $\log\sqrt[3]{500}=\frac13(2\log2+3\log5)\approx\frac13(0{,}6+2{,}1)=\frac9{10}$.',
     r'$\log9\approx1$, $\log50=\log2+2\log5\approx\frac{17}{10}$ e $\log8\approx\frac9{10}$.',
     r'$F\approx\dfrac{(9/10)\cdot1}{(17/10)(9/10)}=\dfrac{10}{17}$.'],
    r'$\dfrac{10}{17}$, com as aproximações dadas.', r'O cancelamento de $9/10$ vale para os fatores numéricos calculados com as aproximações; os logaritmos originais não são iguais.', 'foto-4a')
add('treino-17', 'Treino 17', 'Fatorar antes de substituir', 'Aproximações e frações',
    APPROX + r'Calcule $G=\dfrac{\log(\sqrt{80})\cdot\log25}{\log200\cdot\log4}$.',
    [r'$80=2^4\cdot5$, logo $\log\sqrt{80}=\frac12(4\log2+\log5)\approx\frac{19}{20}$.',
     r'$\log25\approx\frac75$. Como $200=2^3\cdot5^2$, temos $\log200\approx\frac{23}{10}$. Por fim, $\log4\approx\frac35$.',
     r'$G\approx\dfrac{(19/20)(7/5)}{(23/10)(3/5)}=\dfrac{133/100}{69/50}=\dfrac{133}{138}$.',
     r'$133=7\cdot19$ e $138=2\cdot3\cdot23$, portanto a fração é irredutível.'],
    r'$\dfrac{133}{138}$, com as aproximações dadas.', r'$200=2^3\cdot5^2$. Confira a fatoração antes de aplicar as propriedades.', 'foto-4a')

add('treino-18', 'Treino 18', 'Bases três, nove e vinte e sete', 'Equações',
    r'Resolva, para $x>0$, $\log_3x+\log_9x-\log_{27}x=2$. Escreva a resposta como potência.',
    [r'Faça $t=\log_3x$. Como $9=3^2$ e $27=3^3$, a equação vira $t+\frac12t-\frac13t=2$.',
     r'$\frac76t=2$, logo $t=\frac{12}{7}$.',
     r'$x=3^{12/7}$. Conferindo: $\frac{12}{7}+\frac67-\frac47=2$.'],
    r'$x=3^{12/7}$.', r'O segundo membro é 2: multiplique $6/7$ por 2 ao isolar $t$.', 'foto-4b')
add('treino-19', 'Treino 19', 'Um coeficiente antes do logaritmo', 'Equações',
    r'Resolva $2\log_2x-\log_4x+\log_8x=11$, com $x>0$. Dê a resposta na forma de potência.',
    [r'Faça $t=\log_2x$. A equação fica $2t-\frac12t+\frac13t=11$.',
     r'$\left(\frac{12}{6}-\frac36+\frac26\right)t=\frac{11}{6}t=11$, então $t=6$.',
     r'$x=2^6$. Verifique: $2\cdot6-3+2=11$.'],
    r'$x=2^6=64$.', r'Preserve o coeficiente 2 do primeiro termo e o sinal negativo do segundo.', 'foto-4b')
add('treino-20', 'Treino 20', 'Uma solução entre zero e um', 'Equações',
    r'Resolva $\log_2x+\log_4x-\log_8x=-1$, com $x>0$. Escreva o resultado como potência.',
    [r'Faça $t=\log_2x$. Então $t+\frac12t-\frac13t=-1$.',
     r'$\frac76t=-1$, logo $t=-\frac67$.',
     r'$x=2^{-6/7}$. É um número positivo menor que 1.',
     r'Conferindo: $-\frac67-\frac37+\frac27=-1$.'],
    r'$x=2^{-6/7}$.', r'Logaritmo negativo não implica argumento negativo: o argumento $x$ continua positivo.', 'foto-4b')
