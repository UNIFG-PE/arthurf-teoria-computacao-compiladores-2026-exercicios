from linguagens import sigma_n, sigma_star, concat, potencia, kleene, positivo

def test_sigma_n():
    assert sigma_n(set(), 4) == set()
    assert sigma_n({''}, 4) == {''}
    assert sigma_n({'a', 'b'}, 2) == {'aa', 'ab', 'ba', 'bb'}
    assert sigma_n({'a', 'b', 'c'}, 2) == {'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'}
    assert sigma_n({'a', 'b'}, 3) == {'aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'}


def test_sigma_star():
    assert sigma_star(set(), 1) == {''}
    assert sigma_star({''}, 1) == {''}
    assert sigma_star({'a', 'b'}, 3) == {'', 'ab', 'b', 'aab', 'aba', 'bbb', 'ba', 'a', 'bb', 'aa', 'baa', 'bab', 'abb', 'bba', 'aaa'}


def test_concat():
    assert concat({'a', 'ab'}, {''}) == {'a', 'ab'}
    assert concat({'a', 'ab'}, {'b', ''}) == {'a', 'ab', 'abb'}
    assert concat({'ab', 'ac'}, {'cd', 'a', 'b'}) == {'abcd', 'aba', 'abb', 'accd', 'aca', 'acb'}


def test_concat_aniquilador():
    assert concat({"a", "b"}, set()) == set()


def test_potencia():
    assert potencia(set(), 4) == set()
    assert potencia({''}, 4) == {''}
    assert potencia({'a', 'b'}, 0) == {''}
    assert potencia({'a', 'b'}, 2) == {'aa', 'ab', 'ba', 'bb'}
    assert potencia({'a', 'ab'}, 2) == {'aa', 'aab', 'aba', 'abab'}
    

def test_kleene():
    assert kleene({''}, 2) == {''}
    assert kleene({'ab', 'a'}, 1) == {'', 'ab', 'a'}
    assert kleene({'ab', 'cbe'}, 3) == {'', 'abcbeab', 'cbecbecbe', 'cbeabcbe', 'cbecbeab', 'abcbe', 'ab', 'ababcbe', 'cbeab', 'abab', 'abcbecbe', 'cbe', 'cbeabab', 'cbecbe', 'ababab'}


def test_kleene_do_vazio():
    assert kleene(set(), 3) == {""}


def test_positivo():
    assert positivo(set(), 3) == set()
    assert positivo({'ab', 'a'}, 1) == {'ab', 'a'}
    assert positivo({'ab', 'cbe'}, 3) == {'abcbeab', 'cbecbecbe', 'cbeabcbe', 'cbecbeab', 'abcbe', 'ab', 'ababcbe', 'cbeab', 'abab', 'abcbecbe', 'cbe', 'cbeabab', 'cbecbe', 'ababab'}
    

'''
def test_ordem_canonica():
    assert ordem_canonica({"0", "1"}, 7) == ["", "0", "1", "00", "01", "10", "11"]
'''
