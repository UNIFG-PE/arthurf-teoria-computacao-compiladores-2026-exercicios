from reconhecedores import reconhece_abc, balanceado, palindromo, tokenize

def test_abc():
    assert reconhece_abc("")
    assert reconhece_abc("aaabbbccc")
    assert not reconhece_abc("aabbc")
    assert not reconhece_abc("abcabc")

def test_balanceado():
    assert balanceado("")
    assert balanceado("(()(()))()")
    assert balanceado("[([][{}{}])]{[()]}[]")
    assert not balanceado("(()([)])")
    assert not balanceado("())(")
    assert not balanceado("((((")
    assert not balanceado("))))")

def test_palindromo():
    assert palindromo("")
    assert palindromo("a")
    assert palindromo("aa")
    assert palindromo("abba")
    assert palindromo("acbbca")
    assert palindromo("aaabaaa")
    assert not palindromo("aaab")
    assert not palindromo("baaba")
    assert not palindromo("aabaaa")

def test_tokenize():
    assert tokenize("x = 1;") == [
        ("ID", "x"), ("ASSIGN", "="), ("NUM", "1"), ("SEMI", ";"),
    ]
    assert tokenize("a<=-1")[1] == ("LE", "<=")
    assert tokenize("") == []
    assert tokenize("foo = 10+ 4;") == [
        ("ID", "foo"),
        ("ASSIGN", "="),
        ("NUM", "10"),
        ("PLUS", "+"),
        ("NUM", "4"),
        ("SEMI", ";"),
    ]
    assert tokenize("""
        while(value <= 10000) {
            value = (value + 5) * 10.5;
            print(value);
        }
    """) == [
        ("WHILE", "while"),
        ("LPAREN", "("),
        ("ID", "value"),
        ("LE", "<="),
        ("NUM", "10000"),
        ("RPAREN", ")"),
        ("LBRACE", "{"),
        ("ID", "value"),
        ("ASSIGN", "="),
        ("LPAREN", "("),
        ("ID", "value"),
        ("PLUS", "+"),
        ("NUM", "5"),
        ("RPAREN", ")"),
        ("MUL", "*"),
        ("NUM", "10.5"),
        ("SEMI", ";"),
        ("ID", "print"),
        ("LPAREN", "("),
        ("ID", "value"),
        ("RPAREN", ")"),
        ("SEMI", ";"),
        ("RBRACE", "}"),
    ]
    assert not tokenize("a == b") == [
        ("ID", "a"),
        ("ASSIGN", "="),
        ("ASSIGN", "="),
        ("ID", "b"),
    ]