import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        seen = set()

        def breadth_first_search(start_row, start_column):

            nonlocal seen

            moves = [(1,0), (-1,0), (0,1), (0,-1)]

            queue = collections.deque()
            queue.append((start_row, start_column))

            while queue:

                current_row, current_column = queue.popleft()
                seen.add((current_row, current_column))

                for row_move, column_move in moves:
                    new_row = current_row + row_move
                    new_column = current_column + column_move

                    if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                        if grid[new_row][new_column] == "1":
                            if (new_row, new_column) not in seen:
                                seen.add((current_row, current_column))
                                queue.append((new_row, new_column))

            return 

        islands = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    if (row, column) not in seen:
                        islands += 1
                        breadth_first_search(row, column)

        return islands
