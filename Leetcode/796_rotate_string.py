class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Brute force solution below
        '''
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False
        '''
        # Optimal solution
        if len(goal) == len(s) and goal in s+s:
            return True
        else:
            return False