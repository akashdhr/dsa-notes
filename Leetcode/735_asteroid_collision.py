class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            alive = True
            while stack and i < 0 and stack[-1] > 0:
                if stack[-1] < abs(i):
                    stack.pop()
                elif stack[-1] == abs(i):
                    alive = False
                    stack.pop()
                    break
                else:
                    alive = False
                    break
            if alive:
                stack.append(i)
        return stack
        
#time complexity: O(N) where N is the number of asteroids.
#space complexity: O(N) in the worst case when all asteroids are moving in the same direction and there are no collisions, we will have to store all asteroids in the stack.