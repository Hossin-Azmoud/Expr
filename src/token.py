from enums import ENUMS

class Token:
    def __init__(self, TType, TValue):
        self.token_type = TType
        self.value      = TValue

    def display(self):
        t = ENUMS[self.token_type]

        print(f"""
type: {t}
v:    {self.value}
""")


