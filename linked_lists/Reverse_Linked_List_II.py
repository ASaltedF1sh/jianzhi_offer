class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(None)
        dummy.next = head
        head, tail = dummy, dummy
        count, len_ = 0, n - m + 1
        #head指向会被reverse的第一个元素的前一个元素
        #tail指向会被reverse的最后一个元素
        while count < n:
            tail = tail.next
            if count < m - 1:
                head = head.next
            count += 1

        #start指向会被reverse的第一个元素
        #end指向会被reverse的最后一个元素的下一个元素
        start, end = head.next, tail.next

        while len_:
            tmp = start.next
            start.next = end
            end = start
            start = tmp
            len_ -= 1
        head.next = tail
        return dummy.next
