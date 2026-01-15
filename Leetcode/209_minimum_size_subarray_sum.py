class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = high = 0
        curr = 0
        res = float('inf')
        for high in range(len(nums)):
            curr += nums[high]
            
            while curr >= target:
                res = min(res, high - low + 1)
                curr -= nums[low]
                low += 1
        if res == float('inf'):
            return 0
        else:
            return res
# time complexity: O(N) why? because we are iterating through the array once with the high pointer and the low pointer only moves forward.
# space complexity: O(1) we are using only a constant amount of extra space. 