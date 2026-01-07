class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        res = window_sum/k
        end = len(nums) - k + 1
        for i in range(1, end):
            window_sum = window_sum - nums[i-1] + nums[i+k-1]
            res = max(window_sum/k, res)
        return res