class Solution:
    def MoreThanHalfNum_Solution(self, numbers):

        if len(numbers) < 1:
            return 0

        else:
            if len(numbers) & 1:
                order, arr = self.KthInArray(numbers, (len(numbers) + 1) // 2)
            else:
                order, arr =  self.KthInArray(numbers, len(numbers) // 2) 
            if self.exist(order, arr):
                return arr[order]
            else:
                return 0
            
    def exist(self, order, arr):

        count = 0
        for num in arr:
            if num == arr[order]:
                count += 1

        if count > len(arr) / 2.:
            return True
        else:
            return False        

    def KthInArray(self, arr, k):
        if k > len(arr):
            return 0
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
            return order-1, arr

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
