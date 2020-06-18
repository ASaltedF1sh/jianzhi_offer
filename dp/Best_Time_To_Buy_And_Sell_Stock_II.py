# 状态 dp[i][j] 定义如下
# 第一维 i 表示索引为 i 的那一天（具有前缀性质，即考虑了之前天数的收益）能获得的最大利润；
# 第二维 j 表示索引为 i 的那一天是持有股票，还是持有现金。这里 0 表示持有现金（cash），1 表示持有股票（stock）。

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        #第一天如买入股票，受益为负数
        dp[0][1] = -prices[0]

        for i in range(1, n):
            #第i+1天如卖出股票，则前一天一定持有股票,或者第i+1天不做操作，受益等于前一天的
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i-  1][0])
            #第i+1天如买入股票，则前一天一定没有股票
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
