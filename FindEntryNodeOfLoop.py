class Solution:
    def EntryNodeOfLoop(self, pHead):
        #最少有三个有效结点才能成环
        if not pHead or not pHead.next or not pHead.next.next:
            return None

        else:
            p_fast = pHead.next.next
            p_slow = pHead
            
            #判断是否成环
            while p_fast != p_slow:
                p_fast = p_fast.next.next
                p_slow = p_slow.next
            #不成环
            if p_fast == p_slow == None:
                return None
            #成环，先计算环的结点数
            else:
                loop_node_nums = 1
                while p_fast.next.next != p_slow.next:
                    p_fast = p_fast.next.next
                    p_slow = p_slow.next
                    loop_node_nums += 1

                p_slow = pHead
                p_fast = pHead

                for i in range(loop_node_nums):
                    p_fast = p_fast.next

                while p_slow != p_fast:
                    p_slow = p_slow.next
                    p_fast = p_fast.next

                return p_slow
    

    def EntryNodeOfLoop2(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        else:
            p_fast = pHead.next.next
            p_slow = pHead.next
            
            while p_fast != p_slow:
                if p_fast.next.next != None and p_slow.next != None:
                    p_fast = p_fast.next.next
                    p_slow = p_slow.next
                else:
                    return None
    #简化做法，推导可知当fast以slow两倍速前进，二者首次在环内相遇时
    #slow前进的距离恰好为环内长度，因此此时再重置p_fast以单位速度从头出发
    #当二者再次相遇时恰好会在入口结点的位置
            p_fast = pHead

            while p_slow != p_fast:
                p_slow = p_slow.next
                p_fast = p_fast.next

            return p_slow
                
