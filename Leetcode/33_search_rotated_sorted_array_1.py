class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # Check if left half is sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            # Check if right half is sorted
            else:
                if nums[m] <= target and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1

            
        