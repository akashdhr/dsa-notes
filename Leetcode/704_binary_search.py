class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m 
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

# time complexity: O(log N) where N is the number of elements in the input array since we are using binary search to find the target element.
# space complexity: O(1) since we are using only a constant amount of extra space