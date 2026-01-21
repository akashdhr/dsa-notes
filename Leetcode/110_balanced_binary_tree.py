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