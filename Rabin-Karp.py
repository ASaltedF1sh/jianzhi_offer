class Solution:
    def rabin_karp(self, source, target):
        if not source or not target:
            return -1
        len_s = len(source)
        len_t = len(target)
        if len_t == 0:
            return 0
        if len_s < len_t:
            return -1

        BASE = 31
        MOD = 19260817
        
        power = 1
        for i in range(len_t):
            power = (power * BASE) % MOD

        targetHash = 0
        for i in range(len_t):
            targetHash = (targetHash * BASE + ord(target[i])) % MOD

        hashcode = 0
        for i in range(len_s):
            hashcode = (hashcode * BASE + ord(source[i])) % MOD
            if i < len_t - 1:
                continue
            if i >= len_t:
                hashcode = (hashcode - power * ord(source[i - len_t])) % MOD
                if hashcode < 0:
                    hashcode = (hashcode + MOD) % MOD
            if hashcode == targetHash:
                if source[i - len_t + 1: i + 1] == target:
                    return i - len_t + 1
        return -1
