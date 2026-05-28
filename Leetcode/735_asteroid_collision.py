class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while alive and stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(a)
        return stack
                
        
#time complexity: O(N) where N is the number of asteroids.
#space complexity: O(N) in the worst case when all asteroids are moving in the same direction and there are no collisions, we will have to store all asteroids in the stack.