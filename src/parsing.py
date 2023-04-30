from structures import (
    Stack,
    ok,
    err,
    Result
)

from enums import (
    START,
    PLUS,
    MINUS,
    MULT,
    DIV,
    NUMBER,
    OPAR,
    CPAR,
    END
)

from token     import Token
from constants import PREC_TABLE 

def dump_stack(stack, label):
    
    print()
    
    print(label)
    it = 0 
    print("[", end=" ")
    
    while it < len(stack):
        print(stack.at(it), end=" ")
        it += 1
    
    print("]", end=" \n")
    
    print()

class Transformer:

    def __init__(self, lexer=None):
        self.lexer   = lexer
        self.stack   = Stack()
        
    def JIT_postfix(self, toks: list[Token]) -> Result:
        self.stack = Stack()
        tmp        = Stack()
        it         = 0
        
        while it < len(toks):
            prev  = tmp.peek()
            token  = toks[it]
            it += 1

            if token.is_number(): 
                self.stack.push(token)
                continue
            
            if token.token_type == CPAR:   # )
                if prev: 
                    while prev.token_type != OPAR and len(tmp) > 0:
                        
                        self.stack.push(prev) #out... 
                        tmp.pop() # operand... + 
                        prev = tmp.peek()
                        if not prev: break
                    
                    if prev:
                        if prev.token_type == OPAR:
                            tmp.pop()
                            continue

                return err(f"A non closed bracket accurred!")

            if token.token_type == OPAR:
                tmp.push(token)
                continue

            if token.value in PREC_TABLE:
                if prev and prev.value in PREC_TABLE:
                    if PREC_TABLE[token.value] > PREC_TABLE[prev.value]:
                        tmp.push(token)
                        continue
                    
                    while PREC_TABLE[token.value] <= PREC_TABLE[prev.value] and prev.value != token.value:
                        self.stack.push(prev)
                        tmp.pop()
                        prev = tmp.peek()
                        
                        if not prev:
                            break

                        if prev.value not in PREC_TABLE:
                            break

                tmp.push(token)
        
        while len(tmp) > 0: 
            self.stack.push(tmp.pop())
        
        # reverse the stack.
        self.stack.reverse()

        if self.stack.contains(Token(OPAR, '(')) or self.stack.contains(Token(CPAR, ')')):
            return err(f"A non closed bracket accurred!")

        return ok()

    def to_postfix(self) -> Result:
        tmp = Stack()
        while not self.lexer.isEmpty():
           
            token = self.lexer.next()
            prev = tmp.peek()

            if token.is_number(): 
                self.stack.push(token)
                continue
            
            if token.token_type == CPAR:   # )
                if prev: 
                    while prev.token_type != OPAR and len(tmp) > 0:
                        
                        self.stack.push(prev) #out... 
                        tmp.pop() # operand... + 
                        prev = tmp.peek()
                        if not prev: break
                    
                    if prev:
                        if prev.token_type == OPAR:
                            tmp.pop()
                            continue

                return err(f"A non closed bracket accurred!")

            if token.token_type == OPAR:
                tmp.push(token)
                continue

            if token.value in PREC_TABLE:
                if prev and prev.value in PREC_TABLE:
                    if PREC_TABLE[token.value] > PREC_TABLE[prev.value]:
                        tmp.push(token)
                        continue
                    
                    while PREC_TABLE[token.value] <= PREC_TABLE[prev.value] and prev.value != token.value:
                        self.stack.push(prev)
                        tmp.pop()
                        prev = tmp.peek()
                        
                        if not prev:
                            break

                        if prev.value not in PREC_TABLE:
                            break

                tmp.push(token)
           
        while len(tmp) > 0: 
            self.stack.push(tmp.pop())
        
        
        # reverse the stack.
        self.stack.reverse()
        
        if self.stack.contains(Token(OPAR, '(')) or self.stack.contains(Token(CPAR, ')')):
            return err(f"A non closed bracket accurred!")

        return ok()

           
    
    def clear_stack(self):
        self.stack = Stack()
    
    def evaluate_stack_(self) -> Result:
        res = Stack()
        
        while len(self.stack) > 0:
            l = self.stack.pop()
            
            if l.value in PREC_TABLE:
                a = res.pop().value
                b = res.pop().value

                if l.value == '+':
                    res.push(Token(NUMBER , a + b))
                    continue
                
                if l.value == '-':
                    res.push(Token(NUMBER, b - a))
                    continue
                
                if l.value == '*':
                    res.push(Token(NUMBER, b * a))
                    continue
                
                if l.value == '/':
                    if a == 0:
                        return err("Division by zero error.")

                    res.push(Token(NUMBER, b / a))
                    continue
                
                if l.value == '^':
                    res.push(Token(NUMBER, b ** a))
                    continue
                
                return err(f"Unsupported operand { l }")
            
            res.push(l)
        
        self.stack.push(res.pop())
        return ok()
        
    def evaluate_stack(self):
        while len(self.stack) > 2:
            n        = self.stack.pop().value
            m        = self.stack.pop().value
            operand  = self.stack.pop()

            if operand.token_type == PLUS: 
                self.stack.push(Token(NUMBER, m + n))
                continue

            if operand.token_type == MINUS: 
                self.stack.push(Token(NUMBER, n - m))
                continue
            if operand.token_type == MULT:
                self.stack.push(Token(NUMBER, n * m))
                continue
            
            if operand.token_type == MULT:
                if m == 0:
                    print(f"Division by zero {n}/{m}")
                    return False
                
                self.stack.push(Token(NUMBER, n / m))
                continue           

            print(f"Unsupported operand {operand.value}")
        
        return True
