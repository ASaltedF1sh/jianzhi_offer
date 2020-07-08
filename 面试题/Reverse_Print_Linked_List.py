class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans[::-1]
