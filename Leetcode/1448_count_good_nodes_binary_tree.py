# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return
        def dfs(node, t):
            if not node:
                return
            if node.val >= t:
                self.res += 1
                t = node.val
            dfs(node.left, t)
            dfs(node.right, t)
        dfs(root, root.val)
        return self.res
            
        
# time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
# space complexity: O(H) where H is the height of the binary tree. This space