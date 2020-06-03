class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        nums = len(coins)
        for n in range(1, amount + 1):
            tmp = [dp[n - coins[i]] + 1 for i in range(nums) if n - coins[i] >= 0 and dp[n - coins[i]] != -1]
            if tmp:
                dp[n] = min(tmp)
        return dp[-1]
