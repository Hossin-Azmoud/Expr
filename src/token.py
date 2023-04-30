from enums import ENUMS

class Token:
    def __init__(self, TType, TValue):
        self.token_type = TType
        self.value      = TValue
    
    def is_number(self) -> bool:
        return isinstance(self.value, int)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        T = ENUMS[self.token_type]
        return f"{self.value} | {T}"
    
    def __eq__(self, other) -> bool: return (self.value == other.value)



