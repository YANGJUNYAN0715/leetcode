from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 遍历+sort()
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        self.preTraverse(root1, res)
        self.preTraverse(root2, res)
        res.sort()
        return res

    def preTraverse(self, root: TreeNode, list: List[int]):
        if root is not None:
            list.append(root.val)
            self.preTraverse(root.left, list)
            self.preTraverse(root.right, list)


if __name__ == '__main__':
    s = Solution()
    root1 = TreeNode(1, None, TreeNode(8))
    root2 = TreeNode(8, TreeNode(1))
    print(s.getAllElements(root1, root2))
