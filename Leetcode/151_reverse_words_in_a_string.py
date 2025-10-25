class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        temp = ""
        for c in s:
            # Check for no whitespace characters
            if c != " ":
                temp += c
            # If whitespace is encountered and we have some legitimate temp then add it to stack. Reset temp.
            elif temp:
                stack.append(temp)
                temp = ""
        # Last word will not be captured in previous loop so add it separately
        if temp:
            stack.append(temp)
        return ' '.join(stack[::-1])
        