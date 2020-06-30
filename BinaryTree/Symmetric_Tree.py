#1.递归法
class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        def helper(s, t):
            if s == None and t == None:
                return True
            if s == None or t == None:
                return False
            if s.val != t.val:
                return False
            return helper(s.left, t.right) and helper(s.right, t.left)
            
        return helper(root.left, root.right)
