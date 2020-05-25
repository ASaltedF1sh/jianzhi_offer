class Solution:
    def search(self, nums, target):
        if not len(nums):
            return -1
        start = 0
        end = len(nums) - 1
        if target == nums[end]:
            return end

        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if target < nums[-1]:
                    start = mid + 1
                else:
                    if nums[mid] < nums[-1]:
                        end = mid - 1
                    elif nums[mid] > nums[-1]:
                        start = mid + 1
            else:
                if target < nums[-1]:
                    if nums[mid] < nums[-1]:
                        end = mid - 1
                    elif nums[mid] > nums[-1]:
                        start = mid + 1
                else:
                    end = mid - 1

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
