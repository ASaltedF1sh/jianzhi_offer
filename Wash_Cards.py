import random 

#有n张卡，需要洗n-1次
def shuffle(nums):
    for i in range(len(nums) - 1, 0, -1):
        random_num = random.randint(0, i)
        tmp = nums[i]
        nums[i] = nums[random_num]
        nums[random_num] = tmp
    return nums
