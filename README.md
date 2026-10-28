# Álgebra, passo a passo

Página de estudo com 407 exercícios em oito cadernos. A aba principal tem 100 exercícios de manipulação algébrica para o primeiro ano do ensino médio, soluções detalhadas e alertas sobre erros comuns.

**Acesse:** https://renatovicente.github.io/algebra-passo-a-passo/

## Nova aba: Polígonos regulares

[Abrir explicações e 70 exercícios](https://renatovicente.github.io/algebra-passo-a-passo/poligonos.html)

Adaptação didática original do capítulo XVII do documento `poligonos_regulares.pdf` enviado pelo usuário (páginas impressas 212–225). Explica os resultados a partir de poucas ideias anteriores, usando a história de uma praça dividida em triângulos, quinze explorações interativas e demonstrações avançadas expansíveis. O documento original não é redistribuído.

- As seis ideias de partida têm ilustrações interativas: volta e meia volta, triângulos, quadrados de Pitágoras, área por duas cópias, relações do círculo e medianas na razão 2:1.
- Visualizações de regularidade, ângulos, circunferências, triangulação, Pitágoras, comparação de figuras, área, duplicação de lados e divisão áurea.
- Controles para mudar lados e medidas, caminhar pelas viradas externas e preencher a área setor por setor.

- 20 exercícios de fundamentos.
- 20 exercícios de aplicações.
- 10 exercícios de conexões e desafios.
- 20 exercícios exclusivos de apótema e lado em triângulos equiláteros, quadrados e hexágonos regulares, com desenhos nas soluções.

Cada exercício tem solução detalhada oculta por botão e alerta de erro comum. O progresso desta aba é independente do caderno original.

## Nova aba: Equações e inequações

[Abrir revisão e 50 exercícios](https://renatovicente.github.io/algebra-passo-a-passo/equacoes-segundo-grau.html)

- Revisão com gráficos interativos de parábolas, discriminante e estudo de sinais.
- 25 equações do segundo grau com soluções passo a passo e raízes marcadas nos gráficos.
- 25 inequações: 8 quadráticas, 8 razões entre polinômios de segundo e primeiro grau e 9 razões entre dois polinômios de segundo grau.
- Soluções ocultas com gráficos dos polinômios, quadros de sinais e intervalos na reta real, incluindo as restrições do denominador.
- Nas 17 razões, gráfico da função racional com assíntotas verticais, horizontais ou oblíquas, furos por cancelamento e intervalos da solução destacados em verde.

O progresso é salvo neste navegador. Há filtros por assunto e impressão com ou sem soluções.

## Nova aba: Exponenciais e logaritmos

[Abrir revisão e 70 exercícios](https://renatovicente.github.io/algebra-passo-a-passo/exponenciais-logaritmos.html)

Revisão interativa de bases, incluindo e, crescimento, decaimento, funções inversas e propriedades dos logaritmos. Inclui exercícios de exponencial natural e ln, nos 50 exercícios de revisão. Cinco blocos com 10 exercícios cada: funções exponenciais; equações e inequações exponenciais; definição e propriedades dos logaritmos; equações e inequações logarítmicas; aplicações e conexões.

Cada exercício tem solução oculta passo a passo, gráfico relacionado à questão e alerta de erro comum. Inclui filtros, progresso independente e impressão com ou sem soluções.

A seção **Lista Função Exponencial** acrescenta as 20 questões do PDF, com gráficos originais e animações interativas nas soluções (reprodução/pausa, marcos anterior/próximo, reinício e controle deslizante). O total da aba é 70 exercícios. Na questão 19, o gabarito foi corrigido para B=30, conforme o gráfico.

## Novas abas: Termologia e Cinemática

- [Termologia: teoria e 25 exercícios](https://renatovicente.github.io/algebra-passo-a-passo/termologia.html): calor, temperatura, escalas térmicas e equilíbrio, com simulações e soluções ilustradas.
- [Cinemática: teoria e 25 exercícios](https://renatovicente.github.io/algebra-passo-a-passo/cinematica.html): movimentos, componentes da velocidade, lançamentos e gráficos, com animações nos dois laboratórios e nas 25 soluções.

As animações têm reprodução, pausa, reinício, avanço por etapas e controle de ritmo. As equações usam LaTeX renderizado por KaTeX, inclusive durante as animações. Os cadernos retomam os quatro problemas da prova fornecida e explicam os erros observados nas resoluções; o PDF original não é redistribuído.

Todas as oito páginas compartilham a navegação entre cadernos. Os filtros, o progresso local e a impressão com ou sem soluções continuam disponíveis. Na impressão, os desenhos estáticos substituem os controles das animações.

## Movimento circular: 37 exercícios

[Abrir teoria e exercícios](https://renatovicente.github.io/algebra-passo-a-passo/movimento-circular.html)

Ângulos e arcos, período e frequência, MCU, aceleração centrípeta, transmissões e MCUV. Dois laboratórios interativos e 25 soluções com desenhos animados, equações LaTeX, reprodução, pausa e avanço por etapas. Inclui também os 12 exercícios do anexo de outubro de 2026 (Anexo 1 a 12), com resoluções passo a passo e os diagramas dos problemas 3 e 6. Inclui filtros, progresso local e impressão com desenhos estáticos.

Para reconstruir esta aba e integrar sua navegação: `python3 tools/build-circular.py`. O gerador reutiliza o KaTeX e o estilo incorporados em `cinematica.html`, sem baixar dependências.

## Conteúdo do caderno original

- Sinais, ordem das operações e frações.
- Potências, expoentes negativos e fracionários.
- Raízes, fatoração numérica e racionalização.
- Produtos notáveis, fatorações e frações algébricas.
- Exercícios mistos e aplicações em fórmulas de física.
- 25 práticas adicionais de física: movimento, forças, energia, densidade, molas e impulso.
- 25 práticas adicionais de geometria: perímetros, áreas, volumes, Pitágoras e proporções.

As soluções ficam ocultas até clicar em “Ver solução”. A página também permite filtrar por assunto, marcar exercícios concluídos e imprimir com ou sem soluções.

## Como usar

Abra o site ou baixe `index.html`, `poligonos.html`, `equacoes-segundo-grau.html`, `exponenciais-logaritmos.html`, `termologia.html`, `cinematica.html` e `movimento-circular.html` para a mesma pasta e abra no navegador. O HTML contém os scripts, estilos e fontes matemáticas e funciona sem internet. O progresso é salvo apenas no navegador utilizado, sem cadastro nem envio de respostas.

## Publicação

GitHub Pages publica o arquivo `index.html` da raiz da branch `main`. Para atualizar o site, altere os arquivos HTML e envie um novo commit.

## Prova: polígonos e exponenciais

[Abrir a prova de matemática](https://renatovicente.github.io/algebra-passo-a-passo/prova-matematica.html)

Cinco questões discursivas de polígonos regulares inscritos e circunscritos, funções, equações e inequações exponenciais. A distribuição de dificuldade foi estimada pelas cinco páginas fornecidas de `provaQ3.pdf`: quatro subitens básicos, cinco intermediários e dois avançados. A matriz de correspondência, as referências aos exercícios dos cadernos e os critérios de correção ficam disponíveis na aba. O PDF original e seus dados pessoais não são publicados.

Cada questão tem um cronômetro independente de 15 minutos, acionado por **Iniciar**. A contagem continua ao trocar de aba ou recarregar a página. Ao esgotar o tempo, aparece um aviso; **Reiniciar** retorna a 15:00 e aguarda um novo início. Inclui gabarito comentado e impressão separada da prova e das soluções.

Fontes editáveis em `tools/prova/`. Reconstrua com `python3 tools/build-exam.py`; o gerador preserva as demais abas e reaproveita o KaTeX já incorporado ao site.

## Renderização matemática

As expressões LaTeX são renderizadas pelo [KaTeX](https://katex.org/), versão 0.19.0, incorporado ao HTML. Sua licença MIT está em `KATEX-LICENSE.txt`.

## Conversão de unidades: 50 exercícios

[Abrir teoria e exercícios](https://renatovicente.github.io/algebra-passo-a-passo/conversao-unidades.html)

Cinco blocos de 10 problemas: comprimento (km, cm, m), tempo (h, min, s), massa (kg, g), energia (J, cal) e aplicações em física. Inclui soluções passo a passo com 50 esquemas ilustrados dos dados, conversões e resultados, alertas de erros comuns, filtros, progresso local e impressão com ou sem soluções. Os esquemas se adaptam ao celular e à impressão. Nas conversões de energia, cada enunciado informa o fator adotado.

Para reconstruir a aba e integrar a navegação: `python3 tools/build-units.py`. O gerador reutiliza o estilo e as fontes incorporados em `cinematica.html`, sem baixar dependências.

## Inscrição e circunscrição: Lista 9 — 2026

[Resolver as 14 questões](https://renatovicente.github.io/algebra-passo-a-passo/inscricao-circunscricao.html)

Lista transcrita das duas fotos, com alternativas, gabarito conferido, desenhos vetoriais reconstruídos e 14 soluções visuais interativas. Cada construção permite avançar e voltar entre quatro etapas, reproduzir/pausar, alterar a escala e restaurar os dados do enunciado. Inclui progresso local, filtro de pendentes e impressão das soluções.

Fontes editáveis em `tools/inscricao/`. Para reconstruir a aba e integrar a navegação: `python3 tools/build-inscricao.py`. O gerador reutiliza o KaTeX incorporado ao caderno de exponenciais.

## Recuperação: calor e lançamento horizontal

[Resolver os 8 exercícios](https://renatovicente.github.io/algebra-passo-a-passo/recuperacao-calor-lancamento.html)

Lista de 19 e 21 de outubro de 2026: cinco questões de calor e mudanças de fase e três de lançamento horizontal, com todos os subitens. Inclui curvas interativas de temperatura por calor acumulado, proporções das fases, comparação de quedas e simulação do corredor com velocidade ajustável. Soluções, gabarito, filtros, progresso e impressão incluídos. Na questão 1 é explicitado o calor específico da água usado; na questão 8 são distinguidos o valor-limite de 9 m/s e a interceptação estritamente acima da areia.

Fontes em `tools/rec-fisica/`. Reconstrua com `python3 tools/build-rec-fisica.py`.

## Física: aquecimento e prova com soluções animadas

[Abrir os 10 aquecimentos e a prova](https://renatovicente.github.io/algebra-passo-a-passo/prova-fisica.html)

Lançamento horizontal, calorimetria e mudança de estado, sistemas de blocos e tração. Os dez aquecimentos retomam erros de decomposição de forças, sinais, aritmética, leitura de gráficos, variação de temperatura e conversão de unidades observados na prova fornecida. Tração e mudança de fase são preparação para conteúdos novos. A análise pública não inclui nomes, notas, manuscritos ou o PDF original.

A prova tem cinco questões de dois itens, totalizando 5,0 pontos. A distribuição estimada é de dois itens básicos, cinco intermediários e três avançados, com a correspondência disponível em **Erros a revisar**. Cada questão tem seu próprio cronômetro de 15 minutos, iniciado por botão, com prazo preservado ao trocar de aba ou recarregar.

As cinco soluções incluem animações interativas: blocos e forças; trajetória e componentes da velocidade; gráfico de velocidade e altura; troca de calor; aquecimento do gelo e fusão parcial. Há reprodução/pausa, marcos anterior/próximo, reinício, ritmo e controle deslizante. O equilíbrio térmico usa energia transferida, não um tempo físico arbitrário. A impressão substitui as animações por desenhos estáticos no estado final. Aquecimento, prova, gabarito e análise têm impressão separada.

Fontes em `tools/prova-fisica/`. Reconstrua com `python3 tools/build-physics-exam.py`. O gerador reutiliza o KaTeX local e acrescenta a aba à navegação de todas as páginas existentes. Não há dependências de rede para usar esta página depois de baixada. Progresso e cronômetros usam chaves próprias no armazenamento local do navegador.

## Prova 2: polígonos e exponenciais

[Abrir a segunda prova de matemática](https://renatovicente.github.io/algebra-passo-a-passo/prova-matematica-2.html)

Uma nova rodada com os mesmos assuntos e a mesma matriz da primeira prova: cinco questões, 11 subitens, 5,0 pontos, sendo 2,5 em geometria e 2,5 em álgebra. São quatro itens básicos, cinco intermediários e dois avançados, nas mesmas posições; a equivalência de dificuldade é uma estimativa pedagógica.

Inclui triângulo circunscrito e quadrado inscrito na mesma circunferência, construção do dodecágono a partir do hexágono, raio interno e externo de um hexágono, função exponencial decrescente, inequação racional exponencial, quadrado perfeito e mudança de base. O gabarito apresenta passos, critérios de correção, referências aos cadernos e alertas de erros.

Cada questão tem um cronômetro de 15 minutos iniciado por botão, com persistência e reinício. As contagens são independentes da primeira prova e da prova de física. Há impressão separada de enunciados e soluções. A aba foi acrescentada à navegação das páginas existentes.

Fontes em `tools/prova2/`. Reconstrua com `python3 tools/build-exam-2.py`.

## Prova 2: lançamento horizontal, calorimetria e tração

[Abrir a segunda prova de física](https://renatovicente.github.io/algebra-passo-a-passo/prova-fisica-2.html)

Cinco questões inéditas com dois itens cada, totalizando 5,0 pontos. Mantém a matriz da primeira prova do site: dois itens básicos, cinco intermediários e três avançados, nas mesmas posições. A dificuldade é uma estimativa pedagógica. Inclui blocos ligados por polia com força oblíqua, lançamento horizontal, gravidade deduzida de um gráfico, equilíbrio térmico entre corpos de capacidades diferentes e fusão parcial do gelo.

Cada questão tem um cronômetro independente de 15 minutos, iniciado por botão, com prazo preservado ao recarregar ou trocar de aba. O armazenamento é separado das outras provas. As cinco soluções têm animações controladas por reprodução/pausa, etapas, ritmo e controle deslizante; os modelos conservam o comprimento do fio, a energia e a massa. O equilíbrio térmico é exibido por fração da energia trocada, sem atribuir um tempo físico arbitrário.

Há impressão separada de prova, gabarito e critérios, com desenhos estáticos no gabarito. Os links remetem aos cadernos e aos dez aquecimentos da primeira prova. Fontes em `tools/prova-fisica2/`; reconstrua com `python3 tools/build-physics-exam-2.py`.


## Simulado de química

`prova-quimica.html`: cinco questões discursivas, 5 pontos, baseadas na circular 148/2026 e nas listas fornecidas. Foco nos assuntos da próxima prova: hidrocarbonetos e combustíveis fósseis; síntese, decomposição e simples troca; ácidos, bases e sais. Cálculos de estequiometria, gases e pureza são aplicados a esses assuntos. Inclui gabarito por etapas, critérios de correção, impressão e cronômetros independentes. Fontes editáveis em `tools/quimica/`; reconstruir com `python3 tools/build-chemistry.py`. Os documentos e as fotos originais não são publicados.
