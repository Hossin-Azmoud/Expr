from structures import Stack

from enums import (
    START,
    PLUS,
    MINUS,
    DIV,
    NUMBER,
    OPAR,
    CPAR,
    END
)

from token import Token



class Transformer:

    def __init__(self, lexer):
        self.lexer   = lexer
        self.stack   = Stack()
    
    def to_postfix(self):
        tmp = Stack()
        
        while not self.lexer.isEmpty():
            token = self.lexer.next()
            
            if not token.is_number():
                
                if len(tmp) > 0:
                    if tmp.peek().token_type == PLUS: 
                        self.stack.push(tmp.pop())
                
                tmp.push(token)
                continue
            
            self.stack.push(token)
        
        # Pop the left operands.
        if len(tmp) > 0: 
            while len(tmp) > 0:
                self.stack.push(tmp.pop())
        
        # reverse the stack.
        self.stack.reverse()
    
    def dump_stack(self):
         
        it = len(self.stack) - 1

        while it >= 0:
            print(self.stack.at(it))
            it -= 1
            
    
    def clear_stack(self):
        self.stack = Stack()
    
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

"""
    def to_postfix(expr) -> str:    
        operand_stack = []
        final_stack   = []

        for i, v in enumerate(expr):
            
            if v.isspace(): continue
            
            if v == '+' or v == '-' or v == '*':

                if len(operand_stack) > 0: 
                    final_stack.append(operand_stack.pop())
                        
                operand_stack.append(v)
                continue
            
            if v.isdigit():
                final_stack.append(int(v))
                continue
            
            else:
                print("Unsupported: ", v)
                exit(1)
         
        if len(operand_stack) > 0: 
            final_stack.append(operand_stack.pop())

        final_stack.reverse()
        print(final_stack)

        return final_stack
"""



