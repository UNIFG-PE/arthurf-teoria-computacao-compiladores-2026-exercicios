# Respostas — Aula 04: Hierarquia de Chomsky

## Parte A — Classificando gramáticas

> Critério usado: tipo 3 = regular; tipo 2 = livre de contexto; tipo 1 = sensível ao contexto; tipo 0 = irrestrita.

### A1
**Tipo 3 (regular).** Todas as produções são lineares à direita: `S → 0S`, `S → 1S` e `S → ε`. Não há produção que impeça um tipo superior, pois 3 já é o tipo mais restrito.

### A2
**Tipo 3 (regular).** A gramática é linear à esquerda: `S → S0 | S1 | 0 | 1`. Não há produção que impeça um tipo superior.

### A3
**Tipo 2 (livre de contexto).** A produção `S → 0S1` impede o tipo 3, pois a variável `S` aparece entre terminais; uma gramática regular deve manter orientação linear compatível, com no máximo uma variável em uma extremidade.

### A4
**Tipo 2 (livre de contexto).** As produções `S → 0S` e `S → S1` misturam orientação à direita e à esquerda. Assim, a gramática não é tipo 3.

### A5
**Tipo 1 (sensível ao contexto).** A produção `cB → Bc` tem mais de uma variável/símbolo no lado esquerdo e impede que a gramática seja tipo 2. As produções não encurtam a cadeia.

### A6
**Tipo 2 (livre de contexto).** A produção `S → AB` impede o tipo 3, pois seu lado direito possui duas variáveis.

### A7
**Tipo 1 (sensível ao contexto).** A produção `AB → BA` impede o tipo 2, pois o lado esquerdo contém duas variáveis. Ela preserva o comprimento, portanto é compatível com tipo 1.

### A8
**Tipo 0 (irrestrita).** A produção `aA → ε` encurta a cadeia e não é uma exceção do tipo 1 para o símbolo inicial. Além disso, o lado esquerdo tem terminal e variável, então não é tipo 2.

### A9
**Tipo 3 (regular).** `S → aB`, `S → ε` e `B → bS` são produções lineares à direita. Não há impedimento para um tipo mais restrito que o próprio tipo 3.

### A10
**Tipo 2 (livre de contexto).** A produção `S → aSa` impede o tipo 3, pois a variável aparece entre dois terminais. Como todo lado esquerdo possui uma única variável, a gramática é livre de contexto.

---

## Parte B — Localizando linguagens

### B1
**Regular.** A linguagem depende apenas dos dois últimos símbolos. Um AFD com estados que registram o sufixo relevante (`ε`, `0`, `00`) reconhece exatamente as palavras que terminam em `00`.

### B2
**LLC (livre de contexto).** Uma GLC é `S → 0S1 | ε`. A pilha permite contar os `0`s e associar cada um a um `1`.

### B3
**LSC (sensível ao contexto).** A linguagem `{0ⁿ1ⁿ2ⁿ}` exige comparar três quantidades simultaneamente. Ela não é livre de contexto, mas é sensível ao contexto.

### B4
**LSC (sensível ao contexto).** `{ww}` exige copiar exatamente a primeira metade na mesma ordem. Essa linguagem não é livre de contexto, mas é sensível ao contexto.

### B5
**LLC (livre de contexto).** Uma GLC é `S → aSa | bSb | ε`. A pilha consegue guardar a primeira metade e comparar a segunda metade na ordem inversa.

### B6
**Recursiva.** Para uma entrada `aⁿ`, basta contar `n` e testar efetivamente se existe inteiro `k` tal que `k² = n`. Logo, há um algoritmo que sempre termina e decide a linguagem.

### B7
**Recursiva.** Para uma entrada `aⁿ`, conta-se `n` e testa-se se `n` é primo por divisão até `√n`, por exemplo. O algoritmo sempre termina.

### B8
**RE (recursivamente enumerável), mas não recursiva.** Essa é a linguagem de máquinas de Turing que aceitam pelo menos uma cadeia. Podemos enumerar pares `(entrada, tempo)` e simular todas as máquinas: se alguma entrada for aceita, eventualmente encontramos uma aceitação. Porém, não existe algoritmo geral que sempre decida o problema.

