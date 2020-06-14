class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        dp = triangle.copy()
        for i in range(len(triangle) - 2, -1, -1):
            tmp = len(dp[i])
            for j in range(tmp):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]
