#给一个数，输出他的所有质数因子，例如180，输出2，2，3，3，5

class Solution:
    def prime(self, nums):
        if not nums or nums == 1:
            return -1
        ans = []
        for factor in range(2, nums + 1):
            while nums % factor == 0:
                ans.append(factor)
                nums /= factor
        return ans



if __name__ == '__main__':
    example1 = 180
    example1 = 0
    example1 = 1
    example1 = 81
    print(Solution().prime(99999999))
