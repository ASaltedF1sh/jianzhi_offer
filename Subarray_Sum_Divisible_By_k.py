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
