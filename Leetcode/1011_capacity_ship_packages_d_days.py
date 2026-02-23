
class Solution:
    def calculateDays(self, arr, weight):
        days = 1
        curr = 0
        for i in arr:
            if curr + i > weight:
                days += 1
                curr = i
            else:
                curr += i
        return days
    
    # Lower Bound for BS: max(weights) if your ship capacity is less than the heaviest package, you cannot ship
    # Upper Bound for BS: sum(weights) in case all packages are onboarded on the same day
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res = -1
        while low <= high:
            mid = (low+high)//2
            if self.calculateDays(weights, mid) <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

#time complexity: O(N log(S)) where N is the number of packages and S is the sum of weights. The binary search will run in log(S) time and for each mid value, we will calculate the number of days required to ship all packages which takes O(N) time.
#space complexity: O(1) since we are using constant space to store the pointers and temporary variables.