class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ds = []
        def find(ind, val, ds):
            if val == target:
                res.append(ds.copy())
                return
            if ind >= len(candidates) or val > target:
                return
            ds.append(candidates[ind])
            find(ind, val+candidates[ind], ds)
            ds.pop()
            find(ind+1, val, ds)
        find(0, 0, ds)
        return res
# Time Complexity: O(2t * k) due to exploring all combinations up to the target with copying each valid combination of average length k.
# Space Complexity: O(k * x) to store all valid combinations, where x is the number of combinations and k is their average length.