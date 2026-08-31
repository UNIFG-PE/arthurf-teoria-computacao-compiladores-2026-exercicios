Considere `Σ = {a, b, c}` salvo indicação contrária.

**A1 (5 pts).** Calcule: (a) `|Σ⁵|`; (b) o número de cadeias de tamanho ≤ 5;
(c) o número de cadeias de tamanho exatamente 4 sobre um alfabeto de 7 símbolos.
Mostre a fórmula usada.

**R:** 
|#|Formula|Resposta|
|---|---|---|
|a|$k^n$|$3^5=243$|
|b|$\frac{k^{n+1}-1}{k-1}$|$\frac{3^{5+1}-1}{3-1}=364$|
|c|$k^n$|$7^4=2401$|

---

**A2 (5 pts).** Liste **todos** os elementos de:
(a) `{ab, c}²`  (b) `{a, ε} · {b, c}`  (c) `{ab}³`  (d) `∅²`  (e) `{ε}⁴`

**R:**
|#|Resposta|
|---|---|
|a|`{abab, abc, cab, cc}`|
|b|`{ab, ac, b, c}`|
|c|`{ababab}`|
|d|`∅`|
|e|`{ε}`|

---

**A3 (5 pts).** Para `w = abcab`, liste: todos os prefixos, todos os sufixos,
todos os prefixos **próprios**, e 5 subcadeias distintas de tamanho ≥ 2.
Quantas subcadeias distintas `w` possui no total?

**R:** 
- Prefixos: `{ε, a, ab, abc, abca, abcab}`
- Sufixos: `{ε, b, ab, cab, bcab, abcab}`
- Prefixos próprios: `{a, ab, abc, abca}`
- `{ab, bc, ca, abc, bca}`
- $1+3+3+3+2+1=13$

---

**A4 (5 pts).** Prove que `|Σⁿ| = kⁿ` para `|Σ| = k`, por **indução em `n`**.

**R:**

Primeiramente será confirmado o caso base:
$\lvert\Sigma^0\rvert=k^0$
\
Por definição $\Sigma^0=\lbrace\varepsilon\rbrace$ e $k^0=1$
\
Logo $\lvert\Sigma^0\rvert=1$ então $\lvert\Sigma^0\rvert=k^0$, o caso base é provado.
\
Para o passo indutivo, suponha que $\lvert\Sigma^n\rvert=k^n$ seja verdadeiro.
\
Seria preciso provar que $\lvert\Sigma^{n+1}\rvert=k^{n+1}$
\
Pela regra de contagem de produtos cartesianos $\vert\Sigma^{n+1}\vert=\lvert\Sigma^n\rvert\cdot\lvert\Sigma\rvert$
\
Por fim considerando que $\lvert\Sigma\rvert=k$ e a hipotese de $\lvert\Sigma^n\rvert=k^n$ poderá ser confirmado que $\lvert\Sigma^{n+1}\rvert=k^{n+1}$
\
Logo provando $\lvert\Sigma^n\rvert=k^n$ para todo $n\ge0$


---

**A5 (5 pts).** Quantas cadeias de tamanho `n` sobre `{a,b}` são palíndromos?
Dê a fórmula para `n` par e `n` ímpar e justifique. 

**R:**

|Caso|Fórmula|Justificativa|
|---|---|---|
|`n` par|$2^\frac{n}{2}$|Uma cadeia pode ser considerada um palíndromo caso $w=w^R$, como a segunda metade vai ser sempre derivada da primeira, o número de combinações possíveis é determinado apenas pela primeira metade.|
|`n` ímpar|$2^\frac{n+1}{2}$|No caso ímpar precisará ser considerado o símbolo no meio da cadeia, já que ele não é exclusivo de nenhuma das duas metades da cadeia e não afeta a classificação de palíndromo, logo pode ser qualquer símbolo, multiplicando a quantidade de combinações.|

---

Para cada item, responda **V** ou **F** e justifique em 1–3 linhas
(contraexemplo vale como justificativa de falsidade).

| # | Afirmação |
|---|---|
| B1 | `∅ = {ε}` |
| B2 | `∅* = {ε}` |
| B3 | `L · ∅ = L` para toda linguagem `L` |
| B4 | `(L*)* = L*` |
| B5 | `L⁺ = L*` se e somente se `ε ∈ L` |
| B6 | `(L₁L₂)ᴿ = L₂ᴿ L₁ᴿ` |
| B7 | `L₁ ∩ L₂ = ∅` implica `L₁L₂ = ∅` |
| B8 | Se `L` é finita, `L*` é finita |
| B9 | `Σ*` é enumerável |
| B10 | O conjunto de todas as linguagens sobre `Σ` é enumerável |

**R:**

