#回溯法base版，超时

class Solution:
    def numDistinct(self, s, t):
        self.ans = 0
        self.helper(s, t, 0)
        return self.ans

    def helper(self, s, t, index):

        if index == len(t):
            self.ans += 1
            return
        for i in range(len(s)):
            if s[i] == t[index]:
                self.helper(s[i + 1:], t, index + 1)

#利用 Memoization trick 加快回溯过程，勉强AC
class Solution:
    def numDistinct(self, s, t):
        self.ans = 0
        hashmap = {}
        self.helper(s, t, 0, hashmap)
        return self.ans

    def helper(self, s, t, index, map):

        if index == len(t):
            self.ans += 1
            return
        if s + str(index) in map:
            self.ans += map[s + str(index)]
            return
        for i in range(len(s)):
            if s[i] == t[index]:
                tmp = self.ans
                self.helper(s[i + 1:], t, index + 1, map)
                increment = self.ans - tmp
                map[s[i + 1:] + str(index + 1)] = increment
