#自下而上，复杂度O(N)
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = 0
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.ans += abs(left - right)
            return left + right + node.val
        helper(root)
        return self.ans
