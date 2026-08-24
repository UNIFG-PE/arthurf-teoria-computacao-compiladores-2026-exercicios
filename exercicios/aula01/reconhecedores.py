
def reconhece_abc(input: str):
    a_count = 0
    b_count = 0
    c_count = 0
    phase = "a"
    for c in input:
        if c not in ["a", "b", "c"]:
            return False 
        if c == "a":
            if phase != "a":
                return False
            a_count += 1
        elif c == "b":
            if phase == "a":
                phase = "b"
            elif phase != "b":
                return False
            b_count += 1
        elif c == "c":
            if phase == "b":
                phase = "c"
            elif phase != "c":
                return False
            c_count += 1
    return a_count == b_count == c_count


def balanceado(input: str):
    stack = []
    for c in input:
        if c in ["(", "[", "{"]:
            stack.append(c)
        elif c == ")":
            if len(stack) == 0 or stack.pop() != "(":
                return False
        elif c == "]":
            if len(stack) == 0 or stack.pop() != "[":
                return False
        elif c == "}":
            if len(stack) == 0 or stack.pop() != "{":
                return False
    return len(stack) == 0


def palindromo(input: str):
    if len(input) < 2:
        return True
    l = 0
    r = len(input)-1
    while l < r:
        if input[l] != input[r]:
            return False 
        l += 1
        r -= 1 
    return True

def tokenize(input: str):
    NUMBER_CHARS = "0123456789."
    ID_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    RESERVED_WORDS = {
        "if": "IF",
        "while": "WHILE",
        "else": "ELSE",
        "for": "FOR",
        "do": "DO",
        "or": "OR",
        "and": "AND",
        "not": "NOT"
    }
    buffer = ""
    tokens = []
    i = 0
    while i < len(input):
        if input[i] == ";":
            tokens.append(("SEMI", ";"))
        elif input[i] == "(":
            tokens.append(("LPAREN", "("))
        elif input[i] == ")":
            tokens.append(("RPAREN", ")"))
        elif input[i] == "{":
            tokens.append(("LBRACE", "{"))
        elif input[i] == "}":
            tokens.append(("RBRACE", "}"))
        elif input[i] == "+":
            tokens.append(("PLUS", "+"))
        elif input[i] == "-":
            tokens.append(("MINUS", "-"))
        elif input[i] == "*":
            tokens.append(("MUL", "*"))
        elif input[i] == "/":
            tokens.append(("DIV", "/"))
        elif input[i] == "%":
            tokens.append(("MOD", "%"))
        elif input[i] == "=":
            if i < len(input)-1 and input[i+1] == "=":
                i += 1
                tokens.append(("EQUALS", "=="))
            else:
                tokens.append(("ASSIGN", "="))
        elif input[i] == ">":
            if i < len(input)-1 and input[i+1] == "=":
                i += 1
                tokens.append(("GE", ">="))
            else:
                tokens.append(("GREATER", ">"))
        elif input[i] == "<":
            if i < len(input)-1 and input[i+1] == "=":
                i += 1
                tokens.append(("LE", "<="))
            else:
                tokens.append(("LESSER", "<"))      
        elif input[i] == "!":
            if i < len(input)-1 and input[i+1] == "=":
                i += 1
                tokens.append(("NE", "!="))
            else:
                raise ValueError 
        elif input[i] in NUMBER_CHARS:
            while i < len(input) and input[i] in NUMBER_CHARS:
                buffer += input[i]
                i += 1
            try:
                float(buffer)
            except ValueError:
                raise ValueError
            tokens.append(("NUM", buffer))
            buffer = ""
            continue 
        elif input[i] in ID_CHARS:
            while i < len(input) and input[i] in ID_CHARS:
                buffer += input[i]
                i += 1
            if buffer in RESERVED_WORDS:
                tokens.append((RESERVED_WORDS[buffer], buffer))
            else:
                tokens.append(("ID", buffer))
            buffer = ""
            continue
        elif input[i].isspace():
            pass
        else:
            raise ValueError
        i += 1
    return tokens 

