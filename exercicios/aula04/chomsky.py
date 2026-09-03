"""
Classificação de gramáticas formais na hierarquia de Chomsky.

Uma produção é representada como uma tupla (lado_esquerdo, lado_direito),
onde cada lado é uma *lista* de símbolos (para suportar terminais/variáveis
com mais de um caractere, como "if", "then", etc):

    Producao = tuple[list[str], list[str]]
    P = [(["S"], ["if", "E", "then", "S"]), (["S"], ["cmd"])]

Tipos (Chomsky):
    3 - Regular         : lado esquerdo é uma única variável; lado direito
                           tem no máximo uma variável, sempre na mesma
                           extremidade (só no fim = "direita/right-linear"
                           ou só no início = "esquerda/left-linear"), sem
                           misturar as duas orientações na mesma gramática.
    2 - Livre de contexto: lado esquerdo é sempre uma única variável.
    1 - Sensível ao ctx.: |lado_esquerdo| <= |lado_direito| em toda produção,
                           exceto a produção S -> ε, permitida somente se S
                           não aparecer no lado direito de nenhuma produção.
    0 - Irrestrita       : qualquer produção (lado esquerdo não vazio).
"""

from __future__ import annotations

Simbolos = list[str]
Producao = tuple[Simbolos, Simbolos]


# --------------------------------------------------------------------------- #
# Utilidades de formatação
# --------------------------------------------------------------------------- #

def _formatar_lado(simbolos: Simbolos) -> str:
    if not simbolos:
        return "ε"
    if all(len(s) == 1 for s in simbolos):
        return "".join(simbolos)
    return " ".join(simbolos)


def formatar_producao(producao: Producao) -> str:
    """Formata uma produção como 'lado_esq → lado_dir', em português."""
    lhs, rhs = producao
    return f"{_formatar_lado(lhs)} → {_formatar_lado(rhs)}"


# --------------------------------------------------------------------------- #
# Tipo 3 (regular)
# --------------------------------------------------------------------------- #

def _analisar_regular(lhs: Simbolos, rhs: Simbolos, V: set[str]):
    """
    Analisa se uma única produção é compatível com gramática regular.

    Retorna (compat, motivo):
      - compat: subconjunto de {"D", "E"} com as orientações compatíveis
        ("D" = direita/right-linear, variável só pode vir no fim;
         "E" = esquerda/left-linear, variável só pode vir no início).
        Uma produção sem nenhuma variável no lado direito é compatível com
        as duas orientações.
      - motivo: None se compat não for vazio; caso contrário, uma string em
        português explicando por que a produção não é regular.
    """
    if len(lhs) != 1 or lhs[0] not in V:
        return set(), "não tem uma única variável do lado esquerdo"

    variaveis = [i for i, s in enumerate(rhs) if s in V]

    if len(variaveis) > 1:
        return set(), "tem mais de uma variável do lado direito"

    if len(variaveis) == 0:
        return {"D", "E"}, None

    idx = variaveis[0]
    compat = set()
    if idx == len(rhs) - 1:
        compat.add("D")
    if idx == 0:
        compat.add("E")

    if compat:
        return compat, None

    # a variável está "no meio" da cadeia: não é nem right- nem left-linear
    if idx != len(rhs) - 1:
        return set(), "tem terminal após a variável"
    return set(), "tem terminal antes da variável"


def eh_tipo3(V: set[str], Sigma: set[str], P: list[Producao]) -> bool:
    compats = []
    for lhs, rhs in P:
        compat, motivo = _analisar_regular(lhs, rhs, V)
        if motivo is not None:
            return False
        compats.append(compat)
    if not compats:
        return True
    intersecao = set.intersection(*compats)
    return len(intersecao) > 0


# --------------------------------------------------------------------------- #
# Tipo 2 (livre de contexto)
# --------------------------------------------------------------------------- #

def eh_tipo2(V: set[str], Sigma: set[str], P: list[Producao]) -> bool:
    return all(len(lhs) == 1 and lhs[0] in V for lhs, rhs in P)


# --------------------------------------------------------------------------- #
# Tipo 1 (sensível ao contexto)
# --------------------------------------------------------------------------- #

def _s_aparece_do_lado_direito(P: list[Producao], S: str) -> bool:
    return any(S in rhs for _, rhs in P)


def eh_tipo1(V: set[str], Sigma: set[str], P: list[Producao], S: str) -> bool:
    s_no_lado_direito = _s_aparece_do_lado_direito(P, S)
    for lhs, rhs in P:
        if len(rhs) >= len(lhs):
            continue
        if lhs == [S] and rhs == [] and not s_no_lado_direito:
            continue
        return False
    return True


# --------------------------------------------------------------------------- #
# E1: classificar
# --------------------------------------------------------------------------- #

def classificar(V: set[str], Sigma: set[str], P: list[Producao], S: str) -> int:
    """Devolve o tipo de Chomsky da gramática (3, 2, 1 ou 0)."""
    V = set(V)
    Sigma = set(Sigma)

    if eh_tipo3(V, Sigma, P):
        return 3
    if eh_tipo2(V, Sigma, P):
        return 2
    if eh_tipo1(V, Sigma, P, S):
        return 1
    return 0


