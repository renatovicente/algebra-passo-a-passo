# Plano inclinado — lista de Física

Página: `plano-inclinado.html`. Conteúdo transcrito das duas fotos de 19/11/2026; fotos, nomes e anotações não são incorporados.

## Gerar e validar

```sh
python3 tools/plano-inclinado/build.py
node tools/plano-inclinado/validate.cjs
```

O build usa Python 3 e Node.js, sem dependências adicionais. Incorpora o KaTeX e as fontes já existentes no `index.html`, gera SVGs estáticos e acrescenta a aba à navegação dos cadernos. O HTML final funciona offline. `content.json` é gerado a partir de `data.py`.

`physics.js` calcula estados em unidades SI. `visuals.js` produz os diagramas a partir desses estados. `app.js` controla parâmetros, reprodução, progresso local e impressão. As equações e a animação usam o mesmo modelo. Os testes verificam Newton, conservação de energia, comprimento constante do fio, limites dos controles e fórmulas LaTeX.

## Hipóteses didáticas

- Questão 3: g = 10 m/s², omitido na folha e coerente com o gabarito.
- Questão 4: sem atrito; não há coeficiente nem força de atrito informados. Como não há velocidade inicial nem tempo, o controle monta o diagrama, sem inventar trajetória.
- Questão 6: transição ideal para a rampa; a resposta é simbólica. Os valores do laboratório são explicitamente ilustrativos.
- Questões 7 e 8: fio e polia ideais; o laboratório escolhe repouso inicial e 1 s de movimento. Na questão 8, massas absolutas servem apenas para dar escala às forças.
- Seno e cosseno fornecidos na questão 7 são aproximações distintas: dinâmica usa sen 30° = 0,5, normal usa cos 30° = 0,87. O desenho usa o ângulo geométrico de 30°.
- A reprodução dura 8 s na tela, independentemente do tempo físico. Não há reprodução automática. Preferência por movimento reduzido troca a reprodução por avanços discretos.
- No fim da subida, velocidade zero não remove a aceleração. No fim da descida, a velocidade exibida é a de chegada, sem colisão simulada.
- Componentes do peso substituem o peso no diagrama, que fica tracejado como referência; não são forças adicionais.
- Impressão com soluções restaura os dados iniciais e usa o último instante/etapa. Ao fechar a impressão, os parâmetros anteriores são restaurados.

Verificação no navegador: oito soluções inicialmente recolhidas; parâmetros/restauração, reprodução/pausa e navegação por etapas; polias em equilíbrio e sentido inverso; filtros/progresso persistente; movimento reduzido; impressão; fórmulas e layout em 320, 390 e 1280 px.
