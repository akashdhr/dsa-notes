# Lower Bound - Binary Search Implementation
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        ans = len(nums)
        while l<=r:
            m = (l+r)//2
            if nums[m] >= target:
                ans = m
                r = m-1
            else:
                l = m+1
        return ans


## Alternative Implementation

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        ans = len(nums)
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans + 1

#time complexity: O(logN) where N is the number of elements in the array.
#space complexity: O(1) as we are using constant space.