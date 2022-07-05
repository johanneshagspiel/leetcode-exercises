import collections
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        self.fresh_oranges = 0


        def bfs(row, column):

            moves = [(1,0), (-1,0), (0,1), (0,-1)]

            queue = collections.deque()
            queue.append((row, column))

            minutes = 0

            while queue:

                rotten_oranges = len(queue)
                minutes += 1

                for rotten_orange in range(rotten_oranges):
                    current_row, current_column = queue.popleft()

                    for row_move, column_move in moves:
                        new_row = current_row + row_move
                        new_column = current_column + column_move

                        if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                            if grid[new_row][new_column] == 1:
                                queue.append((new_row, new_column))
                                grid[new_row][new_column] = 2
                                self.fresh_oranges -= 1

            if self.fresh_oranges > 0:
                return -1
            else:
                return minutes



        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    self.fresh_oranges += 1

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    return bfs(row, column)
