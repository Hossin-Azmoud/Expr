iota_: int = 0

def iota() -> int:
    global iota_
    cache = iota_
    iota_ += 1
    return cache

START   = iota()
PLUS    = iota()
MINUS   = iota()
MULT    = iota()
DIV     = iota()
POW     = iota()

NUMBER  = iota()
OPAR    = iota() 
CPAR    = iota() 
END     = iota()

ENUMS = [
    "START ",
    "PLUS  ", 
    "MINUS ", 
    "MULT  ",
    "DIV   ",
    "POW   ",
    "NUMBER",
    "OPAR  ",
    "CPAR  ",
    "END   "
]

