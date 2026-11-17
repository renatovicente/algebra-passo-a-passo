# Listas enviadas em 17/11/2026

Duas abas, com numeração e alternativas preservadas, resoluções recalculadas e equações em LaTeX renderizadas pelo KaTeX incorporado ao HTML:

- `areas-figuras-planas-lista-11.html`: Lista 11 — Área de figuras planas, 17 questões (a questão 8 contém os itens a e b), com 17 desenhos SVG.
- `matematica-revisao-17-novembro.html`: revisão de matemática, 9 questões e 2 gráficos SVG.

As quatro fotos fornecidas são a fonte dos enunciados. Os textos foram ajustados apenas para explicitar relações geométricas das figuras e tornar a versão digital autossuficiente. Fotos, rasuras, nomes de professores e dados pessoais não são incorporados. As imagens vetoriais são reconstruções; as questões 5 e 10 de geometria ganharam diagramas auxiliares.

## Conteúdo e manutenção

- `data.py`: enunciados, alternativas, soluções, respostas e alertas.
- `figures.py`: 19 figuras vetoriais, com títulos e descrições acessíveis.
- `template.html`, `style.css`, `app.js`: apresentação, filtros, progresso local e impressão.
- `build.py`: gera os HTMLs, reutiliza o KaTeX e as fontes do site e integra as duas abas à navegação existente. A base visual é a da revisão de logaritmos.
- `content.json`: conteúdo gerado para auditoria; não editar diretamente.
- `validate.cjs`: contagens, fórmulas, cálculos, alternativas, referências, scripts e navegação.

Da raiz do repositório:

```sh
python3 tools/listas-17-novembro/build.py
node tools/listas-17-novembro/validate.cjs
```

Os enunciados e as soluções existem no HTML, mesmo sem JavaScript. JavaScript renderiza a matemática, aplica os filtros e salva o progresso em uma chave distinta para cada lista. A navegação entre questões mantém as soluções fechadas; o gabarito rápido abre a resolução correspondente. A impressão inclui todos os exercícios, independentemente do filtro, e permite escolher com ou sem soluções.

## Conferência editorial

O gabarito de geometria da foto coincide com os cálculos. Na questão 13, usa-se expressamente π = 3,1; nos demais itens os resultados com π são mantidos exatos. Na questão 15, os círculos não são concêntricos: o disco menor está contido no maior e é tangente internamente, o que basta para subtrair as áreas.

A questão 7 de matemática contém a sequência impressa `g(x) = 4^(x²−3x)g(x) = 4`. A versão digital usa as duas funções completas, `f(x) = 2^(x²−9)` e `g(x) = 4^(x²−3x)`, tratando o fragmento final como duplicação de impressão. A solução registra essa normalização e explica que tomar `g(x) = 4` como condição adicional seria incompatível. O resultado é x = 3 e 2^x = 8, alternativa D.

## Validação

26 exercícios, 19 figuras com XML válido e descrições acessíveis, 382 fórmulas verificadas pelo KaTeX. Os resultados numéricos e as 20 alternativas corretas são conferidos independentemente; a região da questão 17 de geometria também é integrada numericamente como verificação da decomposição.

Chromium: ambas as páginas sem erros de JavaScript; filtros combinados; progresso após recarga; navegação sem revelar respostas antes da tentativa; gabarito abrindo a solução; impressão com 17 ou 9 enunciados e zero ou todas as soluções; larguras de 320, 390 e 1280 px sem transbordamento horizontal. Nenhum rótulo das figuras ultrapassa seu quadro. Símbolos de reais são isolados dos delimitadores de LaTeX.