|#|Resposta|Justificativa|
|---|---|---|
|B1|F|`{ε}` é uma linguagem que contem apenas uma cadeia vazia, ou seja aceita uma cadeia vazia, já `∅` é uma linguagem vazia que não aceitaria uma cadeia vazia.|
|B2|V|O fechamento de Kleene sempre irá incluir uma cadeia vazia na linguagem resultante.|
|B3|F|Verdadeiro apenas caso `L = ∅`, contraexemplo: `{a} · ∅ = ∅`.|
|B4|V|Aplicar o fechamento de Kleene duas vezes não cria elementos novos.|
|B5|V|O fechamento positivo não irá automaticamente incluir uma cadeia vazia na linguagem resultante ao contrário do fechamento de Kleene, mas caso a linguagem já inclua a cadeia vazia, ela será mantida.|
|B6|V|Verdadeiro pois a ordem dos fatores é invertida caso a ordem da concatenação total seja invertida.|
|B7|F|Mesmo que duas linguagens sejam disjuntas, não significa uqe a concatenação delas resulte tem uma linguagem vazia, contraexemplo: `{a} ∩ {b} = ∅`, mas `{a} · {b} = {ab}` |
|B8|F|O fechamento de Kleene pode criar linguagens infinitas usando linguagens finitas, contraexemplo: `{a*} = {a, aa, aaa, aaaa, ...}`|
|B9|V|Mesmo que infinito, um conjunto em que o fechamento de Kleene foi aplicado ainda é enumerável, pois seus elementos ainda podem ser listados individualmente.|
|B10|F|Assuma que hipoteticamente uma enumeração de todas as linguagens seja criada, agora selecione o elemento no indice `n` de cada linguagem na enumeração `n` (diagonalmente), altere cada um dos elementos para simbolos diferentes e junte os elementos selecionados para criar uma linguagem nova, essa linguagem nova é garantida de não estar na enumeração, pois difere de cada uma das linguagens em pelo menos um elemento, logo essa enumeração não pode existir, significando que o conjunto de todas as linguagens sobre `Σ` não é enumerável.|

---

**C1 (10 pts).** Escreva na notação `{ w ∈ Σ* | P(w) }` e dê 3 exemplos de
cadeias pertencentes + 2 não pertencentes. `Σ = {a, b}`:

1. Cadeias que começam e terminam com símbolos diferentes
2. Cadeias com número de `a`s múltiplo de 3
3. Cadeias em que nenhum `b` é seguido por outro `b`
4. Cadeias de tamanho par cujo primeiro e último símbolos são iguais
5. `{ aⁱbʲaᵏ | i + k = j }`

**R:**

|#|Notação|Pertencentes|Não pertencentes|
|---|---|---|---|
|1|$\lbrace w\in \Sigma^*\mid primeiro(w)\ne último(w)\rbrace$|`ab`, `aab` e `baa`|`aa` e `a`|
|2|$\lbrace w\in \Sigma^*\mid \#_a(w) \equiv 0\pmod 3\rbrace$|`aaa`, `baaa` e `aaaaaa`|`baa` e `aaaa`|
|3|$\lbrace w\in \Sigma^*\mid bb \text{ não ocorre em }w\rbrace$|`aabaaa`, `baba` e `abaab`|`bb` e `aabb`|
|4|$\lbrace w\in \Sigma^*\mid \lvert w\rvert\equiv 0 \pmod 2\land primeiro(w)=último(w)\rbrace$|`bb`, `baab` e `aabbba`|`aab` e `ab`|
|5|$\lbrace w\in \Sigma^*\mid w=a^ib^ja^k, i+k=j\rbrace$|`abba`, `aabbba` e `aaabbbbbaa`|`aabba` e `abbba`|

---

**E1.** Escreva `enumerar(sigma)` como um **gerador infinito** (`yield`) que
produz `Σ*` em ordem canônica indefinidamente. Use-o para imprimir a 1000ª
cadeia sobre `{a,b,c}`. Explique por que esse gerador é a prova construtiva de
que `Σ*` é enumerável — e por que **não** existe gerador análogo para o conjunto
de todas as linguagens sobre `Σ`.

(Utilizando as funções definidas em `linguagens.py`)
```py
def enumerar(sigma: set[str]) -> Iterator[str]:
    tamanho = 0
    while True:
        cadeias = sorted(sigma_n(sigma, tamanho))
        for cadeia in cadeias:
            yield cadeia
        tamanho += 1
```

O gerador é uma **prova construtiva** de que `Σ*` é enumerável porque ele produz todas as cadeias de `Σ*` em uma sequência, em ordem canônica. Como toda cadeia possui tamanho finito, ela será alcançada pelo gerador em algum momento.
\
Já o conjunto de **todas as linguagens** sobre `Σ` é `𝒫(Σ*)`, o conjunto das partes de `Σ*`. Pelo **Teorema de Cantor**, o conjunto das partes de um conjunto enumerável infinito é **não enumerável**.
\
Portanto, existe um gerador para todas as cadeias de `Σ*`, mas não existe um gerador que produza todas as linguagens sobre `Σ`.
