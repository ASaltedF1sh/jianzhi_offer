#BFS
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

# 思路：尽可能到达最远位置（贪心）。
# 如果能到达某个位置，那一定能到达它前面的所有位置。
# 方法：初始化最远位置为 0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。
# 复杂度：时间复杂度 O(n)，空间复杂度 O(1)。

class Solution:
    def canJump(self, nums):
        n = len(nums)
        if not n:
            return True
        max_len = 0
        for i, num in enumerate(nums):
            #i <= max_len保证当前起跳点是合法的
            if i <= max_len and i + num > max_len:
                max_len = i + num
            if max_len >= n - 1:
                return True
        return False

#第一种动态规划
#dp[i]:能否到达索引为i的点
#取决于能否到达i-1点且i+1至少能跳跃的距离大于1
#时间复杂度O(N ** 2),空间复杂度O(N)
class Solution:
    def canJump(self, nums):
        n = len(nums)
        if not n:
            return True
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                dp[i] = (dp[j] and j + nums[j] >= i)
                if dp[i]:
                    break
        return dp[-1]


# 第二种动态规划
# 如果转化一下题目的思维：dp[i]是从前i个元素最远可以到达哪个下标 加个判断再return
class Solution:
    def canJump(self, nums):
        n = len(nums)
        if not n:
            return True
        dp = [0] * n
        dp[0] = nums[0]
        if dp[0] >= n - 1:
            return True
        for i in range(1, n):
            if dp[i - 1] >= i:
                dp[i] = max(dp[i - 1], i + nums[i])
            else:
                dp[i] = dp[i - 1]
            if dp[i] >= n - 1:
                return True
        return False

