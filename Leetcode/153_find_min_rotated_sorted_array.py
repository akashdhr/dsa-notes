class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            # Optimization Step 
            # If array is already sorted then no need to perform BS on that space. Just return the minimum from the sorted half
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            # Identify sorted half
            if nums[l] <= nums[m]:
                # Update the minimum value in res
                # move l to m+1 and eliminate left sorted half
                res = min(res, nums[l])
                l = m+1
            else:
                # If right half is sorted
                # Update the minimum value in res
                # move h to m-1 and eliminate right sorted half
                res = min(res, nums[m])
                r = m-1
        return res 


            
        