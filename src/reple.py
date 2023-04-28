from colorama   import Fore
from parsing    import Transformer
from lexer      import Lexer
from structures import Isok

class Reple:
    
    def __init__(self) -> None:
        self.quit = False
        self.cmds = {
            "Q": self.Quit
        }
        
        self.lexer       = Lexer()
    
    def evaluate_expr(self, expr):
        self.lexer.set(expr)
        
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

