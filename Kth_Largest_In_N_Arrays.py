class Solution:
    def KthInArrays(self, arrays, k):
        import heapq
        list_num = len(arrays)
        hashmap = {}
        head = [0] * list_num
        count = 0

        for i in range(list_num):
            arrays[i] = sorted(arrays[i], reverse = True)
            hashmap[i] = 1
        # print(arrays)
        min_heap = []

        for i in range(list_num):
            if len(arrays[i]):
                heapq.heappush(min_heap, (arrays[i][0], i, 0))
                if head[i] + 1 < len(arrays[i]):
                    head[i] += 1
                else:
                    head[i] = -1
                    hashmap[i] = 0

        while len(min_heap) > k:
            _, array_ind, _ = heapq.heappop(min_heap)
            hashmap[array_ind] = 0
            count += 1

        for j in range(k):
            for i in range(list_num):
                if len(min_heap) < k:
                    if head[i] != -1:
                        heapq.heappush(min_heap, (arrays[i][head[i]], i, head[i]))
                        if head[i] + 1 < len(arrays[i]):
                            head[i] += 1
                        else:
                            head[i] = -1
                            hashmap[i] = 0
                else:
                    if list_num - count > 0:
                        if hashmap[i]:
                            if arrays[i][head[i]] > min_heap[0][0]:
                                _, array_ind, _ = heapq.heappop(min_heap)
                                hashmap[array_ind] = 0
                                count += 1
                                heapq.heappush(min_heap, (arrays[i][head[i]], i, head[i]))
                            elif arrays[i][head[i]] < min_heap[0][0]:
                                array_ind = heapq[0][1]
                                hashmap[array_ind] = 0
                                count += 1
                            if head[i] + 1 < len(arrays[i]):
                                head[i] += 1
                            else:
                                head[i] = -1
                                hashmap[i] = 0
                    else:
                        return min_heap[0][0]
        return min_heap[0][0] 
