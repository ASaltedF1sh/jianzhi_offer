class Solution:
    def pacificAtlantic(self, matrix):

        if not len(matrix) or not len(matrix[0]):
            return []
        height = len(matrix)
        width = len(matrix[0])
        pacific = set()
        atlantic = set()
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        def helper(m, n, res):
            res.add((m, n))
            for i, j in zip(dx, dy):
                x = m + i
                y = n + j
                if  0 <= x < height and 0 <= y < width and matrix[x][y] >= matrix[m][n] and (x, y) not in res:
                    helper(x, y, res)

        for i in range(height):
            helper(i, 0, pacific)
            helper(i, width - 1, atlantic)

        for i in range(width):
            helper(0, i, pacific)
            helper(height - 1, i, atlantic)

        return list(pacific & atlantic)
