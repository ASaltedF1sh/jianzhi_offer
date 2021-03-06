class Solution:
    def cutRope(self, number):

        if number <=1:
            return 0
        elif number == 2:
            return 1
        elif number == 3:
            return 2
        else:
            import math
            result = [1] * number
            result[1] = 2
            result[2] = 3

            for i in range(3, number):
                result[i] = max([result[i-m] * result[m-1] for m in list(range(1, (math.ceil(i/2) + 1)))])
            return result[-1]
