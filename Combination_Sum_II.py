class Solution1:
    def combinationSum2(self, nums, target):
        nums = sorted(nums)
        n = len(nums)
        ans = []

        def helper(nums, tmp):
            if sum(tmp) == target:
                ans.append(tmp)
                return
            if sum(tmp) > target:
                return
            for k in range(len(nums)):
                if k-1 >= 0 and nums[k] == nums[k-1]:
                    continue
                helper(nums[k+1:], tmp + [nums[k]])
        helper(nums, [])
        return ans  
