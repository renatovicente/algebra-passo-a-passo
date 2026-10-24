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
