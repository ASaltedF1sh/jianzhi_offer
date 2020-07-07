# 二分查找有序数组，输出目标值最大的坐标(即存在多个目标值，输出最后一个的坐标)
#递归做法

class Solution:
    def bs_last(self, nums, target, left, right):
        if not nums:
            return -1
        l, r = left, right
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                if mid == len(nums) - 1 or nums[mid+1] != target:
                    return mid
                else:
                    return self.bs_last(nums, target, mid + 1, len(nums) - 1)
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        return -1


if __name__ == '__main__':

    example1 = [0,1,2,2,2,2,2,3,4,6,8]
    # example1 = [0,1,2,3,4,6,8]
    # example1 = [0,1,4,6,8]
    # example1 = [2,2,2,2,2,2]
    print(Solution().bs_last(example1, 2, 0, len(example1) - 1))
