class Solution:

    # def minDepth(self, root: TreeNode) -> int:
    #         if not root: return 0
    #         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth(self, root):

        if not root: return 0
        def helper(root):
            if not root: return float("inf")
            if not root.left and not root.right: return 1
            return min(helper(root.left), helper(root.right)) + 1
        return helper(root)
