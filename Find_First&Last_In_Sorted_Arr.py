class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or not len(nums):
            return [-1, -1]
            
        def search_first(start, end, tg):
            while start + 1 < end:
                mid = int(start + (end - start) / 2)
                if nums[mid] == target:
                    if nums[mid - 1] == target:
                        end = mid - 1
                    else:
                        return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            return -1

        def search_last(start, end, tg):
            while start + 1 < end:
                mid = int(start + (end - start) / 2)
                if nums[mid] == target:
                    if nums[mid + 1] == target:
                        start = mid + 1
                    else:
                        return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
            return -1

        s = search_first(0, len(nums) - 1, target)
        e = search_last(0, len(nums) - 1, target)
        return [s, e]
