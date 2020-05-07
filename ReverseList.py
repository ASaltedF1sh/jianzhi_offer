#题目为无头链表

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        else:
            new_head = ListNode(None)
            while pHead != None:
                new_node = ListNode(pHead.val)
                new_node.next = new_head.next
                new_head.next = new_node
                pHead = pHead.next
            return new_head.next
