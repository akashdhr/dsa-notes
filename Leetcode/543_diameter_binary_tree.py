# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
            
        if not root:
            return 0
        
        left = maxDepth(root.left)
        right = maxDepth(root.right)
        diameter = left + right
        subtree = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, subtree)
        

#time complexity: O(N^2) in the worst case for a skewed tree, where N is the number of nodes in the binary tree. This is because for each node, we are calculating the max depth which takes O(N) time, and we do this for all N nodes.
#space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).