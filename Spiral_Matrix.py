class Solution:
    def spiralOrder(self, matrix):
        ans = []
        if matrix and len(matrix[0]) == 1:
            for t in matrix:
                ans.append(t[0])
            return ans

        def top(res):
            if res and res[0]:
                ans.extend(res[0])
            return res[1:]
        def right(res):
            if res and res[0]:
                tmp = []
                for row in res:
                    ans.append(row[-1])
                    tmp.append(row[:-1])
                return tmp
        def bottom(res):
            if res:
                ans.extend(reversed(res[-1]))
            return res[:-1]                
        def left(res):
            if res and res[0]:
                tmp = []
                for row in reversed(res):
                    ans.append(row[0])
                    tmp.append(row[1:])
                return list(reversed(tmp))
                
        tmp = matrix
        while tmp:
            tmp = top(tmp)
            if not tmp:
                break
            tmp = right(tmp)
            if not tmp:
                break
            tmp = bottom(tmp)
            if not tmp:
                break
            tmp = left(tmp)
        return ans
