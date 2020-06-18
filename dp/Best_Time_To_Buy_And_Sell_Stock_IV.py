# 定义状态转移数组dp[天数][当前是否持股][卖出的次数]
class Solution:
    def maxProfit(self, prices, k):
        if not prices:
            return 0
        n = len(prices)
        #k超出范围，等同于不限交易次数能获取的最大利润
        if k > n // 2:
            return self.maxProfit_inf(prices)
        dp = [[[float('-inf') for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]

        for i in range(1, n):
            for j in range(k + 1):
                if j == 0:
                    dp[i][0][0] = dp[i - 1][0][0]
                    dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][0] - prices[i])
                else:
                    dp[i][0][j] = max(dp[i - 1][1][j - 1] + prices[i], dp[i - 1][0][j])
                    dp[i][1][j] = max(dp[i - 1][0][j] - prices[i], dp[i - 1][1][j])
        return max(dp[n - 1][0])

    def maxProfit_inf(self, prices):
        if not prices:
            return 0
        tmp = prices[0]
        ans = 0
        for i in range(len(prices)):
            if prices[i] > tmp:
                ans += prices[i] - tmp
            tmp = prices[i]
        return ans
