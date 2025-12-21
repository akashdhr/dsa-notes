class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        # Loop through every index in s
        for i in range(len(s)):
            # Reset freq
            freq = {}
            # Loop through every substring
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1
                values = freq.values()
                maxi = max(values)
                mini = min(values)
                total += maxi - mini
        return total  