class Solution:
    def max_head(self, mylist, headsize, root_index):
        left = root_index * 2 + 1
        right = root_index * 2 + 2
        large_index = root_index
        if left < headsize and mylist[left] > mylist[large_index]:
            large_index = left
        if right < headsize and mylist[right] > mylist[large_index]:
            large_index = right
        if large_index != root_index:
            mylist[large_index], mylist[root_index] = mylist[root_index], mylist[large_index]
            self.max_head(mylist, headsize, large_index)
     
    def create_head(self, mylist):
        length = len(mylist)
        max_child_index = (length - 2) // 2
        for i in range(max_child_index, -1, -1):
            self.max_head(mylist, length, i)
     
    def sort(self, mylist):
        create_head(mylist)
        for i in range(len(mylist)-1, -1, -1):
            mylist[0], mylist[i] = mylist[i], mylist[0]
            self.max_head(mylist, i, 0)
 
