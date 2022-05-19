from typing import List


class Solution:
    # 小学奥数题
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        while n > 1:
            res += (max(nums) - min(nums))
            nums.remove(max(nums))
            nums.remove(min(nums))
            n -= 2
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.minMoves2(nums))
