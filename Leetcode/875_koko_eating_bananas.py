import math

class Solution:
    def totalHrs(self, piles, speed):
        hrs = 0
        for i in piles:
            hrs += math.ceil(i/speed)
        return hrs
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ith pile has piles[i] bananas
        # h = hours; k = bananas/hr speed
        # if pile[i] < k all bananas eaten and no more will be eaten the same hour
        
        high = max(piles) # Speed cannot be more than this value why?
        low = 1 # why? because min speed can be 1 banana/hr
        res = -1
        while low <= high:
            mid = (low+high)//2
            # check if Koko can finish with speed = mid
            if self.totalHrs(piles, mid) <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

# time complexity: O(N log M) where N is the number of piles and M is the maximum bananas in a pile. why? because for each speed we are calculating total hours which takes O(N) time and we are doing binary search on speed which takes O(log M) time.
# space complexity: O(1) as we are using only constant extra space.       

        