# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(res, node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)
            dfs(res, node.right, depth + 1)
            dfs(res, node.left, depth + 1)
        dfs(res, root, 0)
        return res
            
# time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
# space complexity: O(H) where H is the height of the binary tree. This space is used by the recursion stack. In the worst case (skewed tree), H can be O(N). In a balanced tree, H is O(log N).

# BFS approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        if not root:
            return []
        res = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
# time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
# space complexity: O(W) where W is the maximum width of the binary tree. 

# Another BFS Approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            level = []
            cur = 0
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                cur = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(cur)
        return res
#time complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
# space complexity: O(W) where W is the maximum width of the binary tree.