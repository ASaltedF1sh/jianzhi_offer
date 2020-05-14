#异或运算有以下三个性质:
#1.任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
#2.任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
#3.异或运算满足交换律和结合律，即 a⊕b⊕a = b⊕a⊕a = b⊕(a⊕a) = b⊕0 = b。

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        base = 0
        for i in range(len(nums)):
            base = base ^ nums[i]
        return base
