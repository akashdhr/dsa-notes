# Brute force approach which uses O(n^2)
class Solution:
    def countNumbersGreaterorEqual(self, nums, n):
        cnt = 0
        for i in nums:
            if i >= n:
                cnt += 1
        return cnt
    def specialArray(self, nums: List[int]) -> int:
        for x in range(1, len(nums)+1):
            totalCount = self.countNumbersGreaterorEqual(nums, x)
            print("Total count for ", x , " is ", totalCount)
            if totalCount == x:
                return x
        return -1