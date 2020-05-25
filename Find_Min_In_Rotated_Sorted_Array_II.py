#当数组中有重复数字时，时间复杂度退化为O(N)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] < nums[-1]:
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                elif nums[mid] == nums[mid - 1]:
                    return self.bf_search(nums)
                else:
                    end = mid - 1
            elif nums[mid] > nums[-1]:
                start = mid + 1
            else:
                return self.bf_search(nums)
        return min(nums[start], nums[end])

    def bf_search(self, arr):
        ans = float('inf')
        for n in arr:
            if n < ans:
                ans = n
        return ans
