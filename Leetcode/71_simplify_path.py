class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        pathArr = path.split('/')
        for i in pathArr:
            if stack and i == '..':
                stack.pop()
            elif i == '..' or i == '.':
                continue
            elif i != '':
                stack.append(i)
        return ('/' + '/'.join(stack))
        
# time complexity: O(N) where N is the length of the input path string, since we need to iterate through the path string once to split it and then again to process each component.
# space complexity: O(N) in the worst case, if the input path contains many valid directory names, we may end up storing all of them in the stack.
        