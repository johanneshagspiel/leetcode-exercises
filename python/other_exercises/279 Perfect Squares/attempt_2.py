import math


class Solution:
    def numSquares(self, n: int) -> int:

        square_list = [i*i for i in range(1, int(math.sqrt(n)) + 1)]

        queue = {n}
        level = 0

        while queue:

            next_queue = set()

            for remainder in queue:

                for square in square_list:

                    if remainder == square:
                        return level

                    elif square > remainder:
                        break

                    else:
                        next_queue.add(remainder - square)

            level += 1
            queue = next_queue

        return level
