class Transformer:
    
    def to_postfix(expr) -> str:    
        operand_stack = []
        final_stack   = []

        for i, v in enumerate(expr):
            
            if v.isspace(): continue
            
            if v == '+' or v == '-' or v == '*':

                if len(operand_stack) > 0: 
                    final_stack.append(operand_stack.pop())
                        
                operand_stack.append(v)
                continue
            
            if v.isdigit():
                final_stack.append(int(v))
                continue
            
            else:
                print("Unsupported: ", v)
                exit(1)
         
        if len(operand_stack) > 0: 
            final_stack.append(operand_stack.pop())

        final_stack.reverse()
        print(final_stack)

        return final_stack




