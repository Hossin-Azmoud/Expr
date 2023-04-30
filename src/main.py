from   func       import define_func
from   lexer      import Lexer, Token
from   parsing    import Transformer
from   structures import Stack
from   reple      import Reple
import enums

FNC_TABLE = {}
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


def Shunting_yard():

    


    # 3 4 2 × 1 5 − 2 3 ^ ^ ÷ + 

    op       = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"

    output   = Stack()
    op_stack = Stack()

    i  = 0
    
    while i < len(op):

        o    = op[i]
        prev = op_stack.peek()

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
    
    output.reverse()
    
    print_stack(output, "FINAL")
    # Eval the stack.
    res = Stack()
    
    while len(output) > 0:
        l = output.pop()
        
        if l in prec:
            a = res.pop()
            b = res.pop()

            if l == '+':
                res.push(a + b)
                continue
            
            if l == '-':
                res.push(b - a)
                continue
            
            if l == '*':
                res.push(b * a)
                continue
            
            if l == '/':
                res.push(b / a)
                continue
            
            if l == '^':
                res.push(b ** a)
                continue
            
            print(f"Unsupported operand { l }")
            exit(1)

        res.push(l)
        
    print_stack(res, "result")


def main():
    Reple_Test()

def read_source(f: str) -> Lexer:
    with open(f) as code:
        return Lexer(code.read())

def funcsss():
    fs: dict = {}

    # lex = Lexer("Func Add(a, b) => | a + b |") # Give the expression to the lexer.

    lex = read_source("source.math")
    
    while not lex.isEmpty():
        T = lex.next()
        
        if T.token_type == enums.FUNC:
            fn = define_func(lex)            
            # fn.ast()
            
            fs[fn.name] = fn
        
        if T.token_type == enums.FUNC_CALL:
            if T.value in fs:
                fn = fs[T.value]
                args = []
                
                while not lex.isEmpty():
                    T = lex.next()
                    
                    if T.token_type == enums.OPAR: continue
                    if T.token_type == enums.CPAR: 
                        break

                    if T.token_type == enums.NUMBER:
                        args.append(T)
                
                if T.token_type != enums.CPAR:
                    print(f"Expected closing parent.. got {T.value}")
                    exit(1)
                    
                cach = fn.call(args)
                parser = Transformer()
                
                parser.clear_stack()
                
                parser.JIT_postfix(cach)
                r = parser.evaluate_stack_()
                
                if r.code == 200: 
                    print(parser.stack.pop().value)
                    
                
                continue
             
            print(f"Function {T.value} is not defined !")
            exit(1)
           


def fizzbuzz():
    mam = {
        3: "fizz",
        5: "buzz",
        1: "Poof"
    }

    def fizzbuzz(n: int):
        buff = ""
        for k in mam: 
            if n % k == 0: 
                buff += mam[k]

        print(n, " : ", buff)

    for i in range(0, 100): fizzbuzz(i) 


# ENTRY.
(
    lambda : 
    main() if is_main 
    else exit(0)
)()


