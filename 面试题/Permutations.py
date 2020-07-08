class Solution:
    def permute(self, nums):
        ans = []
        def helper(res, tmp):
            if not res:
                ans.append(tmp)
                return
            for k in range(len(res)):
                helper(res[:k] + res[k+1: ], tmp + [res[k]])
        helper(nums, [])
        return ans
