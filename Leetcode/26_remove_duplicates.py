class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[curr]:
                curr += 1
                nums[curr] = nums[fast]
        return curr + 1
        
#time complexity: O(n) where n is the number of elements in the array.
#space complexity: O(1) as we are not using any extra space.