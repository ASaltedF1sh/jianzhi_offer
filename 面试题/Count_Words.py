# 对字符串统计字母出现个数，并以字符大小排序，然后以字符+出现次数输出，如[asda],输出[a2d1s1]

class Solution:
    def count(self, nums):
        from collections import Counter
        tmp = Counter(nums).most_common()
        tmp = sorted(tmp, key = lambda x: x[-1])
        ans = ''.join([x[0] + str(x[1]) for x in tmp])
        return ans 

if __name__ == '__main__':

    print(Solution().count('aadfdfjadofjhdfaisdfpawexkfzaei'))
