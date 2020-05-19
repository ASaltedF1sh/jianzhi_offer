class Solution1:
    def validPalindrome(self, s):
        lens = len(s)
        if lens <= 2:
            return True

        start = 0
        end = lens - 1
        de_flag = 0

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                if de_flag:
                    return False
                if start + 1 == end or start == end - 1:
                    return True
                elif s[start + 1] == s[end] and s[start + 2] == s[end - 1]:
                    start += 1
                    de_flag = 1
                elif s[end -1] == s[start] and s[end - 2] == s[start + 1]:
                    end -= 1
                    de_flag = 1
                else:
                    return False
                start += 1
                end -= 1

        return True

class Solution2:
    def validPalindrome(self, s):
        lens = len(s)
        if lens <= 2:
            return True
        start = 0
        end = lens - 1

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.is_palindrome(s[start + 1: end + 1]) | self.is_palindrome(s[start: end])

        return True

    def is_palindrome(self, subs):
        start = 0
        end = len(subs) - 1

        while start < end:
            if subs[start] != subs[end]:
                return False
            start += 1
            end -= 1

        return True
