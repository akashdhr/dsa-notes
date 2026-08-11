class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(maxf, r-l+1)
        return res

# time complexity: O(N) where N is the number of characters in the string.
# space complexity: O(1) as we are using a fixed size hashmap of 26

# Explanation: 
# We are using a sliding window approach to find the longest substring that can be formed by replacing at most k characters. 
# We maintain a count of characters in the current window and keep track of the maximum frequency of any character in that window. 
# If the length of the window minus the maximum frequency is greater than k, we shrink the window from the left. 
# The result is updated with the maximum length of valid windows found during the iteration.