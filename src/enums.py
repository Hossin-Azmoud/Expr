iota_: int = 0

def iota() -> int:
    global iota_
    cache = iota_
    iota_ += 1
    return cache

START   = iota()
PLUS    = iota()
NUMBER  = iota()
OPAR    = iota() 
CPAR    = iota() 
END     = iota()

ENUMS = [
    "START ",
    "PLUS  ", 
    "NUMBER", 
    "OPAR  ",
    "CPAR  ",
    "END   "
]







