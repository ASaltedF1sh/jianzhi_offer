#用栈
class Solution1:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k 
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            if count: 
                p.next = head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = tmp
            head = tmp
        return dummy.next

# 递归
class Solution2:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur   
        return head

#class Solution:
#     def reverseKGroup(self, head, k):

#         if k == 1:
#             return head

#         count = 0
#         new_head = ListNode(None)

#         while head:
#             count += 1
#             if count == 1:
#                 h_node = ListNode(None)
#                 node = ListNode(head.val)
#                 node.next = h_node.next
#                 h_node.next = node

#                 node_ = ListNode(head.val)
#                 new_head.next = node_
#                 end = node_

#             elif count % k == 1:
#                 h_node = ListNode(None)
#                 node = ListNode(head.val)
#                 node.next = h_node.next
#                 h_node.next = node

#                 node_ = ListNode(head.val)
#                 next_start.next = node_
#                 end = node_

#             elif count % k != 0:
#                 node = ListNode(head.val)
#                 node.next = h_node.next
#                 h_node.next = node

#                 node_ = ListNode(head.val)
#                 end.next = node_
#                 end = node_

#             elif count == k:
#                 node = ListNode(head.val)
#                 node.next = h_node.next
#                 new_head.next = node
#                 end = new_head
#                 while(end.next):
#                     end = end.next
#                 next_start = end
                
#             elif count % k == 0:
#                 node = ListNode(head.val)
#                 node.next = h_node.next
#                 next_start.next = node
#                 end = next_start   
#                 while(end.next):
#                     end = end.next
#                 next_start = end

#             head = head.next
#         return new_head.next
