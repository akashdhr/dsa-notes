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
#time complexity: So the real complexity is: O(2ⁿ + C(n, k) * k) But in interviews we usually say: O(2ⁿ) because that dominates.
#space complexity: O(k) for the recursion stack and the temporary list used to store combinations.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(ind, ds):
            if len(ds) == k:
                res.append(ds.copy())
                return
            for i in range(ind, n+1):
                ds.append(i)
                dfs(i+1, ds)
                ds.pop()
        dfs(1, [])
        return res        
    
# time complexity: O(C(n, k) * k)
# space complexity: O(C(n, k) * k)