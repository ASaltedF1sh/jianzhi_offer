class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack, length = [], len(heights)
        ans = 0

        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:
                remove_ind = stack.pop(-1)
                ans = max(ans, heights[remove_ind] * ((i - stack[-1] - 1) if stack else i))
            stack.append(i)
        return ans
