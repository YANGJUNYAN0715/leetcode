class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res, left, right = [0] * n, 0, n - 1
        for num in nums:
            if num % 2 == 0:
                res[left] = num
                left += 1
            else:
                res[right] = num
                right -= 1
        return res


if __name__ == '__main__':
    nums = [3, 1, 2, 4]
    s = Solution()
    print(s.sortArrayByParity(nums))
