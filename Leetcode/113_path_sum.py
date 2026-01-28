# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, ds, curr):
            if not node:
                return
            curr += node.val
            ds.append(node.val)
            if not node.left and not node.right:
                if curr == targetSum:
                    res.append(ds.copy())
                ds.pop()
                return
            dfs(node.left, ds, curr)
            dfs(node.right, ds, curr)
            ds.pop()
        dfs(root, [], 0)
        return res

#time complexity: O(N) where N is number of nodes in the binary tree as we visit each node once.
#space complexity: O(H) where H is the height of the binary tree which is used by the recursion stack.