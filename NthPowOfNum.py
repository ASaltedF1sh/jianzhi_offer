class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 :
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x

        temp_n = abs(n)

        k = 0
        temp = 1
        while temp < temp_n:
            k += 1
            temp *= 2
        res1 = temp_n - temp
        res2 = temp_n - temp / 2
        k, res = (k, res1) if abs(res1) < abs(res2) else (k-1, res2)

        result = x
        for i in range(k):
            result *= result

        if n > 0:
            return result / self.myPow(x, abs(res)) if res < 0 else result * self.myPow(x, abs(res))
        else:
            return self.myPow(x, abs(res)) / result if res < 0 else 1. / (result * self.myPow(x, abs(res)))
