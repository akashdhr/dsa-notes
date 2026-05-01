class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        res = ''
        # for each item in base loop over all strings to check if the same is matching
        for i in range(len(base)):
            for s in strs[1:]:
                if i >= len(s) or s[i] != base[i]:
                    return res
            res += base[i]
        return res
                
# time complexity: O(S) where S is the sum of all characters in all strings. In the worst case, we compare each character of each string.
# space complexity: O(1) if we don't consider the output string, otherwise O(M