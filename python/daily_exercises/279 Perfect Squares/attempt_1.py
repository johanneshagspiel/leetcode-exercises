class Solution:
    def numSquares(self, n: int) -> int:

        min_square = float("inf")

        def find_sum(remainder, count, mem_dic):

            nonlocal min_square

            if count >= min_square:
                return
            elif remainder in mem_dic:
                return

            max_square = int(sqrt(remainder))

            if pow(max_square, 2) == remainder:
                min_square = min(min_square, count + 1)
                mem_dic[remainder] = count + 1

            else:
                for perfect_square_op in range(max_square, 0, -1):
                    perfect_square = pow(perfect_square_op, 2)
                    find_sum(remainder - perfect_square, count + 1)

        find_sum(n, 0, {})
        return min_square

