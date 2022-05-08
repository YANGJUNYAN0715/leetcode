from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # a = set()
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] in a:
        #         res.append(nums[i])
        #     a.add(nums[i])
        # return res
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [num for i, num in enumerate(nums) if num - 1 != i]


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    print(s.findDuplicates(nums))
