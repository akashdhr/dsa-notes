# Recursive approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
# time complexity: O(H) where H is the height of the binary search tree. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).
# space complexity: O(H) where H is the height of the binary search tree.

# Iterative approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if cur.val > val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
        
#time complexity: O(H) where H is the height of the binary search tree. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).
# space complexity: O(1) since we are using an iterative approach and not using any additional space that grows with the input size.