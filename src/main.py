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

def print_stack(s: Stack, name: str):
    print(name, end=": ")
    for i in s.base:
        print(i, end=" ")



def main():
    prec = {
        '^': 4,
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2
    }


    # 3 4 2 × 1 5 − 2 3 ^ ^ ÷ + 

    op       = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"

    output   = Stack()
    op_stack = Stack()

    i  = 0
    
    while i < len(op):
        

        o    = op[i]
        prev = op_stack.peek()
        print(o) 
        if o == '-':
            print(f"\n{'-'*5}({i}){'-'*5}\n")
            print_stack(op_stack, "OP")
            print()
            print_stack(output, "OUT")
            print("\n--------------------------\n")


        if o.isspace():
            i += 1 
            continue

        if o.isdigit(): 
            output.push(int(o))
            i += 1
            continue
        
        if o in prec:
            if prev and prev in prec:
                if prec[o] > prec[prev]:
                    op_stack.push(o)
                    i += 1
                    continue

                while prec[o] <= prec[prev] and prev != o:
                    output.push(prev)
                    op_stack.pop()
                    prev = op_stack.peek()
                    if not prev:
                        break

            op_stack.push(o)


        if o == '(':
            op_stack.push(o)
        
        if o == ')':
            
            while prev != '(' and len(op_stack) > 0:
                output.push(prev)
                op_stack.pop()
                prev = op_stack.peek()
           
            if prev == '(': op_stack.pop()
            
            else:
                print(f"Expected ( but found : { prev } ")
                exit(1)
        i += 1

    while len(op_stack) > 0: 
        output.push(op_stack.pop())
    
    print_stack(output, "FINAL")


# ENTRY.
(
    lambda : 
    main() if is_main 
    else exit(0)
)()


