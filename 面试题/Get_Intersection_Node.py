# 给定两个（单向）链表，判定它们是否相交并返回交点。请注意相交的定义基于节点的引用，而不是基于节点的值。换句话说，如果一个链表的第k个节点与另一个链表的第j个节点是同一节点（引用完全相同），则这两个链表相交。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#双指针法：两个指针分别指向两个链表头结点，走完自己的链表接着交换走对方的链表，如果重合则有焦点，且焦点为重合该点
class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return 
        p1 = headA
        p2 = headB
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        return p1

if __name__== "__main__":
    node1 = ListNode(2)
    node2 = ListNode(3)
    node1.next = node2
    print(Solution().getIntersectionNode(node1, node2))
