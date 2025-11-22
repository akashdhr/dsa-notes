class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num//2
        if num == 1:
            return True
        while l <= r:
            m = (l+r)//2
            tmp = m*m
            if tmp == num:
                return True
            elif tmp < num:
                l = m + 1
            else:
                r = m - 1
        return False
        