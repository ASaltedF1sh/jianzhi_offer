# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1 
# 标准的“下一个排列”算法可以描述为：

# 从后向前查找第一个相邻升序的元素对 (i,i+1)，满足 A[i] < A[i+1]。此时 [i+1,end) 必然是降序
# 在 [i+1,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
# 将 A[i] 与 A[k] 交换
# 可以断定这时 [i+1,end) 必然是降序，逆置 [i+1,end)，使其升序
# 如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4


class Solution:

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        #逆序函数
        def reverse(nums, m, n):
            while m < n:
                nums[m], nums[n] = nums[n], nums[m]
                m += 1
                n -= 1

        length = len(nums)
        i = length - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        #不存在下一个更大排列，直接返回逆序
        if i < 0:
            reverse(nums, 0, length - 1)
        else:
            k = length - 1
            while k >= 0:
                if nums[i] < nums[k]:
                    break
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
            reverse(nums, i + 1, length - 1)
