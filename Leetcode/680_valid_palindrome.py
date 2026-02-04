# Brute force
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if temp == temp[::-1]:
                return True
        return False
    
# Optimal solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        low = 0
        high = len(s) - 1
        while low <= high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return s[low+1:high+1] == s[low+1:high+1][::-1] or s[low:high] == s[low:high][::-1]
        return True
        