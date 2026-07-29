class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        window = set()
        left = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[left])
                left += 1
            window.add(s[i])
            maxLen = max(maxLen, len(window))
        return maxLen

# time complexity: O(N)
# space complexity: O(min(N, M)) where N is the length of the string and M is the size of the character set.