#分析出每个元素的作用范围即可，起点应是其出栈后栈中最后一个值+1，如果栈中此时没值则起点为0
#终点应该是代替它入栈的index的前一个位置
#时间空间复杂度都是O（N）

class Solution:
    def sumSubarrayMins(self, A):
        A.append(0)
        stack, length = [], len(A)
        ans = 0
        for i in range(length):
            while stack and A[i] < A[stack[-1]]:
                tmp_ind =  stack.pop()
                if stack:
                    start = stack[-1] + 1
                else:
                    start = 0
                end = i - 1
                ans += (end - tmp_ind + 1) * (tmp_ind - start + 1) * A[tmp_ind]
                ans = ans % 1000000007
            stack.append(i)
        return ans
