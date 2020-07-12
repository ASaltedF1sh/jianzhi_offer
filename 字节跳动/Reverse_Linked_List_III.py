# 递归反转链表的倒数K个节点
# 必须先遍历到链表的尾部，才能知道从哪里开始反转


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseLast(self, head, n):
        def reverseBetween(head, m, n):
            def reverseN(head, n):
                if n == 1:
                    return head
                cur = reverseN(head.next, n - 1)
                successor = head.next.next
                head.next.next = head
                head.next = successor
                return cur

            if m == 1:
                return reverseN(head, n)
            head.next = reverseBetween(head.next, m - 1, n - 1)
            return head

        length = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            length += 1
        if n > length:
            return
        return reverseBetween(head, length - n + 1, length)

if __name__ == '__main__':
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    Node3 = ListNode(3)
    Node4 = ListNode(4)
    Node5 = ListNode(5)
    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    Node4.next = Node5

    Node = Solution().reverseLast(Node1, 3)
    while Node:
        print(Node.val)
        Node = Node.next 
