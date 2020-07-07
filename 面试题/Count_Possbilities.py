# 地下车库三类车：二轮、三轮、四轮共计50辆（每类至少一辆），轮数150，计算有多少种可能

class Solution:
    def helper(self, car_nums, wheel_nums):
        ans = 0
        for x in range(1, 48):
            for y in range(1, 49 - x):
                z = 50 - x - y
                if x * 2 + y * 3 + z * 4 == 150:
                    ans += 1
        return ans 

if __name__ == '__main__':

    print(Solution().helper(50, 150))
