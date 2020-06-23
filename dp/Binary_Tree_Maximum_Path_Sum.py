class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float('inf')
        def helper(node):
            if not node:
                return 0
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            self.ans = max(self.ans, left + right + node.val)
            return max(left, right) + node.val
        helper(root)
        return self.ans
        
