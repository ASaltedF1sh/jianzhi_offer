class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = []
        queue.append(root)
        while queue != []:
            size = len(queue)
            cur = []
            for i in range(size):
                node = queue[0]
                cur.append(node.val)
                queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(cur)

        return ans 
