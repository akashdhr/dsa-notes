class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ds = []
        candidates.sort()
        def find_combination(candidates, res, ds, ind, target):
            if target == 0:
                res.append(ds.copy())
                return
            if ind == len(candidates) or target < 0:
                return
            
            ds.append(candidates[ind])
            find_combination(candidates, res, ds, ind+1, target - candidates[ind])
            ds.pop()
            next_ind = ind + 1

            while next_ind < len(candidates) and candidates[next_ind] == candidates[ind]:
                next_ind += 1

            find_combination(candidates, res, ds, next_ind, target)
        find_combination(candidates, res, ds, 0, target)
        return res
#time complexity: O(2^n) in the worst case, where n is the number of candidates, as we explore all possible combinations.
#space complexity: O(k * x) to store all valid combinations, where x is the number of combinations and k is their average length.