#brute force
class Solution:
    def new21Game(self, N, K, W):
        # if K == 0:
        #     return 1.0
            
        # self.NO = 0
        # base_prob = 1 / W

        # def helper(res, tmp, prob):
        #     res += tmp
        #     prob *= base_prob
        #     if res >= K:
        #         if res <= N:
        #             self.NO += prob
        #         return
        #     else:
        #         for i in range(1, W + 1):
        #             helper(res, i, prob)
        # for i in range(1, W + 1):
        #     helper(0, i, 1)
        # return self.NO

#DP
# dp[i] = 1 / W * (dp[i+1] + dp[i+2] + ... + dp[i+W])
# dp[i-1] = 1 / W * (dp[i] + dp[i+1] + ... + dp[i+W-1])

# ...
# dp[0] = 1 / W * (dp[1] + dp[2] + ... + dp[W])

class Solution:
    def new21Game(self, N, K, W):
        if K == 0:
            return 1.0
        dp = [0.0 for _ in range(K + W)]
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        for i in range(1, W + 1):
            dp[K - 1] += 1/W * dp[K - 1 + i]
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i+1] - 1/ W * (dp[i + W + 1] - dp[i+1])
        return dp[0]
