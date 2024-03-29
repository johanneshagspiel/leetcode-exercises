import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        def depth_first_search(start_row, start_column):

            moves = [(1,0), (-1,0), (0,1), (0,-1)]

            stack = []
            stack.append((start_row, start_column))

            while stack:

                current_row, current_column = stack.pop()

                grid[current_row][current_column] = "2"

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                        if grid[new_row][new_column] == "1":
                            stack.append((new_row, new_column))

        islands = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    depth_first_search(row, column)

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "2":
                    grid[row][column] = "1"

        return islands
