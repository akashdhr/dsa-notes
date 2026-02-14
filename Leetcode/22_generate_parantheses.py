class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(arr, s, c):
            if s == c == n:
                res.append(''.join(arr.copy()))
                return
            if s < n:
                arr.append('(')
                dfs(arr, s+1, c)
                arr.pop()
            if c < s:
                arr.append(')')
                dfs(arr, s, c+1)
                arr.pop()
        dfs([], 0, 0)
        return res
        
        
# time complexity: O(4^n / sqrt(n)) where n is the number of pairs of parentheses.
# space Complexity: O(4^n / sqrt(n)) to store all valid combinations. 