class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        n = len(nums)
        ans = []

        def helper(i, tmp):
            if sum(tmp) == target:
                ans.append(tmp)
                return
            if sum(tmp) > target:
                return
            for k in range(i, n):
                helper(k, tmp + [nums[k]])
        helper(0, [])

        return ans  
