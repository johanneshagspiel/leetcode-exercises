import collections
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited_ones = set()
        max_size = 0

        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for column in range(columns):
                current_value = grid[row][column]
                if current_value == 1 and current_value not in visited_ones:
                    visited_ones, island_size = self.bfs(grid, row, column, visited_ones)
                    if island_size > max_size:
                        max_size = island_size

        return max_size


    def bfs(self, grid, start_row, start_column, visited_ones):

        moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])

        queue = collections.deque([(start_row, start_column)])
        visited_ones.add((start_row, start_column))
        size = 0

        while queue:
            current_row, current_column = queue.popleft()
            size += 1

            for move_row, move_column in moves:
                new_row = current_row + move_row
                new_column = current_column + move_column

                if new_row >= 0 and new_row < rows and new_column >= 0 and new_column < columns:
                    if (new_row, new_column) not in visited_ones:
                        if grid[new_row][new_column] == 1:
                            visited_ones.add((new_row, new_column))
                            queue.append((new_row, new_column))

        return visited_ones, size



if __name__ == "__main__":
    solution = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    output = solution.maxAreaOfIsland(grid)
    print(output)