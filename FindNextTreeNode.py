class Solution:
    def GetNext(self, pNode):
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        else:
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                else:
                    pNode = pNode.next
            return None
