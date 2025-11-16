# This solution is not optimal as it uses extra space
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        arr = []
        cnt = 0
        curr = s[0]
        for c in s:
            if c == curr:
                cnt += 1
            else:
                arr.append(cnt)
                curr = c
                cnt = 1
        arr.append(cnt)
        res = 0
        for i in range(len(arr)-1):
            res += min(arr[i], arr[i+1])
        return res
