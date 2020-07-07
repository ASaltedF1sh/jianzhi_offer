#新建数组
class Solution:
    def exchange(self, nums):
        if not nums:
            return nums
        odd = []
        even = []

        for num in nums:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)
        odd.extend(even)
        return odd

#首尾指针
    def exchange(self, nums):
        if not nums:
            return nums
        l = 0
        r = len(nums) - 1
        while l < r:
            #如果l指向奇
            if nums[l] & 1:
                l += 1
                continue
            #如果r指向偶
            if not nums[r] & 1:
                r -= 1
                continue
            #如果l指向偶，r指向奇，二者交换即可
            nums[l], nums[r] = nums[r], nums[l]

        return nums               
