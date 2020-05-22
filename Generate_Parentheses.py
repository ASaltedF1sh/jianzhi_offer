#回溯，常规做法
class Solution:
    def generateParenthesis(self, n):
        self.ans = []
        self.helper(n, n, '')
        return self.ans

    def helper(self, k_l, k_r, res):
        if k_l == 0 and k_r == 0:
            self.ans.append(res)
            return

        if k_l > 0:
            self.helper(k_l - 1, k_r, res + '(')
        if k_l < k_r:
            self.helper(k_l, k_r - 1, res + ')')

#DP
class Solution:
    def generateParenthesis(self, n):

        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']
        dp[1] = ['()']
        for i in range(2, n + 1):
            for j in range(i):
                for p in dp[j]:
                    for q in dp[i - 1 - j]:
                        dp[i].append('(' + p + ')' + q)
        return dp[-1]
