class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        l = 0
        r = len(s)-1
        res = ['']*len(s)
        while l<=r:
            while l<r and s[l] not in vowels:
                res[l] = s[l]
                l += 1
            while l<r and s[r] not in vowels:
                res[r] = s[r]
                r -= 1   
            res[l], res[r] = s[r], s[l]
            l+=1
            r-=1
        return ''.join(res)     
        