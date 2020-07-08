# 输入: 5
# 输出:
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        ans = [[1 for _ in range(k)] for k in range(1, numRows + 1)]
        if numRows == 1 or numRows == 2:
            return ans
        for i in range(1, numRows):
            for j in range(1, len(ans[i]) - 1):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        return ans
