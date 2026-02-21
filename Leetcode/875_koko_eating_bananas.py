class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalTime(piles, speed):
            t = 0
            for i in piles:
                t += math.ceil(i/speed)
            return t
        
        high = max(piles) # speed cannot be more than max bananas/pile in piles
        low = 1
        res = -1
        while low <= high:
            mid = (low + high)//2
            if totalTime(piles, mid) <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res


# time complexity: O(N log M) where N is the number of piles and M is the maximum bananas in a pile. why? because for each speed we are calculating total hours which takes O(N) time and we are doing binary search on speed which takes O(log M) time.
# space complexity: O(1) as we are using only constant extra space.       

        