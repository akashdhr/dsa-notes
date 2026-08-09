import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(s):
            total = 0
            for i in piles:
                total += math.ceil(i/s)
            return total
        
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high)//2
            timeTaken = totalTime(mid)
            if timeTaken <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        

# time complexity: O(N log M) where N is the number of piles and M is the maximum bananas in a pile. why? because for each speed we are calculating total hours which takes O(N) time and we are doing binary search on speed which takes O(log M) time.
# space complexity: O(1) as we are using only constant extra space.       

        