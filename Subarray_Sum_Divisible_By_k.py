#同余数的性质：
# 1.反身性：a≡a (mod m)；
# 2.对称性：若a≡b(mod m)，则b≡a (mod m)；
# 3.传递性：若a≡b(mod m)，b≡c(mod m)，则a≡c(mod m)；
# 4.同余式相加：若a≡b(mod m)，c≡d(mod m)，则a  c≡b  d(mod m)；
# 5.同余式相乘：若a≡b(mod m)，c≡d(mod m)，则ac≡bd(mod m)。

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        hashmap = {}
        hashmap[0] = 1
        ans = 0
        tmp = 0

        for i in range(len(A)):
            tmp = (A[i] + tmp) % K
            if tmp < 0:
                tmp += K
            if tmp in hashmap:
                ans += hashmap[tmp]
                hashmap[tmp] += 1
            else:
                hashmap[tmp] = 1
        return ans
