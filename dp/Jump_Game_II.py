#dp做法1：O(N ** 2),超时
#dp[n]:跳到索引为n的点最少需要跳多少次
class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [0] + [float('inf')] * (n - 1)
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

#dp做法2：
#dp[n]:跳n次最远能到达的距离
#本质还是O(N ** 2)，但是有常数级别的优化
class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        ind = 0
        dp = nums[ind]
        while True:
            if dp >= n - 1:
                return ind + 1
            #在上次最大距离基础上，再跳nums[dp]距离
            tmp = dp + nums[dp]
            #回头找是否有更远的
            for i in range(dp - 1, ind, -1):
                tmp = max(nums[i] + i, tmp)
            dp = tmp
            ind += 1

#贪心：每次选择跳到能跳到更远的位置
class Solution:
    def jump(self, nums):
        n = len(nums)
        #maxPos:保存遍历到当前i时，能到达的最远位置
        #end保存上一个能够到达的最远距离（前最远距离）
        maxPos, end, step = 0, 0, 0
        #不访问最后一个元素
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
