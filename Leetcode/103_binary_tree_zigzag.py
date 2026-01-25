# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        left_to_right = True
        q = deque([root])
        res = []
        if not root:
            return []
        while q:
            level = deque()
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            left_to_right = not left_to_right
            res.append(list(level))
        return res


# Time complexity: O(N) why? we visit each node once
# Space complexity: O(N) why? the size of the queue can grow up to N/2 in the last level  