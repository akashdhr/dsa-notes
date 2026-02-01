class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currElem = nums[0] # will store the current element
        currInd = 1 # will store the current index where current element is present first
        for i in range(1, len(nums)):
            if nums[i] != currElem:
                nums[currInd] = nums[i]
                currElem = nums[i]
                currInd += 1
        return currInd
#time complexity: O(n) where n is the number of elements in the array.
#space complexity: O(1) as we are not using any extra space.