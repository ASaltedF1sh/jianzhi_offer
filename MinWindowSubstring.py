class Solution:
    def minWindow(self, s: str, t: str) -> str:

        len_s = len(s)
        len_t = len(t)

        hash_s = [ 0 for _ in range(256)]
        hash_t = [ 0 for _ in range(256)]
        for i in range(len_t):
            hash_t[ord(t[i])] += 1

        ans = float('inf')
        minstr = ''
        j = 0

        for i in range(len_s):

            while not self.contains(hash_s, hash_t) and j < len_s:
                hash_s[ord(s[j])] += 1
                j += 1

            if self.contains(hash_s, hash_t):
                minstr = s[i: j] if ans > len(s[i: j]) else minstr
                ans = len(s[i: j]) if ans > len(s[i: j]) else ans
            hash_s[ord(s[i])] -= 1
        return minstr

    def contains(self, s, t):
        for i in range(len(t)):
            if t[i] > s[i]:
                return False
        return True

if __name__ == '__main__':

    print(Solution().minWindow("cabwefgewcwaefgcf", "cae"))
