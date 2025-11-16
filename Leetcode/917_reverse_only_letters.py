class Solution:
    def check(self, c):
        if (ord('a') <= ord(c) and ord(c) <= ord('z')) or (ord('A') <= ord(c) and ord(c) <= ord('Z')):
            return True
        else:
            return False
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0
        r = len(s)-1
        s = list(s)
        while l<=r:
            if self.check(s[l]) and self.check(s[r]):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif self.check(s[l]) == False:
                l += 1
            elif self.check(s[r]) == False:
                r -= 1
        return ''.join(s)
        