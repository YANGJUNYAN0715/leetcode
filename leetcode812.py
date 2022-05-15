import math
from typing import List


# 感觉还是哪里有点问题，如果在三个点在一条线上时，应该是无法构成三角形的，但我这里还是有答案
def calculateArea(point1: List[int], point2: List[int], point3: List[int]):
    if (point1[1] - point2[1]) * (point3[0] - point2[0]) == (point3[1] - point2[1]) * (point1[0] - point2[0]):
        return 0
    else:
        a = math.sqrt(math.pow(point1[1] - point2[1], 2) + math.pow(point1[0] - point2[0], 2))
        b = math.sqrt(math.pow(point2[1] - point3[1], 2) + math.pow(point2[0] - point3[0], 2))
        c = math.sqrt(math.pow(point3[1] - point1[1], 2) + math.pow(point3[0] - point1[0], 2))
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points) - 2):
            x1 = points[i]
            for j in range(i + 1, len(points) - 1):
                x2 = points[j]
                for k in range(j + 1, len(points)):
                    x3 = points[k]
                    res = max(res,calculateArea(x1, x2, x3))
        return res


if __name__ == '__main__':
    s = Solution()
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(s.largestTriangleArea(points))
