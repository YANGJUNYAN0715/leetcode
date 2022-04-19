class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ans = [0] * n

        idx = -n
        for i in range(0,n):
            if s[i] == c:
                idx = i
            ans[i] = i - idx

        idx = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], idx - i)
        return ans


if __name__ == '__main__':
    s = Solution()
    str1 = "loveleetcode"
    c = "e"
    print(s.shortestToChar(str1, c))
