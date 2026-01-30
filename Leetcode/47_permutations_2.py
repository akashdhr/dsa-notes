class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        ds = []
        def find(nums, used, ds):
            if len(ds) == len(nums):
                res.append(ds.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                ds.append(nums[i])
                find(nums, used, ds)
                ds.pop()
                used[i] = False
        find(nums, used, ds)
        return res
#time complexity: O(N * N!) where N is the length of nums. There are N! permutations and generating each permutation takes O(N) time.
#space complexity: O(N) for the recursion stack and the temporary list used to store permutations