class Solution:
    def climb_stairs(self, N):

        dp = [0] * (N + 1)
        dp[0] = 1
        #初始位置还没上楼题，默认为1
        for i in range(1, N + 1):
            if i - 1 >= 0:
                dp[i] += dp[i - 1]
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
            if i - 4 >= 0:
                dp[i] += dp[i - 4]
        return dp[-1]

if __name__ == '__main__':
    print(Solution().climb_stairs(4))
