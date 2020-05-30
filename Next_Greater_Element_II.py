class Solution:
    def nextGreaterElement(self, nums):

        stack, length = [], len(nums)
        ans = [-1 for _ in range(length)]

        for i in range(length * 2):
            while stack and nums[i % length] > nums[stack[-1]]:
                ans[stack.pop(-1)] = nums[i % length]
            stack.append(i % length)

        return ans

