from bisect import bisect_left
from typing import List


class Solution:
    # 抄答案的，官方题解，写的真好，我是想不出来，第一次知道bisect_left
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            interval.append(i)
        intervals.sort()

        n = len(intervals)
        ans = [-1] * n
        for _, end, id in intervals:
            i = bisect_left(intervals, [end])
            if i < n:
                ans[id] = intervals[i][2]
        return ans


if __name__ == '__main__':
    s = Solution()
    intervals = [[1, 2]]
    print(s.findRightInterval(intervals))