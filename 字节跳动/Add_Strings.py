class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, adv, ans = len(num1) - 1, len(num2) - 1, 0, ''
        while i >= 0 or j >= 0:
            res = 0
            if i >= 0:
                res += int(num1[i])
            if j >= 0:
                res += int(num2[j])
            res += adv
            adv = 0
            if res >= 10:
                res, adv = res - 10, 1
            ans += str(res)
            i, j = i - 1, j - 1
        if adv:
            ans += '1'
        return ''.join(reversed(ans))
