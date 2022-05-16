class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res = []

        # 二叉树的中序遍历
        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            res.append(root)
            inorder(root.right)

        inorder(root)

        for i in range(len(res)):
            if i == len(res) - 1:
                return None
            if res[i] == p:
                return res[i + 1]


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    p = 6
    print(s.inorderSuccessor(root, root.left))
