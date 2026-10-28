const examQuestions = [
  {
    "id": 1,
    "title": "Hidrocarbonetos e combustíveis fósseis",
    "subject": "Compostos do carbono",
    "prompt": "Considere X = CH₃–CH(CH₃)–CH₂–CH₂–CH₃ e Y = 3-metilpent-1-eno. Massas atômicas: C = 12; H = 1.",
    "points": 1,
    "parts": [
      {
        "label": "a",
        "points": 0.25,
        "prompt": "Dê o nome IUPAC e a fórmula molecular de X. Represente Y em fórmula bastão e determine sua fórmula molecular.",
        "answer": "X: 2-metilpentano, C₆H₁₄. Y: C₆H₁₂; estrutura equivalente CH₂=CH–CH(CH₃)–CH₂–CH₃.",
        "steps": [
          "X tem cadeia principal com cinco carbonos e metil no carbono 2. São seis carbonos totais, com 14 H.",
          "Em Y, desenhe uma cadeia de cinco vértices/extremidades, dupla entre C1 e C2 e ramificação de um carbono em C3. A dupla reduz dois H em relação ao alcano: C₆H₁₂."
        ],
        "rubric": "0,125 por cada composto, incluindo estrutura e fórmula solicitadas."
      },
      {
        "label": "b",
        "points": 0.25,
        "prompt": "Calcule a massa total de uma mistura com 0,50 mol de X e 0,50 mol de Y.",
        "answer": "85 g.",
        "steps": [
          "M(X) = 6×12 + 14 = 86 g/mol; M(Y) = 6×12 + 12 = 84 g/mol.",
          "m = 0,50×86 + 0,50×84 = 43 + 42 = 85 g."
        ],
        "rubric": "0,125 pelas massas molares; 0,125 pelo total."
      },
      {
        "label": "c",
        "points": 0.25,
        "prompt": "Balanceie a combustão completa de Y e calcule os mols de O₂ consumidos por 0,20 mol de Y.",
        "answer": "C₆H₁₂ + 9 O₂ → 6 CO₂ + 6 H₂O; 1,80 mol de O₂.",
        "steps": [
          "Ajuste primeiro 6 C e 12 H; os produtos contêm 18 átomos de oxigênio.",
          "A relação é 1:9; 0,20×9 = 1,80 mol."
        ],
        "rubric": "0,125 pela equação; 0,125 pela proporção."
      },
      {
        "label": "d",
        "points": 0.25,
        "prompt": "Explique por que o petróleo é um combustível fóssil não renovável na escala humana. A fórmula C₆H₁₂, isoladamente, permite afirmar que um composto é alceno? Justifique.",
        "answer": "O petróleo se forma por transformação de matéria orgânica ao longo de tempos geológicos; C₆H₁₂ também pode representar um cicloalcano.",
        "steps": [
          "A reposição natural é muito mais lenta que o consumo.",
          "Hex-1-eno e ciclo-hexano têm C₆H₁₂, mas pertencem a famílias distintas."
        ],
        "rubric": "0,125 pela escala de formação; 0,125 pela ambiguidade estrutural."
      }
    ],
    "pitfall": "Conte todos os carbonos das ramificações e confira os hidrogênios antes de calcular a massa molar.",
    "sources": [
      [
        "#calibracao",
        "Conteúdo e referências do simulado"
      ]
    ]
  },
  {
    "id": 2,
    "title": "Simples troca e reagente limitante",
    "subject": "Transformações químicas",
    "prompt": "Uma amostra de 5,4 g de alumínio reage com 14,6 g de HCl puro em solução aquosa. Considere reação completa, sem passivação. Produtos: AlCl₃ e H₂. Dados: Al = 27; H = 1; Cl = 35,5.",
    "points": 1,
    "parts": [
      {
        "label": "a",
        "points": 0.25,
        "prompt": "Escreva a equação balanceada com os menores coeficientes inteiros e classifique a reação.",
        "answer": "2 Al + 6 HCl → 2 AlCl₃ + 3 H₂; simples troca.",
        "steps": [
          "O alumínio desloca o hidrogênio do ácido.",
          "Conserve 2 Al, 6 Cl e 6 H em cada lado."
        ],
        "rubric": "0,20 pelo balanceamento; 0,05 pela classificação."
      },
      {
        "label": "b",
        "points": 0.25,
        "prompt": "Determine o reagente limitante, comparando mols disponíveis divididos pelos coeficientes.",
        "answer": "HCl é o limitante.",
        "steps": [
          "n(Al) = 5,4/27 = 0,20 mol; n(HCl) = 14,6/36,5 = 0,40 mol.",
          "0,20/2 = 0,10; 0,40/6 ≈ 0,0667. O menor quociente é o do HCl."
        ],
        "rubric": "0,125 pelos mols; 0,125 pela comparação."
      },
      {
        "label": "c",
        "points": 0.5,
        "prompt": "Calcule a massa de AlCl₃ formada e a massa de alumínio que sobra.",
        "answer": "17,8 g de AlCl₃ e 1,8 g de Al em excesso.",
        "steps": [
          "6 mol de HCl formam 2 mol de AlCl₃: n = 0,40/3 mol.",
          "M(AlCl₃) = 27 + 3×35,5 = 133,5 g/mol; m = (0,40/3)×133,5 = 17,8 g.",
          "Al consumido = (0,40/3)×27 = 3,6 g; sobra = 5,4 − 3,6 = 1,8 g."
        ],
        "rubric": "0,25 pela massa de sal; 0,25 pelo excesso; valorize proporções corretas."
      }
    ],
    "pitfall": "O menor número de mols não identifica sozinho o limitante: divida pelo coeficiente da equação balanceada.",
    "sources": [
      [
        "#calibracao",
        "Conteúdo e referências do simulado"
      ]
    ]
  },
  {
    "id": 3,
    "title": "Gás produzido e pureza",
    "subject": "Transformações químicas",
    "prompt": "Uma amostra de 0,50 g de zinco impuro reage com HCl em excesso e produz 123 mL de H₂ seco a 1 atm e 27 °C. As impurezas não reagem. Dados: Zn = 65; R = 0,082 atm·L·mol⁻¹·K⁻¹. Use T(K) = T(°C) + 273.",
    "points": 1,
    "parts": [
      {
        "label": "a",
        "points": 0.25,
        "prompt": "Equacione a reação e determine a quantidade de H₂ em mol.",
        "answer": "Zn + 2 HCl → ZnCl₂ + H₂; n(H₂) = 0,0050 mol.",
        "steps": [
          "123 mL = 0,123 L; 27 °C = 300 K.",
          "n = PV/RT = 0,123/(0,082×300) = 0,123/24,6 = 0,0050 mol."
        ],
        "rubric": "0,125 pela equação; 0,125 pelos mols com unidades."
      },
      {
        "label": "b",
        "points": 0.5,
        "prompt": "Determine a massa de zinco puro, a massa de impurezas e o percentual de pureza.",
        "answer": "0,325 g de Zn; 0,175 g de impurezas; 65% de pureza.",
        "steps": [
          "A relação Zn:H₂ é 1:1, logo n(Zn) = 0,0050 mol.",
          "m(Zn) = 0,0050×65 = 0,325 g.",
          "Impurezas = 0,50 − 0,325 = 0,175 g; pureza = 100×0,325/0,50 = 65%."
        ],
        "rubric": "0,20 pelo Zn; 0,15 pelas impurezas; 0,15 pela pureza."
      },
      {
        "label": "c",
        "points": 0.25,
        "prompt": "Se a massa calculada de zinco puro fosse 3,25 g, ela seria compatível com o enunciado? Explique.",
        "answer": "Não: a massa de Zn puro não pode superar os 0,50 g da amostra.",
        "steps": [
          "Confira a conversão mL→L e a divisão por 24,6.",
          "O metal é uma parte da amostra: sua massa deve estar entre zero e 0,50 g."
        ],
        "rubric": "0,25 pela comparação e justificativa."
      }
    ],
    "pitfall": "Use litros com este valor de R. Faça uma estimativa antes de aceitar o resultado: a parte pura não pode pesar mais que a amostra.",
    "sources": [
      [
        "#calibracao",
        "Conteúdo e referências do simulado"
      ]
    ]
  },
  {
    "id": 4,
    "title": "Ácidos, bases e sais",
    "subject": "Constituição da matéria",
    "prompt": "Use os íons Ca²⁺, Al³⁺, OH⁻, NO₃⁻, SO₄²⁻ e PO₄³⁻ quando necessário.",
    "points": 1,
    "parts": [
      {
        "label": "a",
        "points": 0.25,
        "prompt": "Escreva as fórmulas do hidróxido de alumínio e do fosfato de cálcio, justificando a neutralidade elétrica.",
        "answer": "Al(OH)₃ e Ca₃(PO₄)₂.",
        "steps": [
          "Al³⁺ exige três OH⁻: +3 − 3 = 0.",
          "Três Ca²⁺ e dois PO₄³⁻ fornecem +6 − 6 = 0."
        ],
        "rubric": "0,125 por fórmula justificada."
      },
      {
        "label": "b",
        "points": 0.25,
        "prompt": "Dê o nome e a função inorgânica de H₂SO₄, Ca(OH)₂ e Al(NO₃)₃.",
        "answer": "Ácido sulfúrico (ácido); hidróxido de cálcio (base); nitrato de alumínio (sal).",
        "steps": [
          "H₂SO₄ ioniza em água; Ca(OH)₂ libera OH⁻ por dissociação.",
          "Al(NO₃)₃ é formado por cátion Al³⁺ e ânions nitrato."
        ],
        "rubric": "Divida 0,25 igualmente entre os três pares nome/função."
      },
      {
        "label": "c",
        "points": 0.25,
        "prompt": "Escreva a neutralização total entre H₂SO₄ e Ca(OH)₂ e dê o nome do sal.",
        "answer": "H₂SO₄ + Ca(OH)₂ → CaSO₄ + 2 H₂O; sulfato de cálcio.",
        "steps": [
          "Dois H ionizáveis neutralizam dois OH.",
          "Ca²⁺ e SO₄²⁻ combinam na proporção 1:1."
        ],
        "rubric": "0,125 pela equação; 0,125 pelo nome."
      },
      {
        "label": "d",
        "points": 0.25,
        "prompt": "Na neutralização total do item anterior, quantos mols de Ca(OH)₂ são necessários para reagir com 0,20 mol de H₂SO₄? Quantos mols de água se formam?",
        "answer": "0,20 mol de Ca(OH)₂ e 0,40 mol de H₂O.",
        "steps": [
          "Use os coeficientes de H₂SO₄ + Ca(OH)₂ → CaSO₄ + 2 H₂O: ácido, base e água estão na proporção 1:1:2.",
          "n[Ca(OH)₂] = 0,20×1/1 = 0,20 mol; n(H₂O) = 0,20×2/1 = 0,40 mol.",
          "O índice 2 de (OH)₂ faz parte da fórmula da base; ele não significa que sejam necessários 2 mol dessa base para cada mol do ácido."
        ],
        "rubric": "0,125 pelos mols de base; 0,125 pelos mols de água, com as proporções indicadas."
      }
    ],
    "pitfall": "Confira a soma das cargas para escrever o sal. Diferencie índices da fórmula e coeficientes da equação; só os coeficientes dão a proporção em mol.",
    "sources": [
      [
        "#calibracao",
        "Conteúdo e referências do simulado"
      ]
    ]
  },
  {
    "id": 5,
    "title": "Reconhecer e justificar transformações",
    "subject": "Transformações químicas",
    "prompt": "Considere os processos: I. N₂ + H₂ → NH₃; II. CaCO₃ → CaO + CO₂ (aquecimento); III. Cu + AgNO₃ → Cu(NO₃)₂ + Ag. Série de reatividade, da maior para a menor: Zn > H > Cu > Ag. Massas atômicas: Ca = 40; C = 12; O = 16.",
    "points": 1,
    "parts": [
      {
        "label": "a",
        "points": 0.25,
        "prompt": "Balanceie I e II e classifique cada um como síntese ou decomposição.",
        "answer": "I: N₂ + 3 H₂ → 2 NH₃, síntese. II: CaCO₃ → CaO + CO₂, decomposição.",
        "steps": [
          "Em I, dois reagentes formam um único composto.",
          "Em II, um composto origina dois produtos; os coeficientes já são 1:1:1."
        ],
        "rubric": "0,125 por processo balanceado e classificado."
      },
      {
        "label": "b",
        "points": 0.25,
        "prompt": "Balanceie III, classifique-o e explique se Ag metálica deslocaria Cu de Cu(NO₃)₂.",
        "answer": "Cu + 2 AgNO₃ → Cu(NO₃)₂ + 2 Ag; simples troca. A reação inversa não ocorre espontaneamente nas condições consideradas.",
        "steps": [
          "Cu é mais reativo que Ag e a desloca do sal.",
          "Ag é menos reativa que Cu; não o desloca da solução."
        ],
        "rubric": "0,125 pela equação e classificação; 0,125 pela justificativa."
      },
      {
        "label": "c",
        "points": 0.25,
        "prompt": "Uma amostra de 25,0 g de CaCO₃ puro sofre decomposição completa pelo processo II. Calcule a massa de CaO formada, mostrando as massas molares e a proporção usada.",
        "answer": "14,0 g de CaO.",
        "steps": [
          "M(CaCO₃) = 40 + 12 + 3×16 = 100 g/mol; M(CaO) = 40 + 16 = 56 g/mol.",
          "n(CaCO₃) = 25,0/100 = 0,250 mol. A equação balanceada fornece a relação 1 mol de CaCO₃ para 1 mol de CaO.",
          "m(CaO) = 0,250×56 = 14,0 g. A proporção 1:1 é em mol, não em gramas."
        ],
        "rubric": "0,125 pelas massas molares e proporção; 0,125 pela massa de CaO com unidade."
      },
      {
        "label": "d",
        "points": 0.25,
        "prompt": "Calcule a massa de CO₂ liberada no mesmo processo e verifique a conservação da massa. Explique por que a massa do sólido restante é menor que a massa inicial.",
        "answer": "11,0 g de CO₂; 14,0 + 11,0 = 25,0 g. A massa do sólido diminui porque parte da matéria sai na forma de gás.",
        "steps": [
          "M(CO₂) = 12 + 2×16 = 44 g/mol. Como a relação CaCO₃:CO₂ é 1:1, formam-se 0,250 mol de CO₂.",
          "m(CO₂) = 0,250×44 = 11,0 g. Somando os produtos: 14,0 g de CaO + 11,0 g de CO₂ = 25,0 g.",
          "Se o gás escapa do recipiente, pesar só o sólido não contabiliza toda a matéria produzida. A massa total se conserva quando o gás também é incluído."
        ],
        "rubric": "0,125 pela massa de CO₂; 0,125 pela soma e explicação. Valorize a verificação coerente se houver erro transportado do item anterior."
      }
    ],
    "pitfall": "Depois de balancear, converta massa em mol, use a razão dos coeficientes e só então volte para gramas. Inclua todos os produtos ao conferir a conservação da massa.",
    "sources": [
      [
        "#calibracao",
        "Conteúdo e referências do simulado"
      ]
    ]
  }
];
const examCalibration = [];
