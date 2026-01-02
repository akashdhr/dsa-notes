class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ds = []
        nums.sort()
        def subset(nums, res, ds, ind):
            if ind == len(nums):
                res.append(ds.copy())
                return
            ds.append(nums[ind])
            subset(nums, res, ds, ind+1)
            ds.pop()
            next_ind = ind + 1
            while next_ind < len(nums) and nums[next_ind] == nums[ind]:
                next_ind += 1
            subset(nums, res, ds, next_ind)
        subset(nums, res, ds, 0)
        return res