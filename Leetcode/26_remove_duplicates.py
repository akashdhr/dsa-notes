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
