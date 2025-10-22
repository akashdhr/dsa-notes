class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Edge cases in order to trim down search space
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        # Check based on even/odd positions of the numbers
        # if (even, odd) element is on right half
        # if (odd, even) element is on left half
        l, r = 1, len(nums)-2
        while l<=r:
            m = (l+r)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            # Check if element is on right half: even,odd condition is satisfied
            elif (m%2==0 and nums[m]==nums[m+1]) or (m%2!=0 and nums[m]==nums[m-1]):
                l = m+1
            else:
                r = m-1
        return-1
