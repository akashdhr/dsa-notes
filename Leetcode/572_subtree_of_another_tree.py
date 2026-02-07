# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            else:
                return False
        if not subRoot:
            return True
        if not root:
            return False
        if isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
#time complexity: O(N*M) in the worst case, where N is the number of nodes in the main tree and M is the number of nodes in the subtree. This occurs when we have to check each node of the main tree against the subtree.
#space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).
