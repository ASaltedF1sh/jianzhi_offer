class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#前中后序指的是遍历到根节点时的次序
def preOrderRecursion(root):
    if root == None:
        return None
    print(root.val, end=' ')
    preOrderRecursion(root.left)
    preOrderRecursion(root.right)

def inOrderRecursion(root):
    if root == None:
        return None
    inOrderRecursion(root.left)
    print(root.val, end=' ')
    inOrderRecursion(root.right)

def postOrderRecursion(root):
    if root == None:
        return None    
    postOrderRecursion(root.left)
    postOrderRecursion(root.right)
    print(root.val, end=' ')
