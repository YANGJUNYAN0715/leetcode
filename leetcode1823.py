from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # d = {}
        # for i in range(0, n):
        #     d[i] = i+1
        # init = 0
        # while n > 1:
        #     L = len(d)
        #     if init + k - 1 > L:
        #         init = (init + k - 1) % L
        #     else:
        #         init = init + k - 1
        #     del d[init]
        #     n -= 1
        # return d
        q = deque(range(1, n + 1))
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q[0]


if __name__ == '__main__':
    n = 6
    k = 5
    s = Solution()
    print(s.findTheWinner(n, k))
