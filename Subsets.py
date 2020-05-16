#迭代法
class Solution1:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
            print(res)
        return res

#回溯（递归）做法
class Solution2:
    def subsets(self, nums):
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]])
        helper(0, [])
        return res  
