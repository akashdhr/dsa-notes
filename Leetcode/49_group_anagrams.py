class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(list(s)))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
        return list(anagrams.values())
#time complexity: O(N K log K) where N is the number of strings and K is the maximum length of a string.
#space complexity: O(N K) why? because in the worst case, all strings are different and we need to store all of them in the hashmap.