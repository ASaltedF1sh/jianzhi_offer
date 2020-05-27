class Solution:
    def findDuplicate(self, nums):
        #起始搜索范围是1 ~ n
        start = 1
        end = len(nums) - 1
        while start < end:
            #二分之
            mid = int(start + (end - start) / 2)
            count = 0
            for num in nums:
                # 遍历统计知start ~ mid范围内共有count个数
                if start <= num <= mid:
                    count += 1
                #易知start ~ mid范围内最多能容纳mid - start + 1个不重复的数
            if count <= mid - start + 1:
                #此时显然start ~ mid内没有重复数，转而搜索mid + 1 ~ end范围
                start = mid + 1
            else:
                #继续在start ~ mid范围内二分搜索
                end = mid
        return start
