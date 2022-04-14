class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.leng = len(arr)

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return self.leng


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        leng = mountain_arr.length()
        topindex = self.findMountTopindex(mountain_arr, 0, leng - 1)
        minl = self.findTargetLeft(target, mountain_arr, 0, topindex)
        return minl if minl != -1 else self.findTargetRight(target, mountain_arr, topindex + 1, leng - 1)

    def findMountTopindex(self, mountain_arr, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                right = mid
            else:
                left = mid + 1
        return left

    def findTargetLeft(self, target, mountain_arr, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        return -1 if mountain_arr.get(left) != target else left

    def findTargetRight(self, target, mountain_arr, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) <= target:
                right = mid
            else:
                left = mid + 1
        return -1 if mountain_arr.get(left) != target else left


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 3, 1]
    mountain_arr = MountainArray(arr)
    target = 3
    solution = Solution()
    ans = solution.findInMountainArray(target, mountain_arr)
    print(ans)
