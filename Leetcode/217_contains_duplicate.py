class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = {}
        for i in nums:
            hset[i] = hset.get(i, 0) + 1
        for i in hset.values():
            if i > 1:
                return True
        return False
        