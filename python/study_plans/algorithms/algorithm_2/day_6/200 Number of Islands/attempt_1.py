import collections
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        number_islands = 0
        n_rows = len(grid)
        n_col = len(grid[0])
        seen_set = set()

        def bfs(start_row, start_column):

            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            queue = collections.deque()
            queue.append((start_row, start_column))

            while queue:
                row, column = queue.popleft()

                for row_move, column_move in moves:
                    new_row = row + row_move
                    new_column = column + column_move
                    new_key = str(new_row) + "_" + str(new_column)

                    if new_row >= 0 and new_row < n_rows and new_column >= 0 and new_column < n_col:
                        if new_key not in seen_set:
                            new_entry = grid[new_row][new_column]
                            if new_entry == "1":
                                seen_set.add(new_key)
                                queue.append((new_row, new_column))

        for row in range(n_rows):
            for column in range(n_col):
                entry = grid[row][column]
                key = str(row) + "_" + str(column)

                if entry == "1":
                    if key not in seen_set:
                        number_islands += 1
                        seen_set.add(key)

                        bfs(row, column)

        return number_islands