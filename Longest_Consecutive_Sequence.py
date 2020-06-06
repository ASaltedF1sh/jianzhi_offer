class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        hashmap = {}
        ans = 1

        for num in nums:
            if num in hashmap:
                continue
            else:
                if (num - 1 in hashmap) and (num + 1 in hashmap):
                    hashmap[num] = 'a'
                    if hashmap[num + 1] - hashmap[num - 1] + 1 > ans:
                        ans = hashmap[num + 1] - hashmap[num - 1] + 1
                    tmp = hashmap[num - 1]
                    hashmap[hashmap[num - 1]] = hashmap[num + 1]
                    hashmap[hashmap[num + 1]] = tmp

                elif num - 1 in hashmap:
                    tmp = hashmap[num - 1]
                    hashmap[tmp] = num
                    hashmap[num] = tmp

                    if num - tmp + 1 > ans:
                        ans = num - tmp + 1

                elif num + 1 in hashmap:
                    tmp = hashmap[num + 1]
                    hashmap[tmp] = num
                    hashmap[num] = tmp
                    if tmp - num + 1 > ans:
                        ans = tmp - num + 1
                else:
                    hashmap[num] = num
        return ans
