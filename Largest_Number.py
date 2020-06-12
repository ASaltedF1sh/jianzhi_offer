#反证法证明：按照 's1' + 's2' > 's2' + 's1' 的规律对数组进行排序，然后从大到小组合成的整数一定是最大整数
# 假设排序后，从大到小分别为 [s1, s2, s3, s4, s5]
#若上面的形式组成的整数不是最大，假设由挨着的两个元素顺序翻过来组成的整数更大
#即假设 s1, s3, s2, s4, s5 > s1, s2, s3, s4, s5
#但根据排序规则，显然有s2, s3 > s3, s2，则s1, s2, s3, s4, s5组成的整数更大，与假设矛盾
#假设不是挨着的两个元素，即s3,s2,s1 > s1, s2, s3
#由s1,s2 > s2, s1 --> s1,s2,s3 > s2,s1,s3
#由s1,s3 > s3, s1 --> s2,s1,s3 > s2,s3,s1 
#由s2,s3 > s3, s2 --> s2,s3,s1 > s3,s2,s1
# 综上，可知 s1,s2,s3 > s2,s1,s3 > s2,s3,s1 > s3,s2,s1 与已知矛盾，故假设成立


#利用functools库中的cmp_to_key函数实现两个对象比较
class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        def helper(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        return "".join(sorted(map(str, nums), key=cmp_to_key(helper))).lstrip("0") or "0"

#利用__lt__魔法方法实现两个对象比较
class Solution:
    def largestNumber(self, nums):
        class large_num(str):
            def __lt__(self, other):
                return self + other > other + self
        return "".join(sorted(map(str, nums), key=large_num)).lstrip("0") or "0"
