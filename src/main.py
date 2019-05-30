from lexer import *
from parser import *


def main(file_name):
    content = ""
    with open(file_name, 'r') as f:
        content = f.read()

    # Lexer odje
    lex = Lexer(content)
    tokens = lex.tokinize()
    print(tokens)
    

if __name__ == "__main__":
    main('./test.dr')