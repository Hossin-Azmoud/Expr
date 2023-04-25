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

from token import Token

OPERAND_MAP = {
    '+':  PLUS,
    '(':  OPAR,
    ')':  CPAR,
    '-':  MINUS,
    '*':  MULT,
    '/':  DIV
}

class Lexer:
    def __init__(self, src="") -> None:
        self.src  = src
        self.size = len(self.src)
        self.cur  = 0
    
    def set(self, src):
        self.src  = src
        self.size = len(self.src)
        self.cur  = 0

    def clear(self):
        self.src  = ""
        self.size = 0 
 
    def isEmpty(self) -> bool:
        return self.cur == self.size
    
    @property 
    def current(self):
        if self.isEmpty():
            return '/0'
        
        return self.src[self.cur]

    def chop(self):
        if not self.isEmpty():
            self.cur += 1
    
    def trim_spaces(self):
        while not self.isEmpty() and self.current.isspace():
            
            self.chop()
            
    def next(self) -> Token:
        
        self.trim_spaces()
        token_value_buffer = ""
        
        while self.current.isdigit() and not self.isEmpty():
            token_value_buffer += self.current
            self.chop()
         

        if len(token_value_buffer) > 0:
            return Token(
                NUMBER, 
                int(token_value_buffer)
            )
        
        if self.current in OPERAND_MAP:
            
            operand = self.current
            self.chop()
            
            return Token(
                OPERAND_MAP[operand], 
                operand
            )

        print(f"Unknwn Token type: {self.current}.")
        exit(1)

