class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []
        for i in s:
            if i not in store:
                stack.append(i)
            elif i in store:
                if stack and stack[-1] == store[i]:
                    stack.pop()
                else:
                    return False
        return stack == []
    
# time complexity: O(N) where N is the length of the string.
# space complexity: O(N) in the worst case, we may store all the opening brackets in the stack.