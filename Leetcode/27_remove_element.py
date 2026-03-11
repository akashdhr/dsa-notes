class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                first = i
                break
        for j in range(first+1, len(nums)):
            if nums[j] != val:
                nums[j], nums[first] = nums[first], nums[j]
                first += 1
        return first

# time complexity: O(N) where N is the length of the input array. We traverse the array once to find the first occurrence of val and then traverse it again to move the non-val elements to the left.
# space complexity: O(1) since we are using only a constant amount of extra space to store the index of the first occurrence of val and to swap elements in place.