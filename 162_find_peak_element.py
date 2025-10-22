class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            # Check if m is the first index and a peak
            if m == 0 and nums[m] > nums[m+1]:
                return m
            # Check if m is the last index and a peak
            if m == len(nums)-1 and nums[m] > nums[m-1]:
                return m    
            # Base case for peak
            if nums[m] > nums[m-1] and nums[m+1] < nums[m]:
                return m
            # Check if left side is having peak
            elif nums[m] > nums[m+1]:
                r = m
                # Not updating r as m-1 as m could be the peak
            # Check if the right side is having peak
            else:
                l = m+1
        return -1
        