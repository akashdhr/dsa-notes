# Brute Force Approach
# time complexity: O(N^2) where N is the number of nodes in the binary tree. For each node, we calculate the depth of its left and right subtrees, which takes O(N) time in the worst case.
# space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).

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
        
        def dfs(node):
            if not node:
                return 0
            leftDepth = maxDepth(node.left)
            rightDepth = maxDepth(node.right)
            diameter = leftDepth + rightDepth
            return max(diameter, dfs(node.left), dfs(node.right))

        return dfs(root)
    
# Optimized Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def find(node):
            if not node:
                return 0

            lh = find(node.left)
            rh = find(node.right)
            self.maxi = max(self.maxi, lh + rh)

            return 1 + max(lh, rh)
        find(root)
        return self.maxi

# time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
# space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).