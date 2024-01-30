class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        while tokens:
            i = tokens.pop(0)

            # Usage of Numbers
            if i not in operators:
                stack.append(i)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
            
                # Usage of operators:
                if i == "+":
                    t = num1 + num2 
                elif i == '-':
                    t = num1 - num2
                elif i == '*':
                    t = num1 * num2
                elif i == '/':
                    t = num1 / num2

                # Add back the resultant number
                stack.append(t)

        print(tokens)
        print(stack)


        return int(stack.pop(0))

                

                
