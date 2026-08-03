class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        ans = []
        for i in range(minLen):
            ans.append(word1[i])
            ans.append(word2[i])
        i = minLen
        while i < len(word1):
            ans.append(word1[i])
            i += 1
        while i < len(word2):
            ans.append(word2[i])
            i += 1
        return ''.join(ans)
        
    
# time complexity: O(N + M) where N and M are the lengths of word1 and word2 respectively.
# space complexity: O(N + M) for the result string.