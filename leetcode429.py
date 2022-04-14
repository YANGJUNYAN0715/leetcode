"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, *children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if root is None:
            return []
        ans = list()
        q = deque([root])

        while q:
            cnt = len(q)
            level = list()
            for _ in range(cnt):
                cur = q.popleft()
                level.append(cur.val)
                for child in cur.children:
                    q.append(child)
            ans.append(level)
        return ans


if __name__ == '__main__':
    s = Solution()
    root = Node(1, Node(3,Node(5),Node(6)),Node(2),Node(4))
    print(s.levelOrder(root))
