from itertools import pairwise
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 自己琢磨了半天都做不对，答案就两行
        # def isOrderSorted(word1: str, word2: str, order: str):
        #     n = max(len(word1), len(word2))
        #     for i in range(n):
        #         if i == len(word1)-1 and i == len(word2)-1:
        #             return True
        #         elif i == len(word1):
        #             return True
        #         elif i == len(word2):
        #             return False
        #         if order.index(word1[i]) > order.index(word2[i]):
        #             return False
        #         elif order.index(word1[i]) < order.index(word2[i]):
        #             return True
        #         elif order.index(word1[i]) == order.index(word2[i]):
        #             continue
        #
        # n = len(words)
        # for i in range(n - 1):
        #     for j in range(i + 1, i + 2):
        #         if not isOrderSorted(words[i], words[j], order):
        #             return False
        #     return True
        index = {c: i for i, c in enumerate(order)}
        return all(s <= t for s, t in pairwise([index[c] for c in word] for word in words))


if __name__ == '__main__':
    s = Solution()
    words = ["hello", "hello"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(s.isAlienSorted(words, order))
