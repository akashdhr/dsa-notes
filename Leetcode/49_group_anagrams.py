class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            temp = ''.join(sorted(list(s)))
            if temp in anagrams:
                anagrams[temp].append(s)
            else:
                anagrams[temp] = [s]
        return list(anagrams.values())
        
# time complexity: O(N * K log K) where N is the number of strings in the input array and K is the maximum length of a string in the input array. Sorting each string takes O(K log K) time and we do this for all N strings.
# space complexity: O(N * K) in the worst case when all strings are anagrams of each other, we will have to store all strings in the hash map.