# 按层次从根节点打印二叉树，按照z字型的方式打印，第一层正序打印，第二层逆序打印，第三层正序打印…………


# 思路：用两个栈实现：奇数层压第一个栈，偶数层压第二个栈。打印第一个栈中元素时，在第二个栈中先压该节点的左子节点，
# 后压右子节点；打印第二个栈中元素时，在第一个栈中先压该节点的右子节点，后压左子节点

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tranversal_z(self, root):
        if not root:
            return
        from collections import deque
        stack_odd, stack_even = deque(), deque()
        stack_odd.append(root)

        while stack_odd or stack_odd:
            while stack_odd:
                res = stack_odd.pop()
                print(res.val)
                if res.left:
                    stack_even.append(res.left)
                if res.right:
                    stack_even.append(res.right)
            while stack_even:
                res = stack_even.pop()
                print(res.val)
                if res.right:
                    stack_odd.append(res.right)
                if res.left:
                    stack_odd.append(res.left)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    node4.right = node6
    node5.left = node7
    Solution().tranversal_z(node1)


