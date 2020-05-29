class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        return nums

    def reverse(self, array, start, end):
        lenA = end - start + 1
        for i in range(start, start + lenA // 2):
            tmp = array[i]
            array[i] = array[end - (i - start)]
            array[end - (i - start)] = tmp
            
        # while start < end:
        #     tmp = array[start]
        #     array[start] = array[end]
        #     array[end] = tmp            
        #     start += 1
        #     end -= 1
