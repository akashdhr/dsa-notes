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

       #    time complexity: O(N * 2^N) where N is the length of nums. In the worst case, we generate all subsets (2^N) and copying each subset takes O(N) time.
       #    space complexity: O(N) for the recursion stack and the temporary list used to store subsets. 