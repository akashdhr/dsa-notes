class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Find breakpoint where a[i] < a[i+1]
        # 2. Swap a[i] with the immediate greater number present between the nums range a[i+1] and a[-1]
        # 3. Place the nums range a[i+1] and a[-1] in sorted maner

        breakpt = -1
        # Searching for longest common prefix where the breakpoint is located
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                breakpt = i
                break
        print(breakpt)
        if breakpt == -1:
            print("inside -1")
            nums.reverse()
            return
        # Swapping the closest greater value from the second part of the array with the breakpoint
        for j in range(len(nums)-1, -1, -1):
            if nums[j]>nums[breakpt]:
                nums[j], nums[breakpt] = nums[breakpt], nums[j]
                break
        print(nums)
        # Since the second part of the array is already in decreasing sorted order we can simply
        # reverse the array
        
        l, r = breakpt+1, len(nums)-1
        while l<=r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        print(nums)
        return
        

