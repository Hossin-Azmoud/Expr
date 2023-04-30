iota_: int = 0

def iota() -> int:
    global iota_
    cache = iota_
    iota_ += 1
    return cache

START        = iota()
PLUS         = iota()
MINUS        = iota()
MULT         = iota()
DIV          = iota()
POW          = iota()
EQ           = iota()
GT           = iota()
LT           = iota()
COMA         = iota()
ARROW        = iota()
PIPE         = iota()
NUMBER       = iota()
OPAR         = iota() 
CPAR         = iota() 
FUNC         = iota()
FUNC_CALL    = iota()
ID           = iota()
END          = iota()

ENUMS = [
    "START       ",
    "PLUS        ",
    "MINUS       ",
    "MULT        ",
    "DIV         ",
    "POW         ",
    "EQ          ",
    "GT          ",
    "LT          ",
    "COMA        ",
    "ARROW       ",
    "PIPE        ",
    "NUMBER      ",
    "OPAR        ",
    "CPAR        ",
    "FUNC        ",
    "FUNC_CALL   ",
    "ID          ",
    "END         " 
]

OPERAND_MAP = {
    '+':  PLUS,
    '(':  OPAR,
    ')':  CPAR,
    '-':  MINUS,
    '*':  MULT,
    '/':  DIV,
    '^':  POW,
    ',':  COMA,
    '=':  EQ,
    '<':  LT,
    '>':  GT,
    '|':  PIPE,
    '/0': END

}