# --------------------------------------------------------------------------- #
# E2: explicar
# --------------------------------------------------------------------------- #

def _razao_nao_tipo3(V: set[str], Sigma: set[str], P: list[Producao]) -> str:
    compats_por_producao = []
    for producao in P:
        lhs, rhs = producao
        compat, motivo = _analisar_regular(lhs, rhs, V)
        if motivo is not None:
            return f"a produção {formatar_producao(producao)} {motivo}."
        compats_por_producao.append((producao, compat))

    # Todas as produções são individualmente regulares, mas misturam
    # orientações (uma exige "D" e outra exige "E").
    producao_direita = next(
        (p for p, c in compats_por_producao if c == {"D"}), None
    )
    producao_esquerda = next(
        (p for p, c in compats_por_producao if c == {"E"}), None
    )
    if producao_direita is not None and producao_esquerda is not None:
        return (
            f"a produção {formatar_producao(producao_direita)} tem a variável "
            f"à direita (right-linear) e a produção "
            f"{formatar_producao(producao_esquerda)} tem a variável à esquerda "
            "(left-linear); a gramática mistura as duas orientações."
        )
    return "as produções misturam orientações incompatíveis entre si."


def _razao_nao_tipo2(V: set[str], Sigma: set[str], P: list[Producao]) -> str:
    for producao in P:
        lhs, rhs = producao
        if not (len(lhs) == 1 and lhs[0] in V):
            return (
                f"a produção {formatar_producao(producao)} não tem uma única "
                "variável do lado esquerdo."
            )
    return "motivo desconhecido."


def _razao_nao_tipo1(V: set[str], Sigma: set[str], P: list[Producao], S: str) -> str:
    s_no_lado_direito = _s_aparece_do_lado_direito(P, S)
    for producao in P:
        lhs, rhs = producao
        if len(rhs) >= len(lhs):
            continue
        if lhs == [S] and rhs == [] and not s_no_lado_direito:
            continue
        return (
            f"a produção {formatar_producao(producao)} tem o lado direito "
            "mais curto que o lado esquerdo."
        )
    return "motivo desconhecido."


def explicar(V: set[str], Sigma: set[str], P: list[Producao], S: str) -> str:
    """Devolve o tipo da gramática e a produção que bloqueou o tipo superior."""
    V = set(V)
    Sigma = set(Sigma)
    tipo = classificar(V, Sigma, P, S)

    if tipo == 3:
        return "Tipo 3."
    if tipo == 2:
        return f"Tipo 2. Não é tipo 3: {_razao_nao_tipo3(V, Sigma, P)}"
    if tipo == 1:
        return f"Tipo 1. Não é tipo 2: {_razao_nao_tipo2(V, Sigma, P)}"
    return f"Tipo 0. Não é tipo 1: {_razao_nao_tipo1(V, Sigma, P, S)}"


# --------------------------------------------------------------------------- #
# E3: valida_gramatica
# --------------------------------------------------------------------------- #

def valida_gramatica(V: set[str], Sigma: set[str], P: list[Producao], S: str) -> list[str]:
    """Devolve a lista de problemas estruturais encontrados na gramática."""
    V = set(V)
    Sigma = set(Sigma)
    problemas: list[str] = []

    intersecao = V & Sigma
    if intersecao:
        problemas.append(
            f"Variáveis e terminais têm símbolos em comum: {sorted(intersecao)}."
        )

    if S not in V:
        problemas.append(f"O símbolo inicial '{S}' não pertence ao conjunto de variáveis V.")

    alfabeto = V | Sigma
    for producao in P:
        lhs, rhs = producao
        for simbolo in lhs + rhs:
            if simbolo not in alfabeto:
                problemas.append(
                    f"O símbolo '{simbolo}' da produção {formatar_producao(producao)} "
                    "não pertence a V ∪ Σ."
                )
        if not any(s in V for s in lhs):
            problemas.append(
                f"A produção {formatar_producao(producao)} não tem nenhuma "
                "variável do lado esquerdo."
            )

    # Variáveis inalcançáveis a partir de S
    alcancaveis: set[str] = {S} if S in V else set()
    mudou = True
    while mudou:
        mudou = False
        for lhs, rhs in P:
            variaveis_lhs = [s for s in lhs if s in V]
            if variaveis_lhs and all(s in alcancaveis for s in variaveis_lhs):
                for s in rhs:
                    if s in V and s not in alcancaveis:
                        alcancaveis.add(s)
                        mudou = True
    for variavel in sorted(V - alcancaveis):
        problemas.append(f"A variável '{variavel}' é inalcançável a partir de {S}.")

    # Variáveis improdutivas (não derivam nenhuma cadeia de terminais)
    produtivas: set[str] = set()
    mudou = True
    while mudou:
        mudou = False
        for lhs, rhs in P:
            if all(s in Sigma or s in produtivas for s in rhs):
                for s in lhs:
                    if s in V and s not in produtivas:
                        produtivas.add(s)
                        mudou = True
    for variavel in sorted(V - produtivas):
        problemas.append(
            f"A variável '{variavel}' é improdutiva (não deriva nenhuma "
            "cadeia de terminais)."
        )

    return problemas
