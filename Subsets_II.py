class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []

        def helper(nums_, tmp):
            ans.append(tmp)
            for k in range(len(nums_)):
                if k - 1 >= 0 and nums_[k] == nums_[k - 1]:
                    continue
                helper(nums_[k + 1: ], tmp + [nums_[k]])
                
        helper(nums, [])
        return ans
