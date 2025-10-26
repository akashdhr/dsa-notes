class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numset = set(nums)
        # Always take end till the length + 1 because array might contain all multiples of k
        end = k * (len(nums) + 1)
        for i in range(k, end+1, k):
            if i not in numset:
                return i
