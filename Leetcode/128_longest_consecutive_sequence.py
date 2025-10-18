'''
First, we will put all the array elements into the set data structure.
If a number, num, is a starting number, ideally, num-1 should not exist. So, for every element, x, in the set, we will check if x-1 exists inside the set. :
If x-1 exists: This means x cannot be a starting number and we will move on to the next element in the set.
If x-1 does not exist: This means x is a starting number of a sequence. So, for number, x, we will start finding the consecutive elements.
How to search for consecutive elements for a number, x:

Instead of using linear search, we will use the set data structure itself to search for the elements x+1, x+2, x+3, and so on.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxCount = 0
        for i in numset:
            if i-1 in numset:
                continue
            count = 0
            while i+count in numset:
                count+=1
            maxCount = max(count, maxCount)
        return maxCount
            