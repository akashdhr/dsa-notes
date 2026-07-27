class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxD = 0
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
            r += 1
            maxD = max(diff, maxD)
        return maxD

# time complexity: O(N) where N is the number of days (length of the prices array) since we traverse the array once.
# space complexity: O(1) since we are using only a constant amount of extra space to store the pointers and the profit variable.