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
        
        high = max(piles) # Speed cannot be more than this value
        low = 1
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
            

        