class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head == None or k <= 0:
            return None
        else:
            p_r = head
            while count != 0 and p_r.next != None:
                p_r = p_r.next
                count -= 1
            if count != 0:
                return None
            else:
                p_l = head
                while p_r.next:
                    p_l = p_l.next
                    p_r = p_r.next
                return p_l
