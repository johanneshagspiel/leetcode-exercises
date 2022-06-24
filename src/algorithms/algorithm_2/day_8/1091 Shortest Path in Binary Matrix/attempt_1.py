import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] != 0:
            return -1

        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        visited = set()
        queue = collections.deque()
        queue.append((0, 0))
        start_key = str(0) + "-" + str(0)
        visited.add(start_key)

        moves_needed = 1
        n = len(grid)

        if grid[n - 1][n - 1] != 0:
            return -1

        while queue:
            queue_length = len(queue)

            for element in range(queue_length):
                row, column = queue.popleft()

                if (row == (n - 1)) and (column == (n - 1)):
                    return moves_needed
                else:
                    for row_move, column_move in moves:
                        new_row = row + row_move
                        new_column = column + column_move

                        if new_row >= 0 and new_row < n and new_column >= 0 and new_column < n:
                            new_key = str(new_row) + "-" + str(new_column)
                            if new_key not in visited:
                                element = grid[new_row][new_column]
                                if element == 0:
                                    visited.add(new_key)
                                    queue.append((new_row, new_column))
            moves_needed += 1
        return -1
