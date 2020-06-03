class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        if length % 2 == 0:
            return True
        else:
            dp = [[0 for _ in range(length)] for _ in range(length)]
            for i in range(length):
                dp[i][i] = nums[i]
            for i in range(length - 1, -1, -1):
                for j in range(i + 1, length):
                    dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
            return dp[0][length-1] >= 0
