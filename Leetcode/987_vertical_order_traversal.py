# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Dictionary to store nodes by vertical and level
        nodes = {}
        q = deque([(root, 0, 0)]) # [node, x-axis, y-axis] root node should be (0,0)
        while q:
            temp, x, y = q.popleft()
            if x not in nodes:
                nodes[x] = {}
            if y not in nodes[x]:
                nodes[x][y] = []
            nodes[x][y].append(temp.val)
            if temp.left:
                q.append((temp.left, x-1, y+1))
            if temp.right:
                q.append((temp.right, x+1, y+1))
        ans = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))
            ans.append(col)
        return ans
#time complexity: O(NlogN) where N is number of nodes in the tree. why? because we are sorting the nodes at each vertical level
#space complexity: O(N) for storing the nodes in the dictionaryfrom collections import deque