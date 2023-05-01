from colorama   import Fore
from parsing    import Transformer, dump_stack
from lexer      import Lexer
from structures import Isok
from func       import define_func
from token      import Token

import enums

HELP = """ 
COMMANDS:
    q   => Quit
    ans => Show the latest computed value
    reg => Show registered functions and variables.
"""

class Reple:
    def __init__(self) -> None:
        self.quit = False
        
        self.cmds = {
            "Q":    self.Quit,
            "HELP": (lambda : print(HELP)),
            "REG":  self.show_reg,
        }

        self.functions   = {}
        self.register    = {}
        self.lexer       = Lexer()
    

    def show_reg(self):
        print()
        for k in self.functions.keys():

            fn = self.functions[k]
            params = ', '.join([p.value for p in fn.params])
            print(f"Func {fn.name}({params});")


        for k in self.register.keys():
            print("{} -> {}".format(k, self.register[k]))
 
        print()


    def register_(self, name):
        n = 0
        if not self.lexer.isEmpty():
            token = self.lexer.next()
            
            if token.token_type == enums.EQ:
                n += 1
                token = self.lexer.next()
                if token.token_type == enums.NUMBER:
                    n += len(token.value)
                    self.register[name] = int(token.value)
                    return (True, 0)
        
        return (False, n)

    def callf(self, name):
        
        if name in self.functions:
            fn = self.functions[name]
            args = []
            T = None 

            while not self.lexer.isEmpty():
                T = self.lexer.next()
                
                if T.token_type == enums.OPAR: continue
                if T.token_type == enums.CPAR: 
                    break

                if T.token_type == enums.NUMBER:
                    args.append(T)
            
            if T.token_type != enums.CPAR:
                print(f"Expected closing parent.. got {T.value}")
                return

            cach = fn.call(args)
            parser = Transformer()
            parser.clear_stack()
            parser.JIT_postfix(cach)
            r = parser.evaluate_stack_()
            
            if r.code == 200: 
                self.printans(parser.stack) 
                return

         
        print(f"Function { name } is not defined !")
    
    def sub_vars_from_reg(self, parser) -> None:
        it = 0
        while it < len(parser.stack):
            token = parser.stack.base[it]
                        
            if token.token_type == enums.ID:
                if token.value in self.register:
                    parser.stack.base[it] = Token(enums.NUMBER, self.register[token.value])

            
            it += 1


    def evaluate_expr(self, expr):
        self.lexer.set(expr)
        cur =  self.lexer.latest
        
        if cur:
            if cur.token_type == enums.FUNC:
                self.lexer.chop_n(len(cur.value))
                fn = define_func(self.lexer)
                self.functions[fn.name] = fn
                return

            if cur.token_type == enums.FUNC_CALL:
                self.lexer.chop_n(len(cur.value))
                self.callf(cur.value) 
                return
            
            if cur.token_type == enums.ID:
                self.lexer.chop_n(len(cur.value))
                (flag, n) = self.register_(cur.value)
                
                if flag: 
                    return
                
        self.lexer.set(expr)
        parser = Transformer(self.lexer)
        r = parser.to_postfix()

        
        if not Isok(r):
            r.report()
            return
        
        self.sub_vars_from_reg(parser)
        r = parser.evaluate_stack_() 
        
        if Isok(r):
            self.printans(parser.stack) 
            return

        r.report()

    def printans(self, stack):
        
        top = stack.pop() 
        if isinstance(top, Token):
            top = top.value
        
        print('----------------')           
        print(f"{Fore.GREEN}ans: ", top, f"{Fore.RESET}")
        self.register['ans'] = top
        print('----------------')



    def parse_cmd(self, cmd):
        return cmd.upper().strip()

    def Quit(self):
        self.quit = True

    def run(self):
        while not self.quit:
            command = input(f"{Fore.YELLOW}REPLE > {Fore.RESET}")
            
            if command:
                cmd = self.parse_cmd(command)
                if cmd in self.cmds:
                    self.cmds[cmd]()
                    continue
                
                # it is not a command, but an expr
                self.evaluate_expr(command.strip())

