class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        if k > len(nums):
            self.heap = self.create_min_heap(sorted(self.heap))
        else:
            self.heap = self.create_min_heap(sorted(self.heap))[-k:]

    def add(self, val):
        if len(self.heap) < self.k:
            self.heap.append(val)
            self.ajust_min_heap(self.heap, 0)
            return self.heap[0]
        if val <= self.heap[0]:
            return self.heap[0]
        self.heap[0] = val
        self.ajust_min_heap(self.heap, 0)
        return self.heap[0]

    def ajust_min_heap(self, nums, root_ind):
        length = len(nums)
        left_ind = root_ind * 2 + 1
        right_ind = root_ind * 2 + 2
        min_ind = root_ind
        if left_ind < length and nums[left_ind] < nums[min_ind]:
            min_ind = left_ind
        if right_ind < length and nums[right_ind] < nums[min_ind]:
            min_ind = right_ind
        if min_ind != root_ind:
            nums[root_ind], nums[min_ind] = nums[min_ind], nums[root_ind]
            self.ajust_min_heap(nums, min_ind)

    def create_min_heap(self, nums):
        length = len(nums)
        last_root_ind = (length - 2) // 2
        for i in range(last_root_ind, -1, -1):
            self.ajust_min_heap(nums, i)
        return nums
    
#不使用内置的排序函数，自行初始化堆
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        #正常建立堆的时间是O(n)，一次向下调整堆的时间复杂度是O(log2k)
        self.heap = self.create_min_heap(nums)

    def add(self, val):
        #如果堆中数字还没有k个，则向堆中添加一个元素，此时堆中必定有K个元素
        if len(self.heap) < self.k:
            self.heap.append(val)
            self.ajust_min_heap(self.heap, 0, self.k)
            return self.heap[0]
        #如果val <= self.heap[0]，则第K个值和堆本身不会受到影响，直接返回堆顶的值即可
        if val <= self.heap[0]:
            return self.heap[0]
        #将堆顶元素替换出去，重新整理为小根堆即可
        self.heap[0] = val
        self.ajust_min_heap(self.heap, 0, self.k)
        return self.heap[0]

    def ajust_min_heap(self, nums, root_ind, size):
        left_ind = root_ind * 2 + 1
        right_ind = root_ind * 2 + 2
        min_ind = root_ind
        if left_ind < size and nums[left_ind] < nums[min_ind]:
            min_ind = left_ind
        if right_ind < size and nums[right_ind] < nums[min_ind]:
            min_ind = right_ind
        if min_ind != root_ind:
            nums[root_ind], nums[min_ind] = nums[min_ind], nums[root_ind]
            self.ajust_min_heap(nums, min_ind, size)

    def create_min_heap(self, nums):
        length = len(nums)
        last_root_ind = (length - 2) // 2
        for i in range(last_root_ind, -1, -1):
            self.ajust_min_heap(nums, i, length)
        if length <= self.k:
            return nums
        else:
            tmp = length
            #先将最小的几个数放在堆底部，实际堆中有效数字只剩K个
            for i in range(length - 1, length - self.k, -1):
                nums[0], nums[i] = nums[i], nums[0]
                self.ajust_min_heap(nums, 0, i)
            last_root_ind = (self.k - 2) // 2
            #再次调整为小根堆,堆的初始化完成
            for i in range(last_root_ind, -1, -1):
                self.ajust_min_heap(nums, i, self.k)
            return nums
