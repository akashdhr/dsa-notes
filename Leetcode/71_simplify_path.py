class Solution:
    def simplifyPath(self, path: str) -> str:
        # Start by splitting the path based on / slashes
        pathArr = path.split('/')
        res = []
        # Base cases check for ignoring
        for i in pathArr:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(i)
        res = '/' + '/'.join(res)
        return res
# time complexity: O(N) where N is the length of the path.
# space complexity: O(N) in the worst case, we may store all the directories in the stack.
        