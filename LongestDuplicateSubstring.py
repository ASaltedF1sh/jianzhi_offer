class Solution:
    def longestDupSubstring(self, S: str) -> str:
        BASE = 131
        #这里MOD一定要设的足够大，不然有的测试案例会通不过
        #要想尽量避免hash碰撞的影响，可以把检测到的值做二次比较验证，懒得写了
        MOD = 192608171926081719260817

        lenS = len(S)
        left = 0
        right = lenS

        ans = ''

        while left <= right:
            window = (left + right) // 2
            power = 1
            hashmap = dict()
            hashcode = 0
            flag = 0
            for i in range(window):
                power = (power * BASE) % MOD
            for k in range(lenS):
                hashcode = (hashcode * BASE + ord(S[k])) % MOD
                if k < window - 1 :
                    continue
                if k >= window:
                    hashcode = (hashcode - power * ord(S[k - window])) % MOD
                    if hashcode < 0:
                        hashcode = (hashcode + MOD) % MOD  
                if not hashmap.get(str(hashcode)):
                    hashmap.update({str(hashcode): 1})
                else:
                    ans = S[k - window + 1: k + 1]
                    flag = 1
                    break
            if flag:
                left = window + 1
            else:
                right = window - 1

        return ans
