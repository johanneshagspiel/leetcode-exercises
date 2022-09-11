import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        visited = [[0]*columns for _ in range(rows)]

        def bfs(start_row, start_column):

            visited[start_row][start_column] = 1

            queue = collections.deque()
            queue.append((start_row, start_column))

            while queue:
                row, column = queue.popleft()

                for delta in [1, -1]:

                    if column + delta >= 0 and (column + delta) < columns and visited[row][column+delta] == 0 and grid[row][column+delta] == '1':
                        visited[row][column+delta] = 1
                        queue.append((row, column+delta))

                    if row + delta >= 0 and (row + delta) < rows and visited[row+delta][column] == 0 and grid[row+delta][column] == '1':
                        visited[row+delta][column] = 1
                        queue.append((row+delta, column))

        islands = 0

        for row in range(rows):
            for column in range(columns):
                if visited[row][column] == 0 and grid[row][column] == "1":
                    bfs(row, column)
                    islands += 1
        return islands
