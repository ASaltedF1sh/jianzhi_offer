class Solution:
    def minSubArrayLen(self, s, nums):
        if not s or not nums:
            return 0
        len_t = len(nums)

        j = 0
        sub_sum = 0
        ans = float("inf")

        for i in range(len_t):
            while(j < len_t and sub_sum < s):
                sub_sum += nums[j]
                j += 1
            if sub_sum >= s:
                ans = min(ans, j - i)
            sub_sum -= nums[i]

        if ans == float('inf'):
            return 0
        return ans
