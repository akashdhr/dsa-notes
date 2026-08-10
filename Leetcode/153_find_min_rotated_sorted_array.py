class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        low = 0
        high = len(nums) - 1
        ans = nums[0]
        while low <= high:
            mid = (low + high)//2
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            elif nums[mid] < nums[high]:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans

# time complexity: O(logN) where N is the number of elements in the array.
# space complexity: O(1) as we are using constant space.