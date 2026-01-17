class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        low = 0
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                diff = i - stack[-1]
                res[stack[-1]] = diff
                stack.pop()
            stack.append(i)
            
        return res

#time complexity: O(N) where N is the number of temperatures.   
#space complexity: O(N) in the worst case, we may store all the temperatures in the stack.