class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            # check edge case where nums[l] == nums[m] == nums[r]
            if nums[l] == nums[m] and nums[m] == nums[r]:
                l += 1
                r -= 1
                continue # continue does not execute the rest of the code to ensure the search space does not contain edge case
            # Check if left half is sorted
            if nums[l] <= nums[m]:
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
        return False