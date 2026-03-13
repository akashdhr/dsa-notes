class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Brute: Loop through every item and scan the entire array. TC: O(n^2)
        # Better: using hashing as shown. TC: O(n)+O(m) SC: O(m) where m is the size of the hashmap
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        for k, v in hashmap.items():
            if v > (len(nums)/2):
                return k
        # Optimal: Moore's Voting Algorithm
        # TC: O(n)
        # SC: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = 0
        ele = nums[0]
        for i in nums:
            if curr == 0:
                ele = i
            if i == ele:
                curr += 1
            else:
                curr -= 1
        return ele

        