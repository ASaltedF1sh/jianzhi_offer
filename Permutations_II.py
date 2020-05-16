class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums) 
        ans = []

        def helper(nums_, tmp):
            if len(tmp) == n:
                ans.append(tmp)

            for k in range(len(nums_)):
                if k - 1 >= 0 and nums_[k - 1] == nums_[k]:
                    continue
                helper(nums_[: k] + nums_[k + 1: ], tmp + [nums_[k]])

        helper(nums, [])
        return ans
