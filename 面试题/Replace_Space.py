class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:
            return s
        return s.replace(' ', '%20')
