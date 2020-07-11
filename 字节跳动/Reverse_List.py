class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if len(s) == 0:
            return 
        tmp = s[0]
        del s[0]
        self.reverseString(s)
        s.append(tmp)
