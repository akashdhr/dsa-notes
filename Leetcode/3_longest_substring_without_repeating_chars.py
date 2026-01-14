class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            res = max(res, len(seen))
        return res

# time complexity: O(N)
# space complexity: O(min(N, M)) where N is the length of the string and M is the size of the character set.