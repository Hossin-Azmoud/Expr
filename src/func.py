import enums
from   token  import Token
from   lexer  import Lexer
from   json   import dumps

def parse_err(err: str):
    print(err)
    exit(1)

class Func:
    def __init__(self, name: str, params: list[str], body: list[Token]):
        self.name        = name        # hello
        self.params      = params      # p0
        self.args        = {}
        self.body        = body        # 1 + (p0)
        
    def pass_args(self, args: list[Token]):
        
        if self.args:
            self.args = {}

        for i in range(len(args)):            
            self.args[self.params[i].value] = args[i] 

    def call(self, args: list[Token]):
        self.pass_args(args)
        cache  = self.body.copy()
        
        for i, token in enumerate(cache):
            if token.token_type == enums.ID:
                cache[i] = self.args[token.value]
        
        return cache
    
    def ast(self) -> None:
        print(self.name)
        print(self.params)
        print(self.body)
    
def exec_func(fn: Func, args: list[Token]):
    if len(fn.params) != len(args):
        parse_err(f"Syntax error, provided {len(args)} args, but the {fn.name} needs only {len(fn.params)}")
        params = ', '.join([p for p in fn.params])
        parse_err(f"Declaration: Func {fn.name}({params});")
    #type check..
    return fn.call(args)


def getPms(lexer: Lexer) -> list:
    pms = []
    current = lexer.next()
    if current.token_type == enums.OPAR:
        current = lexer.next()
        while not lexer.isEmpty():
            
            
            if current.token_type == enums.COMA:
                current = lexer.next()
                continue
            
            if current.token_type == enums.CPAR:
                return pms 

            if current.token_type == enums.ID:
                pms.append(current)
                current = lexer.next()
                continue

        parse_err(f"Expected ) but got: {current.value} ")

    parse_err(f"Expected ( but got: {current.value} ")

def parse_body(lexer: Lexer) -> list[Token]:
    body: list[Token] = []
    
    current = lexer.next()
    if current.token_type == enums.ARROW:
        current = lexer.next()

        if current.token_type != enums.PIPE:    
            parse_err(f"Expected | but got: {current.value}")
        current = lexer.next()

        while True:
            if current.token_type == enums.PIPE: return body
            if lexer.isEmpty(): break 
            body.append(current)
            current = lexer.next()
        
        parse_err(f"Expected | as an ending to the body but got: {current.value}")

     
    parse_err(f"Expected => but got: {current.value} ")

def define_func(lexer: Lexer) -> Func:
    """ Parses this expr: Func add(a, b) => | x + 1 |  """

    pms:  list[Token]  = []
    name: str          = ""
    body: list[Token]  = []

    if not lexer.isEmpty():
        current = lexer.next()
        
        if current.token_type == enums.FUNC_CALL:
            name = current.value
            pms  = getPms(lexer) 
            body = parse_body(lexer)            
            return Func(name, pms, body)
