class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == '+':
                stack.append(stack[-1] + stack[-2])
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        total = sum(stack)
        return total

# time complexity: O(N) where N is the number of operations.
# space complexity: O(N) in the worst case, we may store all the operations in the stack.