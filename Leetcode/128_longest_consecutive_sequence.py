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
        og = set(nums)
        longest = 0
        for i in og:
            cnt = 0
            val = i
            if i-1 in og:
                continue
            while val in og:
                val += 1
                cnt += 1
            longest = max(longest, cnt)
        return longest    
        
                

# time complexity: O(N) where N is the number of elements in the input array. We traverse the array once to put all elements into the set and then we traverse the set to find the longest consecutive sequence.
# space complexity: O(N) in the worst case when all elements in the array are distinct 
            