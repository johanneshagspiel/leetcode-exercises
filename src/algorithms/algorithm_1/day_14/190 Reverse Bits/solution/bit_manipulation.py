class Solution:
    def reverseBits(self, n: int) -> int:
        num_shifts = 31
        accumulator = 0

        while n:
            bit = n & 1
            shifted_bit = bit << num_shifts
            n = n >> 1
            accumulator += shifted_bit
            num_shifts -= 1

        return accumulator