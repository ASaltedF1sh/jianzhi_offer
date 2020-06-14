class Solution:
    def findBestValue(self, arr, target):
        if sum(arr) < target:
            return max(arr)
        start, end = 0, max(arr)
        while start + 1 < end:
            mid = start + (end - start) // 2
            total = sum([mid if x > mid else x for x in arr])
            if total < target:
                start = mid
            elif total > target:
                end = mid
            else:
                return mid
        if abs(sum([start if x > start else x for x in arr ]) - target) <= abs(sum([end if x > end else x for x in arr]) - target):
            return start
        else:
            return end
