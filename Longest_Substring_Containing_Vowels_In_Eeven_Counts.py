class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        vowels = 'aeiou'
        hashmap = {}
        hashmap[0] = -1
        state = 0
        ans = 0

        for i, w in enumerate(s):
            if w in vowels:
                state ^= 1 << vowels.index(w)
            if state in hashmap:
                ans = max(ans, i - hashmap[state])
            else:
                hashmap[state] = i
        return ans              
