class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for roid in asteroids:
            # check for collisions
            while stack and roid < 0 and stack[-1] > 0:
                diff = stack[-1] + roid
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    roid = 0
                else:
                    roid = 0
                    stack.pop()
            if roid:
                stack.append(roid)
        return stack
#time complexity: O(N) where N is the number of asteroids.
#space complexity: O(N) in the worst case when all asteroids are moving in the same direction and there are no collisions, we will have to store all asteroids in the stack.