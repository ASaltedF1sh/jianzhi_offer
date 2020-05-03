class Solution:
	def GetUglyNumber_Solution(self, index):

		if index <= 0:
			return 0
		else:
			ugly_list = [1] * index
			ugly2 = 0
			ugly3 = 0
			ugly5 = 0

			for i in range(1, index):
				min_num = min(ugly_list[ugly2] * 2, ugly_list[ugly3] * 3, ugly_list[ugly5] * 5)
				if min_num == ugly_list[ugly2] * 2:
					ugly2 += 1
				if min_num == ugly_list[ugly3] * 3:
					ugly3 += 1
				if min_num == ugly_list[ugly5] * 5:
					ugly5 += 1

				ugly_list[i] = min_num

			return ugly_list[-1]
