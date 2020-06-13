#dp[n]=min(dp[n-1] + cost[0] , dp[n-7] + cost[1] , dp[n-30] + cost[2] )
class Solution:
    def mincostTickets(self, days, costs):
        costs[0] = min(costs)
        costs[1] = min(costs[1:])
        dp = [0 for _ in range(days[-1] + 1)]
        for d in days:
            dp[d] = 1
        for n in range(1, len(dp)):
            if dp[n]:
                if n - 7 < 0:
                    dp[n] = min(dp[n - 1] + costs[0], costs[1], costs[2])
                elif n - 30 < 0:
                    dp[n] = min(dp[n - 1] + costs[0], dp[n - 7] + costs[1], costs[2])
                else:
                    dp[n] = min(dp[n - 1] + costs[0], dp[n - 7] + costs[1], dp[n - 30] + costs[2])
            else:
                dp[n] = dp[n - 1]
        return dp[days[-1]]
