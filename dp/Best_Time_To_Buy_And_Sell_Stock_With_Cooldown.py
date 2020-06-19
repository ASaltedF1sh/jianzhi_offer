class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)

        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], -prices[1])

        for i in range(2, n):
            #没有股票，今天卖的或之前卖的
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            #有股票，昨天就有，或者昨天没有今天买的，如果昨天没有而且今天能买股票，那么前天一定不能有股票，不然昨天卖了今天就买不了了
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])

        return dp[-1][0]
