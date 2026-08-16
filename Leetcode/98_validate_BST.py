# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            elif not(low < node.val < high):
                return False
            else:
                return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float('-inf'), float('inf'))
        
        
#time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
#space complexity: O(H) where H is the height of the binary tree.