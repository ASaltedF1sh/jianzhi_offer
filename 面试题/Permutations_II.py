#多一个判断即可

class Solution:
    def permuteUnique(self, nums):
        nums = sorted(nums)
        ans = []
        def helper(res, tmp):
            if not res:
                ans.append(tmp)
            for k in range(len(res)):
                if k - 1 >= 0 and res[k - 1] == res[k]:
                    continue
                helper(res[: k] + res[k + 1: ], tmp + [res[k]])
        helper(nums, [])
        return ans
