class Solution:
    def numSquares(self, n: int) -> int:

        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]

        level = 0
        queue = {n}

        while queue:
            level += 1
            new_queue = set()

            for remainder in queue:
                for square in squares:
                    if square > remainder:
                        break
                    elif square == remainder:
                        return level
                    else:
                        new_queue.add(remainder - square)

            queue = new_queue

        return level
