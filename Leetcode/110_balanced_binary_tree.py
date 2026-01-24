## Naiive Recursive Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Helper function to calculate the maximum height of a subtree
        def maxHeight(node):
            if not node:
                return 0
            left = maxHeight(node.left)
            right = maxHeight(node.right)
            return 1 + max(left, right)
        
        if not root:
            return True
            
        leftHeight = maxHeight(root.left)
        rightHeight = maxHeight(root.right)

        if abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
#time complexity: O(N log N) in the average case for a balanced tree, where N is the number of nodes in the binary tree. This is because for each node, we are calculating the max height which takes O(log N) time, and we do this for all N nodes. In the worst case (skewed tree), the time complexity can degrade to O(N^2).
#space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(left-right) > 1:
                return -1

            return 1 + max(left, right)
        if check(root) == -1:
            return False
        return True
#time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
#space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).