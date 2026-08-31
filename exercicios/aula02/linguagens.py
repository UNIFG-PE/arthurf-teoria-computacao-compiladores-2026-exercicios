from itertools import product

def sigma_n(sigma: set[str], n: int) -> set[str]:
    return {"".join(t) for t in product (sorted (sigma), repeat=n)}


def sigma_star(sigma: set[str], limite: int) -> set[str]:
    return set().union(*(sigma_n(sigma, n) for n in range(limite + 1)))


def potencia(L: set[str], n: int) -> set[str]:
    if n < 0:
        raise ValueError('n não pode ser menor do que 0')
    resultado = {''}
    for _ in range(n):
        resultado = {x+y for y in resultado for x in L}
    return resultado


def concat(L1: set[str], L2: set[str]) -> set[str]:
    return {x+y for y in L2 for x in L1}


def kleene(L: set[str], n_max: int) -> set[str]:
    return set().union(*(potencia(L, n) for n in range(n_max + 1)))


def positivo(L: set[str], n_max: int) -> set[str]:
    return set().union(*(potencia(L, n) for n in range(1, n_max + 1)))


def reverso(L: set[str]) -> set[str]:
    def inverter(s: str) -> str:
        resultado = ''
        for i in range(len(s)):
            resultado += s[len(s)-i-1]
        return resultado
    return {inverter(x) for x in L}


def complemento(L: set[str], sigma: set[str], limite: int) -> set[str]:
    return sigma_star(sigma, limite) - L


def prefixos(w: str) -> set[str]:
    return {w[:i] for i in range(len(w)+1)}    


def sufixos(w: str) -> set[str]:
    return {w[i:] for i in range(len(w)+1)}    


def subcadeias(w: str) -> set[str]:
    return {w[s:e] for e in range(len(w)+1) for s in range(e+1)}


# Por padrão sets em python não são ordenados
def ordem_canonica(sigma: set[str], n: int) -> list[str]:
    if n < 0:
        raise ValueError('n não pode ser menor do que 0')
    tamanho = 0
    resultado = []
    while True:
        cadeias = sorted(sigma_n(sigma, tamanho))
        for cadeia in cadeias:
            if len(resultado) == n:
                return resultado
            resultado.append(cadeia)
        tamanho += 1


def eh_palindromo(w: str) -> bool:
    for i in range(len(w) // 2):
        if w[i] != w[len(w) - i - 1]:
            return False
    return True


def verificar_identidades() -> dict[str, bool]:
    L1 = {"a","ab"}
    L2 = {"b",""}
    limite = 6
    esquerda = kleene(kleene(L1, limite), limite)
    direita = kleene(L1, limite)
    return {
        "(L*)* == L*": {w for w in esquerda if len(w) <= limite} == {w for w in direita if len(w) <= limite},
        "L·{ε} == L": concat(L1, {''}) == L1,
        "L·∅ == ∅": concat(L1, set()) == set(),
        "(L₁L₂)ᴿ == L₂ᴿ L₁ᴿ": reverso(concat(L1, L2)) == concat(reverso(L2), reverso(L1)),
    }