# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(res, node):
            if not node:
                return
            dfs(res, node.left)
            res.append(node.val)
            dfs(res, node.right)
        dfs(res, root)
        return res
# time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
# space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).
