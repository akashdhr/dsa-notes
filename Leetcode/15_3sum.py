class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            low = i+1
            high = len(nums)-1

            while low < high:
                if nums[low] + nums[high] < target:
                    low += 1
                elif nums[low] + nums[high] > target:
                    high -= 1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1
        return res
# time complexity: O(N^2)
# space complexity: O(1)



        