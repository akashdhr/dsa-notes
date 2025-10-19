# Use Binary Search to look for the first and last position for O(logN) time
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        # first position check
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                first = m
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        # last position check
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                last = m
                l = m+1
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return [first, last]      