class Solution:
    def reverseBits(self, n: int) -> int:

        acc = 0
        num_shift = 31

        while n:
            bit = n & 1
            bit_shifted = bit << num_shift
            n = n >> 1
            acc += bit_shifted
            num_shift -= 1

        return acc
