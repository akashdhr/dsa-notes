class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for i in s:
            if stack and i in store:
                if store[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return stack == []
        
    
# time complexity: O(N) where N is the length of the string.
# space complexity: O(N) in the worst case, we may store all the opening brackets in the stack.