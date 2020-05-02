#方法用于严格递增数列的旋转数列，恒等数列将会返回None

class Solution:
    def minNumberInRotateArray(self, mylist):
        if mylist[0] < mylist[-1]:
            return mylist[0]
        else:
            if len(mylist) == 1:
                return mylist[0]
            elif len(mylist) == 2:
                return mylist[-1]
            else:
                half_ind = len(mylist) // 2
                list1 = mylist[:half_ind]
                list2 = mylist[half_ind:]
                if self.if_order(list1) and not self.if_order(list2):
                    return self.minNumberInRotateArray(list2)
                elif self.if_order(list2) and not self.if_order(list1):
                    return self.minNumberInRotateArray(list1)
                else:
                    if list1[-1] < list2[0]:
                        return self.minNumberInRotateArray(list1)
                    elif list1[-1] > list2[0]:
                        return self.minNumberInRotateArray(list2)
                    else:
                        for i, j in zip(list1[:-1][::-1], list2[1:]):
                            if i < j:
                                target_list = list1
                                break
                            elif i > j:
                                target_list = list2
                                break
                            else:
                                target_list = None
                                break
                        if target_list is not None:
                            return self.minNumberInRotateArray(target_list)
                        else:
                            return target_list
                        
    def if_order(self, list_):
        if list_[0] <= list_[-1]:
            return True
        else:
            return False
