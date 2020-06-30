class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float('inf')
        def helper(node):
            if not node:
                return 0
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            #更新全局变量，由上面两个max可知，若某条路径的贡献小于0，压根就不用考虑
            self.ans = max(self.ans, left + right + node.val)
            #return的是从根节点往左，从根节点往左两条路径中大的那条
            return max(left, right) + node.val
        helper(root)
        return self.ans
        
