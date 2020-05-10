class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#前序遍历
def preOrderNonRecursion(root):
    if root == None:
        return None

    stack = []
    stack.append(root)
    while stack:
        node = stack.pop(-1)
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

#中序遍历
def inOrderNonRecursion(root):
    if root == None:
        return None

    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop(-1)
        print(root.val)
        root = root.right

#后序遍历使用两个栈
def postOrderNonRecursion(root):
    if root == None:
        return None
    else:
        s1 = []
        s2 = []
        s1.append(root)
        while s1:
            node = s1.pop(-1)
            s2.append(node)
            if node.left :
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            print(s2.pop(-1).val)
            
#后序遍历使用一个栈
def postOrderNonRecursion1(root):
    if root == None:
        return
    else:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left if root.left else root.right
            root = stack.pop(-1)
            print(root.val)
            if stack and stack[-1].left == root:
                root = stack[-1].right
            else:
                root = None      
