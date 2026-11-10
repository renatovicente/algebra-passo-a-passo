# Revisão anual

Fonte editorial: 73 imagens da pasta Lara, com 53 novas páginas de provas e 20 anexos anteriores (incluindo duplicatas, listas e teoria). As quatro fotos reenviadas em 10/11 correspondem à mesma lista de 14 logaritmos já trabalhada em novembro.

## Conteúdo

- `cursos.py`: 34 temas, cada um com introdução, método, foco de revisão e três aquecimentos.
- `originais.py`: 53 páginas transcritas. `build.py` acrescenta as nove questões distintas de provas dos anexos anteriores: 62 questões ao todo, preservando seus subitens.
- `simulados.py`: cinco provas com 15 questões e 30 itens cada; cinco questões de cada disciplina. Os 34 temas aparecem no conjunto das provas.
- `logs.py`: 14 questões da escola, alternativas, domínio, soluções completas, conferência e ressalvas de notação/modelo.
- `visuals.js`: 34 demonstrações controladas por parâmetros e 14 ilustrações específicas para logaritmos.
- `figures.js`: reconstruções de diagramas dos enunciados.
- `app.js`: etapas, progresso, filtro, rascunhos, autocorreção, cronômetro e impressão.
- `content.json`: conteúdo consolidado gerado para auditoria; não editar manualmente.

Gerar, a partir da raiz do repositório:

```sh
python3 tools/anual/build.py
node tools/anual/validate.cjs
```

São geradas 11 novas páginas. A navegação dos cadernos existentes recebe links para a revisão, as provas originais e os logaritmos ilustrados. Nenhuma foto, nome completo, nota ou identificação escolar individual é publicada.

## Cuidados editoriais

Os erros descritos são observações das resoluções, não inferências sobre desempenho em assuntos novos. Os acertos também são usados como exemplos. Quando o enunciado dependia de uma figura, as relações e medidas foram incluídas em texto. Na questão das vitaminas, fórmulas moleculares substituem três desenhos estruturais para tornar a versão textual autossuficiente; a contagem na estrutura de U permanece explícita.

As correções e gabaritos não foram tratados como infalíveis. Casos destacados nas próprias soluções:

- Três redes sociais: inclusão–exclusão resulta em 550 pessoas.
- Logaritmos 7: a letra β aparece como constante definida e como variável angular; a interpretação do gabarito usa símbolos distintos.
- Logaritmos 10: a função percentual é aproximada e não reproduz aumento zero em t=0.
- Estrutura de U: o cátion desenhado é C₆H₁₄NO₂S⁺; o contraíon não entra na conta.
- Molibdênio: configuração neutra e ionizada verificadas no NIST.
- Mercúrio(I): fórmula molecular Hg₂F₂, distinguida da proporção empírica HgF.
- Fórmula calculada a partir da composição C/H/N: resultado formal dos dados, sem inferir estabilidade da espécie neutra.

As fontes científicas para as exceções estão vinculadas junto às questões correspondentes.

## Verificação

Validação estática: contagens, cobertura dos 34 temas, IDs, scripts, links locais, renderização de mais de mil fórmulas e cálculos críticos independentes.

Verificação em Chromium: 11 páginas sem erros de JavaScript; navegação das soluções; autocorreção e rascunho preservados após recarga; modo prova; impressão de questões sem soluções e impressão completa; largura de 390 px sem vazamento horizontal nas páginas verificadas. Os simulados não corrigem texto automaticamente: a pontuação é uma autocorreção informada pelo aluno.
