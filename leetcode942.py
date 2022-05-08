from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low = 0
        high = n = len(s)
        perm = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = low
                low += 1
            else:
                perm[i] = high
                high -= 1
        perm[n] = high  # 最后剩下一个数，此时 low == high
        return perm


if __name__ == '__main__':
    solution = Solution()
    s = "IDID"
    print(solution.diStringMatch(s))
