class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) <= 0:
            return None
        else:
            max_sum = 0
            i = 0
            count_temp = 0

            while i < len(array):
                count_temp += array[i]
                if max_sum < count_temp:
                    max_sum = count_temp
                if count_temp < 0:
                    count_temp = 0
                i += 1

            if max_sum>= 0:
                return max_sum
            else:
                return -1
