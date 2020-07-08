#两种情况下返回False：1.有重复数 2.最值之差（0不计入最小值）大于4

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        hashmap = dict()
        max_num, min_num = -float('inf'), float('inf')
        for num in nums:
            if num in hashmap:
                return False
            if num:
                hashmap[num] = 1
                min_num = min(min_num, num)
            max_num = max(max_num, num)
        return max_num - min_num <= 4
