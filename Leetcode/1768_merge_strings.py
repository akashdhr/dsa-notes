class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0
        res = ''
        while w1 < len(word1) and w2 < len(word2):
            res += word1[w1]
            res += word2[w2]
            w1 += 1
            w2 += 1
        if w1 < len(word1):
            res += word1[w1:]
        if w2 < len(word2):
            res += word2[w2:]
        return res

# time complexity: O(N + M) where N and M are the lengths of word1 and word2 respectively.
# space complexity: O(N + M) for the result string.