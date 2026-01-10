class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        postfix = 1
        #forward
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        # backward
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer

# time complexity: O(N)
# space complexity: O(1)