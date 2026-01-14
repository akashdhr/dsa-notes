class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for i in s1:
            freq[i] = freq.get(i, 0) + 1

        for i in range(len(s2) - len(s1) + 1):
            temp = {}
            if s2[i] in freq:
                for j in range(i, i+len(s1)):
                    temp[s2[j]] = temp.get(s2[j], 0) + 1
                if temp == freq:
                    return True

        return False
#time complexity: O(N * M) where N is the length of s2 and M is the length of s1. why? because for each character in s2 we are checking a substring of length M
#space complexity: O(M) where M is the length of s1. why? because we are storing the frequency of characters of s1 in a hashmap.