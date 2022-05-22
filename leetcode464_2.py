class Solution:
    def dfs(self, status, dp, total, num):
        # 如果当前状态的 胜负已经被计算过了，直接返回即可
        if dp[status] is not None:
            return dp[status]
        for i in range(1, num + 1):
            b = 1 << (i - 1)  # 取第i个数字，如果已经被用过了直接忽略，status的位记录了已经被使用的
            if status & b:
                continue
            # 如果i能够使用并且已经大于等于total了，那么已经是赢了的
            # 否则需要下一状态要对手输了才行
            if i >= total or not self.dfs(status | b, dp, total - i, num):
                dp[status] = True
                return True
        dp[status] = False
        return False

    def canIWin(self, num: int, total: int) -> bool:
        if num >= total:
            return True
        if (1 + num) * num // 2 < total:
            return False
        return self.dfs(0, [None] * (1 << num), total, num)


if __name__ == '__main__':
    s = Solution()
    maxChoosableInteger = 10
    desiredTotal = 11
    print(s.canIWin(maxChoosableInteger, desiredTotal))
