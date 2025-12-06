class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        res = 0
        i = 0
        # Remove leading whitespaces
        while i < len(s) and s[i] == " ":
            i += 1
        # Check if entire string is whitespaces
        if i == len(s):
            return 0
        if s[i] == "-":
            negative = True
            i += 1
        elif s[i] == "+":
            i += 1
        # Remove leading zeros
        while i < len(s) and s[i] == '0':
            i += 1
        # Check if entire string is zeros
        if i == len(s):
            return 0      
        # Parse until non digit occurs
        while i < len(s):
            if s[i].isdigit():
                res = (res * 10) + int(s[i])
                i += 1
            else:
                break
        if negative:
            res = -res
        if res < (-2**31):
            return -2**31
        elif (2**31 - 1) < res:
            return 2**31 - 1
        else:
            return res
