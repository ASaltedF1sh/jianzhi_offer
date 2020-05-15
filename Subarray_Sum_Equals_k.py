class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
            
        count = 0
        hashset = {}
        hashset[0] = 1
        sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]
            if hashset.get(sum_ - k) != None:
                count += hashset[sum_ - k]
            if hashset.get(sum_) == None:
                hashset[sum_] = 1
            else:
                hashset[sum_] += 1

        return count
