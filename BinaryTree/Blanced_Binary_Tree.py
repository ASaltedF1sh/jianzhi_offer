# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自顶向下：有重复，复杂度O (N**2)
#吧当前状态想象为一个只有三个节点的二叉树
#height函数：思考的时候先把他当做一个能返回子树最大深度的函数
#isBalanced函数：递归判断，如果左右子树高度相差大于2，返回False，否则一直递归判断左子树和右子树
class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        return abs(self.height(root.right) - self.height(root.left)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    # 求某个节点下面的最大深度（层数）
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.right), self.height(node.left))

#自下而上：无重复，复杂度O(N)
#自下而上不一定真是从最下面开始，而可能有上往下，再return回来的过程中做有效的判断
class Solution:
    def isBalanced(self, root):
        self.res = True
        def helper(root):
            if not root or not self.res:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if abs(right - left) > 1: 
                self.res = False
            return max(left, right) + 1
        helper(root)
        return self.res
