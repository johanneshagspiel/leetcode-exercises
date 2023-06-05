class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        mask = 1

        for bits in range(32):
            remainder = mask & n
            if remainder != 0:
                count += 1
            mask <<= 1

        return count
