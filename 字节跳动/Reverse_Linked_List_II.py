class Solution(object):
    #写法1
    def reverseBetween(self, head, m, n):
        def reverseN(head, n):
            #不用反转，直接返回
            if n == 1:
                return head
            # 以 head.next 为起点，需要反转剩下的 n - 1 个节点
            #last指向剩下n -1 个节点中前倒一，现在变成正一了，最后要把它返回
            last = reverseN(head.next, n - 1)
            successor = head.next.next 
            # 以head.next为开头的链表已经完成翻转，那么head.next.next正确指向后继节点（即不用反转部分的首节点
            #此时head.next指向他的小弟，前第二，现在应该变成倒二，而head应该变成倒一，所以用倒二指向倒一
            head.next.next = head
            #倒一指向后继节点，完成
            head.next = successor
            return last
        if m == 1:
            #如果从第一个节点开始反转，就等同于直接反转前N个节点
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head


    #写法2
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverseN(head, n):
            if n == 1:
                successor = head.next # 拿到后继节点
                return head, successor
            # 以 head.next 为起点，需要反转剩下的 n - 1 个节点
            last, successor = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = successor
            return last, successor

        if m == 1: # 递归终止条件
            res, _ = reverseN(head, n)
            return res
        # 如果不是第一个，那么以下一个为头结点开始递归，直到触发条件
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head
