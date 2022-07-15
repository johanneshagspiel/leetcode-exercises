from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        seen = set()
        max_size = 0

        def dfs(row, column):

            stack = []
            stack.append((row, column))
            island_size = 0

            while stack:
                current_row, current_column = stack.pop()
                island_size += 1

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                        if (new_row, new_column) not in seen:
                            if grid[new_row][new_column] == 1:
                                stack.append((new_row, new_column))
                                seen.add((current_row, current_column))

            return island_size

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    if (row, column) not in seen:
                        seen.add((row, column))
                        island_size = dfs(row, column)
                        max_size = max(island_size, max_size)

        return max_size
