import numpy as np


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        dis = np.zeros((len(first)+1, len(second)+1))
        for i in range(len(first)+1):
            for j in range(len(second)+1):
                if i == 0:
                    dis[i][j] = j
                elif j == 0:
                    dis[i][j] = i
                else:
                    dis[i][j] = min(dis[i - 1][j - 1] + (0 if first[i - 1] == second[j - 1] else 1), dis[i - 1][j] + 1,
                                    dis[i][j - 1] + 1)
        return True if dis[len(first)][len(second)] == 1 or dis[len(first)][len(second)] == 0 else False


if __name__ == '__main__':
    s = Solution()
    first = "a"
    second = "a"
    print(s.oneEditAway(first, second))
