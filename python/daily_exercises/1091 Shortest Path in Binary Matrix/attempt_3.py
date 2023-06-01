import heapq


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        max_row = len(grid) -1
        max_col = len(grid[0]) - 1

        moves = [(0,1),(0,-1),
                 (1,-1), (1,0), (1,1),
                 (-1,-1), (-1,0), (-1,1)]

        def get_neighbours(row, col):
            for row_difference, col_difference in moves:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)

        def best_case_estimate(row, col):
            return max(max_row - row, max_col - col)

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        visited = set()
        queue = [(1 + best_case_estimate(0, 0), 1, (0, 0,))]

        while queue:
            estimate, distance, cell = heapq.heappop(queue)
            visited.add(cell)

            if (max_row, max_col) == cell:
                return distance
            else:
                for neighbour in get_neighbours(*cell):
                    # The check here isn't necessary for correctness, but it
                    # leads to a substantial performance gain.
                    if neighbour in visited:
                        continue
                    estimate = best_case_estimate(*neighbour) + distance + 1
                    entry = (estimate, distance + 1, neighbour)
                    heapq.heappush(queue, entry)

        return -1