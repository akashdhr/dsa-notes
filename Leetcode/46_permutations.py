class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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