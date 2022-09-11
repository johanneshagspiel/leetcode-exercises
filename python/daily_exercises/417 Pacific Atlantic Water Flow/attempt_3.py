from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        columns = len(heights[0])

        pacific_set = set()
        atlantic_set = set()

        def dfs(start_row, start_column, input_set):

            input_set.add((start_row, start_column))

            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            start_height = heights[start_row][start_column]

            stack = []
            stack.append((start_row, start_column, start_height))

            while stack:
                current_row, current_column, current_height = stack.pop()

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if (new_row, new_column) not in input_set:

                        if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:

                            new_height = heights[new_row][new_column]
                            if new_height >= current_height:

                                input_set.add((new_row, new_column))
                                stack.append((new_row, new_column, new_height))

        for row in range(rows):
            dfs(row, 0, pacific_set)
            dfs(row, columns - 1, atlantic_set)

        for column in range(columns):
            dfs(0, column, pacific_set)
            dfs(rows - 1, column, atlantic_set)

        res = pacific_set.intersection(atlantic_set)

        return res
