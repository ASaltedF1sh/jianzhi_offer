class Solution:
    def TrappingRainWater_Solution(self, pillar_list):
        list_len = len(pillar_list)
        if list_len <= 2:
            return 0
        else:
            func = lambda x, y, z : min(max(x), max(y)) - z if min(max(x), max(y)) - z > 0 else 0
            pillar_count = 0
            for i in range(1, len(pillar_list) - 1):
                pillar_count += func(pillar_list[:i], pillar_list[i+1:], pillar_list[i])
        return pillar_count
