class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Better solution using count vars. TC: O(2n) SC: O(1)
        '''
        c0, c1, c2 = 0, 0, 0
        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1:
                c1 += 1
            else:
                c2 += 1
        #overwrite unsorted array
        for j in range(c0):
            nums[j] = 0
        for j in range(c0, c0+c1):
            nums[j] = 1
        for j in range(c0+c1, len(nums)):
            nums[j] = 2
        return nums
        '''
        # DNF (Dutch National Flag Alogirthm)
        # Previous one did two iterations so TC was O(2n). In case of further optimization use DNF
        # TC: O(n)
        # SC: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = med = 0
        high = len(nums)-1
        while med <= high:
            if nums[med] == 2:
                nums[med], nums[high] = nums[high], nums[med]
                high -= 1
            elif nums[med] == 0:
                nums[low], nums[med] = nums[med], nums[low]
                low += 1
                med += 1
            else:
                med += 1
        return nums
        

