from lexer import Lexer, Token
from parsing import Transformer
is_main = (__name__ == '__main__')


def main():
    lex = Lexer("1 + 1 + 2 + 3")
    
    while not lex.isEmpty():
        token = lex.next()
        token.display()
















# ENTRY.
(
    lambda : 
    main() if is_main 
    else exit(0)
)()


