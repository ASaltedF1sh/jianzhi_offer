# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     self.ans = - float('inf')
    #     def helper(node, h):
    #         self.ans = max(self.ans, h)
    #         if not node:
    #             return
    #         helper(node.left, h + 1)
    #         helper(node.right, h + 1)
    #     helper(root, 0)
    #     return self.ans 

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
