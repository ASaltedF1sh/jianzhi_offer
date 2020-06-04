class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return nums
        length = len(nums)
        if length == 1:
            return [0]
        prefix = [1] * length
        suffix = [1] * length

        for i in range(length):
            j = length - 1 - i
            if i == 0:
                left = 1
                right = 1
                continue
            left *= nums[i - 1]
            right *= nums[j + 1]
            prefix[i] = left
            suffix[j] = right
        return [suffix[i] * prefix[i] for i in range(length)]

#优化
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        ans = [0] * length
        k = 1
        for i in range(length):
            ans[i] = k
            k = k * nums[i]
        k = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= k
            k *= nums[i]
        return ans
