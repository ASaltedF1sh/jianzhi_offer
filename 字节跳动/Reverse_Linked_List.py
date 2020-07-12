class Solution:
    def reverseList(self, head):
        if head == None or head.next == None :
            return head
        #递归要义:只看当前层次，cur是将head后面所有链表翻转过后返回的头结点，现在要把head续在后面
        cur = self.reverseList(head.next)
        head.next.next = head
        #切断next原来指向的那个节点
        head.next = None
        return cur