### B9
**Não RE.** É o complemento de B8: máquinas que não aceitam nenhuma cadeia. Se essa linguagem fosse RE, B8 e seu complemento seriam RE, o que tornaria B8 recursiva, contrariando a indecidibilidade do problema.

### B10
**LLC (livre de contexto).** JSON sintaticamente válido possui estruturas aninhadas, como objetos e arrays, que podem ser descritas por uma gramática livre de contexto. A validação puramente sintática não exige propriedades semânticas como existência prévia de variáveis.

### Diferença entre B4 e B5
Em `{wwᴿ}`, depois de ler `w`, uma pilha contém os símbolos de `w` e os devolve naturalmente na ordem inversa; por isso a comparação com `wᴿ` é adequada ao comportamento LIFO da pilha. Já `{ww}` exige reproduzir a primeira metade na **mesma ordem**, o que uma única pilha não consegue fazer em geral. Por isso B5 é LLC, enquanto B4 não é LLC e está em uma classe mais ampla, como LSC.

---

## Parte C — Gramática ≠ Linguagem

### C1
Uma gramática de **tipo 2** que gera uma linguagem regular é:

```text
S → aS | aA
A → bA | ε
```

Ela não é tipo 3 no sentido estrito de uma única orientação linear, pois as produções ainda podem ser reorganizadas para uma forma regular; porém uma forma claramente equivalente de tipo 3 para a mesma linguagem é:

```text
S → aS | aA
A → bA | ε
```

A linguagem gerada é `a⁺b*`, que é regular.

Uma maneira ainda mais explícita de mostrar o ponto é usar uma gramática tipo 2 com uma produção não regular, mas que seja redundante para a linguagem:

```text
S → aS | bS | ε | A
A → aAb | ε
```

Como `S → aS | bS | ε` já gera `{a,b}*`, a linguagem total continua sendo `{a,b}*`, que é regular, embora a gramática contenha a produção tipo 2 `A → aAb`.

Uma gramática de tipo 3 equivalente é:

```text
S → aS | bS | ε
```

Portanto, o tipo de uma gramática não determina automaticamente a menor classe da linguagem que ela gera.

### C2
Uma gramática de **tipo 1** que gera uma linguagem livre de contexto pode ser:

```text
S → AB
A → aA | a
B → bB | b
```

Essa gramática também pode ser vista como uma gramática livre de contexto, pois todo lado esquerdo possui exatamente uma variável. Ela gera `a⁺b⁺`.

Uma GLC equivalente é exatamente:

```text
S → AB
A → aA | a
B → bB | b
```

O ponto central é que uma linguagem pode pertencer simultaneamente a várias classes da hierarquia. Como LLC está contida em LSC, toda linguagem livre de contexto também é sensível ao contexto (considerando as convenções usuais para `ε`).

### C3
A afirmação é falsa porque **o tipo da gramática é uma propriedade da forma das produções, enquanto ser regular é uma propriedade da linguagem**. Uma gramática pode conter uma produção que a impeça de ser classificada como tipo 3 e, ainda assim, gerar uma linguagem regular.

Por exemplo:

```text
S → aS | bS | ε | A
A → aAb | ε
```

A produção `A → aAb` não é regular, mas `S → aS | bS | ε` já gera toda a linguagem `{a,b}*`. Portanto, a linguagem gerada pela gramática inteira é regular, mesmo que a gramática seja classificada como tipo 2 e não como tipo 3.

---

## Parte D — Compiladores e a hierarquia

### D1

| Regra | Classe mais adequada | Fase do compilador |
|---|---|---|
| a) identificadores começam com letra ou `_` | Regular | Análise léxica (lexer/tokenizer) |
| b) todo `{` tem um `}` correspondente | LLC | Análise sintática (parser) |
| c) toda variável usada foi declarada | Não é apenas uma propriedade sintática local; exige contexto | Análise semântica / tabela de símbolos |
| d) número de argumentos casa com a assinatura | Exige contexto | Análise semântica / verificação de tipos |
| e) literais de string são delimitados por `"` | Regular | Análise léxica |
| f) `return` em função `void` não pode ter expressão | Exige contexto sobre a função atual | Análise semântica |

