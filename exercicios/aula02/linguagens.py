
def sigma_n(sigma: set[str], n: int) -> set[str]:
    if n < 0:
        raise ValueError('n não pode ser menor do que 0')
    resultado = {''}
    for _ in range(n):
        resultado = {x+y for y in resultado for x in sigma}
    return resultado


def sigma_star(sigma: set[str], limite: int) -> set[str]:
    if limite < 0:
        raise ValueError('limite não pode ser menor do que 0')
    resultado = {''}
    for _ in range(limite):
        resultado = resultado.union({x+y for y in resultado for x in sigma})
    return resultado


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
    if n_max < 0:
        raise ValueError('limite não pode ser menor do que 0')
    resultado = {''}
    for _ in range(n_max):
        resultado = resultado.union({x+y for y in resultado for x in L})
    return resultado


def positivo(L: set[str], n_max: int) -> set[str]:
    if n_max < 0:
        raise ValueError('limite não pode ser menor do que 0')
    elif n_max == 0:
        return set()
    resultado = L
    for _ in range(n_max-1):
        resultado = resultado.union({x+y for y in resultado for x in L})
    return resultado


def reverso(L: set[str]) -> set[str]:
    def inverter(s: str) -> str:
        resultado = ''
        for i in range(len(s)):
            resultado += s[len(s)-i-1]
        return resultado
    return {inverter(x) for x in L}