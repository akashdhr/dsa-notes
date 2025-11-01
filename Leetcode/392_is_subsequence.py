# My first solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for c in s:
            found = False
            for i in range(start, len(t)):
                if t[i] == c:
                    start = i+1
                    found = True
                    break
            if found == False:
                return False
        return True

# Same complexity but canonical 2 pointer style approach
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
 
        