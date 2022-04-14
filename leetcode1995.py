class Solution(object):
    def countQuadruplets(self, nums):
        n = len(nums)
        res = 0
        if n >=4:
            for a in range(n):
                for b in range(a + 1, n):
                    for c in range(b + 1, n):
                        for d in range(c + 1, n):
                            if nums[a] + nums[b] + nums[c] == nums[d]:
                                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.countQuadruplets(nums))