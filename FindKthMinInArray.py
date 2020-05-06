class Solution:
    def KthInArray(self, arr, k):
        if k > len(arr):
            return None
        else:
            start = 0
            end = len(arr) - 1

            while start <= end:
                mid = start + (end - start) // 2
                order, arr = self.partion(arr, start, mid, end)
                if order > k:
                    end = order - 2
                elif order < k:
                    start = order
                else:
                    break
            return arr[order-1]

    def partion(self, myarr, start, mid, end):

        base = myarr[mid]
        low = start
        high = end

        while low < high:
            while mid < high and base <= myarr[high]:
                high -= 1
            if base > myarr[high]:
                myarr[mid] = myarr[high]
                mid = high

            while low < mid and base >= myarr[low] :
                low += 1
            if base < myarr[low]:
                myarr[mid] = myarr[low]
                mid = low

        myarr[low] = base

        return low + 1, myarr
