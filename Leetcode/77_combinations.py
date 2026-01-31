class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(n):
            arr.append(i+1)
        res = []
        def dfs(ind, ds):
            if len(ds) == k:
                res.append(ds.copy())
                return
            if ind == len(arr):
                return
            ds.append(arr[ind])
            dfs(ind + 1, ds)
            ds.pop()
            dfs(ind + 1, ds)
        dfs(0, [])
        return res
#time complexity: O(C(n, k) * k) where C(n, k) is the number of combinations and k is the time taken to copy each combination to the result list.
#space complexity: O(k) for the recursion stack and the temporary list used to store combinations.