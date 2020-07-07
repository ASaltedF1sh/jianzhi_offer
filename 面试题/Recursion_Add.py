# 1+2+3+...+n求和递归方法

class Solution:
    def add(self, nums, res):
        return res if not nums else self.add(nums[1:], res + nums[0])

if __name__ == '__main__':
    example1 = [0,1,2,2,2,2,2,3,4,6,8]
    example1 = [0]
    example1 = [8,8,8]
    example1 = [2,2,2,2,2,2,1]
    print(Solution().add(example1, 0))
