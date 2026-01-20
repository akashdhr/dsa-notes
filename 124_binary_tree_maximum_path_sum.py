# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.maxi = max(self.maxi, left + right + node.val)
            return max(left, right) + node.val
        
        dfs(root)
        return self.maxi
#time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
#space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).