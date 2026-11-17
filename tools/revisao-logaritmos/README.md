# Revisão de logaritmos — prova e treino

As quatro fotos enviadas em 16/11/2026 contêm quatro questões com sete itens:

| Item | Tema | Resposta |
| --- | --- | --- |
| 1 | pH, concentração 0,0032 mol/L | aproximadamente 2,5 |
| 2a | log na base b de a²b/c | 4 |
| 2b | log na base raiz cúbica de 7, mais log 0,001 | 0 |
| 2c | log na base 0,5 de 75 | −a−2b |
| 3 | produto dos seis expoentes | 6 |
| 4a | fração de produtos de logaritmos | 19/104, com as aproximações dadas |
| 4b | equação com bases 2, 4 e 8 | 2^(6/7) |

Os 20 exercícios inéditos cobrem os sete tipos de item: três de pH, três de propriedades, dois de raízes e decimais, três de mudança de base, três de produtos, três de frações e três de equações. Cada um tem resolução, resposta, erro comum e referência ao exemplo original.

As fotos e os dados pessoais não são incorporados. Os enunciados matemáticos são preservados; o texto contextual de pH foi condensado mantendo fórmula, concentração, unidade e aproximação. As resoluções são recalculadas, sem adotar as respostas manuscritas. O símbolo de aproximação distingue o resultado escolar obtido com os valores fornecidos do valor real do logaritmo.

Fontes: `data.py`, `template.html`, `style.css`, `app.js`. `content.json` é gerado para auditoria. O HTML resultante incorpora o KaTeX e suas fontes a partir do caderno existente, sem downloads.

Da raiz do repositório:

```sh
python3 tools/revisao-logaritmos/build.py
node tools/revisao-logaritmos/validate.cjs
```

O gerador cria `logaritmos-prova-treino.html` e insere sua aba ao lado de Logaritmos na navegação dos outros cadernos. Repetir o comando não duplica links. O validador confere os 27 resultados, fórmulas KaTeX, scripts, IDs, referências e navegação.

Verificação visual e funcional em Chromium: LaTeX renderizado, 7 originais e 20 treinos, filtros combinados, marcação preservada após recarga, links para os exemplos abrindo a solução, impressão de 27 itens com ou sem soluções e ausência de transbordamento da página a 320, 390 e 1280 px. Fórmulas extensas têm rolagem horizontal própria no celular. Nenhum erro de JavaScript foi observado.
