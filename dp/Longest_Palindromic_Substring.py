#brute force
class Solution1:
    def longestPalindrome(self, s):

        if len(s) < 2:
            return s
        ans = s[0]
        max_len = 1
        for start in range(len(s)):
            for end in range(len(s)):
                if end - start + 1 > max_len and self.isPalindrome(s[start: end + 1]):
                    if end - start + 1 > max_len:
                        ans = s[start: end + 1]
                        max_len = end - start + 1
        return ans

    def isPalindrome(self, subs):
        i = 0
        j = len(subs) - 1

        while i < j:
            if subs[i] != subs[j]:
                return False
            i += 1
            j -= 1
        return True

#DP
class Solution2:
    def longestPalindrome(self, s):
        lens = len(s)
        if lens < 2:
            return s
        dp = [[False for _ in range(lens)] for _ in range(lens)]
        max_len = 1
        ans = s[0]

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
                if dp[start][end] and end - start + 1 > max_len:
                    max_len = end - start + 1
                    ans = s[start: end + 1]
        return ans
