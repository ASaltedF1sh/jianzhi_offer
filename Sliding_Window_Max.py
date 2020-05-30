class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        stack, length = [], len(nums)
        ans = [0 for _ in range(length - k + 1)]
        for i in range(length):
            if stack:
                if i - stack[0] == k:
                    stack.pop(0)
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop(-1)
            tmp = nums[i] if not stack else nums[stack[0]]
            if i >= k - 1:
                ans[i - k + 1] = tmp
            stack.append(i)

        return ans
