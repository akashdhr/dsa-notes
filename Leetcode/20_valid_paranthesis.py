class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for i in s:
            if i == ')' or i == '}' or i == ']':
                if stack and stack[-1] == store[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return stack == []
            

                