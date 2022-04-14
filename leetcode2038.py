class Solution(object):
    def winnerOfGame(self, colors):
        a, b = 0, 0
        for i in range(1, len(colors) - 1):
            if colors[i] == colors[i - 1] and colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
        return a > b


if __name__ == '__main__':
    s = Solution()
    colors = "AA"
    print(s.winnerOfGame(colors))

