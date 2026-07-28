class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            tmp = ''.join(sorted(i))
            if tmp in anagrams:
                anagrams[tmp].append(i)
            else:
                anagrams[tmp] = [i]
        ans = []
        for v in anagrams.values():
            ans.append(v)
        return ans
        
        
# time complexity: O(N * K log K) where N is the number of strings in the input array and K is the maximum length of a string in the input array. Sorting each string takes O(K log K) time and we do this for all N strings.
# space complexity: O(N * K) in the worst case when all strings are anagrams of each other, we will have to store all strings in the hash map.