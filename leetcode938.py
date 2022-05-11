class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.cur = 0

        def dfs(node):
            if node.left:
                dfs(node.left)
            if node.val > high:
                return
            if node.val >= low:
                self.cur += node.val
            if node.right:
                dfs(node.right)

        dfs(root)
        return self.cur


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, right=TreeNode(18)))
    print(s.rangeSumBST(root, 5, 10))
