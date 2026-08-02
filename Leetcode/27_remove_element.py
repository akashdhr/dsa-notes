class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = -1
        for i in range(len(nums)):
            if nums[i] == val:
                l = i
                break
        if l == -1:
            return len(nums)
        i = l
        for r in range(i+1, len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return l
        
        

# time complexity: O(N) where N is the length of the input array. We traverse the array once to find the first occurrence of val and then traverse it again to move the non-val elements to the left.
# space complexity: O(1) since we are using only a constant amount of extra space to store the index of the first occurrence of val and to swap elements in place.