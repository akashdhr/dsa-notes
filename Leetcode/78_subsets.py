class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        ds = []
        def subset(nums, res, ds, ind):
            if ind == len(nums):
                res.append(ds.copy())
                return
            ds.append(nums[ind])
            subset(nums, res, ds, ind+1)
            ds.pop()
            subset(nums, res, ds, ind+1)
        subset(nums, res, ds, 0)
        return res

        