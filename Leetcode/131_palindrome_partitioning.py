class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        def part(ind, s, temp):
            if ind == len(s):
                res.append(temp.copy())
                return
            for i in range(ind, len(s)):
                if s[ind:i+1] == s[ind:i+1][::-1]:
                    temp.append(s[ind:i+1])
                    part(i + 1, s, temp)
                    temp.pop()
        part(0, s, temp)
        return res