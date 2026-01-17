class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            prod = mid * mid
            if prod <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
# time complexity: O(log X) where X is the input number. We are reducing the search space by half in each iteration.
# space complexity: O(1) as we are using only constant extra space.