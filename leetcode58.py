class Solution(object):
    def lengthOfLastWord(self, s):
        cnt, p = 0, len(s) - 1
        while s[p] == ' ':
            p -= 1
        while p >= 0 and s[p] != ' ':
            p -= 1
            cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("the moon  "))