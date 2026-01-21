# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        q = deque([root])
        level = 0
        max_level = 1
        while q:
            level += 1
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > maxSum:
                maxSum = level_sum
                max_level = level
        return max_level
# time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
# space complexity: O(M) where M is the maximum number of nodes at any level in the binary tree. In the worst case, this can be O(N/2) = O(N) for a balanced binary tree.