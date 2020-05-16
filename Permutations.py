class Solution1:
    def permute(self, nums):
        n = len(nums)
        ans = []

        def helper(i, tmp, ind_list):
            if len(tmp) == n:
                ans.append(tmp)
                return
            for k in ind_list:
                tmp_list = ind_list.copy()
                tmp_list.remove(k)
                helper(k, tmp + [nums[k]], tmp_list)
        helper(0, [], list(range(len(nums))))
        
        return ans
  
#通过优化传参方式降低了空间复杂度
class Solution2:
    def permute(self, nums):   
        n = len(nums)
        ans = []

        def helper(nums_, tmp):
            if not nums_:
                ans.append(tmp)
                return
            for k in range(len(nums_)):
                helper(nums_[:k] + nums_[k+1:], tmp + [nums_[k]])
        helper(nums, [])
        return ans

 
