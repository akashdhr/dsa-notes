# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = None
        def dfs(node):
            if not node or self.res is not None:
                return
            dfs(node.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res
# time complexity: O(H + k) where H is the height of the binary search tree. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N). We may need to visit up to k nodes in the worst case.   
# space complexity: O(H) where H is the height of the binary search tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).