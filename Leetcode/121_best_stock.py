class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 1
        profit = 0
        while high < len(prices):
            diff = prices[high] - prices[low]
            if diff <= 0:
                low = high
            elif diff > 0:
                profit = max(profit, diff)
            high +=1
        return profit

# time complexity: O(N) where N is the number of days (length of the prices array) since we traverse the array once.
# space complexity: O(1) since we are using only a constant amount of extra space to store the pointers and the profit variable.