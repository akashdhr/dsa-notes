class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        while l < len(nums) and nums[l] != val:
            l += 1
        r = l+1
        while r < len(nums):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        print(nums)
        return l
        

# time complexity: O(N) where N is the length of the input array. We traverse the array once to find the first occurrence of val and then traverse it again to move the non-val elements to the left.
# space complexity: O(1) since we are using only a constant amount of extra space to store the index of the first occurrence of val and to swap elements in place.