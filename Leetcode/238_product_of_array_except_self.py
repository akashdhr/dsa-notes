class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = suffix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= suffix
            suffix *= nums[j]
        return ans

# time complexity: O(N)
# space complexity: O(1)