class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def isDividingNumbers(num):
            temp = num
            while temp != 0:
                a = temp % 10
                if a==0 or num % a != 0:
                    return False
                temp = temp // 10
            return True

        res = []
        for i in range(left, right + 1):
            if isDividingNumbers(i):
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    left, right = 47, 85
    print(s.selfDividingNumbers(left, right))
