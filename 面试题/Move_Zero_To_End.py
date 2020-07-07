#将数组中0的元素放在后面，其余元素相对位置不变

#思路：类似冒泡排序的做法，从左往右扫描数组，遇到0就和下一个不为0的元素交换
#优化：内层循环长度可以逐步缩短； 如果外层一次循环没有发生一次交换，则提前终止循环

class Solution:
	def move_zero_to_end(self, nums):
		if not nums:
			return nums
		length = len(nums)
		flag = True
		for i in range(length - 1):
			if flag:
				flag = False
				for j in range(length - i - 1):
					if nums[j] == 0 and nums[j + 1]:
						nums[j], nums[j + 1] = nums[j + 1], nums[j]
						flag = True
			else:
				break
		return nums


if __name__ == '__main__':

	example1 = [0,2,4,2,1,5,0,9,1]
	example2 = []
	example3 = [0]
	example4 = [0,0,0]
	example5 = [1,2,3]
	example6 = [0,2,3]
	example7 = [1,2,0]

	print(Solution().move_zero_to_end(example7))
