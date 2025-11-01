class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charS = {}
        charT = {}
        for i in range(len(s)):
            # Update the position of current char in first map from string s
            if s[i] not in charS:
                charS[s[i]] = i
            # Update position of current char in second map from string t
            if t[i] not in charT:
                charT[t[i]] = i
            # Check if the position matches
            if charS[s[i]] != charT[t[i]]:
                return False
        return True

        