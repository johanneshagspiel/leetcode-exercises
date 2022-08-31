from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        columns = len(grid)
        rows = len(grid[0])
        num_islands = 0

        def dfs(start_column, start_row):

            moves = [(1,0), (-1,0), (0,1), (0,-1)]

            stack = []
            stack.append((start_column, start_row))

            while stack:
                current_column, current_row = stack.pop()

                grid[current_column][current_row] = 2

                for column_move, row_move in moves:
                    new_column = current_column + column_move
                    new_row = current_row + row_move

                    if new_column >= 0 and new_column < columns and new_row >= 0 and new_row < rows:
                        if grid[new_column][new_row] == 1:
                            stack.append((new_column, new_row))



        for column in range(columns):
            for row in range(rows):
                entry = grid[column][row]

                if entry == 1:
                    num_islands += 1
                    dfs(column,row)


        for column in range(columns):
            for row in range(rows):
                entry = grid[column][row]

                if entry == 2:
                    grid[column][row] = 1

        return num_islands

