from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 固定右端点，左端点从i=0开始,每枚举一个右端点j，如果当前子数组乘积prod大于等于
        # k,那么右移左端点，使得当前元素乘积小于k或者i大于j,那么元素乘积小于k的子数组数目为
        # j-i+1
        ans = 0
        prod = 1
        i = 0
        for j, num in enumerate(nums):
            prod *= num
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    print(s.numSubarrayProductLessThanK(nums, k))
