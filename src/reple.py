from colorama  import Fore
from parsing   import Transformer
from lexer     import Lexer

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
        parser.to_postfix() 
        parser.evaluate_stack() 
        
        print(parser.stack.pop())

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

