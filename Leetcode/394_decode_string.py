class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ']':
                substr = ''
                # find the string
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop() # remove the opening brace [
                # find the number
                k = ''
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
            else:
                stack.append(i)
        return ''.join(stack)
# time complexity: O(N) where N is the length of the string.
# space complexity: O(N) in the worst case, we may store all the characters in the stack.