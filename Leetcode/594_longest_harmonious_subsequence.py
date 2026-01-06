class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hset = {}
        longest = 0
        for i in nums:
            hset[i] = hset.get(i, 0) + 1
        for i in hset:
            if i+1 in hset:
                length = hset[i] + hset[i+1]
                longest = max(longest, length)
        return longest

        