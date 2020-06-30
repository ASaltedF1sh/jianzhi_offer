# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):

        if not nums:
            return
        tmp, ind = -float('inf'), -1
        for i, num in enumerate(nums):
            if tmp < num:
                tmp = num
                ind = i
        node = TreeNode(tmp)
        node.left = self.constructMaximumBinaryTree(nums[: ind])
        node.right = self.constructMaximumBinaryTree(nums[ind + 1: ])

        return node
