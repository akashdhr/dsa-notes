class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] # stack will store the current asteroids
        for i in asteroids:
            # check for collisions
            while stack and i<0 and stack[-1]>0:
                diff = stack[-1]+i
                if diff<0:
                    stack.pop()
                elif diff>0:
                    i = 0
                else:
                    i = 0
                    stack.pop()
            if i:
                stack.append(i)

        return stack 