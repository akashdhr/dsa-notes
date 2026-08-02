class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        runa = 1
        runb = 1
        # Run A
        for i in range(len(nums)):
            res[i] = runa
            runa *= nums[i]

        # Run B
        for j in range(len(nums)-1, -1, -1):
            res[j] *= runb
            runb *= nums[j]
        return res


# time complexity: O(N)
# space complexity: O(1)