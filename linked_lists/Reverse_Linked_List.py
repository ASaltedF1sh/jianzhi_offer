#迭代方式
class Solution:
    def reverseList(self, head):
        if not head:
            return head
        dummy = ListNode(None)
        while head:
            tmp = ListNode(head.val)
            tmp.next = dummy.next
            dummy.next = tmp
            head = head.next            
        return dummy.next

#递归方式
class Solution:
    def reverseList(self, head):
        if head == None or head.next == None :
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur

