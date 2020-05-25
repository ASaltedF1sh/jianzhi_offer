class Solution:
    def solveNQueens(self, n):

        board = ['.' * n for _ in range(n)]
        ans = []

        def helper(k, res):
            if k == n:
                ans.append(res)
                return
            for i in range(n):
                if not self.isValid(k, i, res):
                    continue
                res[k] = '.' * i + 'Q' + '.' * (n - i - 1)
                helper(k + 1, res.copy())

        helper(0, board)
        return ans

    def isValid(self, m, n, res):
        length = len(res)
        for i in range(length):
            if res[i][n] == 'Q':
                return False
        left = min(m, n)
        right = min(m, length - n - 1)
        #左上
        if left > 0:
            for i in range(1, left + 1):
                if res[m - i][n - i] == 'Q':
                    return False
        #右上
        if right > 0:
            for i in range(1, right + 1):
                if res[m - i][n + i] == 'Q':
                    return False
        return True
