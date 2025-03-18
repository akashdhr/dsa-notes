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
        cnt = 0
        el = 0
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1
                el = nums[i]
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return el
        