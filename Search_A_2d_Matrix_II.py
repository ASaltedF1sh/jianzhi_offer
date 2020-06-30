class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False 
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1

        while 0 <= i < row and 0 <= j < col:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
