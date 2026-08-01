class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sample = strs[0]
        ans = ''
        for i in range(len(sample)):
            for s in strs[1:]:
                if i == len(s) or sample[i] != s[i]:
                    return ans
            ans += sample[i]
        return ans


                
# time complexity: O(S) where S is the sum of all characters in all strings. In the worst case, we compare each character of each string.
# space complexity: O(1) if we don't consider the output string, otherwise O(M