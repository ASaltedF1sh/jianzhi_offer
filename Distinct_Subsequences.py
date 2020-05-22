#回溯法base版，超时

class Solution:
    def numDistinct(self, s, t):
        self.ans = 0
        self.helper(s, t, 0)
        return self.ans

    def helper(self, s, t, index):

        if index == len(t):
            self.ans += 1
            return
        for i in range(len(s)):
            if s[i] == t[index]:
                self.helper(s[i + 1:], t, index + 1)

#利用 Memoization trick 加快回溯过程，勉强AC
class Solution:
    def numDistinct(self, s, t):
        self.ans = 0
        hashmap = {}
        self.helper(s, t, 0, hashmap)
        return self.ans

    def helper(self, s, t, index, map):

        if index == len(t):
            self.ans += 1
            return
        if s + str(index) in map:
            self.ans += map[s + str(index)]
            return
        for i in range(len(s)):
            if s[i] == t[index]:
                tmp = self.ans
                self.helper(s[i + 1:], t, index + 1, map)
                increment = self.ans - tmp
                map[s[i + 1:] + str(index + 1)] = increment
                
#DP                
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        #前0个到前n个，故长度为n+1
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        #dp[i][j]表示T的前i个字符构成的子序列在S的前j个字符构成的子序列中出现的次数
        #空串是任何串的子串，所以dp[0][j] = 1
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                #t[i - 1]代表的是第i个字符，刚好与下面的dp[i][j]代表的前i个字符相对应
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        #print(dp)
        return dp[-1][-1]
