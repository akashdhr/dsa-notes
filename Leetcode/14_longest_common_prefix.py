class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res
                
# time complexity: O(N * M) where N is the number of strings in the input array and M is the length of the longest common prefix. In the worst case, we compare each character of the longest common prefix with all other strings.
# space complexity: O(M) where M is the length of the longest common prefix, since we are storing the longest common prefix in the result string.