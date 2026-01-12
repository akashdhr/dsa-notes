class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sorting is done to find the smallest available cookie that satisfies a given child efficiently.
        g.sort()
        s.sort()
        cnt = 0
        gp = 0 # Used for maintaining the pointer on g
        sp = 0 # Used for maintaining the pointer on s
        
        while gp < len(g) and sp < len(s):
            if s[sp] >= g[gp]:
                cnt += 1
                gp += 1
            sp += 1
        return cnt
 # time complexity: O(N log N + M log M) where N is the number of children and M is the number of cookies.
 # space complexity: O(1)

        