class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in '*/-+':
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(t))
        return stack[0]

#time complexity: O(N) where N is the number of tokens.
#space complexity: O(N) in the worst case, we may store all the tokens in the stack.