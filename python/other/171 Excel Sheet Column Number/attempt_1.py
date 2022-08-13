class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        n = len(columnTitle)
        acc = 0

        for index in range(n):
            acc += (ord(columnTitle[n-index-1].lower()) - ord('a') + 1) * (26 ** index)

        return acc
