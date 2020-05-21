class Solution:
    def countSubstrings(self, s):
        n = len(s)
        if not n:
            return 0
        ans = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            ans += 1

        for end in range(1, n):
            for start in range(end):
                if s[start] == s[end]:
                    if end - start + 1 <= 3:
                        dp[start][end] = True
                        ans += 1
                    else:
                        dp[start][end] = dp[start + 1][end - 1]
                        if dp[start][end]:
                            ans += 1
                else:
                    dp[start][end] = False
        return ans
