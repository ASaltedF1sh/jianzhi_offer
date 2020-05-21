#BFS 超时
class Solution:
    def canJump(self, nums):
        n = len(nums)
        if not n:
            return true
        from collections import deque
        stack = deque()
        stack.append([0, nums[0]])
        s = set()
        s.add(0)

        while len(stack):
            print(len(stack))
            cur_num = stack.pop()
            max_len = cur_num[1]
            for i in range(max_len + 1):
                if i + cur_num[0] == n - 1:
                    return True
                elif i + cur_num[0] < n - 1:
                    if i + cur_num[0] not in s:
                        stack.append([i + cur_num[0], nums[i + cur_num[0]]])
                        s.add(i + cur_num[0])
        return False

#贪心
class Solution:
    def canJump(self, nums):
        n = len(nums)
        if not n:
            return True
        max_len = 0
        for i, num in enumerate(nums):
            if i <= max_len and i + num > max_len:
                max_len = i + num
            if max_len >= n - 1:
                return True
        return False
