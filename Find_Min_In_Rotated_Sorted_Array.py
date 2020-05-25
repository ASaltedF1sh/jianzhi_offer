class Solution:
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] < nums[-1]:
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                end = mid - 1
            elif nums[mid] > nums[-1]:
                start = mid + 1
        return min(nums[start], nums[end])
