# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(t):
            if t:
                tmp = t.left
                t.left = t.right
                t.right = tmp
                helper(t.left)
                helper(t.right)

        helper(root)

        return root
