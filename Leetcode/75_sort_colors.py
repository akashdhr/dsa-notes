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
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return

