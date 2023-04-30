from enums import (
    OPERAND_MAP,
    NUMBER,
    FUNC,
    ARROW,
    FUNC_CALL,
    ID,
)

from token import Token

class Lexer:
    def __init__(self, src="") -> None:
        self.src    = src
        self.size   = len(self.src)
        self.cur    = 0
        self.latest = None
    
    def set(self, src):
        self.src  = src
        self.size = len(self.src)
        self.cur  = 0

    def clear(self):
        self.src  = ""
        self.size = 0 
 
    def isEmpty(self) -> bool:
        return self.cur == self.size
    
    def get(self, index):
        if 0 <= index < self.size:
            return self.src[index]
        
        return '/0'

    @property 
    def current(self):
        if self.isEmpty():
            return '/0'
        
        return self.src[self.cur]
    
    @property 
    def next_char(self):
        self.trim_spaces()
        if self.cur + 1 >= self.size: return '/0'
        return self.src[self.cur + 1]
    
    @property
    def prev(self):
        if self.cur > 0:
            return self.src[self.cur - 1]

        return '/0'
    
    def chop_n(self, n):
        if not self.isEmpty():
            if self.cur + n > self.size:
                self.cur = self.size
                return

            self.cur += n
 
    def chop(self): self.chop_n(1)

    def trim_spaces(self):
        while not self.isEmpty() and self.current.isspace():
            self.chop()
    
    def register_(self, token: Token) -> Token:
        self.latest = token
        return token

    def next(self) -> Token:
        self.trim_spaces()
        token_value_buffer = ""
        
        if self.current.isdigit():
            while self.current.isdigit() and not self.isEmpty():
                token_value_buffer += self.current
                self.chop()
             
            return self.register_(Token(
                NUMBER, 
                int(token_value_buffer)
            ))
  

        if self.current.isalpha():
            while self.current.isalnum() and not self.isEmpty():
                token_value_buffer += self.current 
                self.chop()
            
            if token_value_buffer == "Func":
                # Declaration...
                return self.register_(Token(FUNC, "Func"))
            
            if token_value_buffer: 
                if self.current == '(':
                    return self.register_(Token(FUNC_CALL, token_value_buffer))
                return self.register_(Token(ID, token_value_buffer))

        if self.current == '=': 
            if self.next_char == '>':
                self.chop_n(2)
                return self.register_(Token(ARROW, '=>'))

        if self.current in OPERAND_MAP:
            
            operand = self.current
            self.chop()
                         
            return Token(
                OPERAND_MAP[operand], 
                operand
            )
        
        print(f"Unknwn Token type: {self.current}.")
        exit(1)

