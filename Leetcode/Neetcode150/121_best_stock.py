class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute: O(n^2)
        # Optimal: Using Two pointer. TC: O(n) SC: O(1) 
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r]-prices[l]
                maxP = max(diff, maxP)
            else:
                l = r
            r += 1
        return maxP