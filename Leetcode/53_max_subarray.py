import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute: TC: O(n^3) SC: O(1)
        # Better: TC: O(n^2) SC: O(1)
        # Optimal: Using Kadane's algorithm where we discard the previous subarray sum when sum < 0 as it does not contribute to anything in the array
        # TC: O(n)
        # SC: O(1)
        maxSum = float(-inf)
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum
