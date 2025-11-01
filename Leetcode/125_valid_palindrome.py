class Solution:
    def isAlpha(self, c):
        if (ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        while l<=r:
            while l<r and not self.isAlpha(s[l]):
                l+=1
            while l<r and not self.isAlpha(s[r]):
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        