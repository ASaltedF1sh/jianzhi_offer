class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) and len(board[0]):
            height = len(board)
            width = len(board[0])
            ans = set()
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]

            def helper(m, n, ans):
                ans.add((m, n))

                for i, j in zip(dx, dy):
                    x = m + i
                    y = n + j
                    if 0 <= x < height and 0 <= y < width and board[x][y] == "O" and (x, y) not in ans:
                        helper(x, y, ans)

            for i in range(height):
                if board[i][0] == "O":
                    helper(i, 0, ans)
                if board[i][width - 1] == "O":
                    helper(i, width - 1, ans)

            for i in range(width):
                if board[0][i] == "O":
                    helper(0, i, ans)
                if board[height - 1][i] == "O":
                    helper(height - 1, i, ans)

            for i in range(height):
                for j in range(width):
                    if (i,j) not in ans and board[i][j] == "O":
                        board[i][j] = "X"

