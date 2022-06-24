class Solution:
    def hammingWeight(self, n: int) -> int:

        m = 1
        count = 0

        while m <= n:
            res = m & n
            if res > 0:
                count += 1
            m <<= 1

        return count