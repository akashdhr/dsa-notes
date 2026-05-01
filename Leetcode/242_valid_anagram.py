class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for i in s:
            seen[i] = seen.get(i, 0) + 1
        for j in t:
            seen[j] = seen.get(j, 0) - 1
        for v in seen.values():
            if v != 0:
                return False
        return True

# time complexity: O(N) where N is the length of the input strings. We traverse both strings once, and each lookup and update operation in the hash map takes O(1) time on average.
# space complexity: O(1) since the hash map will contain at most 26 keys (assuming only lowercase English letters), which is a constant amount of space.