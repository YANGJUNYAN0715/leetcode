class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(5,n+1,5):
            while i % 5 ==0:
                i //= 5
                ans+=1
        return ans


if __name__ == '__main__':
    s = Solution()
    n = 25
    print(s.trailingZeroes(n))
