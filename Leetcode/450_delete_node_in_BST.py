# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            # search on right
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # search on left
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            res = root.right
            del root
            return res
        return root


# time complexity: O(H) where H is the height of the binary search tree. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).
# space complexity: O(H) where H is the height of the binary search tree.