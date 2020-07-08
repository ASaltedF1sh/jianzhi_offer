# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        cur1, cur2 = dummy, head
        while cur2:
            if cur2.val == val:
                cur1.next = cur2.next
                return dummy.next
            cur1, cur2 = cur1.next, cur2.next
        return dummy.next
