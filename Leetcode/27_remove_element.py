class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 1
        # find first index where i = val
        while slow < len(nums):
            if nums[slow] == val:
                break
            slow += 1
        for i in range(slow+1, len(nums)):
            if nums[i] != val:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1
        return slow
# time complexity: O(N)
# space complexity: O(1)