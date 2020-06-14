class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        for ind, t in enumerate(obstacleGrid[0]):
            if t == 1:
                break
            else:
                dp[0][ind] = 1
        for ind in range(n):
            if obstacleGrid[ind][0] == 1:
                break
            else:
                dp[ind][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
