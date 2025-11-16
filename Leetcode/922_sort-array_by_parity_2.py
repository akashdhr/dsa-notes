class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l = 0 #for tracking even indices
        r = 1 #for tracking odd indices
        sz = len(nums)
        while l < sz and r < sz:
            if nums[l] % 2 == 0:
                l += 2
            elif nums[r] % 2 != 0:
                r += 2
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 2
                r -= 2
        return nums


        