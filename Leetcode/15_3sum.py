class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            rem = -nums[i]
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] < rem:
                    low += 1
                elif nums[low] + nums[high] > rem:
                    high -= 1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low-1] == nums[low]:
                        low += 1
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1
        return res

# time complexity: O(n^2) where n is the number of elements in the array.
# space complexity: O(1) if we don't consider the output space.