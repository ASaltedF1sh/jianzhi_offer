class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) < 0:
            return 0
        else:
            max_num = 0
            new_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 0:
                        new_matrix[i][j] = 0
                    else:
                        if i * j:
                            new_matrix[i][j] = min(new_matrix[i-1][j], new_matrix[i-1][j-1], new_matrix[i][j-1]) + 1
                        else:
                            new_matrix[i][j] = 1

            count = 0
            for i in range(len(new_matrix)):
                for j in range(len(new_matrix[0])):
                    count += new_matrix[i][j]
            return count
