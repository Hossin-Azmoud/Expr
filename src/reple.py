from colorama import Fore


class Reple:
    
    def __init__(self) -> None:
        self.quit = False
        self.cmds = {
            "Q": self.Quit
        }
    

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
                print("EXPR: ", command.strip())

