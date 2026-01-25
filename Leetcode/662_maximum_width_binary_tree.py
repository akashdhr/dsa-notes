# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using BFS approach
# time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
# space complexity: O(M) where M is the maximum number of nodes at any level in the binary tree. In the worst case, this can be O(N/2) = O(N) for a balanced binary tree.
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([[root, 1, 0]]) # [node, num, level]
        prevLevel, prevNum = 0, 1
        while q:
            node, num, level = q.popleft()

            if level > prevLevel:
                prevLevel = level
                prevNum = num

            res = max(res, num - prevNum + 1)
            if node.left:
                q.append([node.left, 2*num, level + 1])
            if node.right:
                q.append([node.right, 2*num + 1, level + 1])
            
        return res

# At a time in the queue we are storing parent nodes along with child nodes. Only way to distinguish between levels is by storing level information as well. Hence we are storing level information in the queue.