class Solution:
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        count = 0
        ans = 0
        hashmap = {}
        #奇数为0的情况默认就有1种
        hashmap[0] = 1

        for i, num in enumerate(nums):
            if num % 2:
                count += 1
            if hashmap.get(count - k) != None:
                ans += hashmap.get(count - k)
            if not hashmap.get(count):
                hashmap[count] = 1
            else:
                hashmap[count] += 1
        return ans
