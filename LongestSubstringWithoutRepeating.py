class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hashmap = [ 0 for _ in range(256)]

        length = 0
        j = 0
        for i in range(len(s)):
            while j < len(s) and hashmap[ord(s[j])] == 0:
                hashmap[ord(s[j])] = 1
                length = max(length, j - i + 1)
                j += 1
            hashmap[ord(s[i])] = 0

        return length
