class Solution:
    def quick_sort(self, mylist, start, end):
        if start >= end:
            return
        hole_index = start + (end - start) // 2
        base = mylist[hole_index]
        low = start
        high = end

        while low < high:
            while hole_index < high and base <= mylist[high]:
                high -=1
            if base > mylist[high]:
                mylist[hole_index] = mylist[high]
                hole_index = high

            while low < hole_index and base >= mylist[low] :
                low +=1
            if base < mylist[low]:
                mylist[hole_index] = mylist[low]
                hole_index = low

        mylist[low] = base
        self.quick_sort(mylist, start, low - 1)
        self.quick_sort(mylist, low + 1, end)
