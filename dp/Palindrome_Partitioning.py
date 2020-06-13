class Solution:
    def partition(self, s):
        lens = len(s)
        dp = self.dp_Palindrome(s)
        ans = []
        self.helper(s, 0, dp, [], ans)
        return ans

    def dp_Palindrome(self, s):
        lens = len(s)
        dp = [[False for _ in range(lens)] for _ in range(lens)]
        for i in range(lens):
            dp[i][i] = True
        for end in range(1, lens):
            for start in range(end):
                if s[start] == s[end]:
                    if end - start + 1 <= 3:
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start + 1][end - 1]
                else:
                    dp[start][end] = False
        return dp

    def helper(self, s, start, dp, state, res):
        if start == len(s):
            res.append(state.copy())
        for i in range(start, len(s)):
            if dp[start][i]:
                left = s[start: i + 1]
                state.append(left)
                self.helper(s, i + 1, dp, state, res)
                state.pop()
