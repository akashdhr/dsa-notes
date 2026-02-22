class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                diff = i - stack[-1]
                answer[stack[-1]] = diff
                stack.pop()
            stack.append(i)
        return answer

#time complexity: O(N) where N is the number of temperatures.   
#space complexity: O(N) in the worst case, we may store all the temperatures in the stack.  