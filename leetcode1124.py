from collections import deque
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        for i in range(len(hours)):
            if hours[i] > 8:
                hours[i] = 1
            else:
                hours[i] = -1
        for i in range(1, len(hours)):
            hours[i] += hours[i - 1]
        hours.insert(0, 0)
        # print(hours)
        q = deque()
        for i in range(len(hours)):
            if not q or hours[q[-1]] > hours[i]:
                q.append(i)
        # print("q=", q)
        ans = 0
        for i in range(len(hours) - 1, -1, -1):
            while q and q[-1] > i:
                q.pop()
            while q and hours[q[-1]] < hours[i]:
                ans = max(ans, i - q[-1])
                q.pop()
        return ans


if __name__ == '__main__':
    s = Solution()
    hours = [6,6,6,9,8,8]
    print(s.longestWPI(hours))
