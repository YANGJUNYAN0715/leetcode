from collections import Counter


class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = Counter(arr)
        if cnt[0] % 2:
            return False
        for x in sorted(cnt, key=abs):
            if cnt[2 * x] < cnt[x]:
                return False
            cnt[2 * x] -= cnt[x]
        return True


if __name__ == '__main__':
    s = Solution()
    arr = [4, -2, 2, -4]
    print(s.canReorderDoubled(arr))
