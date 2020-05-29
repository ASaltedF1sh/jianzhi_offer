class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                self.reverse(nums, 0, i)
                self.reverse(nums, i + 1, len(nums) - 1)
                self.reverse(nums, 0, len(nums) - 1)
                return nums

    def reverse(self, array, start, end):

        lenA = end - start + 1

        for i in range(start, start + lenA // 2):
            tmp = array[i]
            array[i] = array[end - (i - start)]
            array[end - (i - start)] = tmp

if __name__ == '__main__':

    print(Solution().rotate([6,8,9,1,2]))
