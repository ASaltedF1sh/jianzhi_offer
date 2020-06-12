#显然要用单减栈

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, length = [], len(T)
        ans = [0 for _ in range(length)]
        for i in range(length):
            while stack and T[i] > T[stack[-1]]:
                tmp_ind = stack.pop()
                ans[tmp_ind] = i - tmp_ind
            stack.append(i)
        return ans 
