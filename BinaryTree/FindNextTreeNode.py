class Solution:
    def GetNext(self, pNode):
        #如果有右孩子
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p

        #如果没有右孩子
        else:
            #必须存在父节点
            while pNode.next:
                #如果当前节点正是父节点的左孩子
                if pNode.next.left == pNode:
                    #父节点就是下一个遍历的对象
                    return pNode.next
                else:
                    #不是的话要继续往上找
                    pNode = pNode.next
            return None
