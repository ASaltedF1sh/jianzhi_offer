class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i-  1][0])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])

        return dp[-1][0]

#可知每天都可同时进行买进和卖出，这样能攫取所有能获得的利润
#即若第二天股价比第一天高，就有可以获取的利润
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        tmp = prices[0]
        ans = 0
        for i in range(len(prices)):
            if prices[i] > tmp:
                ans += prices[i] - tmp
            tmp = prices[i]
        return ans
