# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def dfs(node, path):
            if not node:
                return
            
            # add current node to path
            path += str(node.val)
            
            # if leaf: save the full path
            if not node.left and not node.right:
                paths.append(path)
                return
            
            # otherwise go deeper, adding arrow before child
            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")
        
        dfs(root, "")
        return paths
        