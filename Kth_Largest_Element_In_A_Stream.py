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
