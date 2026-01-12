class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), k*2):
            low = i
            high = i+k-1
            if len(s[low:]) < k:
                high = len(s) - 1
                while low <= high:
                    s[low], s[high] = s[high], s[low]
                    low += 1
                    high -= 1
            else:
                while low <= high:
                    s[low], s[high] = s[high], s[low]
                    low += 1
                    high -= 1
        return ''.join(s)

        