import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])
        n_islands = 0
        visited = set()

        def bfs(start_row, start_column):

            visited.add((start_row, start_column))

            queue = collections.deque()
            queue.append((start_row, start_column))

            while queue:
                current_row, current_column = queue.popleft()

                for delta in [1, -1]:

                    if current_column + delta >= 0 and current_column + delta < columns and grid[current_row][current_column + delta] == "1" and (current_row, current_column + delta) not in visited:
                        queue.append((current_row, current_column + delta))
                        visited.add((current_row, current_column + delta))

                    if current_row + delta >= 0 and current_row + delta < rows and grid[current_row + delta][current_column] == "1" and (current_row + delta, current_column) not in visited:
                        queue.append((current_row + delta, current_column))
                        visited.add((current_row + delta, current_column))

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in visited:
                    n_islands += 1
                    bfs(row, column)

        return n_islands
