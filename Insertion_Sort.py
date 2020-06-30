#二分法加速插入排序的搜索过程
def insertionSort(nums):  
    for i in range(1, len(nums)): 
        key = nums[i]
        start, end = 0, i - 1
        tmp, mid = -1, -1
        #对两种特殊情况作判断，减少后面的判断逻辑
        if nums[i - 1] <= key:
            continue
        if key < nums[0]:
            nums[1: i + 1], nums[0] = nums[: i], key
            continue
        else:
            while start + 1 < end:
                mid = start + (end - start) // 2
                if nums[mid] < key:
                    start = mid
                elif nums[mid] > key:
                    end = mid
                else:
                    tmp = mid + 1
                    for j in range(mid + 1, i):
                        if nums[j] == key:
                            tmp == j + 1
                        else:
                            break
                    break
        if tmp == i:
            continue
        if tmp == -1:
            tmp = end
        nums[tmp + 1: i + 1], nums[tmp] = nums[tmp: i], key
    return nums
