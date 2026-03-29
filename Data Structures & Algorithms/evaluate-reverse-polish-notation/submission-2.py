class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                num_1 = int(stack.pop()) 
                num_2 = int(stack.pop())
                val = num_1 + num_2
                stack.append(val)
            elif token == "-":
                num_1 = int(stack.pop()) 
                num_2 = int(stack.pop())
                val = num_2 - num_1
                stack.append(val)
            elif token == "*":
                num_1 = int(stack.pop()) 
                num_2 = int(stack.pop())
                val = num_1 * num_2
                stack.append(val)
            elif token == "/":
                num_1 = int(stack.pop()) 
                num_2 = int(stack.pop())
                val = num_2 / num_1
                stack.append(val)
            else:
                stack.append(token)
        return int(stack[-1])