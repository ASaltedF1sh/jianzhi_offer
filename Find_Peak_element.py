class Solution:
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            print('mid',mid)
            #为峰值
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]: 
                return mid
            #递增
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]: 
                start = mid + 1
            #递减
            elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
                end = mid - 1
            #谷值，往左往右都有峰值
            else:
                start = mid + 1
                
        #start和end相邻，二者大者为峰值
        if nums[start] < nums[end]:
            return end
        else:
            return start


#对情况进行化简
class Solution:
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            #比左值小，左边一定有峰值
            if nums[mid] < nums[mid - 1]: 
                end = mid - 1
            #比右值小，右边一定有峰值
            elif nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                return mid
        if nums[start] < nums[end]:
            return end
        else:
            return start
