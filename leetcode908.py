from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        max = nums[-1]
        min = nums[0]
        return max - min - 2 * k if max - min - 2 * k > 0 else 0


if __name__ == '__main__':
    nums = [3, 1, 10]
    k = 4
    s = Solution()
    print(s.smallestRangeI(nums, k))
