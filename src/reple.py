from colorama   import Fore
from parsing    import Transformer
from lexer      import Lexer
from structures import Isok
from func       import define_func

class Reple:
    
    def __init__(self) -> None:
        self.quit = False
        self.cmds = {
            "Q": self.Quit
        }
        self.functions   = {}
        self.lexer       = Lexer()
    
    def callf(self, name):
        if name in self.functions:
            fn = fs[name]
            args = []
            
            while not self.lexer.isEmpty():
                T = self.lexer.next()
                
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

         
        print(f"Function {T.value} is not defined !")
        exit(1)

    def evaluate_expr(self, expr):
        self.lexer.set(expr)

        cur =  self.lexer.latest
        if cur:
if cur.token_type == enums.FUNC:
    fn = define_func(self.lexer)
    self.functions[fn.name] = fn
    return

if cur.token_type == enums.FUNC_CALL:
    self.callf()
    return

        parser = Transformer(self.lexer)
        r = parser.to_postfix()

        if not Isok(r):
            r.report()
            return

        r = parser.evaluate_stack_() 
        
        if Isok(r):
            print(parser.stack.pop())
            return        

        r.report()

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

