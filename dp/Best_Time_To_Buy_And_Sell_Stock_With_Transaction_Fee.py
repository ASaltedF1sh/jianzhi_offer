class Solution:
    def maxProfit(self, prices, fee):
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)

        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            #今天没股票，可能是昨天有今天给卖了，也有可能昨天就没
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            #今天有股票，可能昨天就有，也可能昨天没今天卖了
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]

#内存优化
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        a = 0
        b = -prices[0]

        for i in range(1, n):
            #今天没股票，可能是昨天有今天给卖了，也有可能昨天就没
            tmp = a
            a = max(a, b + prices[i] - fee)
            #今天有股票，可能昨天就有，也可能昨天没今天卖了
            b = max(b, tmp - prices[i])
        return a
