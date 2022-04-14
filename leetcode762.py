from math import sqrt


def isPrime(num):
    if num <= 3:
        return num > 1
    if num % 6 != 1 and num % 6 != 5:
        return False
    for i in range(5, int(sqrt(num))):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def numberOfDigit1(num):
    res = 0
    while num > 0:
        res += 1
        num = num & (num - 1)
    return res


class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res = 0
        for i in range(left, right + 1):
            if isPrime(numberOfDigit1(i)):
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    left = 842
    right = 888
    print(s.countPrimeSetBits(left, right))
