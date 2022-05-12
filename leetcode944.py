from typing import List

import numpy as np


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        trans = np.array(strs)
        n = len(trans)
        m = len(trans[0])
        res = 0
        for i in range(m):
            for j in range(n - 1):
                if trans[j][i] > trans[j + 1][i]:
                    res += 1
                    break
        return res


if __name__ == '__main__':
    s = Solution()
    strs = ["rrjk", "furt", "guzm"]
    print(s.minDeletionSize(strs))
