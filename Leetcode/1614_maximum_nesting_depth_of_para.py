class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
                maxDepth = max(depth, maxDepth)
            elif c == ')':
                depth -= 1
        return maxDepth
                