As regras c), d) e f) dependem de informações externas à estrutura local da cadeia, como declarações anteriores, escopo e assinatura de funções. Na prática, os compiladores resolvem isso com tabelas de símbolos, árvores sintáticas e verificações semânticas.

### D2
A linguagem `{wcw | w ∈ {a,b}*}` representa, na prática, uma regra que exigiria que o parser comparasse duas partes arbitrariamente longas do programa e verificasse que elas são **idênticas na mesma ordem**.

Um exemplo conceitual seria exigir que dois trechos separados de código tivessem exatamente a mesma sequência de tokens. Uma GLC comum não consegue impor essa igualdade geral. Compiladores reais resolvem dependências desse tipo fora do parser, usando análise semântica, tabelas de símbolos, árvores sintáticas, estruturas de dados e algoritmos específicos.

### D3
O tokenizador de Python calcula a indentação no início de cada linha lógica e mantém uma **pilha de níveis de indentação**. Se a indentação aumenta, o novo nível é empilhado e é produzido um token `INDENT`. Se diminui, os níveis correspondentes são desempilhados e é produzido um `DEDENT` para cada nível removido. No fim do arquivo, os níveis restantes também geram `DEDENT`. citeturn0search0turn0search2

Essa solução é necessária porque a estrutura dos blocos em Python é escrita com espaço em branco, mas o parser precisa receber marcadores explícitos de início e fim de bloco. Assim, o tokenizer transforma a informação visual de indentação em tokens estruturais. Isso mostra que o problema não é que gramáticas livres de contexto sejam incapazes de representar blocos aninhados: depois da tokenização, o parser recebe `INDENT` e `DEDENT`, que tornam a estrutura explícita. A própria pilha usada pelo tokenizer também é suficiente para acompanhar níveis aninhados de indentação. citeturn0search0turn0search2

Fonte consultada: urlDocumentação oficial do Python — Análise léxica e indentaçãoturn0search0

---

## Parte F — Desafio bônus

### F1 — Gramática sensível ao contexto para `{ww | w ∈ {a,b}*}`

Uma construção sensível ao contexto pode usar símbolos auxiliares para gerar uma primeira cópia de `w` e, ao mesmo tempo, deixar marcadores que serão convertidos na segunda cópia. A ideia geral é:

```text
S → aSA | bSB | c
Aa → aA
Ab → bA
Ba → aB
Bb → bB
Ac → ca
Bc → cb
```

(As regras auxiliares podem ser apresentadas em uma forma equivalente que preserve ou aumente o comprimento; o objetivo é mover os marcadores e materializar a segunda cópia.)

Para `w = ab`, a derivação conceitual produz duas cópias sincronizadas:

```text
S
⇒ aSA
⇒ abSBA
⇒ abcBA
⇒ abABc
⇒ abab
```

A ideia estrutural é que os símbolos auxiliares carregam a informação da primeira cópia até a região posterior, permitindo reproduzi-la na mesma ordem. Essa é justamente a capacidade adicional necessária para reconhecer `{ww}`.

Nenhuma GLC gera `{ww}` porque um autômato com pilha tem acesso à memória em ordem LIFO: o primeiro símbolo retirado é o último que foi guardado. Isso é perfeito para `{wwᴿ}`, pois a segunda metade aparece na ordem inversa da primeira. Para `{ww}`, seria necessário preservar e recuperar uma sequência arbitrariamente longa na mesma ordem, o que uma única pilha não consegue fazer em geral.

Em resumo:

- `{wwᴿ}`: a pilha guarda `w` e o desempilhamento já produz a ordem necessária para comparar com `wᴿ`; portanto é LLC.
- `{ww}`: é preciso copiar `w` na mesma ordem; uma única pilha não oferece essa operação de cópia geral, então a linguagem não é LLC.
- Uma gramática sensível ao contexto dispõe de mecanismos adicionais de reescrita e marcação, suficientes para coordenar as duas cópias.
