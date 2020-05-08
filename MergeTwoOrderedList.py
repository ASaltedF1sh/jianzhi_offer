# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        else:
            p1 = pHead1
            p2 = pHead2
            new_head = ListNode(None)
            p3 = new_head

            while(p1 != None and p2 != None):
                if p1.val <= p2.val:
                    new_node = ListNode(p1.val)
                    p1 = p1.next
                else:
                    new_node = ListNode(p2.val)
                    p2 = p2.next
                p3.next = new_node
                p3 = p3.next

            if p1 == None:
                while p2 != None:
                    new_node = ListNode(p2.val)
                    p2 = p2.next
                    p3.next = new_node
                    p3 = p3.next                                        
            else:
                while p1 != None:
                    new_node = ListNode(p1.val)
                    p1 = p1.next
                    p3.next = new_node
                    p3 = p3.next

            return new_head.next
