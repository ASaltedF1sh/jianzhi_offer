class Solution:
    def permute(self, nums):
        n = len(nums)
        ans = []

        def helper(i, tmp, ind_list):
            # print(tmp)
            # print(ans)
            if len(tmp) == n:
                ans.append(tmp)
                return
            for k in ind_list:
                tmp_list = ind_list.copy()
                tmp_list.remove(k)
                helper(k, tmp + [nums[k]], tmp_list)
        helper(0, [], list(range(len(nums))))
        
        return ans
