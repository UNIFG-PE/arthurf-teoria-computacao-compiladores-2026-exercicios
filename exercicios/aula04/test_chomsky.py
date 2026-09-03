from chomsky import classificar, explicar, valida_gramatica


# --------------------------------------------------------------------------- #
# Tipo 3 (regular) — pelo menos 2 gramáticas
# --------------------------------------------------------------------------- #

def test_tipo3_direita():
    assert classificar({"S"}, {"a", "b"},
        [(["S"], ["a", "S"]), (["S"], ["b"])], "S") == 3


def test_tipo3_esquerda():
    # gramática left-linear: variável sempre no início do lado direito
    assert classificar({"S", "A"}, {"a", "b"},
        [(["S"], ["A", "b"]), (["A"], ["A", "a"]), (["A"], ["a"])], "S") == 3


# --------------------------------------------------------------------------- #
# Tipo 2 (livre de contexto) — pelo menos 2 gramáticas
# --------------------------------------------------------------------------- #

def test_nao_mistura_orientacao():
    # A → aB e A → Ba juntas NÃO são tipo 3
    assert classificar({"S", "A"}, {"a", "b"},
        [(["S"], ["a", "A"]), (["A"], ["S", "b"]), (["A"], [])], "S") == 2


def test_tipo2_parenteses_balanceados():
    # variável no meio do lado direito quebra o tipo 3
    assert classificar({"S"}, {"(", ")"},
        [(["S"], ["(", "S", ")"]), (["S"], ["S", "S"]), (["S"], [])], "S") == 2


# --------------------------------------------------------------------------- #
# Tipo 1 (sensível ao contexto) — pelo menos 2 gramáticas
# --------------------------------------------------------------------------- #

def test_tipo1_anbncn():
    assert classificar({"S", "B"}, {"a", "b", "c"},
        [(["S"], ["a", "B", "S", "c"]), (["S"], ["a", "B", "c"]),
         (["B", "a"], ["a", "B"]), (["B", "b"], ["b", "b"])], "S") == 1


def test_tipo1_troca_de_variaveis():
    # comprimento nunca diminui, mas o lado esquerdo tem 2 símbolos
    assert classificar({"S", "A", "B"}, {"a", "b"},
        [(["S"], ["a", "A", "B"]),
         (["A", "B"], ["B", "A"]),
         (["B", "A"], ["A", "B"]),
         (["A"], ["a"]),
         (["B"], ["b"])], "S") == 1


# --------------------------------------------------------------------------- #
# Tipo 0 (irrestrita) — pelo menos 2 gramáticas
# --------------------------------------------------------------------------- #

def test_tipo0_encurta():
    assert classificar({"S", "A", "B"}, {"a", "b"},
        [(["S"], ["a", "A", "B", "b"]), (["A", "B"], [])], "S") == 0


def test_tipo0_apaga_par():
    # AA → a encurta a cadeia e não é a exceção S → ε
    assert classificar({"S", "A"}, {"a"},
        [(["S"], ["A", "A"]), (["A", "A"], ["a"]), (["A"], ["a"])], "S") == 0


# --------------------------------------------------------------------------- #
# explicar
# --------------------------------------------------------------------------- #

def test_explicar_tipo2_nao_tipo3():
    assert explicar({"S"}, {"a", "b"},
        [(["S"], ["a", "S", "b"]), (["S"], [])], "S") == (
        "Tipo 2. Não é tipo 3: a produção S → aSb tem terminal após a variável."
    )


def test_explicar_tipo3_nao_precisa_de_motivo():
    assert explicar({"S"}, {"a", "b"},
        [(["S"], ["a", "S"]), (["S"], ["b"])], "S") == "Tipo 3."


# --------------------------------------------------------------------------- #
# valida_gramatica
# --------------------------------------------------------------------------- #

def test_valida_detecta_improdutiva():
    problemas = valida_gramatica({"S", "X"}, {"a"},
        [(["S"], ["a"]), (["X"], ["X", "a"])], "S")
    assert any("improdutiva" in p.lower() for p in problemas)


def test_valida_detecta_intersecao_v_sigma():
    problemas = valida_gramatica({"S", "a"}, {"a", "b"},
        [(["S"], ["a"])], "S")
    assert any("comum" in p.lower() for p in problemas)


def test_valida_detecta_s_fora_de_v():
    problemas = valida_gramatica({"A"}, {"a"},
        [(["A"], ["a"])], "S")
    assert any("símbolo inicial" in p.lower() for p in problemas)


def test_valida_detecta_simbolo_invalido():
    problemas = valida_gramatica({"S"}, {"a"},
        [(["S"], ["a", "X"])], "S")
    assert any("'X'" in p and "não pertence" in p.lower() for p in problemas)


def test_valida_detecta_lado_esquerdo_sem_variavel():
    problemas = valida_gramatica({"S"}, {"a", "b"},
        [(["a"], ["b"])], "S")
    assert any("nenhuma" in p.lower() and "variável" in p.lower() for p in problemas)


def test_valida_detecta_inalcancavel():
    problemas = valida_gramatica({"S", "X"}, {"a"},
        [(["S"], ["a"]), (["X"], ["a"])], "S")
    assert any("inalcançável" in p.lower() for p in problemas)


def test_valida_gramatica_correta_sem_problemas():
    problemas = valida_gramatica({"S"}, {"a", "b"},
        [(["S"], ["a", "S", "b"]), (["S"], [])], "S")
    assert problemas == []
