class Solution:
    def numTrees(self, n: int) -> int:

        c = 1

        for num in range(1, n):
            c = ((2 * ((2*num) + 1)) / (num +2)) * c

        return c