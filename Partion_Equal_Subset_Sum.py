class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
        for i in range(target + 1):
            if nums[0] == i:
                dp[0][i] = True
        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if j - nums[i] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
            if dp[i][-1]==True:
                return True
        return dp[-1][-1]

#进一步优化，将二维的表优化为1维的可以进一步节省空间，即“从后前向”填表。
class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = [False] * (total // 2 + 1)
        target = total // 2
        for i in range(target + 1):
            if nums[0] == i:
                dp[i] = True
        print(dp)
        for i in range(1, len(nums)):
            for j in range(target, 0, -1): 
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]] or nums[i] == j
        return dp[-1]
