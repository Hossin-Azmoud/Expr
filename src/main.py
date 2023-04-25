from lexer      import Lexer, Token
from parsing    import Transformer
from structures import Stack
from reple      import Reple

is_main = (__name__ == '__main__')
def parsing_test():
    lex = Lexer("1 - 1 + 2 - 3") # Give the expression to the lexer.
    parser = Transformer(lex)
    parser.to_postfix()
    print("BEFORE EVAL: ")
    parser.dump_stack()
    parser.evaluate_stack()
    print("AFTER EVAL: ")
    parser.dump_stack()

def Stack_Test():
    stack = Stack()
    lst = [1, 2, 3, 4, 5, 6] 
    
    for i in lst:
        print(f"PUSHING: {i}") 
        stack.push(i)
    
    while len(stack) > 0:
        print("POPPED: ", stack.pop())


def Reple_Test():
    new_reple = Reple()
    new_reple.run()

def main():
    Reple_Test()


# ENTRY.
(
    lambda : 
    main() if is_main 
    else exit(0)
)()


