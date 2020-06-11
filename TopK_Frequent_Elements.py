#时间复杂度 max(O(N), O(KlogN)) < O(NlogN)

class Solution:
    def topKFrequent(self, nums, k):
        hashtable = {}
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        tmp = [[hashtable[num], num] for num in hashtable]
        m = len(tmp)
        heap = self.create_max_heap(tmp, m)
        m ,n = m - 1, k
        while n:
            heap[0], heap[m] = heap[m], heap[0]
            self.ajust_heap(heap, 0, m)
            n -= 1
            m -= 1
        return [num[1] for num in heap[-k: ]]

    def create_max_heap(self, nums, size):
        root_ind = (size - 2) // 2
        for i in range(root_ind, -1, -1):
            self.ajust_heap(nums, i, size)
        return nums

    def ajust_heap(self, nums, root, size):
        l = root * 2 + 1
        r = root * 2 + 2
        max_ind = root
        if l < size and nums[l][0] > nums[max_ind][0]:
            max_ind = l
        if r < size and nums[r][0] > nums[max_ind][0]:
            max_ind = r
        if root != max_ind:
            nums[root], nums[max_ind] = nums[max_ind], nums[root]
            self.ajust_heap(nums, max_ind, size)
