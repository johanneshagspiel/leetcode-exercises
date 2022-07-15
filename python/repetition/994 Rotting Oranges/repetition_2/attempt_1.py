import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = collections.deque()
        fresh_oranges = 0

        n = len(grid)
        m = len(grid[0])

        for row in range(n):
            for column in range(m):
                if grid[row][column] == 1:
                    fresh_oranges += 1
                elif grid[row][column] == 2:
                    queue.append((row, column))

        minutes = 1
        seen = set()

        while queue and fresh_oranges > 0:

            len_queue = len(queue)
            minutes += 1

            for rotten_orange in range(len_queue):
                current_row, current_column = queue.popleft()

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if new_row >= 0 and new_row < n and new_column >= 0 and new_column < m:
                        if grid[new_row][new_column] == 1:
                            if (new_row, new_column) not in seen:
                                seen.add((new_row, new_column))
                                fresh_oranges -= 1
                                queue.append((new_row, new_column))

        return minutes if fresh_oranges == 0 else -1
