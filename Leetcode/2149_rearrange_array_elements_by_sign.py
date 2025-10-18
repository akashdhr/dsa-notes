class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        res = [0] * len(nums)
        for i in nums:
            if i < 0:
                res[neg] = i
                neg += 2
            else:
                res[pos] = i
                pos += 2
        for i in range(len(nums)):
            nums[i] = res[i]
        return nums
