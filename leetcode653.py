from pyparsing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root, k):
        s = set()

        def dfs(root):
            if root is None:
                return False
            else:
                if k - root.val in s:
                    return True
                s.add(root.val)
                if dfs(root.left) or dfs(root.right):
                    return True
            return False

        return dfs(root)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, right=TreeNode(7)))
    k = 20
    print(s.findTarget(root, k))
