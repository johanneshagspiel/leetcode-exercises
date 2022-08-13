class Solution:
    def reverseBits(self, n: int) -> int:

        n_shifts = 31
        acc = 0

        while n > 0:
            bit = n & 1
            n = n >> 1

            shifted_bit = bit << n_shifts
            acc += shifted_bit
            n_shifts -= 1

        return acc
