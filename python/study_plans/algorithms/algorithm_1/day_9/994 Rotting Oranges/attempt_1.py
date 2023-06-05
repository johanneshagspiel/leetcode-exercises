import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        queue = collections.deque()
        fresh_oranges = 0

        for row in range(rows):
            for column in range(columns):
                current_value = grid[row][column]

                if current_value == 1:
                    fresh_oranges += 1
                if current_value == 2:
                    queue.append((row, column))

        minutes_passed = 0

        while queue and fresh_oranges > 0:
            minutes_passed += 1

            for rotten_orange in range(len(queue)):
                row_rot, col_rot = queue.popleft()

                moves = ((1,0),(-1,0),(0,1),(0,-1))

                for row_move, col_move in moves:
                    new_row, new_col = row_rot + row_move, col_rot + col_move

                    if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < columns:

                        value_at_position = grid[new_row][new_col]

                        if value_at_position == 1:
                            fresh_oranges -= 1
                            grid[new_row][new_col] = 2
                            queue.append((new_row, new_col))

        return minutes_passed if fresh_oranges == 0 else -1
