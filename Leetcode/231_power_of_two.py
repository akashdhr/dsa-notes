class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def check(num):
            if num <= 0:
                return False
            elif num == 1:
                return True
            elif num % 2 != 0:
                return False
            return check(num//2)
        return check(n)
# Time complexity: O(log N)
# Space complexity: O(log N) due to recursion stack