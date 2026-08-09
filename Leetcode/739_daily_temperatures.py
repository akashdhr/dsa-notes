class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        iwarm = [[temperatures[-1], len(temperatures)-1]] # stores the last warm temperature stack: [temp, index]
        ans = [0] * len(temperatures)
        # iterate from the back
        for i in range(len(temperatures)-2, -1, -1):
            while iwarm and temperatures[i] >= iwarm[-1][0]:
                iwarm.pop()
            if iwarm:
                ans[i] = iwarm[-1][1] - i
            iwarm.append([temperatures[i], i])
        return ans
            


#time complexity: O(N) where N is the number of temperatures.   
#space complexity: O(N) in the worst case, we may store all the temperatures in the stack.  