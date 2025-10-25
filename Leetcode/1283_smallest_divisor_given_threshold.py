import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        res = -1
        while low <= high:
            mid = (low+high) // 2
            if self.check(nums, mid) <= threshold:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
    def check(self, nums, div):
        currSum = 0
        for i in nums:
            currSum += math.ceil(i/div)
        return currSum