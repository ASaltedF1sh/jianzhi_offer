#有重复数的时候时间复杂度最差会退化到O(N)
class Solution:
    def search(self, nums, target):
        if not len(nums):
            return False
        start = 0
        end = len(nums) - 1

        if target == nums[end]:
            return True

        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                if target < nums[-1]:
                    start = mid + 1
                elif target > nums[-1]:
                    if nums[mid] < nums[-1]:
                        end = mid - 1
                    elif nums[mid] > nums[-1]:
                        start = mid + 1
                    else:
                        return self.bf_search(nums, target)
                else:
                    return self.bf_search(nums, target)
            else:
                if target < nums[-1]:
                    if nums[mid] < nums[-1]:
                        end = mid - 1
                    elif nums[mid] > nums[-1]:
                        start = mid + 1
                    else:
                        return self.bf_search(nums, target)
                elif target > nums[-1]:
                    end = mid - 1
                else:
                    return self.bf_search(nums, target)

        if nums[start] == target or nums[end] == target:
            return True
        return False

    def bf_search(self, arr, tg):
        for i, n in enumerate(arr):
            if n == tg:
                return True
        return False
