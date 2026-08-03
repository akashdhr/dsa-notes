class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = nums[0]
        ind = 1
        for i in range(len(nums)):
            if nums[i] != cur:
                nums[ind] = nums[i]
                cur = nums[i]
                ind += 1
        return ind
        
#time complexity: O(n) where n is the number of elements in the array.
#space complexity: O(1) as we are not using any extra space.