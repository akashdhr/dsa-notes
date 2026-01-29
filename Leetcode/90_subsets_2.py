class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(ind, ds):
            if ind == len(nums):
                res.append(ds.copy())
                return
            ds.append(nums[ind])
            dfs(ind + 1, ds)
            ds.pop()
            next_ind = ind + 1
            while next_ind < len(nums) and nums[next_ind] == nums[ind]:
                next_ind += 1
            dfs(next_ind, ds)
        dfs(0, [])
        return res
# time complexity: O(N * 2^N) where N is the length of nums. In the worst case, we generate all subsets (2^N) and copying each subset takes O(N) time.
# space complexity: O(N) for the recursion stack and the temporary list used to store subsets