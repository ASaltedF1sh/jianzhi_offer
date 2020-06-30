class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in {None, p, q}: 
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
