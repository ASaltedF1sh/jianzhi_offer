class Solution:
    def maxProfit(self, prices):
        if not prices or not len(prices):
            return 0
        days = len(prices)
        dp = [0] * days
        min_price = prices[0]
        for i in range(1, days):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max(dp)
