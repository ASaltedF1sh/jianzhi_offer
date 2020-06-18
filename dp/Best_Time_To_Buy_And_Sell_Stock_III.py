class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n)]

        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')

        for i in range(1, n):
            dp[i][0][0] = 0
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i][0][0] - prices[i])
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][0] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][1] - prices[i])
            dp[i][0][2] = max(dp[i - 1][0][2], dp[i - 1][1][1] + prices[i])
            dp[i][1][2]=float('-inf')
        return max(dp[n - 1][0][1], dp[n - 1][0][2], 0)
