class Solution:
    def reversePrint(self, string):
        if not string:
            return string
        return ' '.join(string.split(' ')[::-1])

if __name__== "__main__":
    print(Solution().reversePrint('wsnd hjyz'))
