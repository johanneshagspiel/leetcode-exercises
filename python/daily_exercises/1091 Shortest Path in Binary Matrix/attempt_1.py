import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        moves = [(-1,0), (-1,1), (-1,-1),
                 (1,0), (1,1), (1,-1),
                 (0,1), (0,-1)]
        n = len(grid)

        start_cell = grid[0][0]
        if start_cell != 0:
            return -1

        queue = collections.deque()
        queue.append((0, 0))

        visited_set = {(0, 0)}

        path_length = 1

        while queue:

            que_len = len(queue)

            for _ in range(que_len):
                row, column = queue.popleft()

                if row == (n-1) and column == (n-1):
                    return path_length
                else:
                    for row_move, column_move in moves:
                        new_row = row + row_move
                        new_column = column + column_move

                        if new_row >= 0 and new_row < n and new_column >= 0 and new_column < n:
                            if (new_row, new_column) not in visited_set:
                                cell = grid[new_row][new_column]

                                if cell == 0:
                                    queue.append((new_row, new_column))
                                    visited_set.add((new_row, new_column))

            path_length += 1

        return -1
