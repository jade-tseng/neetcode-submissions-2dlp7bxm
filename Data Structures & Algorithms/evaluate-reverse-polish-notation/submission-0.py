class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack as history: push operands, pop when you hit an operator
        stack = []
        operator = ['+', '-', '*', '/']

        for i in tokens:
            if i not in operator:
                stack.append(int(i))
            else:
                b = stack.pop() 
                a = stack.pop() 
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(int(a / b))
        
        return stack[0]

        
