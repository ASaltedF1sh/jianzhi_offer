# 使用递归找到数组中的最大值

class Solution:
    def search(self, nums, maximum):
    	if not nums:
    		return maximum
    	maximum = max(nums[0], maximum)
    	return self.search(nums[1:], maximum)


if __name__ == '__main__':
    example1 = [0,1,2,2,2,2,2,3,4,6,8]
    example1 = [0]
    example1 = [8,8,8]
    example1 = [2,2,2,2,2,2,1]
    print(Solution().search(example1, - float('inf')))
