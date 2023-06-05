class Solution:
    def numTrees(self, n: int) -> int:

        c = 1

        for n in range(n):
            c *= (2*((2*n) + 1)) / (n + 2)

        return int(c)
