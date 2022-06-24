class Solution:
    def reverseBits(self, n: int) -> int:

        num_shifts = 32
        accumulator = 0

        for position in range(0, 32):

            bit_to_shift = n & (1 << position)

            result_position = 32 - position

            if result_position > 0:
                bit_at_right_position = bit_to_shift << result_position
            elif result_position == 0:
                bit_at_right_position = bit_to_shift
            else:
                bit_at_right_position = bit_to_shift >> result_position

            accumulator = accumulator | bit_at_right_position

        print(bin(accumulator))



if __name__ == "__main__":
    solution = Solution()
    solution.reverseBits(1)