#DP
class Solution1:
    def maxProduct(self, nums):
        n = len(nums)
        dpMax = [1 for _ in range(n)]
        dpMin = [1 for _ in range(n)]
        ans = - float('inf')
        for i in range(n):
            dpMax[i] = max(dpMax[i-1] * nums[i], nums[i], dpMin[i-1] * nums[i])
            dpMin[i] = min(dpMax[i-1] * nums[i], nums[i], dpMin[i-1] * nums[i])
            ans = max(ans, dpMax[i])
        return ans

class Solution2:
    def maxProduct(self, nums):
        ans = - float('inf')
        max_num = 1
        min_num = 1
        for num in nums:
            if num < 0:
                max_num, min_num = min_num, max_num
            max_num = max(num, max_num * num)
            min_num = min(num, min_num * num)
            ans = max(ans, max_num)
        return ans
