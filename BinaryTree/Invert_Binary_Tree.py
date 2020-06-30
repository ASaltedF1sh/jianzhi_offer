class Solution:
    def invertTree(self, root):
        def helper(t):
            if t:
                tmp = t.left
                t.left = t.right
                t.right = tmp
                helper(t.left)
                helper(t.right)
        helper(root)
        return root
