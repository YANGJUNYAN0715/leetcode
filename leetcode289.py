import copy


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 深拷贝浅拷贝，真是头都炸了，算法部分倒是很快就想好了，一直在琢磨怎么深拷贝，还搜了老半天，太蠢了
        n = len(board)
        m = len(board[0])
        res = [[0]*m for _ in range(0,n)]
        for i in range(0, n):
            for j in range(0, m):
                aliveCount = 0
                for x in range(max(i - 1, 0), min(i + 2, n)):
                    for y in range(max(j - 1, 0), min(j + 2, m)):
                        if board[x][y] == 1:
                            if x == i and y == j:
                                continue
                            aliveCount += 1
                if board[i][j] == 1:
                    if aliveCount < 2 or aliveCount > 3:
                        res[i][j] = 0
                    else:
                        res[i][j] = board[i][j]
                elif board[i][j] == 0:
                    if aliveCount == 3:
                        res[i][j] = 1
                    else:
                        res[i][j] = board[i][j]
        return res


if __name__ == '__main__':
    s = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print(s.gameOfLife(board))
