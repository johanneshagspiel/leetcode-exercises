import collections
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        fresh_oranges = 0
        queue = collections.deque()

        for row in range(rows):
            for column in range(columns):

                if grid[row][column] == 1:
                    fresh_oranges += 1

                elif grid[row][column] == 2:
                    queue.append((row, column))

        minutes = 0

        moves = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue and fresh_oranges > 0:
            minutes += 1

            oranges = len(queue)

            for orange in range(oranges):
                current_row, current_column = queue.popleft()

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                        if grid[new_row][new_column] == 1:

                            fresh_oranges -= 1
                            grid[new_row][new_column] = 2
                            queue.append((new_row, new_column))


        if fresh_oranges > 0:
            return -1
        else:
            return minutes
