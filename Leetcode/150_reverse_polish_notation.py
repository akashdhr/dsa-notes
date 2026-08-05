class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                x = stack.pop()
                y = stack.pop()
                if i == '+':
                    stack.append(x + y)
                elif i == '*':
                    stack.append(x * y)
                elif i == '-':
                    stack.append(y - x)
                elif i == '/':
                    stack.append(int(y/x))
            else:
                stack.append(int(i))
        return stack[0]

        
#time complexity: O(N) where N is the number of tokens.
#space complexity: O(N) in the worst case, we may store all the tokens in the stack.