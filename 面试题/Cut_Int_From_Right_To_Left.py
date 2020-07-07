#取一个整数a的从右端的开始4-7位(从1开始)

class Solution:
    def cut(self, nums):
        if not nums:
            return
        nums = list(str(nums))
        if len(nums) < 7:
            return
        nums = nums[-7:-3][::-1]
        return ''.join(nums)


if __name__ == '__main__':

    print(Solution().cut(134578237))
