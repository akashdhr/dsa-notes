class MinStack:

    def __init__(self):
        self.s = []  # stores the main stack values
        self.ms = [] # stores the min value for each index

    def push(self, val: int) -> None:
        self.s.append(val)
        x = min(val, self.ms[-1] if self.ms else val)
        self.ms.append(x)

    def pop(self) -> None:
        self.s.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.s[-1]
        
    def getMin(self) -> int:
        return self.ms[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# time complexity: O(1) for all operations (push, pop, top, getMin) since we are using two stacks to store the values and the minimum values at each index.
# space complexity: O(N) where N is the number of elements in the stack since we are using two stacks to store the values and the minimum values at each index.